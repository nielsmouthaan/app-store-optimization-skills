#!/usr/bin/env python3
"""Fetch approximate app positions from Apple's iTunes Search API."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urlparse
from urllib.request import Request, urlopen


API_URL = "https://itunes.apple.com/search"
SOURCE = "iTunes Search API"
WARNING = (
    "iTunes Search API rankings are somewhat unreliable search result positions "
    "that can differ from reality, but may still be representative of "
    "search-term performance."
)
ENTITY_BY_PLATFORM = {
    "iphone": "software",
    "ipad": "iPadSoftware",
    "mac": "macSoftware",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch approximate App Store search-result positions for one app "
            "and one or more search terms using Apple's iTunes Search API."
        )
    )
    parser.add_argument(
        "--app",
        required=True,
        help="App Store app ID or App Store URL containing /id<APP_ID>.",
    )
    parser.add_argument(
        "--region",
        required=True,
        help="Two-letter App Store country or region code, such as US, NL, or DE.",
    )
    parser.add_argument(
        "--platform",
        choices=sorted(ENTITY_BY_PLATFORM),
        required=True,
        help="App Store platform to query.",
    )
    parser.add_argument(
        "--term",
        action="append",
        required=True,
        help="Search term to check. Repeat for multiple terms.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=200,
        help="Maximum search results to inspect per term. Apple's documented maximum is 200.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=20.0,
        help="HTTP timeout in seconds.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=3.0,
        help="Delay between requests for multiple terms. Default respects roughly 20 calls/minute.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print request URLs without calling the API.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit compact JSON. Without this flag, JSON is pretty-printed.",
    )
    return parser.parse_args()


def parse_app_id(value: str) -> str:
    app = value.strip()
    if re.fullmatch(r"\d+", app):
        return app

    path_match = re.search(r"/id(\d+)", app)
    if path_match:
        return path_match.group(1)

    query = parse_qs(urlparse(app).query)
    query_id = query.get("id", [""])[0]
    if re.fullmatch(r"\d+", query_id):
        return query_id

    raise ValueError("Could not extract an app ID from --app. Use a numeric app ID or App Store URL.")


def normalize_region(region: str) -> str:
    normalized = region.strip().upper()
    if not re.fullmatch(r"[A-Z]{2}", normalized):
        raise ValueError("--region must be a two-letter country or region code, such as US, NL, or DE.")
    return normalized


def normalize_terms(terms: list[str]) -> list[str]:
    normalized: list[str] = []
    seen: set[str] = set()

    for term in terms:
        clean = " ".join(term.strip().split())
        if not clean:
            raise ValueError("--term values cannot be empty.")
        if clean.casefold() in seen:
            continue
        seen.add(clean.casefold())
        normalized.append(clean)

    return normalized


def validate_limit(limit: int) -> int:
    if limit < 1 or limit > 200:
        raise ValueError("--limit must be between 1 and 200.")
    return limit


def validate_delay(delay: float) -> float:
    if delay < 0:
        raise ValueError("--delay cannot be negative.")
    return delay


def build_url(term: str, region: str, platform: str, limit: int) -> str:
    params = {
        "term": term,
        "country": region,
        "media": "software",
        "entity": ENTITY_BY_PLATFORM[platform],
        "limit": str(limit),
    }
    return f"{API_URL}?{urlencode(params)}"


def fetch_json(url: str, timeout: float) -> dict[str, Any]:
    request = Request(url, headers={"User-Agent": "aso-search-terms-rankings/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except HTTPError as error:
        raise RuntimeError(f"HTTP {error.code} from iTunes Search API") from error
    except URLError as error:
        raise RuntimeError(f"Could not reach iTunes Search API: {error.reason}") from error

    try:
        data = json.loads(body)
    except json.JSONDecodeError as error:
        raise RuntimeError("iTunes Search API returned invalid JSON") from error

    if not isinstance(data, dict):
        raise RuntimeError("iTunes Search API returned an unexpected response shape")

    return data


def find_rank(data: dict[str, Any], app_id: str) -> tuple[int | None, dict[str, Any] | None, int]:
    results = data.get("results", [])
    if not isinstance(results, list):
        raise RuntimeError("iTunes Search API response does not contain a results list")

    for index, item in enumerate(results, start=1):
        if isinstance(item, dict) and str(item.get("trackId", "")) == app_id:
            return index, item, len(results)

    return None, None, len(results)


def result_for_term(
    term: str,
    app_id: str,
    region: str,
    platform: str,
    limit: int,
    timeout: float,
    dry_run: bool,
) -> dict[str, Any]:
    url = build_url(term, region, platform, limit)

    if dry_run:
        return {
            "term": term,
            "rank": None,
            "displayRank": "-",
            "found": False,
            "resultCount": None,
            "matchedAppName": None,
            "searchUrl": url,
            "dryRun": True,
        }

    data = fetch_json(url, timeout)
    rank, matched, result_count = find_rank(data, app_id)

    return {
        "term": term,
        "rank": rank,
        "displayRank": str(rank) if rank is not None else "-",
        "found": rank is not None,
        "resultCount": result_count,
        "matchedAppName": matched.get("trackName") if matched else None,
        "searchUrl": url,
        "dryRun": False,
    }


def main() -> int:
    args = parse_args()

    try:
        app_id = parse_app_id(args.app)
        region = normalize_region(args.region)
        terms = normalize_terms(args.term)
        limit = validate_limit(args.limit)
        delay = validate_delay(args.delay)
        if args.timeout <= 0:
            raise ValueError("--timeout must be greater than zero.")
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    print(f"warning: {WARNING}", file=sys.stderr)

    results: list[dict[str, Any]] = []
    for index, term in enumerate(terms):
        try:
            results.append(
                result_for_term(
                    term=term,
                    app_id=app_id,
                    region=region,
                    platform=args.platform,
                    limit=limit,
                    timeout=args.timeout,
                    dry_run=args.dry_run,
                )
            )
        except RuntimeError as error:
            print(f"error: {term}: {error}", file=sys.stderr)
            return 1

        if not args.dry_run and index < len(terms) - 1 and delay > 0:
            time.sleep(delay)

    payload = {
        "source": SOURCE,
        "warning": WARNING,
        "app": args.app,
        "appId": app_id,
        "region": region,
        "platform": args.platform,
        "limit": limit,
        "checkedDate": dt.date.today().isoformat(),
        "results": results,
    }

    if args.json:
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
