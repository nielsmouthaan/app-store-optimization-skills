---
name: aso-search-terms-word-value-scoring
description: Calculates per-word ASO metadata value scores from confirmed search terms and their Strategic score values in `.agents/aso-context.md`. Use after aso-search-terms-strategic-scoring when prioritizing individual words for character-limited App Store metadata fields, keyword coverage, or metadata planning.
---

# ASO Search Terms Word Value Scoring

Act as an ASO metadata efficiency analyst. Calculate which individual words deliver the most strategic search-term coverage per metadata character.

Word value is derived data. Do not invent missing strategic scores, change search-term scores, fetch statistics, assign metadata fields, or decide final metadata placement.

## Before Starting

Read `.agents/aso-context.md` first.

If it exists:

- Summarize the search-term backlog inputs that matter for word value scoring.
- Show confirmed terms in `## Search Terms Backlog` with their `Strategic score`.
- Preserve existing statuses, sources, relevance scores, statistics, strategic scores, notes, and any additional backlog columns unless the user corrects them.

If it does not exist or lacks meaningful app context:

- Invoke or recommend `aso-context` before continuing.
- Abort word value scoring until app context exists.

If `## Search Terms Backlog` is missing or empty:

- Invoke or recommend `aso-search-terms-identification` before continuing.
- Abort word value scoring until search terms exist.

If confirmed terms are missing `Strategic score` values:

- Use `aso-search-terms-strategic-scoring` first.
- Do not estimate missing strategic scores or calculate word values from relevance, popularity, or difficulty directly.

## Word Value Score

Calculate scores only from search-term rows where:

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
- `Value` is the per-character efficiency score.

Store `Total strategic score` and `Value` rounded to the nearest whole number, with no percent sign. Store `Appearances` and `Length` as integers.

## Word Normalization

Normalize words before calculating:

- Lowercase words for matching and display.
- Trim leading and trailing punctuation.
- Split search terms on whitespace and punctuation that separates words, such as commas, slashes, pipes, parentheses, and hyphens.
- Do not stem, singularize, pluralize, translate, or merge related forms. Treat `edit`, `editing`, and `editor` as separate words.
- Do not transliterate or remove accents. Count the written characters in the normalized word.
- Count a word only once per search term, even if the same word appears more than once in that term.

If duplicate normalized search-term rows exist:

- If duplicates have the same `Strategic score`, count the search term once.
- If duplicates have conflicting `Strategic score` values, stop and ask the user to resolve the duplicate rows before calculating.

## Scoring Workflow

### 1. Review Inputs

Use `.agents/aso-context.md` as the canonical source for:

- Existing saved search terms, statuses, notes, and strategic scores

Check every backlog row before calculating. Separate rows into:

- **Eligible:** confirmed terms with numeric strategic scores.
- **Skipped:** candidate, rejected, incomplete, invalid, duplicate-conflicting, or missing-score rows.

If there are no eligible rows, stop after explaining which upstream step is missing.

### 2. Calculate Word Scores

For each eligible search term:

1. Normalize the search term into individual words.
2. Add the term's full `Strategic score` to each word that appears in the term.
3. Increase that word's `Appearances` by `1`.
4. After all terms are processed, calculate `Value = Total strategic score / Length`.

Do not divide a term's strategic score across its words. Each word receives the full strategic score contribution from every eligible search term it helps cover.

When presenting results, sort words by `Value` from highest to lowest. Break ties by `Total strategic score` descending, then `Appearances` descending, then `Word` ascending:

```markdown
| Word | Appearances | Total strategic score | Length | Value |
| --- | --- | --- | --- | --- |
| movie | 3 | 653 | 5 | 131 |
| maker | 2 | 268 | 5 | 54 |
```

Briefly summarize skipped rows only when the reason is useful for the user, such as missing strategic scores or duplicate conflicts.

### 3. Save Results

Update `.agents/aso-context.md` by adding or replacing a `## Word Value Scores` section:

```markdown
## Word Value Scores
| Word | Appearances | Total strategic score | Length | Value |
| --- | --- | --- | --- | --- |
| movie | 3 | 653 | 5 | 131 |
```

When updating the context:

- Add the section after `## Search Terms Backlog` when it is missing.
- Replace only the `## Word Value Scores` table when the section already exists.
- Update only `## Word Value Scores` and `*Last updated:*`.
- Preserve all search-term backlog rows and columns.
- Use `YYYY-MM-DD` for `*Last updated:*`.
- Sort saved rows with the same order used for presentation.

After saving, summarize how many eligible search terms were used, how many unique words were scored, how many rows were skipped, and the highest-value words.

## Common Mistakes

- Calculating word values before strategic scores exist.
- Using relevance, popularity, difficulty, or search volume directly instead of the saved `Strategic score`.
- Counting candidate or rejected terms.
- Dividing a search term's strategic score across its words.
- Merging related words through stemming, singularization, pluralization, translation, or synonym logic.
- Counting repeated words inside one search term more than once.
- Using byte length, phrase length, or metadata field length instead of normalized word character length.
- Editing backlog inputs while saving derived word-value results.
- Treating word value as final metadata placement instead of a character-efficiency signal.

## Related Skills

- Use `aso-context` to create or update shared app context.
- Use `aso-search-terms-identification` to create or expand the search-term backlog.
- Use `aso-search-terms-relevance-scoring` to assign user-reviewed relevance.
- Use `aso-search-terms-statistics` to fetch popularity and difficulty.
- Use `aso-search-terms-strategic-scoring` to calculate strategic scores before word value scoring.
