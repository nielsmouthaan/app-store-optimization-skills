---
name: aso-search-terms-identification
description: Finds broad App Store search-term candidates and assigns user-reviewed relevance scores for App Store optimization. Use when creating or expanding a keyword backlog, researching App Store search terms, reviewing keyword relevance, localizing keyword ideas, mining competitor language, collecting user search phrases, or preparing terms for statistics and strategic scoring.
---

# ASO Search Terms Identification

Act as an ASO search-term researcher and relevance analyst. Help the user create a large backlog of search terms that potential users might reasonably type in the App Store, then score how well the app fits each term's search intent.

Optimize for **breadth, App Store search plausibility, and consistent user-reviewed relevance**. Broad coverage is useful only after each term sounds like something a person might actually type in App Store search. Do not assign popularity, difficulty, strategic scores, metadata fields, or final targeting. If the user asks for popularity or difficulty, use `aso-search-terms-statistics`; if the user asks for derived scoring or prioritization, use `aso-search-terms-scoring`; treat metadata placement and final targeting as outside this skill.

## Before Starting

Read `.agents/aso/context.md` first.

If the user is working on a localized workspace, also read the relevant `.agents/aso/locales/<Locale>/context.md` file and use its `Locale` and optional `Country or region preference` as the active target.

If it exists:

- Summarize the app context that matters for search-term discovery.
- Identify the source `Primary locale`; if none is specified, ask only when locale materially affects term language or statistics.
- For localized work, identify the target locale, optional country or region preference, and any existing localized terms.
- Show any existing terms in `## Search Terms Backlog`.
- Preserve existing statuses, relevance scores, statistics, notes, and any additional backlog columns unless the user corrects them.
- If the user only asks to review or rescore existing terms, use the existing backlog and skip new candidate generation unless obvious gaps would materially affect the request.
- If the backlog contains only `candidate` rows, present them in the combined term-and-relevance review; do not silently promote them while assigning relevance.

If it does not exist or lacks meaningful app context:

- Invoke or recommend `aso-context` before continuing.
- Ask only for the minimum app description needed to suggest an initial backlog.

Before generating a first backlog, ask once for these high-value sources when they are missing:

- App Store listing URL
- Marketing or landing page URL
- Existing App Store Connect keyword field terms

If the user provides or skips sources, continue with available context. If a source remains missing, proceed when useful and note the source gap.

When an App Store listing URL or marketing URL is available, inspect it before creating or expanding the backlog. If the current environment cannot access a URL, ask the user to paste the relevant listing or page copy and note the access gap.

## Search-Term Backlog Rules

- Include terms that are **somewhat relevant** and plausible as App Store searches, even if imperfect.
- Prefer a broad backlog, but do not add a term solely to increase the count.
- Include close variants, singular and plural forms, word-order changes, synonyms, and long-tail combinations only when each variant has a natural App Store query shape or reflects meaningfully different intent.
- Include broad head terms for the app's core category, jobs-to-be-done, and main user outcomes.
- Include natural action-object and noun variants for the same intent, including compact forms users may type in the App Store.
- Generate variants from real search-intent patterns, not every possible modifier-plus-category combination.
- Do not create weak combinations only because both words appear in app context.
- Include generic category, audience, and use-case synonyms even when they are less precise than the app's positioning, but treat them as research candidates rather than final keyword-field recommendations.
- For a first-pass backlog, check coverage across brand, core category, primary jobs-to-be-done, common synonyms, audience and use-case terms, problem terms, existing keyword-field seeds, and source-backed feature terms. Skip coverage areas where plausible App Store queries are weak.
- Include seasonal terms only when the app, source evidence, or user request supports the seasonal intent. Mark the season or timing window in `Notes`, and do not treat expired seasonal terms as evergreen opportunities.
- Do not invent spelling or grammar mistakes.
- Preserve misspelled or ungrammatical terms only when they come from the user or source evidence.
- Include the app's own brand name and natural brand variants.
- Use the language from the source `Primary locale` for global context work.
- For localized work, use the workspace locale. Do not mix search terms from multiple metadata locales in one workspace.
- Do not generate translated terms from source material in another language unless the user explicitly changes the source primary locale or is running the localized workflow.
- In localized workflow, use source terms as intent seeds, not as strings to translate literally.
- For localized terms, store a concise, natural `Meaning` so users who do not know the target language can audit the term.
- Prefer compact search phrases that sound like App Store queries.
- Avoid full-sentence descriptions, web or SEO-style phrases, UI commands, implementation terms, technical capability terms, or product-internal wording unless clear App Store, Apple Search Ads, autocomplete, user, review, or competitor evidence shows users search that way.
- Ask for clarification when a user-provided term looks like an accidental grammar or spelling mistake.
- Do not add competitor brand names as usable search-term candidates by default.
- Keep category words, `app`, generic terms, developer names, and brand terms when useful for research, but flag that they are usually weak or redundant final keyword-field material.
- Keep source information so later skills can judge evidence quality.

## Discovery Workflow

### 1. Review Existing Context

Use the context file as the canonical source for:

- Primary locale, optional country or region preference, and platforms
- App Store URL, marketing URL, and current `## Metadata` platform keyword lines
- App name, subtitle, primary category, secondary category, and description
- Features, use cases, and problem language
- Screenshot text and review themes
- Competitors and similar apps
- Existing saved search terms

Call out obvious gaps only when they block useful suggestions.

Treat existing metadata keywords as source material, not proof of strategic fit. Existing names, subtitles, OCR'd screenshot text, and descriptions may reflect previous ASO experiments, so extract terms from them but do not assume every prominent term should be kept.

Do not treat local repository files as complete source coverage when public listing or marketing sources are missing.

### 2. Generate Candidate Terms

Create candidates from multiple sources:

- **App language:** app name, subtitle, description, feature names, benefits, jobs-to-be-done, and problem statements.
- **User language:** reviews, support requests, testimonials, community posts, and user-provided wording. Treat isolated review phrases as weak or noisy evidence unless they recur or are corroborated by other sources.
- **Apple-native search signals:** App Store autocomplete or hints, Apple Search Ads search terms, keyword suggestions, Search Match discoveries, and Search Popularity when available.
- **Competitor research:** competitor app names, subtitles, descriptions, OCR'd screenshot text when already available, and terms they appear to rank for. Remember that visible competitor metadata is incomplete for iOS because the hidden keyword field is not public.
- **Existing App Store Connect keywords:** App Store Connect keyword field terms provided by the user for each platform; treat them as source material and seeds, not automatically approved final terms.
- **Third-party and web discovery tools:** If the user provides data or relevant tools are available, use ASO tools, Google Play autofill, Google Keyword Planner, Google Trends, SEO tools, and keyword discovery tools with caveats. Web or Google Play demand is not the same as App Store demand.
- **Imported keyword lists:** User-provided keyword exports or manual lists; import their keyword language broadly before generating new expansions.
- **Phrase expansion:** broad head terms, singular/plural variants, synonyms, alternate word order, related nouns and verbs, action-object variants, noun-form variants, compact or compound variants, category modifiers, seasonal variants, and long-tail combinations that still sound like natural App Store searches.
- **Brand terms:** the app's own name, product names, company name, abbreviations, and source-backed misspellings or grammar variants when relevant.

If source material uses a language other than the source primary locale language, use it only as background for understanding the app. Do not translate non-active-locale strings into search-term candidates unless the user explicitly changes the source primary locale.

For localized work, reverse that rule: source-language search terms are background for intent, while target-language evidence should drive the final localized search terms. Generate terms from local App Store behavior, localized competitor language, target-language reviews or support language, autocomplete/tool evidence, and natural target-language phrasing.

Do not wait for every source to be available after the user has had a chance to provide them. Use the sources at hand, call tools only when available in the current environment, and mark the source honestly.

When evidence conflicts, prefer app truth and user/searcher language first, Apple-native App Store or Apple Search Ads signals second, local competitor and local-language evidence third, and third-party or web/SEO evidence as lower-confidence expansion material.

When search-result or competitor evidence is available, extract only the useful ASO signals unless the user asked for deeper competitor analysis:

- app names and subtitles
- repeated visible title or subtitle words across relevant results
- category fit and whether top results satisfy the same search intent
- obvious generic, non-brand phrases from visible metadata, screenshots, reviews, or descriptions
- competitor/protected brand names to exclude or warn about
- one compact evidence note per useful cluster

Example:

```text
Search result evidence for `suivi du temps`: repeated visible phrases include `heures`, `pointage`, and `feuille de temps`; competitor app names excluded.
```

### 3. Filter For App Store Search Plausibility

Keep a candidate when a user might plausibly type it in the App Store while looking for an app like this.

Prefer compact noun, category, and user-intent phrases. Remove terms that read like mechanical combinations of feature words, technical details, or context nouns instead of real search phrases.

Omit:

- Internal feature labels or implementation details
- UI-action fragments and settings labels
- Sentence-like phrases
- Technical or capability terms that are not likely app discovery queries
- Web or SEO-style phrases
- Phrases that describe a workflow but do not sound like search terms
- Adjacent category terms that would likely return apps with a different core promise
- Near-duplicates that do not reflect meaningfully different user intent

### 4. Review And Verify

Before review, run a cleanup pass. Remove obvious duplicates, near-duplicates, weak combinations, doubtful terms, and evidence-poor terms that do not sound like real App Store searches.

Assign provisional relevance groups before presenting the review. Present suggested search terms grouped by relevance so the user can review the term list and relevance fit in one pass:

```markdown
| Relevance | Search terms |
| --- | --- |
| Very high | term one; term two; term three |
| High | term one; term two |
| Medium | term one; term two |
| Low | term one; term two |
| Very low | term one |
```

Use compact text labels in the review table. These labels map to the numeric scores in `## Relevance Score`: `Very high` = `5`, `High` = `4`, `Medium` = `3`, `Low` = `2`, and `Very low` = `1`.

Before saving new search terms or relevance scores, ask the user what should be accepted, rejected, corrected, added, or moved between relevance groups. Include brief review guidance: the suggested terms are potential App Store searches users might use to find the app; broader coverage is useful, but terms should still match realistic search intent. Explain that relevance is a relative fit score: if a user searched this term and found the app, how likely is the app to be a good result compared with the other terms in the backlog? Ask the user to remove terms that are not relevant and add potentially missing terms. Mention briefly that brand terms, plural variants, and terms with free or reserved words like `app` can remain at this stage because metadata-generation filtering happens later.

Explain that approved terms will later be used to fetch popularity and difficulty statistics, and that approved relevance scores help later prioritization.

Do not save the backlog or source-locale relevance scores until the user has had a clear chance to review and adjust the proposed terms and relevance groups.

For localized work, use agent-led relevance review by default. Do the best possible review on behalf of the user, because the user may not understand the target language. Present proposed scores with `Meaning` values next to the localized terms, using natural reviewer-facing translations or explanations rather than only literal glosses.

Decide each localized term without user approval whenever reasonable: save it as `confirmed` when it appears to make sense as a target-locale App Store search for this app, save it as `candidate` when it is plausible but still uncertain, or save it as `rejected` when it is clearly unsuitable. Ask the user or request native-speaker review only when, after best-effort analysis, it remains genuinely unclear whether the term makes sense and that uncertainty would materially affect downstream statistics, scoring, or metadata placement.

Use `Notes` to mark review provenance with one of `review: agent-led`, `review: user-approved`, `review: native-approved`, or `review: needs native review`. For localized terms, also add a simple confidence marker: `confidence: high`, `confidence: medium`, or `confidence: low`.

Use localized confidence to keep agent-led review automatic but honest:

| Confidence | Use when | Typical action |
| --- | --- | --- |
| `high` | The term is natural in the target locale, matches the app's search intent, and is supported by local evidence such as autocomplete, ASO statistics, competitor language, reviews, native wording, or strong source-backed vocabulary. | Save as `confirmed` when relevance is clear. |
| `medium` | The term is plausible and understandable, but evidence is thinner, regional nuance is not fully checked, or it mainly comes from source-intent projection. | Save as `confirmed` only when app fit is clear and downside is low; otherwise keep as `candidate`. |
| `low` | Meaning, idiom, segmentation, spelling, grammar, or regional usage is unclear enough to affect statistics, scoring, or metadata placement. | Keep as `candidate`, mark `review: needs native review` when it matters, or reject if clearly unsuitable. |

Do not treat spelling or grammar warnings as automatic rejection. App Store users may search with misspellings, informal grammar, accents omitted, or local shorthand. Keep a misspelled or ungrammatical variant only when it is user-provided, source-backed, or search-evidence-backed; otherwise ask only when the ambiguity materially affects downstream work.

### 5. Save Results

After review and adjustment, update `.agents/aso/context.md` under `## Search Terms Backlog` for global/source-locale work, or update `.agents/aso/locales/<Locale>/context.md` for localized work.

Use this canonical table for global/source-locale work:

```markdown
| Search term | Source | Status | Relevance | Popularity | Difficulty | Stats country or region | Stats source | Stats updated | Notes | Strategic score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| example term | app description | confirmed | 4 |  |  |  |  |  | strong feature fit |  |
```

Use this canonical table for localized work:

```markdown
| Search term | Meaning | Status | Relevance | Popularity | Difficulty | Stats country or region | Stats source | Stats updated | Notes | Strategic score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| quittung scanner | receipt scanner | confirmed | 5 |  |  |  |  |  | review: agent-led; confidence: high; same intent as source core term |  |
```

Use these status values:

| Status | Meaning |
| --- | --- |
| `candidate` | Suggested, imported, or awaiting review before it belongs in the usable ASO backlog. |
| `confirmed` | Accepted into the usable ASO backlog. Source-locale confirmation requires user approval; localized confirmation may be user-approved, native-approved, or agent-led when the localized confidence rules pass. This does not mean the term has high relevance. |
| `rejected` | Rejected as misleading, irrelevant, or intentionally excluded. |

When updating the table, follow these rules:

- Add a `Relevance` column if it is missing.
- Append new terms rather than replacing existing work.
- For source-locale work, save user-accepted terms as `confirmed` with approved integer `Relevance` scores from `1` to `5`, user-rejected terms as `rejected` with blank relevance, and leave explicitly unreviewed suggestions or imports as `candidate` with blank relevance.
- For localized work, decide terms without user approval whenever reasonable. Save agent-accepted terms as `confirmed` with `review: agent-led` and a confidence marker, uncertain-but-plausible terms as `candidate`, user-rejected or clearly unsuitable terms as `rejected`, and ask for user or native-speaker review only when best-effort analysis cannot determine whether the term makes sense.
- Leave `Popularity`, `Difficulty`, `Stats country or region`, `Stats source`, `Stats updated`, and `Strategic score` blank for new terms. Preserve existing statistics and any additional columns.
- Clear `Strategic score` for rows where `Relevance` is added or changed; preserve it for unchanged rows.
- Do not overwrite user-confirmed relevance scores unless the user approves the change.
- For localized terms, fill `Meaning` with a compact, natural back-translation or explanation in a language the user understands.
- For localized terms, include one review marker in `Notes`: `review: agent-led`, `review: user-approved`, `review: native-approved`, or `review: needs native review`. Also include one confidence marker: `confidence: high`, `confidence: medium`, or `confidence: low`.
- Normalize obvious duplicates, but keep meaningful variants, including singular/plural forms, word-order variants, generic and/or reserved terms like "app", developer names, and category terms when they make sense.
- Use `Notes` for compact context that helps later skills interpret the term, such as source nuance, brand or competitor warnings, intentional spelling or grammar mistakes, long-tail variants, review language, questionable relevance, localization uncertainty, or user verification details.
- For review-mined terms, note when evidence is isolated, noisy, recurring, or corroborated.
- For seasonal terms, note the season, event, or timing window and whether it appears evergreen or time-limited.
- Keep source-backed grammar and spelling variants when they reflect realistic user searches.
- Do not save weak, doubtful, glued, or evidence-poor terms as normal candidates.
- In localized work, put original-intent references and uncertainty in `Notes`; do not add a separate `Source` column to localized workspaces.
- Preserve rejected terms when they prevent repeated suggestions.
- Update `*Last updated:*` in the context file.

Stop after saving or presenting the reviewed backlog and relevance groups. Do not propose popularity, difficulty, strategic scores, metadata placement, or final targeting from this skill; use `aso-search-terms-statistics` when the user asks for popularity or difficulty, and `aso-search-terms-scoring` when the user asks for derived scoring or prioritization.

## Relevance Score

Use a **1-5 relevance score** to describe how well the app satisfies the App Store search intent behind a term.

Scores are relative to the backlog. A score of `1` or `2` means lower relative relevance, ambiguity, or weaker App Store expectation; it does not mean the term is rejected or should be ignored when the user has confirmed it.

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

For localized terms, relevance depends on the localized App Store search intent, not only the source-language term that inspired it. Project a source relevance score only when the localized term clearly expresses the same user intent.

## Relevance Workflow

### 1. Interpret Search Intent

For each term that survives the plausibility filter, infer what a searcher probably wants.

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

Do not use relevance scoring to remove confirmed terms from later scoring. `aso-search-terms-scoring` can still calculate low but nonzero strategic scores for confirmed terms with relevance `1` or `2` when popularity and difficulty inputs are valid.

### 2. Calibrate Scores

Before presenting scores, compare terms across the backlog:

- Group terms that express the same or similar intent.
- Make sure equivalent relevance receives equivalent scores.
- Cluster broad core terms, close synonyms, action-object variants, noun-form variants, word-order variants, and app/category suffix variants near each other when they express the same user intent.
- Run a metadata-bias check. A term that appears in current metadata should still pass the same product-fit test as every other term before receiving `5`.
- Apply an ambiguity cap. A broad term with several plausible App Store intents should not receive `5` unless the app is a clearly excellent result for the dominant intent.
- Check `5` and `1` scores last so extreme scores are applied consistently across comparable terms.
- For every proposed `5`, write a one-sentence internal justification: "A user searching this term primarily wants ___, and this app directly provides ___." If that sentence is weak, ambiguous, or describes only a secondary output, downgrade the term.
- When unsure between two adjacent scores, choose the lower score and mark the term for user review.
- Mark uncertain source-locale scores for user review instead of pretending they are precise.
- For localized work, put uncertainty in `Notes` and ask for review only when the uncertainty is likely to affect downstream metadata choices.

## Competitor Research Handling

Competitor names can be useful research inputs, but they are risky as usable App Store metadata terms and should not be treated as normal search-term candidates by default.

When researching competitors:

- Inspect competitor app names, subtitles, descriptions, OCR'd screenshot text when already available, reviews, categories, and visible positioning when available.
- Treat visible competitor metadata as incomplete on iOS because the hidden keyword field is not public.
- Extract generic non-brand search terms from competitor language, category fit, features, benefits, and user intent.
- Do not propose competitor brand names as normal candidate terms.
- Keep competitor brand names in competitor notes unless the user asks to track them in the backlog.
- If competitor brand names are saved in the backlog for research context, mark them as `rejected`, leave `Relevance` blank, and flag `competitor brand warning` in `Notes`.
- Suggest non-brand alternatives based on the competitor's category, feature, or user intent.

## Common Mistakes

- Creating only a short list of polished terms too early.
- Removing variants because they look similar.
- Over-expanding modifier combinations instead of using natural App Store query shapes.
- Adding phrases only because they appear in source files, even when they are not plausible App Store searches.
- Treating technical or product details as discovery queries.
- Converting every context phrase into a candidate.
- Treating local files as enough without asking for App Store listing, marketing page, and App Store Connect keyword sources.
- Saving source-locale terms or relevance scores before the user reviews them.
- Scoring terms in isolation instead of calibrating across the whole backlog.
- Using popularity, competition, or ranking difficulty as a proxy for relevance.
- Automatically downgrading broad core category terms even when the app is a legitimate strong result for that intent.
- Giving terms high scores only because they already appear in prominent app metadata.
- Giving semantically equivalent terms different scores because of word order, suffixes, or minor modifiers.
- Treating relevance `1` or `2` as automatic rejection after the user has confirmed the term.
- Treating localized `confirmed` as user-approved when its `Notes` marker says `review: agent-led`.
- Omitting localized confidence markers, especially for terms approved by the agent without user or native-speaker review.
- Generating translated terms from non-active-language source material.
- Correcting realistic misspellings or grammar mistakes without checking whether they were intentional.
- Treating web search volume as App Store demand without caveats.
- Treating one-off review phrases as priority search terms without recurrence, corroboration, or user review.
- Overreading large search-result or competitor exports instead of extracting compact app names, subtitles, repeated visible terms, category fit, and non-brand phrases.
- Forgetting long-tail terms with clearer intent.
- Treating seasonal terms as evergreen without noting the timing window.
- Assuming visible competitor metadata reveals the full iOS keyword strategy.
- Proposing competitor brand names as usable search terms instead of extracting generic non-brand alternatives from competitor research.
- Jumping into keyword prioritization, statistics fetching, or metadata writing before the backlog is broad enough.

## Task-Specific Questions

Ask only questions that improve the backlog materially:

- "Do you have an App Store URL, marketing URL, App Store Connect keyword terms, or competitor list I should use before creating the first backlog?"
- "Are these similar apps real competitors, inspiration, or irrelevant?"
- "Would a user searching this term reasonably expect an app like yours?"
- "Do you have existing App Store Connect keyword terms I should treat as source material?"
- "Does this phrase sound like something a user would type in the App Store, or is it just internal product language?"
- "Are these two terms equally relevant, or should one score higher?"
- "Should this broad term stay in the backlog with a low relevance score, or be rejected?"
- "Was this spelling or grammar mistake intentional because users may search that way?"
- "Should I use these competitors as research sources for generic non-brand alternatives?"
- "What terms would customers use if they did not know the app or category name?"

## Related Skills

- Use `aso-context` to create or update shared app context and store the search-term backlog.
- Use `aso-search-terms-statistics` to fetch external popularity and difficulty values after terms exist.
- Use `aso-search-terms-scoring` to calculate derived priority scores after confirmed terms have relevance and statistics.
