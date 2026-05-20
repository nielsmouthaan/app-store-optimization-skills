---
name: aso-search-terms-relevance-scoring
description: Assigns relative 1-5 relevance scores to App Store search terms in the ASO context. Use when reviewing keyword relevance, scoring a search-term backlog, validating ASO search intent fit, or preparing user-reviewed terms for later ASO work. For popularity and difficulty, use aso-search-terms-statistics.
---

# ASO Search Terms Relevance Scoring

Act as an ASO relevance analyst. Help the user score how well each search term in the backlog matches App Store search intent, the app, and the app's ability to satisfy that intent.

Optimize for **consistent, user-validated relevance scoring**. Do not prioritize by volume, competition, metadata placement, or final strategic value. If the user asks for popularity or difficulty, finish or save scoring first and use `aso-search-terms-statistics`; treat prioritization, metadata placement, and final targeting as outside this skill.

## Before Starting

Read `.agents/aso-context.md` first.

If it exists:

- Summarize the app context that matters for relevance scoring.
- Show the existing terms in `## Search Terms Backlog`.
- Preserve existing statuses, sources, relevance scores, statistics, notes, and any additional backlog columns unless the user corrects them.

If it does not exist or lacks meaningful app context:

- Invoke or recommend `aso-context` before continuing.
- Ask only for the minimum app description needed to judge search intent fit.

If `## Search Terms Backlog` is missing or empty:

- Invoke or recommend `aso-search-terms-identification` before continuing.
- Do not invent a backlog only to score it.

## Relevance Score

Use a **1-5 relevance score** to describe how well the app satisfies the App Store search intent behind a term.

| Score | Meaning |
| --- | --- |
| `1` | Very weak fit, mostly ambiguous, unlikely as an App Store query, or likely to disappoint most searchers. |
| `2` | Adjacent, partial, or category-neighbor fit; the app may help some searchers, but it is not a primary App Store expectation. |
| `3` | Relevant but mixed-intent, secondary, or likely to attract many searchers who want a different kind of app. |
| `4` | Strong fit for a meaningful app use case, synonym, feature, audience, or problem, but less central than the app's core category or job-to-be-done. |
| `5` | Own-brand, brand-plus-category, core category, or primary job-to-be-done intent the app directly serves. A `5` term should describe what the user is primarily trying to find, not merely a feature, output, report, or metadata phrase. |

Score terms **relative to the whole backlog**. If two terms have the same level of fit for the app, give them the same score even when they differ in wording, length, or expected search volume.

The app's own brand name and natural brand variants are always highly relevant. Score own-brand terms as `5`; if the brand is also a generic word, note the ambiguity, but do not downgrade the own-brand intent.

Do not penalize broad terms solely because they are broad. If the app is a legitimate strong result for a broad category, core job-to-be-done, or main user outcome, score that term high. Use ambiguity to distinguish `5` from `4` or `3`, not to automatically demote broad terms.

Do not treat a term as highly relevant only because it appears in the app name, subtitle, screenshots, or description. Metadata is useful source evidence, but relevance depends on the app's actual functionality, user value, category, and likely search intent.

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
- **Search phrase shape:** Whether the term is a compact app-search phrase rather than a sentence, UI command, or product-internal label.
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
- Cluster broad core terms, close synonyms, action-object variants, noun-form variants, word-order variants, and app/category suffix variants near each other when they express the same user intent.
- Run a metadata-bias check. A term that appears in current metadata should still pass the same product-fit test as every other term before receiving `5`.
- Apply an ambiguity cap. A broad term with several plausible App Store intents should not receive `5` unless the app is a clearly excellent result for the dominant intent.
- Check `5` and `1` scores last so extreme scores are applied consistently across comparable terms.
- For every proposed `5`, write a one-sentence internal justification: “A user searching this term primarily wants ___, and this app directly provides ___.” If that sentence is weak, ambiguous, or describes only a secondary output, downgrade the term.
- When unsure between two adjacent scores, choose the lower score and mark the term for user review.
- Mark uncertain scores for user review instead of pretending they are precise.

### 4. Present For Validation

Before saving anything, present a review table:

```markdown
| Relevance | Search terms |
| --- | --- |
| Very high | term one; term two; term three |
| High | term one; term two |
| Medium | term one; term two |
| Low | term one; term two |
| Very low | term one |
```

Use compact text labels in the review table so the user can scan the relevance groups quickly. These labels map to the numeric `1`-`5` scores defined in `## Relevance Score`: `Very high` = `5`, `High` = `4`, `Medium` = `3`, `Low` = `2`, and `Very low` = `1`. Save the approved numeric score to the `Relevance` column in `.agents/aso-context.md`.

Require the user to carefully review the proposed relevance groups before saving. Explain that relevance scores are a critical input for later steps in the ASO process; inaccurate relevance scoring can cause later workflow steps to prioritize or use the wrong terms. Do not save scores until the user has explicitly approved or corrected them.

When useful, split the review into groups:

- Core intent terms
- Strong feature or benefit terms
- Broad or mixed-intent terms
- Adjacent or weak-fit terms
- Terms needing user judgment

### 5. Save Approved Scores

Only update `.agents/aso-context.md` after the user has explicitly approved or corrected the scores.

Store relevance in the canonical `## Search Terms Backlog` table:

```markdown
| Search term | Source | Status | Relevance | Popularity | Difficulty | Stats region | Stats source | Stats updated | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| example term | app description | candidate | 4 |  |  |  |  |  | strong feature fit |
```

When updating the table, follow these rules:

- Add a `Relevance` column if it is missing.
- Preserve existing `Search term`, `Source`, `Status`, `Popularity`, `Difficulty`, `Stats region`, `Stats source`, `Stats updated`, `Notes`, and any additional column values.
- Preserve rejected terms without assigning them a relevance score.
- Use only integer scores from `1` to `5`.
- Keep rationale in `Notes` compact and useful for later prioritization.
- Do not overwrite user-confirmed relevance scores unless the user approves the change.
- Update `*Last updated:*` in the context file.

## Common Mistakes

- Scoring terms in isolation instead of calibrating across the whole backlog.
- Using popularity, competition, or ranking difficulty as a proxy for relevance.
- Automatically downgrading broad core category terms even when the app is a legitimate strong result for that intent.
- Giving broad terms high scores when search intent clearly points to a different kind of app.
- Giving feature-internal or UI-action phrases high scores only because the app supports the feature.
- Giving terms high scores only because they already appear in prominent app metadata.
- Giving semantically equivalent terms different scores because of word order, suffixes, or minor modifiers.
- Downgrading the app's own brand terms because the brand is broad or generic.
- Penalizing relevant long-tail terms only because they may have lower volume.
- Scoring competitor brand names as normal target terms instead of using competitor research to find generic alternatives.
- Saving proposed scores before the user reviews them.
- Treating relevance as final truth instead of a user-validated input for later ASO work.
- Overwriting popularity, difficulty, region, source, or statistics date while saving relevance scores.

## Task-Specific Questions

Ask only questions that materially improve scoring:

- "Would a user searching this term expect the app's core workflow, or something adjacent?"
- "Would a user plausibly type this phrase in the App Store?"
- "Does the app fully support this feature today, or is it only related?"
- "Are these two terms equally relevant, or should one score higher?"
- "Should this broad term stay in the backlog with a low relevance score, or be rejected?"
- "Is this term a generic non-brand alternative extracted from competitor research, or a competitor brand name?"

## Related Skills

- Use `aso-context` to create or update shared app context and store the search-term backlog.
- Use `aso-search-terms-identification` to create or expand the backlog before scoring relevance.
- Use `aso-search-terms-statistics` to fetch external popularity and difficulty values after relevance scoring.
