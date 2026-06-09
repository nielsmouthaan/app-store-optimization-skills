---
name: aso-search-terms-scoring
description: Calculates strategic scores and per-word value scores for confirmed App Store search terms. Use after relevance scoring and popularity/difficulty statistics when prioritizing keywords for App Store optimization metadata planning, keyword focus, character-limited metadata fields, or metadata generation.
---

# ASO Search Terms Scoring

Act as an ASO scoring analyst. Calculate derived scoring outputs that help later metadata work focus on terms and words with the best mix of demand, ranking feasibility, app fit, and metadata character efficiency.

Search term scoring is derived data. Do not invent missing inputs, change subjective relevance scores, fetch statistics, assign metadata fields, or decide final metadata placement.

## Before Starting

Read `.agents/aso/context.md` first.

If the user is working on a localized workspace, also read the relevant `.agents/aso/locales/<Locale>/context.md` file and calculate scores only inside that localized workspace.

If it exists:

- Summarize the search-term backlog inputs that matter for scoring.
- Show confirmed terms in `## Search Terms Backlog` with `Relevance`, `Popularity`, `Difficulty`, `Stats updated`, and existing `Strategic score`.
- Show existing `## Word Value Scores` when present.
- Preserve existing statuses, sources, relevance scores, statistics, notes, and any additional backlog columns unless the user corrects them.

If it does not exist or lacks meaningful app context:

- Invoke or recommend `aso-context` before continuing.
- Abort scoring until app context exists.

If `## Search Terms Backlog` is missing or empty:

- Invoke or recommend `aso-search-terms-identification` before continuing.
- Abort scoring until search terms exist.

If confirmed terms are missing relevance, popularity, or difficulty values:

- Use `aso-search-terms-relevance-scoring` for missing or unapproved relevance.
- Use `aso-search-terms-statistics` for missing popularity or difficulty.
- Do not estimate missing inputs or score incomplete rows.
- Treat relevance scores `1` and `2` as lower relative relevance, not as automatic exclusions.

If confirmed terms have `Stats updated` values more than one month older than the current date:

- Use `aso-search-terms-statistics` to offer a statistics refresh before scoring when that has not already happened.
- If the user declines the refresh or explicitly asks to continue, calculate scores with existing values and include a stale-statistics warning in the summary.

## Scoring Workflow

Run search term scoring as one workflow with two ordered internal stages:

1. Calculate or refresh `Strategic score` values for eligible confirmed search terms.
2. Calculate or refresh `## Word Value Scores` from confirmed terms with numeric `Strategic score`.

If strategic scores are already current and the user only asks for word value scores, skip directly to the word value stage after verifying the inputs.

## Strategic Score

Calculate strategic scores only for rows where:

- `Status` is exactly `confirmed`.
- `Relevance` is an integer from `1` to `5`.
- `Popularity` is validated numeric from `1` to `100`.
- `Difficulty` is validated numeric from `1` to `100`.

Do not exclude a confirmed term only because its relevance is `1` or `2`. Low relevance can still be useful as a planning signal when the user confirmed the term and statistics are valid; the formula discounts it strongly.

Use this skill suite's derived prioritization formula exactly. Apple does not publish a strategic keyword scoring formula; this model is a planning aid that combines relevance, popularity, difficulty, and reachability for later metadata decisions.

```text
Strategic score = 100 * (Popularity / 100)^0.8 * ((101 - Difficulty) / 100) * (Relevance / 5)^1.5
```

Store `Strategic score` as a `0`-`100` value rounded to one decimal, with no percent sign.

Leave `Strategic score` blank for candidate, rejected, incomplete, or invalid rows. If an existing strategic score is present for a row that is no longer eligible, clear it.

Do not rescale, normalize, or infer input values in this skill. If popularity or difficulty values are missing, unclear, or outside the validated `1`-`100` range, use `aso-search-terms-statistics` to obtain valid values before calculating.

The formula intentionally dampens popularity so broad high-volume terms do not dominate by volume alone, converts difficulty into ranking feasibility with easier terms scoring higher, and weights relevance strongly because a term is strategically useful only when the app satisfies the search intent.

When presenting strategic scores, sort terms by `Strategic score` from highest to lowest:

```markdown
| Search term | Relevance | Popularity | Difficulty | Strategic score |
| --- | --- | --- | --- | --- |
| example term | 5 | 50 | 40 | 34.5 |
```

When inferable from terms, sources, or `Notes`, mention obvious portfolio patterns or imbalances that later metadata generation should consider, such as overreliance on broad head terms, long-tail terms, seasonal terms, or questionable terms. Do not save a separate portfolio section or add portfolio columns.

## Word Value Score

Calculate word value scores only from search-term rows where:

- `Status` is exactly `confirmed`.
- `Strategic score` is numeric.

For each individual word, use this formula exactly:

```text
Value = Total strategic score / Length
```

Where:

- `Appearances` is the count of eligible search terms that contain the word.
- `Total strategic score` is the sum of `Strategic score` values from every eligible search term that contains the word.
- `Length` is the character count of the normalized word.
- `Value` is the per-character efficiency score for metadata planning.

Store `Total strategic score` and `Value` rounded to the nearest whole number, with no percent sign. Store `Appearances` and `Length` as integers.

Normalize words before calculating:

- Lowercase words for matching and display.
- Trim leading and trailing punctuation.
- Split search terms on whitespace and punctuation that separates words, such as commas, slashes, pipes, parentheses, and hyphens.
- For languages without reliable whitespace word boundaries, use a language-aware tokenizer when available. If none is available, use conservative whole-term or obvious-segment tokens, record the tokenizer choice in the summary, and do not pretend the word value scores are directly comparable to whitespace-segmented locales.
- Do not stem, singularize, pluralize, translate, or merge related forms. Treat `edit`, `editing`, and `editor` as separate words.
- Do not transliterate or remove accents. Count the written characters in the normalized word.
- Count a word only once per search term, even if the same word appears more than once in that term.

If duplicate normalized search-term rows exist:

- If duplicates have the same `Strategic score`, count the search term once.
- If duplicates have conflicting `Strategic score` values, stop and ask the user to resolve the duplicate rows before calculating.

Do not divide a term's strategic score across its words. Each word receives the full strategic score contribution from every eligible search term it helps cover.

When presenting word values, sort words by `Value` from highest to lowest. Break ties by `Total strategic score` descending, then `Appearances` descending, then `Word` ascending:

```markdown
| Word | Appearances | Total strategic score | Length | Value |
| --- | --- | --- | --- | --- |
| movie | 3 | 653 | 5 | 131 |
| maker | 2 | 268 | 5 | 54 |
```

## Saving Results

Update `.agents/aso/context.md` after calculating source-locale derived scores. For localized work, update the active `.agents/aso/locales/<Locale>/context.md` file instead.

For `## Search Terms Backlog`:

- Add a `Strategic score` column as the last column if it is missing.
- Update only the `Strategic score` column and `*Last updated:*`.
- Recalculate and overwrite existing strategic scores for eligible rows.
- Clear `Strategic score` for candidate, rejected, incomplete, invalid, or out-of-range rows.
- Preserve `Search term`, `Source` when present, `Meaning` when present, `Status`, `Relevance`, `Popularity`, `Difficulty`, `Stats country or region`, `Stats source`, `Stats updated`, `Notes`, and any additional column values.

For `## Word Value Scores`:

- Add the section after `## Search Terms Backlog` when it is missing.
- Replace only the `## Word Value Scores` table when the section already exists.
- Update only `## Word Value Scores` and `*Last updated:*`.
- Preserve all search-term backlog rows and columns.
- Sort saved rows with the same order used for presentation.

Use `YYYY-MM-DD` for `*Last updated:*`.

After saving, summarize how many terms received strategic scores, how many terms were skipped, how many unique words were scored, whether stale statistics were used, the workspace updated, the highest-scoring terms and words, and any obvious portfolio imbalance when useful.

## Common Mistakes

- Scoring candidate or rejected terms.
- Guessing relevance, popularity, or difficulty values to make the formula work.
- Calculating strategic scores from popularity or difficulty values that `aso-search-terms-statistics` did not validate.
- Treating relevance `1` or `2` as rejected or unscorable after the user confirmed the term.
- Ignoring stale-statistics warnings when `Stats updated` is more than one month old.
- Using popularity alone as the priority order.
- Treating one sorted strategic-score list as the final metadata portfolio.
- Treating strategic scores or word value scores as subjective user inputs instead of derived data.
- Leaving stale strategic scores after relevance, popularity, difficulty, or status changes.
- Calculating word values before valid strategic scores exist.
- Dividing a search term's strategic score across its words.
- Merging related words through stemming, singularization, pluralization, translation, or synonym logic.
- Applying English tokenization, singular/plural, stemming, or transliteration assumptions to localized workspaces.
- Counting repeated words inside one search term more than once.
- Editing backlog inputs while saving derived word-value results.
- Treating word value as final metadata placement instead of a character-efficiency signal.

## Related Skills

- Use `aso-context` to create or update shared app context.
- Use `aso-search-terms-identification` to create or expand the search-term backlog.
- Use `aso-search-terms-relevance-scoring` to assign user-reviewed relevance.
- Use `aso-search-terms-statistics` to fetch popularity and difficulty before scoring.
- Use `aso-metadata-generation` after scoring to generate metadata drafts from strategic scores and word value scores.
