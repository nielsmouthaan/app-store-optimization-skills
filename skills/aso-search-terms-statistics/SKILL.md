---
name: aso-search-terms-statistics
description: Fetches App Store search term popularity and difficulty statistics from App Store optimization tools, normalized Apple Ads Search Popularity, or user-provided exports. Use after search terms have been identified and relevance-scored, when refreshing stale search term metrics, or when the user asks for exploratory statistics on candidate or rejected terms.
---

# ASO Search Terms Statistics

Act as an ASO statistics operator. Fetch external popularity and difficulty values for confirmed search terms, validate their scale, normalize accepted Apple Ads Search Popularity values, convert accepted `0` values to `1`, then record them in `.agents/aso/context.md` or the active localized workspace.

Popularity and difficulty are not public App Store values and must come from an available ASO service, tool, Apple Ads Search Popularity input, or user-provided export. Do not estimate, invent, or derive these scores from unrelated metrics. Strategic scoring requires complete statistics for every in-scope confirmed term unless the user explicitly accepts partial scoring.

## Before Starting

Read `.agents/aso/context.md` first.

If the user is working on a localized workspace, also read the relevant `.agents/aso/locales/<Locale>/context.md` file and use its `Locale` and optional `Country or region preference` as the statistics target.

If it exists:

- Summarize the app context that matters for statistics fetching.
- Identify the source `Primary locale`, optional `Country or region preference`, `Platforms`, and any `Search surface preference`.
- For localized work, identify the target locale, optional country or region preference, and localized terms that need statistics.
- Show the confirmed terms in `## Search Terms Backlog` that need missing or refreshed statistics.
- Preserve existing statuses, relevance scores, statistics, strategic scores, notes, and any additional backlog columns unless the user corrects them.

If it does not exist or lacks meaningful app context:

- Invoke or recommend `aso-context` before continuing.
- Abort statistics fetching until app context exists.

If `## Search Terms Backlog` is missing or empty:

- Invoke or recommend `aso-search-terms-identification` before continuing.
- Abort statistics fetching until search terms exist.

Prefer running this skill after `aso-search-terms-identification` has assigned relevance, but do not block statistics fetching only because relevance scores are blank. Relevance and statistics are independent inputs for later ASO work. Fetch statistics for `confirmed` terms by default; fetch `candidate` or `rejected` terms only when the user explicitly asks for exploratory statistics.

## Country Or Region Selection

Resolve the App Store country or region before fetching statistics.

1. Use an explicit country or region request for the current run.
2. Use saved `Country or region preference` from the active source context or localized workspace.
3. Derive the default country or region for the active `Primary locale` or localized workspace `Locale` from `references/app-store-localizations.md`.
4. Ask the user if no safe default exists.

Use one primary country or region per run for saved `Popularity` and `Difficulty` values. If the user explicitly asks for multiple countries or regions, or the active locale clearly targets multiple important storefronts, choose one primary scoring country or region and treat the others as secondary validation.

Validate the resolved country or region against Apple's supported App Store localizations when localized work is active. If the resolved country or region does not support the active locale, stop before fetching statistics unless the user explicitly wants exploratory comparison data outside the localized workflow.

If a statistics source requires a two-letter country or region parameter, derive it from the resolved Apple country or region ISO code using `references/app-store-localizations.md` or a standard ISO 3166 lookup. Do not store the derived tool parameter in the workspace.

## Multi-Region Validation

Use multi-region validation only when it can materially improve the recommendation, such as a locale used across several target markets or a user request for broader regional growth.

Keep it simple:

- Save primary-country statistics in the backlog's `Popularity`, `Difficulty`, `Stats country or region`, `Stats source`, and `Stats updated` columns.
- Keep secondary-country checks out of the primary scoring columns. Record them in `Notes`, a run summary, or a separate comparison artifact when needed.
- Do not average, merge, or substitute secondary-country values into the primary scoring values.
- Run secondary checks for the most important terms only when full multi-country collection is not needed for the current decision.
- Ask the user only when the primary country choice or a secondary-country conflict would materially change metadata recommendations.

Examples:

- For German metadata targeting DACH, use `DEU` as the primary scoring country unless the user specifies otherwise, and optionally validate important terms against `AUT` or `CHE`.
- For Spanish (Mexico) metadata with U.S. Spanish relevance, use `MEX` as the primary scoring country unless the user specifies otherwise, and optionally validate important terms against `USA`.

## Platform And Statistics Scope

Choose a platform/statistics scope before fetching when multiple App Store Connect metadata platforms exist, a target platform is saved, or the user asks about platform-specific `Keywords` fields. Keep `Platforms` as App Store Connect metadata platforms, and derive any search surface or tool parameter only at tool-call time from `references/platforms.md`, the tool's skill, CLI help, or documentation.

Use one of these scope labels in the run summary:

- `target-platform-only`: Fetch statistics for the requested or saved target platform/search surface. Record that only target-platform evidence is available for downstream metadata generation.
- `all-metadata-platforms`: Fetch or collect compatible evidence for every metadata platform that needs its own `Keywords` field. If the active backlog has only one `Popularity` and `Difficulty` column, choose one primary scoring platform for saved values and record secondary platform checks in `Notes` or a separate artifact instead of mixing platform values in one row.
- `primary-platform-reuse`: Fetch statistics for the primary platform only because saved guidance says to mirror or reuse `Keywords` fields across platforms, or one platform is clearly primary. Mark the run summary as primary-platform evidence intended for reuse and warn that platform-specific validation is still missing.

If no platform scope is explicit and only one metadata platform exists, use that platform. If multiple metadata platforms exist and no saved guidance identifies a target or reuse strategy, choose the most relevant platform from the current user request or ask only when the choice would materially change the metadata recommendation.

## Tool Discovery

Before fetching, check whether a statistics source is available in the current environment.

Prefer sources in this order:

1. **ASO Suite CLI or skill** when `asosuite` is available.
2. **Astro MCP** when relevant Astro tools are exposed and can return search term popularity and difficulty for the target country or region.
3. **User-provided Apple Ads Search Popularity** on a `1`-`5` scale for popularity only, when it matches the target country or region and platform or no conflict is present.
4. Another user-provided ASO export or tool that clearly provides App Store popularity and difficulty values for the same country or region.

If no usable source is available, recommend:

- ASO Suite: https://nielsmouthaan.dev/asosuite
- Astro: https://nielsmouthaan.dev/astro

Then stop and ask the user to provide a usable statistics source, a compatible export, compatible manual values, or to pause the workflow.

If a source is available but authentication, subscription, quota, network access, or execution fails, report the blocker and use that tool's skill, CLI help, or documentation to diagnose the source. Ask the user whether to fix access, provide compatible values manually, try another available statistics source, or pause the workflow when the blocker remains.

## Stats Freshness

Treat statistics as outdated when `Stats updated` is more than one month older than the current date.

Before fetching, identify confirmed terms with:

- missing `Popularity` or `Difficulty`
- missing `Stats updated`
- `Stats updated` more than one month old

When a statistics source is available, fetch or refresh these values without treating this as a normal user review gate. Continue to strategic scoring only when every in-scope confirmed term has complete, fresh, valid `Popularity` and `Difficulty`.

If any requested statistics remain missing, pending, stale, incompatible, or unusable after the fetch attempt, stop and ask the user how to proceed before continuing to strategic scoring. Required options are: retry through the statistics source, try another available statistics source, provide compatible values manually, remove terms from the scoring scope, explicitly proceed with partial data, or pause until statistics can be fetched.

If the user explicitly chooses partial data, warn that incomplete terms will not receive `Strategic score`, will not contribute to `## Word Value Scores`, and may be omitted or underweighted during metadata generation.

If outdated statistics are refreshed, clear `Strategic score` for rows where `Popularity` or `Difficulty` changes, is removed, remains missing after an attempted refresh, or is reattempted after being stale.

## Metric Validation

Store `Popularity` and `Difficulty` as `1`-`100` scoring inputs.

Use these rules:

- Accept only source-provided popularity and difficulty scores on a documented `0`-`100` scale.
- If a source value is `0`, store it as `1`.
- Preserve source values from `1` to `100` as-is.
- Accept user-provided Apple Ads Search Popularity on a `1`-`5` scale as a popularity proxy only.
- Normalize Apple Ads Search Popularity as `1 -> 5`, `2 -> 20`, `3 -> 40`, `4 -> 60`, and `5 -> 80`.
- Store normalized Apple Ads popularity with `Stats source` as `Apple Ads normalized` and add a compact note such as `Apple Ads Search Popularity 4/5 normalized to 60`.
- Do not infer `Difficulty` from Apple Ads Search Popularity. If no compatible difficulty value is available, leave `Difficulty` blank.
- A statistics run may save normalized Apple Ads popularity while leaving `Difficulty` blank; later strategic scoring will skip rows until difficulty is available.
- If a value is below `0`, above `100`, or not clearly documented as a popularity or difficulty score on an accepted scale, leave the field blank.
- When values are not usable as `0`-`100` scores, record the blocker in `Notes` and ask the user how to deal with those values before continuing.

## Fetching With A Statistics Source

When using any statistics source:

- Use the source according to its own skill, CLI help, API documentation, or user-provided export format.
- Prefer structured output when the source supports it.
- Use the resolved Apple country or region for the run, and derive any tool-specific country or region parameter only at tool-call time.
- Map the requested platform or search surface to tool-specific parameters only at tool-call time using `references/platforms.md`, the tool's skill, CLI help, or documentation.
- Use the app URL or app ID from context when the source supports app-bound statistics, but do not require app-bound data when the user only needs per-search term popularity and difficulty.

Use the returned search term metrics according to `## Metric Validation`. Store the resolved Apple country or region ISO code in `Stats country or region`, the source in `Stats source`, the date in `Stats updated`, and compact notes when a value could not be used. Record unresolved tool-parameter derivation, search-surface preference, or mismatch notes in `Notes`.

If a value is pending or missing:

- Leave that metric blank in the backlog.
- Add a compact note such as `popularity pending`, `difficulty missing`, or `stats unavailable`.
- Do not fill missing values from another source unless the source is explicit and compatible with that country or region.
- Require a user decision before continuing to strategic scoring.

## Saving Results

Store statistics in the canonical `## Search Terms Backlog` table for the active workspace.

For source-locale work:

```markdown
| Search term | Source | Status | Relevance | Popularity | Difficulty | Stats country or region | Stats source | Stats updated | Notes | Strategic score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| example term | app description | confirmed | 4 | 38 | 21 | NLD | ASO Suite | 2026-05-20 | strong feature fit |  |
```

For localized work:

```markdown
| Search term | Meaning | Status | Relevance | Popularity | Difficulty | Stats country or region | Stats source | Stats updated | Notes | Strategic score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| quittung scanner | receipt scanner | confirmed | 5 | 38 | 21 | DEU | ASO Suite | 2026-05-20 | same intent as source core term |  |
```

When updating the table:

- Add missing statistics columns without dropping existing columns.
- Update only confirmed terms unless the user explicitly asks to fetch candidate or rejected terms.
- Preserve rejected terms without assigning popularity or difficulty.
- Preserve existing `Search term`, `Source` when present, `Meaning` when present, `Status`, `Relevance`, and unrelated columns.
- Do not change a term from `confirmed` to `candidate` only because statistics are missing, pending, stale, incompatible, or unusable. Preserve review status and record the metric gap in `Notes`.
- Clear `Strategic score` for rows where `Popularity` or `Difficulty` is added, changed, removed, or left missing after a fetch attempt; preserve it for unchanged rows.
- Fill `Popularity`, `Difficulty`, `Stats country or region`, `Stats source`, and `Stats updated` only for terms with obtained or attempted statistics.
- For localized work, if an imported value was fetched for a different country or region than the resolved country or region, leave popularity and difficulty blank and record the mismatch in `Notes`.
- Store only validated `1`-`100` values in `Popularity` and `Difficulty`.
- Store normalized Apple Ads Search Popularity only in `Popularity`, never in `Difficulty`.
- Use `Stats updated` as `YYYY-MM-DD`.
- Append compact statistics notes to `Notes` only when needed; do not erase existing notes.
- Update `*Last updated:*` in the active context or locale workspace file.

After saving, summarize how many terms were updated, how many had pending or missing values, whether any values were unusable because they were outside the accepted scale, whether any stale statistics were kept, the primary locale or localized workspace used, the primary scoring country or region, any secondary-region validation notes, any derived source country or region parameter, any explicit search-surface preference, and the source used.

Also summarize the platform/statistics scope, the primary scoring platform or search surface when relevant, and whether any platform evidence is being reused or left unvalidated for metadata generation.

If all requested statistics are present, validated, and fresh enough for the run, proceed to strategic scoring. If any requested statistic is missing, pending, stale, incompatible, or unusable, stop after the summary and ask the user how to proceed before strategic scoring. Required options are: retry through the statistics source, try another available statistics source, provide compatible values manually, remove terms from the scoring scope, explicitly proceed with partial data, or pause until statistics can be fetched. If the user chooses partial data, summarize the skipped terms and warn that they will not influence strategic scoring, word value scoring, or generated metadata.

## Common Mistakes

- Guessing popularity or difficulty from relevance, search results, App Store metadata, or web SEO volume.
- Using the US store for every language.
- Mixing values from different countries or regions without recording the country or region per term.
- Treating an iPad search-surface preference as a metadata platform choice.
- Silently reusing one platform's statistics for another platform's `Keywords` field.
- Mixing primary and secondary country or region statistics in the same scoring columns.
- Using values that are neither documented `0`-`100` scores nor explicitly accepted Apple Ads `1`-`5` Search Popularity.
- Storing Apple Ads `1`-`5` Search Popularity without normalizing it first.
- Inferring difficulty from Apple Ads Search Popularity.
- Fetching rejected terms by default.
- Dropping existing relevance scores, notes, statuses, strategic scores, or added backlog columns while adding statistics.
- Changing `confirmed` terms to `candidate` because statistics are missing.
- Leaving stale strategic scores after changing popularity or difficulty.
- Continuing without warning when statistics are more than one month old.
- Continuing to derived scoring when no statistics source is available.
- Continuing to derived scoring with partial statistics unless the user explicitly approved partial data.

## Related Skills

- Use `aso-context` to create or update shared app context.
- Use `aso-search-terms-identification` to create or expand the search term backlog and assign relevance scores before prioritization.
- Use `aso-search-terms-scoring` to calculate derived priority scores after popularity and difficulty are saved.
