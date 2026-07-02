#!/usr/bin/env python3
"""Count App Store metadata field characters deterministically."""

from __future__ import annotations

import argparse
import sys
import unicodedata


def normalized(value: str) -> tuple[str, bool]:
    nfc = unicodedata.normalize("NFC", value)
    return nfc, nfc != value


def add_field(rows: list[tuple[str, int, str]], label: str, limit: int, value: str) -> None:
    rows.append((label, limit, value))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Count App Store metadata characters after NFC normalization."
    )
    parser.add_argument("--name", help="App name; limit 30 characters.")
    parser.add_argument("--subtitle", help="Subtitle; limit 30 characters.")
    parser.add_argument(
        "--keywords",
        action="append",
        default=[],
        metavar="PLATFORM=VALUE",
        help="Platform keyword field; limit 100 characters. Repeat for multiple platforms.",
    )
    parser.add_argument(
        "--field",
        action="append",
        default=[],
        metavar="LABEL:LIMIT:VALUE",
        help="Custom field with explicit limit, for example 'Promo:170:text'.",
    )
    args = parser.parse_args()

    rows: list[tuple[str, int, str]] = []

    if args.name is not None:
        add_field(rows, "App Name", 30, args.name)
    if args.subtitle is not None:
        add_field(rows, "Subtitle", 30, args.subtitle)

    for item in args.keywords:
        if "=" not in item:
            parser.error("--keywords must use PLATFORM=VALUE")
        platform, value = item.split("=", 1)
        platform = platform.strip()
        if not platform:
            parser.error("--keywords platform must not be empty")
        add_field(rows, f"Keywords ({platform})", 100, value)

    for item in args.field:
        parts = item.split(":", 2)
        if len(parts) != 3:
            parser.error("--field must use LABEL:LIMIT:VALUE")
        label, limit_text, value = parts
        try:
            limit = int(limit_text)
        except ValueError:
            parser.error("--field LIMIT must be an integer")
        if not label:
            parser.error("--field LABEL must not be empty")
        add_field(rows, label, limit, value)

    if not rows:
        parser.error("Provide at least one metadata field to count")

    failed = False
    for label, limit, value in rows:
        checked_value, changed = normalized(value)
        count = len(checked_value)
        status = "PASS" if count <= limit else "FAIL"
        if count > limit:
            failed = True
        suffix = " NFC-normalized" if changed else ""
        print(f"{status} {label}: {count}/{limit} chars{suffix}")
        print(checked_value)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
