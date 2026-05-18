---
name: aso-search-terms-relevance-scoring
description: Assigns relative 0-5 relevance scores to App Store search terms in the ASO context. Use when reviewing keyword relevance, scoring a search-term backlog, validating ASO search intent fit, or preparing search terms for later prioritization and metadata strategy.
---

# ASO Search Terms Relevance Scoring

Act as an ASO relevance analyst. Help the user score how well each search term in the backlog matches App Store search intent, the app, and the app's ability to satisfy that intent.

Optimize for **consistent, user-validated relevance scoring**. Do not prioritize by volume, competition, metadata placement, or final strategic value unless the user explicitly asks.

## Before Starting

Read `.agents/aso-context.md` first.

If it exists:

- Summarize the app context that matters for relevance scoring.
- Show the existing terms in `## Search Terms Backlog`.
- Preserve existing statuses, sources, relevance scores, and notes unless the user corrects them.

If it does not exist or lacks meaningful app context:

- Invoke or recommend `aso-context` before continuing.
- Ask only for the minimum app description needed to judge search intent fit.

If `## Search Terms Backlog` is missing or empty:

- Invoke or recommend `aso-search-terms-identification` before continuing.
- Do not invent a backlog only to score it.

## Relevance Score

Use a **0-5 relevance score** to describe how well the app satisfies the App Store search intent behind a term.

| Score | Meaning |
| --- | --- |
| `0` | Irrelevant, misleading, or clearly not an intent the app should target. |
| `1` | Very weak fit, mostly ambiguous, unlikely as an App Store query, or likely to disappoint most searchers. |
| `2` | Adjacent or partial fit; the app may help some searchers, but it is not a primary App Store expectation. |
| `3` | Relevant, but broad, mixed-intent, or not one of the app's strongest promises. |
| `4` | Strong fit for a meaningful app use case, feature, audience, or problem. |
| `5` | Exact or core intent the app directly serves and should confidently satisfy. |

Score terms **relative to the whole backlog**. If two terms have the same level of fit for the app, give them the same score even when they differ in wording, length, or expected search volume.

## Scoring Workflow

### 1. Review Existing Context

Use `.agents/aso-context.md` as the canonical source for:

- App name, subtitle, category, and description
- Features, use cases, and problem language
- Screenshot text and review themes
- Competitors and similar apps
- Existing saved search terms, statuses, notes, and relevance scores

Call out obvious gaps only when they block reliable scoring.

### 2. Interpret Search Intent

For each non-rejected term, infer what a searcher probably wants.

Consider:

- **Specificity:** Long-tail terms often reveal clearer intent than short, broad terms.
- **App Store query fit:** Whether the term sounds like something a user would type in the App Store to find an app.
- **Feature fit:** Whether the app directly offers the feature, workflow, content, or outcome implied by the term.
- **Audience fit:** Whether the likely searcher is part of the app's intended audience.
- **Problem fit:** Whether the app solves the problem implied by the term.
- **Category fit:** Whether the term belongs to the app's category or an adjacent category.
- **Ambiguity:** Whether the same term could mean unrelated things in the App Store.
- **Search-result evidence:** If available, whether top-ranking apps for the term satisfy a different intent.
- **User evidence:** Whether user wording, reviews, support requests, or provided source material confirm the intent.

Do not treat product-feature fit alone as relevance. A term can describe a real feature but still deserve a low score if it is unlikely to be used as an App Store search.

Do not treat search volume as relevance. A high-volume term can be irrelevant, and a low-volume term can be highly relevant.

### 3. Calibrate Scores

Before presenting scores, compare terms across the backlog:

- Group terms that express the same or similar intent.
- Make sure equivalent relevance receives equivalent scores.
- Check `5` and `0` scores last so extreme scores are applied consistently across comparable terms.
- When unsure between two adjacent scores, choose the lower score and mark the term for user review.
- Mark uncertain scores for user review instead of pretending they are precise.

### 4. Present For Validation

Before saving anything, present a review table:

```markdown
| Search term | Proposed relevance | Rationale |
| --- | --- | --- |
| example term | 4 | Strong feature fit; search intent matches a core workflow. |
```

Ask the user to validate, correct, or reject the proposed scores. Make clear that later ASO prioritization depends on accurate relevance scoring.

When useful, split the review into groups:

- Core intent terms
- Strong feature or benefit terms
- Broad or mixed-intent terms
- Adjacent or weak-fit terms
- Irrelevant or misleading terms
- Terms needing user judgment

### 5. Save Approved Scores

Only update `.agents/aso-context.md` after the user has explicitly approved or corrected the scores.

Store relevance in the same `## Search Terms Backlog` table:

```markdown
| Search term | Source | Status | Relevance | Notes |
| --- | --- | --- | --- | --- |
| example term | app description | candidate | 4 | strong feature fit |
```

When updating the table, follow these rules:

- Add a `Relevance` column if it is missing.
- Preserve existing `Search term`, `Source`, `Status`, and `Notes` values.
- Preserve rejected terms, but leave relevance blank unless the user wants rejected terms scored.
- Use only integer scores from `0` to `5`.
- Keep rationale in `Notes` compact and useful for later prioritization.
- Do not overwrite user-confirmed relevance scores unless the user approves the change.
- Update `*Last updated:*` in the context file.

## Common Mistakes

- Scoring terms in isolation instead of calibrating across the whole backlog.
- Using popularity, competition, or ranking difficulty as a proxy for relevance.
- Giving broad category words high scores when search intent is unclear.
- Giving feature-internal or UI-action phrases high scores only because the app supports the feature.
- Penalizing relevant long-tail terms only because they may have lower volume.
- Scoring competitor brand names as usable targets without noting legal or metadata risk.
- Saving proposed scores before the user reviews them.
- Treating relevance as final truth instead of a user-validated input for later ASO work.

## Task-Specific Questions

Ask only questions that materially improve scoring:

- "Would a user searching this term expect the app's core workflow, or something adjacent?"
- "Would a user plausibly type this phrase in the App Store?"
- "Does the app fully support this feature today, or is it only related?"
- "Are these two terms equally relevant, or should one score higher?"
- "Should this broad term stay in the backlog with a low relevance score, or be rejected?"
- "Is this competitor-derived term safe to keep only as research context?"

## Related Skills

- Use `aso-context` to create or update shared app context and store the search-term backlog.
- Use `aso-search-terms-identification` to create or expand the backlog before scoring relevance.
- Use future prioritization skills to combine relevance with popularity, difficulty, and strategic value.
