---
name: aso-search-terms-identification
description: Identifies broad App Store search-term candidates for ASO. Use when creating or expanding a search-term backlog, doing ASO keyword research, finding competitor-derived ideas, collecting user search terms, or preparing terms for relevance scoring. For relevance scoring, use aso-search-terms-relevance-scoring; for popularity and difficulty, use aso-search-terms-statistics; for prioritization, use aso-search-terms-strategic-scoring.
---

# ASO Search Terms Identification

Act as an ASO search-term researcher. Help the user create a large backlog of search terms that potential users might reasonably type in the App Store and expect to find the app in the results.

Optimize for **breadth and App Store search plausibility**. Do not assign relevance scores, popularity, difficulty, strategic scores, prioritize terms, assign metadata fields, or decide final targeting. If the user asks for relevance scoring, finish or save the backlog and use `aso-search-terms-relevance-scoring`; if the user asks for popularity or difficulty, use `aso-search-terms-statistics`; if the user asks for strategic scoring or prioritization, use `aso-search-terms-strategic-scoring`; treat metadata placement and final targeting as outside this skill.

## Before Starting

Read `.agents/aso-context.md` first.

If it exists:

- Summarize the app context that matters for search-term discovery.
- Identify the active `Search language`; if none is specified, use English.
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
- Prefer more candidates over fewer candidates, but avoid phrases that a real App Store user is unlikely to type.
- Include close variants, singular and plural forms, word-order changes, synonyms, and long-tail combinations.
- Include broad head terms for the app's core category, jobs-to-be-done, and main user outcomes.
- Include natural action-object and noun variants for the same intent, including compact forms users may type in the App Store.
- Include generic category, audience, and use-case synonyms even when they are less precise than the app's positioning.
- Do not invent spelling or grammar mistakes.
- Preserve misspelled or ungrammatical terms only when they come from the user or source evidence.
- Include the app's own brand name and natural brand variants.
- Use one active search language. Default to English unless the prompt or `.agents/aso-context.md` specifies another language.
- Do not generate translated terms from source material in another language unless the user explicitly switches the active search language.
- Prefer compact search phrases that sound like App Store queries.
- Avoid full-sentence descriptions, UI commands, or product-internal wording unless external evidence shows users search that way.
- Ask for clarification when a user-provided term looks like an accidental grammar or spelling mistake.
- Do not add competitor brand names as usable search-term candidates by default.
- Keep source information so later skills can judge evidence quality.

## Discovery Workflow

### 1. Review Existing Context

Use the context file as the canonical source for:

- Search language and search region
- App Store URL, marketing URL, and App Store Connect keywords
- App name, subtitle, category, and description
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
- **User language:** reviews, support requests, testimonials, community posts, and user-provided wording.
- **Competitor research:** competitor app names, subtitles, descriptions, OCR'd screenshot text when already available, and terms they appear to rank for.
- **Existing ASC keywords:** App Store Connect keyword field terms provided by the user; treat them as source material and seeds, not automatically approved final terms.
- **External discovery tools:** If the user provides data or relevant tools are available, use App Store autofill, Google Play autofill, Apple Search Ads terms, Google Keyword Planner, Google Trends, ASO tools, SEO tools, and keyword discovery tools.
- **Imported keyword lists:** User-provided keyword exports or manual lists; import their keyword language broadly before generating new expansions.
- **Phrase expansion:** broad head terms, singular/plural variants, synonyms, alternate word order, related nouns and verbs, action-object variants, noun-form variants, compact or compound variants, category modifiers, and long-tail combinations.
- **Brand terms:** the app's own name, product names, company name, abbreviations, and source-backed misspellings or grammar variants when relevant.

If source material uses a language other than the active search language, use it only as background for understanding the app. Do not translate non-active-language strings into search-term candidates unless the user explicitly switches the active search language.

Do not wait for every source to be available after the user has had a chance to provide them. Use the sources at hand, call tools only when available in the current environment, and mark the source honestly.

### 3. Filter For App Store Search Plausibility

Keep a candidate when a user might plausibly type it in the App Store while looking for an app like this.

Avoid or mark as `questionable search intent`:

- Internal feature labels or implementation details
- UI-action fragments and settings labels
- Sentence-like phrases
- Integration-only terms that are not likely app discovery queries
- Phrases that describe a workflow but do not sound like search terms
- Adjacent category terms that would likely return apps with a different core promise

### 4. Review And Verify

Present proposed search terms in a compact flat list or table that makes review easy without changing the saved backlog schema.

Before saving new search terms, ask the user what should be accepted, rejected, corrected, or added. Include brief review guidance: keep terms that users might search for and reasonably expect to find this app in the App Store results; keep more relevant possibilities rather than narrowing the list too early; keep useful singular/plural variants, word-order variants, generic and/or reserved terms like "app", developer names, and category terms when they make sense; reject or correct terms that are misleading or unlikely to be searched.

Do not save the backlog until the user has had a clear chance to review and adjust the proposed terms.

### 5. Save Results

After review and adjustment, update `.agents/aso-context.md` under `## Search Terms Backlog` using the canonical table:

```markdown
| Search term | Source | Status | Relevance | Popularity | Difficulty | Stats region | Stats source | Stats updated | Notes | Strategic score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| example term | app description | confirmed |  |  |  |  |  |  | feature phrase |  |
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
- Leave `Relevance`, `Popularity`, `Difficulty`, `Stats region`, `Stats source`, `Stats updated`, and `Strategic score` blank for new terms. Preserve existing relevance scores, statistics, strategic scores, and any additional columns.
- Normalize obvious duplicates, but keep meaningful variants, including singular/plural forms, word-order variants, generic and/or reserved terms like "app", developer names, and category terms when they make sense.
- Use `Notes` for compact context that helps later skills interpret the term, such as source nuance, brand or competitor warnings, intentional spelling or grammar mistakes, long-tail variants, review language, questionable relevance, or user verification details.
- Keep source-backed grammar and spelling variants when they reflect realistic user searches.
- Mark weak-but-possibly-useful terms as `questionable search intent`.
- Preserve rejected terms when they prevent repeated suggestions.
- Update `*Last updated:*` in the context file.

Stop after saving or presenting the backlog. Do not propose relevance, popularity, difficulty, or strategic scores from this skill; use `aso-search-terms-relevance-scoring` when the user asks for relevance scoring, `aso-search-terms-statistics` when the user asks for popularity or difficulty, and `aso-search-terms-strategic-scoring` when the user asks for strategic scoring or prioritization.

## Competitor Research Handling

Competitor names can be useful research inputs, but they are risky as usable App Store metadata terms and should not be treated as normal search-term candidates by default.

When researching competitors:

- Inspect competitor app names, subtitles, descriptions, OCR'd screenshot text when already available, reviews, categories, and visible positioning when available.
- Extract generic non-brand search terms from competitor language, category fit, features, benefits, and user intent.
- Do not propose competitor brand names as normal candidate terms.
- Keep competitor brand names in competitor notes unless the user asks to track them in the backlog.
- If competitor brand names are saved in the backlog for research context, mark them as `rejected`, leave `Relevance` blank, and flag `competitor brand warning` in `Notes`.
- Suggest non-brand alternatives based on the competitor's category, feature, or user intent.

## Common Mistakes

- Creating only a short list of polished terms too early.
- Removing variants because they look similar.
- Adding phrases only because they appear in source files, even when they are not plausible App Store searches.
- Treating local files as enough without asking for App Store listing, marketing page, and ASC keyword sources.
- Proposing relevance scores during search-term identification.
- Generating translated terms from non-active-language source material.
- Correcting realistic misspellings or grammar mistakes without checking whether they were intentional.
- Treating web search volume as App Store demand without caveats.
- Forgetting long-tail terms with clearer intent.
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
- Use `aso-search-terms-strategic-scoring` to calculate derived priority scores after confirmed terms have relevance and statistics.
