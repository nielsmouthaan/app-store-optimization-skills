---
name: aso-search-terms-strategic-scoring
description: Calculates derived strategic scores for confirmed App Store search terms in `.agents/aso-context.md` using relevance, popularity, and difficulty. Use after aso-search-terms-relevance-scoring and aso-search-terms-statistics when prioritizing verified terms for ASO metadata planning, keyword focus, or backlog ranking.
---

# ASO Search Terms Strategic Scoring

Act as an ASO prioritization analyst. Calculate a deterministic strategic score for confirmed search terms so later metadata work can focus on terms with the best mix of demand, ranking feasibility, and app fit.

The strategic score is derived data. Do not invent missing inputs, change subjective relevance scores, fetch statistics, assign metadata fields, or decide final metadata placement.

## Before Starting

Read `.agents/aso-context.md` first.

If it exists:

- Summarize the search-term backlog inputs that matter for strategic scoring.
- Show confirmed terms in `## Search Terms Backlog` with their `Relevance`, `Popularity`, `Difficulty`, and existing `Strategic score`.
- Preserve existing statuses, sources, relevance scores, statistics, notes, and any additional backlog columns unless the user corrects them.

If it does not exist or lacks meaningful app context:

- Invoke or recommend `aso-context` before continuing.
- Abort strategic scoring until app context exists.

If `## Search Terms Backlog` is missing or empty:

- Invoke or recommend `aso-search-terms-identification` before continuing.
- Abort strategic scoring until search terms exist.

If confirmed terms are missing relevance, popularity, or difficulty values:

- Use `aso-search-terms-relevance-scoring` for missing or unapproved relevance.
- Use `aso-search-terms-statistics` for missing popularity or difficulty.
- Do not estimate missing inputs or score incomplete rows.

If confirmed terms have `Stats updated` values more than one month older than the current date:

- Use `aso-search-terms-statistics` to offer a statistics refresh before scoring when that has not already happened.
- If the user declines the refresh or explicitly asks to continue, calculate scores with existing values and include a stale-statistics warning in the summary.

## Strategic Score

Calculate scores only for rows where:

- `Status` is exactly `confirmed`.
- `Relevance` is an integer from `1` to `5`.
- `Popularity` is validated numeric from `1` to `100`.
- `Difficulty` is validated numeric from `1` to `100`.

Use this formula exactly:

```text
Strategic score = 100 * (Popularity / 100)^0.8 * ((101 - Difficulty) / 100) * (Relevance / 5)^1.5
```

Store `Strategic score` as a `0`-`100` value rounded to one decimal, with no percent sign.

Leave `Strategic score` blank for candidate, rejected, incomplete, or invalid rows. If an existing strategic score is present for a row that is no longer eligible, clear it.

Do not rescale, normalize, or infer input values in this skill. If popularity or difficulty values are missing, unclear, or outside the validated `1`-`100` range, use `aso-search-terms-statistics` to obtain valid values before calculating.

The formula intentionally dampens popularity so broad high-volume terms do not dominate by volume alone, converts difficulty into ranking feasibility with easier terms scoring higher, and weights relevance strongly because a term is strategically useful only when the app satisfies the search intent.

## Scoring Workflow

### 1. Review Inputs

Use `.agents/aso-context.md` as the canonical source for:

- Existing saved search terms, statuses, notes, relevance scores, and statistics

Check every backlog row before calculating. Separate rows into:

- **Eligible:** confirmed terms with complete valid inputs.
- **Skipped:** candidate, rejected, incomplete, invalid, or out-of-range rows.

If there are no eligible rows, stop after explaining which upstream step is missing.

### 2. Calculate Scores

Calculate each eligible row with the exact formula in `## Strategic Score`.

When presenting results, sort terms by `Strategic score` from highest to lowest:

```markdown
| Search term | Relevance | Popularity | Difficulty | Strategic score |
| --- | --- | --- | --- | --- |
| example term | 5 | 50 | 40 | 34.5 |
```

Briefly summarize skipped rows only when the reason is useful for the user, such as missing relevance or missing statistics.

### 3. Save Results

Update `.agents/aso-context.md` under `## Search Terms Backlog` using the canonical table:

```markdown
| Search term | Source | Status | Relevance | Popularity | Difficulty | Stats region | Stats source | Stats updated | Notes | Strategic score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| example term | app description | confirmed | 5 | 50 | 40 | NL | ASO Suite | 2026-05-20 | core category term | 34.5 |
```

When updating the table:

- Add a `Strategic score` column as the last column if it is missing.
- Update only the `Strategic score` column and `*Last updated:*`.
- Recalculate and overwrite existing strategic scores for eligible rows.
- Clear `Strategic score` for candidate, rejected, incomplete, invalid, or out-of-range rows.
- Preserve `Search term`, `Source`, `Status`, `Relevance`, `Popularity`, `Difficulty`, `Stats region`, `Stats source`, `Stats updated`, `Notes`, and any additional column values.
- Use `YYYY-MM-DD` for `*Last updated:*`.

After saving, summarize how many terms were scored, how many were skipped, and the highest-scoring terms.

## Common Mistakes

- Scoring candidate or rejected terms.
- Guessing relevance, popularity, or difficulty values to make the formula work.
- Calculating strategic scores from popularity or difficulty values that `aso-search-terms-statistics` did not validate.
- Using popularity alone as the priority order.
- Treating the strategic score as subjective user input instead of derived data.
- Leaving stale strategic scores after relevance, popularity, difficulty, or status changes.
- Ignoring stale-statistics warnings when `Stats updated` is more than one month old.
- Changing search-term status, relevance, statistics, notes, or metadata placement while saving scores.
- Continuing to metadata writing when no confirmed terms have complete scoring inputs.

## Related Skills

- Use `aso-context` to create or update shared app context.
- Use `aso-search-terms-identification` to create or expand the search-term backlog.
- Use `aso-search-terms-relevance-scoring` to assign user-reviewed relevance.
- Use `aso-search-terms-statistics` to fetch popularity and difficulty before strategic scoring.
- Use `aso-search-terms-word-value-scoring` after strategic scoring to calculate per-word metadata value scores.
