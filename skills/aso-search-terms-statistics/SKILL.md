---
name: aso-search-terms-statistics
description: Fetches App Store search-term popularity and difficulty statistics from App Store optimization tools or user-provided exports. Use after relevance scoring, when refreshing stale keyword metrics, or when the user asks for exploratory statistics on candidate or rejected terms.
---

# ASO Search Terms Statistics

Act as an ASO statistics operator. Fetch external popularity and difficulty values for confirmed search terms, validate their scale, convert accepted `0` values to `1`, then record them in `.agents/aso/context.md` or the active localized workspace.

Popularity and difficulty are not public App Store values and must come from an available ASO service, tool, or user-provided export. Do not estimate, invent, or derive these scores from other metrics.

## Before Starting

Read `.agents/aso/context.md` first.

If the user is working on a localized workspace, also read the relevant `.agents/aso/locales/<ISO code>/<language-slug>.md` file and use its `ISO code`, `Country or region`, and `Language` as the statistics target.

If it exists:

- Summarize the app context that matters for statistics fetching.
- Identify the active `Search language` and `Search region`.
- For localized work, identify the target `ISO code`, country or region, language, and localized terms that need statistics.
- Show the confirmed terms in `## Search Terms Backlog` that need missing or refreshed statistics.
- Preserve existing statuses, relevance scores, statistics, strategic scores, notes, and any additional backlog columns unless the user corrects them.

If it does not exist or lacks meaningful app context:

- Invoke or recommend `aso-context` before continuing.
- Abort statistics fetching until app context exists.

If `## Search Terms Backlog` is missing or empty:

- Invoke or recommend `aso-search-terms-identification` before continuing.
- Abort statistics fetching until search terms exist.

Prefer running this skill after `aso-search-terms-relevance-scoring`, but do not block statistics fetching only because relevance scores are blank. Relevance and statistics are independent inputs for later ASO work. Fetch statistics for `confirmed` terms by default; fetch `candidate` or `rejected` terms only when the user explicitly asks for exploratory statistics.

## Region Selection

Use the App Store country or region most associated with the context's active search language or localized workspace.

1. For localized work, use the workspace `ISO code`. If it is missing, derive or ask for it before fetching.
2. For source-locale work, use `.agents/aso/context.md` `Search region` when present.
3. If `Search region` is blank, derive it from `Search language` using `../../references/app-store-localizations.md`.
4. Store the chosen source-locale region back in `.agents/aso/context.md` as uppercase ISO 3166-1 alpha-2, such as `US`, `NL`, or `DE`.
5. If the language is genuinely ambiguous and no context clue resolves it, ask the user for the country or region before fetching. Do not default to a convenient country or region when the wrong storefront would make the data misleading.

Validate localized `ISO code` and `Language` pairs against Apple's supported App Store localizations when localized work is active. If the target country or region is unresolved or incompatible with the target language, stop before fetching statistics.

If a statistics source requires a two-letter region parameter, derive it from the localized workspace `ISO code` using `../../references/app-store-localizations.md` or a standard ISO 3166 lookup. Do not store the derived tool region in the localized workspace.

Use one region per run unless the user explicitly asks for multi-region statistics.

## Tool Discovery

Before fetching, check whether a statistics source is available in the current environment.

Prefer sources in this order:

1. **ASO Suite CLI or skill** when `asosuite` is available.
2. **Astro MCP** when relevant Astro tools are exposed and can return keyword popularity and difficulty for the target region.
3. Another user-provided ASO export or tool that clearly provides App Store popularity and difficulty values for the same region.

If no usable source is available, recommend:

- ASO Suite: https://nielsmouthaan.dev/asosuite
- Astro: https://nielsmouthaan.dev/astro

Then abort. Popularity and difficulty statistics are required for later ASO steps, and the agent must not continue by guessing.

If a source is available but authentication, subscription, quota, or network access fails, report the blocker and abort instead of estimating missing values.

## Stats Freshness

Treat statistics as outdated when `Stats updated` is more than one month older than the current date.

Before fetching, show confirmed terms with:

- missing `Popularity` or `Difficulty`
- missing `Stats updated`
- `Stats updated` more than one month old

Ask the user whether to refresh outdated statistics before continuing. If the user declines, continue with existing values only when useful and include a stale-statistics warning in the summary. If outdated statistics are refreshed, clear `Strategic score` for rows where `Popularity` or `Difficulty` changes, is removed, remains missing after an attempted refresh, or is reattempted after being stale.

## Metric Validation

Store `Popularity` and `Difficulty` as `1`-`100` scoring inputs.

Use these rules:

- Accept only source-provided popularity and difficulty scores on a documented `0`-`100` scale.
- If a source value is `0`, store it as `1`.
- Preserve source values from `1` to `100` as-is.
- If a value is below `0`, above `100`, or not clearly documented as a popularity or difficulty score on an accepted scale, leave the field blank.
- When values are not usable as `0`-`100` scores, record the blocker in `Notes` and ask the user how to deal with those values before continuing.

## Fetching With ASO Suite

When using ASO Suite:

- Use JSON output.
- Use the selected region.
- For localized work, derive the selected ASO Suite `--region` parameter from the workspace `ISO code`.
- Use the app URL or app ID from context when available.
- Use `iphone` as the platform unless the context or user specifies `ipad`, `mac`, `appletv`, `watch`, or `vision`.
- Fetch at most 50 keywords per request.

Command shape:

```bash
asosuite keywords --json --region <REGION> --platform <PLATFORM> [--app <APP_ID_OR_URL>] <keyword...>
```

Use the returned keyword metrics according to `## Metric Validation`. Preserve source context in `Stats source`, `Stats region` for source-locale rows that already use that column, `Stats updated`, and compact notes when a value could not be used. For localized rows, do not add `Stats region`; record only unresolved tool-region derivation or mismatch notes in `Notes`.

If a value is pending or missing:

- Leave that metric blank in the backlog.
- Add a compact note such as `popularity pending`, `difficulty missing`, or `stats unavailable`.
- Do not fill missing values from another source unless the source is explicit and region-compatible.

## Saving Results

Store statistics in the canonical `## Search Terms Backlog` table for the active workspace.

For source-locale work:

```markdown
| Search term | Source | Status | Relevance | Popularity | Difficulty | Stats region | Stats source | Stats updated | Notes | Strategic score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| example term | app description | confirmed | 4 | 38 | 21 | NL | ASO Suite | 2026-05-20 | strong feature fit |  |
```

For localized work:

```markdown
| Search term | Meaning | Status | Relevance | Popularity | Difficulty | Stats source | Stats updated | Notes | Strategic score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| quittung scanner | receipt scanner | confirmed | 5 | 38 | 21 | ASO Suite | 2026-05-20 | same intent as source core term |  |
```

When updating the table:

- Add missing statistics columns without dropping existing columns.
- Update only confirmed terms unless the user explicitly asks to fetch candidate or rejected terms.
- Preserve rejected terms without assigning popularity or difficulty.
- Preserve existing `Search term`, `Source` when present, `Meaning` when present, `Status`, `Relevance`, and unrelated columns.
- Clear `Strategic score` for rows where `Popularity` or `Difficulty` is added, changed, removed, or left missing after a fetch attempt; preserve it for unchanged rows.
- For source-locale rows with the existing schema, fill `Popularity`, `Difficulty`, `Stats region`, `Stats source`, and `Stats updated` only for terms with obtained or attempted statistics.
- For localized rows, fill `Popularity`, `Difficulty`, `Stats source`, and `Stats updated`; do not add `Stats region`.
- For localized work, if an imported value was fetched for a different country or region than the workspace `ISO code`, leave popularity and difficulty blank and record the mismatch in `Notes`.
- Store only validated `1`-`100` values in `Popularity` and `Difficulty`.
- Use `Stats updated` as `YYYY-MM-DD`.
- Append compact statistics notes to `Notes` only when needed; do not erase existing notes.
- Update `*Last updated:*` in the active context or locale workspace file.

After saving, summarize how many terms were updated, how many had pending or missing values, whether any values were unusable because they were outside the accepted scale, whether any stale statistics were kept, the country or region used, any derived ASO tool region parameter, and the source used.

## Common Mistakes

- Guessing popularity or difficulty from relevance, search results, App Store metadata, or web SEO volume.
- Using the US store for every language.
- Mixing values from different regions without recording the region per term.
- Using values that are not documented `0`-`100` scores.
- Fetching rejected terms by default.
- Dropping existing relevance scores, notes, statuses, strategic scores, or added backlog columns while adding statistics.
- Leaving stale strategic scores after changing popularity or difficulty.
- Continuing without warning when statistics are more than one month old.
- Continuing to derived scoring when no statistics source is available.

## Related Skills

- Use `aso-context` to create or update shared app context.
- Use `aso-search-terms-identification` to create or expand the search-term backlog.
- Use `aso-search-terms-relevance-scoring` to assign user-reviewed relevance before prioritization.
- Use `aso-search-terms-scoring` to calculate derived priority scores after popularity and difficulty are saved.
