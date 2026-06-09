---
name: aso-search-terms-identification
description: Finds broad App Store search-term candidates for App Store optimization. Use when creating or expanding a keyword backlog, researching App Store search terms, localizing keyword ideas, mining competitor language, collecting user search phrases, or preparing terms for relevance scoring.
---

# ASO Search Terms Identification

Act as an ASO search-term researcher. Help the user create a large backlog of search terms that potential users might reasonably type in the App Store and expect to find the app in the results.

Optimize for **breadth and App Store search plausibility**. Broad coverage is useful only after each term sounds like something a person might actually type in App Store search. Do not assign relevance scores, popularity, difficulty, strategic scores, prioritize terms, assign metadata fields, or decide final targeting. If the user asks for relevance scoring, finish or save the backlog and use `aso-search-terms-relevance-scoring`; if the user asks for popularity or difficulty, use `aso-search-terms-statistics`; if the user asks for derived scoring or prioritization, use `aso-search-terms-scoring`; treat metadata placement and final targeting as outside this skill.

## Before Starting

Read `.agents/aso/context.md` first.

If the user is working on a localized workspace, also read the relevant `.agents/aso/locales/<Locale>/context.md` file and use its `Locale` and optional `Country or region preference` as the active target.

If it exists:

- Summarize the app context that matters for search-term discovery.
- Identify the source `Primary locale`; if none is specified, ask only when locale materially affects term language or statistics.
- For localized work, identify the target locale, optional country or region preference, and any existing localized terms.
- Show any existing terms in `## Search Terms Backlog`.
- Preserve existing statuses, relevance scores, statistics, notes, and any additional backlog columns unless the user corrects them.

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
- For localized terms, store a concise `Meaning` so users who do not know the target language can audit the term.
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
- **Existing ASC keywords:** App Store Connect keyword field terms provided by the user for each platform; treat them as source material and seeds, not automatically approved final terms.
- **Third-party and web discovery tools:** If the user provides data or relevant tools are available, use ASO tools, Google Play autofill, Google Keyword Planner, Google Trends, SEO tools, and keyword discovery tools with caveats. Web or Google Play demand is not the same as App Store demand.
- **Imported keyword lists:** User-provided keyword exports or manual lists; import their keyword language broadly before generating new expansions.
- **Phrase expansion:** broad head terms, singular/plural variants, synonyms, alternate word order, related nouns and verbs, action-object variants, noun-form variants, compact or compound variants, category modifiers, seasonal variants, and long-tail combinations that still sound like natural App Store searches.
- **Brand terms:** the app's own name, product names, company name, abbreviations, and source-backed misspellings or grammar variants when relevant.

If source material uses a language other than the source primary locale language, use it only as background for understanding the app. Do not translate non-active-locale strings into search-term candidates unless the user explicitly changes the source primary locale.

For localized work, reverse that rule: source-language search terms are background for intent, while target-language evidence should drive the final localized search terms. Generate terms from local App Store behavior, localized competitor language, target-language reviews or support language, autocomplete/tool evidence, and natural target-language phrasing.

Do not wait for every source to be available after the user has had a chance to provide them. Use the sources at hand, call tools only when available in the current environment, and mark the source honestly.

When evidence conflicts, prefer app truth and user/searcher language first, Apple-native App Store or Apple Search Ads signals second, local competitor and local-language evidence third, and third-party or web/SEO evidence as lower-confidence expansion material.

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

Present proposed search terms in a compact flat list or table that makes review easy without changing the saved backlog schema.

Before saving new search terms, ask the user what should be accepted, rejected, corrected, or added. Include brief review guidance: review the suggested terms, remove terms that are not relevant, and add potentially missing terms. Brand terms, plural variants, and terms with free or reserved words like `app` can remain at this stage because metadata-generation filtering happens later.

Do not save the backlog until the user has had a clear chance to review and adjust the proposed terms.

### 5. Save Results

After review and adjustment, update `.agents/aso/context.md` under `## Search Terms Backlog` for global/source-locale work, or update `.agents/aso/locales/<Locale>/context.md` for localized work.

Use this canonical table for global/source-locale work:

```markdown
| Search term | Source | Status | Relevance | Popularity | Difficulty | Stats country or region | Stats source | Stats updated | Notes | Strategic score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| example term | app description | confirmed |  |  |  |  |  |  | feature phrase |  |
```

Use this canonical table for localized work:

```markdown
| Search term | Meaning | Status | Relevance | Popularity | Difficulty | Stats country or region | Stats source | Stats updated | Notes | Strategic score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| quittung scanner | receipt scanner | confirmed |  |  |  |  |  |  | inspired by source intent: receipt scanner |  |
```

Use these status values:

| Status | Meaning |
| --- | --- |
| `candidate` | Suggested or imported, not yet reviewed by the user. |
| `confirmed` | User accepted the term into the usable ASO backlog. This does not mean it has high relevance. |
| `rejected` | User said the term is misleading, irrelevant, or something they do not want to use. |

When updating the table, follow these rules:

- Append new terms rather than replacing existing work.
- Save user-accepted terms as `confirmed`, user-rejected terms as `rejected`, and leave unreviewed suggestions or imports as `candidate`.
- Leave `Relevance`, `Popularity`, `Difficulty`, `Stats country or region`, `Stats source`, `Stats updated`, and `Strategic score` blank for new terms. Preserve existing relevance scores, statistics, strategic scores, and any additional columns.
- For localized terms, fill `Meaning` with a compact back-translation or explanation in a language the user understands.
- Normalize obvious duplicates, but keep meaningful variants, including singular/plural forms, word-order variants, generic and/or reserved terms like "app", developer names, and category terms when they make sense.
- Use `Notes` for compact context that helps later skills interpret the term, such as source nuance, brand or competitor warnings, intentional spelling or grammar mistakes, long-tail variants, review language, questionable relevance, or user verification details.
- For review-mined terms, note when evidence is isolated, noisy, recurring, or corroborated.
- For seasonal terms, note the season, event, or timing window and whether it appears evergreen or time-limited.
- Keep source-backed grammar and spelling variants when they reflect realistic user searches.
- Do not save weak, doubtful, glued, or evidence-poor terms as normal candidates.
- In localized work, put original-intent references and uncertainty in `Notes`; do not add a separate `Source` column to localized workspaces.
- Preserve rejected terms when they prevent repeated suggestions.
- Update `*Last updated:*` in the context file.

Stop after saving or presenting the backlog. Do not propose relevance, popularity, difficulty, or strategic scores from this skill; use `aso-search-terms-relevance-scoring` when the user asks for relevance scoring, `aso-search-terms-statistics` when the user asks for popularity or difficulty, and `aso-search-terms-scoring` when the user asks for derived scoring or prioritization.

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
- Treating local files as enough without asking for App Store listing, marketing page, and ASC keyword sources.
- Proposing relevance scores during search-term identification.
- Generating translated terms from non-active-language source material.
- Correcting realistic misspellings or grammar mistakes without checking whether they were intentional.
- Treating web search volume as App Store demand without caveats.
- Treating one-off review phrases as priority search terms without recurrence, corroboration, or user review.
- Forgetting long-tail terms with clearer intent.
- Treating seasonal terms as evergreen without noting the timing window.
- Assuming visible competitor metadata reveals the full iOS keyword strategy.
- Proposing competitor brand names as usable search terms instead of extracting generic non-brand alternatives from competitor research.
- Jumping into keyword prioritization, statistics fetching, or metadata writing before the backlog is broad enough.

## Task-Specific Questions

Ask only questions that improve the backlog materially:

- "Do you have an App Store URL, marketing URL, ASC keyword terms, or competitor list I should use before creating the first backlog?"
- "Are these similar apps real competitors, inspiration, or irrelevant?"
- "Would a user searching this term reasonably expect an app like yours?"
- "Do you have existing App Store Connect keyword terms I should treat as source material?"
- "Does this phrase sound like something a user would type in the App Store, or is it just internal product language?"
- "Was this spelling or grammar mistake intentional because users may search that way?"
- "Should I use these competitors as research sources for generic non-brand alternatives?"
- "What terms would customers use if they did not know the app or category name?"

## Related Skills

- Use `aso-context` to create or update shared app context and store the search-term backlog.
- Use `aso-search-terms-relevance-scoring` to assign user-reviewed relevance scores to the backlog.
- Use `aso-search-terms-statistics` to fetch external popularity and difficulty values after terms exist.
- Use `aso-search-terms-scoring` to calculate derived priority scores after confirmed terms have relevance and statistics.
