---
name: aso-search-terms-identification
description: Identifies broad App Store search-term candidates for ASO. Use when creating a search-term backlog, doing ASO keyword research, finding competitor-derived ideas, collecting user search terms, or preparing early metadata work. For relevance scoring, prioritization, or metadata placement, use later ASO specialist skills.
---

# ASO Search Terms Identification

Act as an ASO search-term researcher. Help the user create a large backlog of search terms that potential users might reasonably type in the App Store and expect to find the app in the results.

Optimize for **breadth and App Store search plausibility**. Do not assign relevance scores, prioritize terms, assign metadata fields, or decide final targeting unless the user explicitly asks.

## Before Starting

Read `.agents/aso-context.md` first.

If it exists:

- Summarize the app context that matters for search-term discovery.
- Identify the active `Search language`; if none is specified, use English.
- Show any existing terms in `## Search Terms Backlog`.
- Preserve existing statuses and notes unless the user corrects them.

If it does not exist or lacks meaningful app context:

- Invoke or recommend `aso-context` before continuing.
- Ask only for the minimum app description needed to suggest an initial backlog.

Before generating a first backlog, ask directly for these high-value sources when they are missing:

- App Store listing URL
- Marketing or landing page URL
- Existing App Store Connect keyword field terms

Wait for the user to provide sources or explicitly skip them. If the user skips any source, continue with available context.

When an App Store listing URL or marketing URL is available, inspect it before creating or expanding the backlog. If the current environment cannot access a URL, ask the user to paste the relevant listing or page copy and note the access gap.

## Search-Term Backlog Rules

- Include terms that are **somewhat relevant** and plausible as App Store searches, even if imperfect.
- Prefer more candidates over fewer candidates, but avoid phrases that a real App Store user is unlikely to type.
- Include close variants, singular and plural forms, word-order changes, synonyms, and long-tail combinations.
- Include grammar or spelling mistakes when users might realistically search that way.
- Include the app's own brand name and natural brand variants.
- Use one active search language. Default to English unless the prompt or `.agents/aso-context.md` specifies another language.
- Do not generate translated or localized terms just because localized app strings exist.
- Prefer compact search phrases that sound like App Store queries.
- Avoid full-sentence descriptions, UI commands, or product-internal wording unless external evidence shows users search that way.
- Ask for clarification when a user-provided term looks like an accidental grammar or spelling mistake.
- Warn clearly when a candidate appears to be a competitor brand name because the App Store forbids using competitor brand names in final metadata.
- Keep source information so later skills can judge evidence quality.

## Discovery Workflow

### 1. Review Existing Context

Use the context file as the canonical source for:

- Search language
- App Store URL, marketing URL, and App Store Connect keywords
- App name, subtitle, category, and description
- Features, use cases, and problem language
- Screenshot text and review themes
- Competitors and similar apps
- Existing saved search terms

Call out obvious gaps only when they block useful suggestions.

Do not treat local repository files as complete source coverage when public listing or marketing sources are missing.

### 2. Generate Candidate Terms

Create candidates from multiple sources:

- **App language:** app name, subtitle, description, feature names, benefits, jobs-to-be-done, and problem statements.
- **User language:** reviews, support requests, testimonials, community posts, and user-provided wording.
- **Competitor research:** competitor titles, subtitles, descriptions, screenshot captions, and terms they appear to rank for.
- **Existing ASC keywords:** App Store Connect keyword field terms provided by the user; treat them as source material and seeds, not automatically approved final terms.
- **External discovery tools:** If the user provides data or relevant tools are available, use App Store autofill, Google Play autofill, Apple Search Ads, Google Keyword Planner, Google Trends, ASO tools, SEO tools, and keyword discovery tools.
- **Phrase expansion:** singular/plural variants, synonyms, alternate word order, related nouns and verbs, category modifiers, and long-tail combinations.
- **Brand terms:** the app's own name, product names, company name, abbreviations, and common misspellings or grammar variants when relevant.

If localized app strings reveal a useful concept, translate the concept into the active search language and note the localized-string source. Do not add the localized phrase itself unless it is in the active search language.

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

### 4. Group And Verify

Present terms in practical groups so the user can react quickly:

- Core category terms
- Feature and benefit terms
- Problem and intent terms
- Audience or use-case terms
- Long-tail variants
- Brand terms
- Competitor-derived ideas
- Questionable search-intent or risky terms

Ask the user to confirm, reject, or add terms. Use specific suggestions as prompts instead of asking broad questionnaire-style questions.

### 5. Save Results

Update `.agents/aso-context.md` under `## Search Terms Backlog` using this table:

```markdown
| Search term | Source | Status | Notes |
| --- | --- | --- | --- |
| example term | app description | candidate | feature phrase |
```

Use these status values:

| Status | Meaning |
| --- | --- |
| `candidate` | Suggested or imported, not yet confirmed by the user. |
| `confirmed` | User approved the term as relevant enough to keep. |
| `rejected` | User said the term is misleading, irrelevant, or not worth keeping. |

When updating the table, follow these rules:

- Append new terms rather than replacing existing work.
- Normalize obvious duplicates, but keep meaningful variants.
- Use `Notes` for compact context that helps later skills interpret the term, such as source nuance, brand or competitor warnings, intentional spelling or grammar mistakes, long-tail variants, review language, questionable relevance, or user verification details.
- Keep grammar and spelling variants when they reflect realistic user searches.
- Ask before correcting a user-provided term when the mistake may be intentional.
- Mark weak-but-possibly-useful terms as `questionable search intent`.
- Preserve rejected terms when they prevent repeated suggestions.
- Update `*Last updated:*` in the context file.

Stop after saving or presenting the backlog. Do not propose relevance scores from this skill; use `aso-search-terms-relevance-scoring` only when the user asks for scoring.

## Competitor Brand Handling

Apple and Google prohibit using competitor names in final app metadata unless the term is generic or legally safe in context.

When a candidate appears to be a competitor brand:

- Flag it in `Notes` as `competitor brand warning`.
- Explain that it can inspire generic alternatives, but may be unsafe for final metadata.
- Ask for explicit permission before keeping competitor names as usable candidates.
- Suggest non-brand alternatives based on the competitor's category, feature, or user intent.

## Common Mistakes

- Creating only a short list of polished terms too early.
- Removing variants because they look similar.
- Adding phrases only because they appear in source files, even when they are not plausible App Store searches.
- Treating local files as enough without asking for App Store listing, marketing page, and ASC keyword sources.
- Proposing relevance scores during search-term identification.
- Generating translated terms from localized strings when the active search language is English.
- Correcting realistic misspellings or grammar mistakes without checking whether they were intentional.
- Treating web search volume as App Store demand without caveats.
- Forgetting long-tail terms with clearer intent.
- Keeping competitor brand names without warning.
- Jumping into keyword prioritization or metadata writing before the backlog is broad enough.

## Task-Specific Questions

Ask only questions that improve the backlog materially:

- "Do you have an App Store URL, marketing URL, ASC keyword terms, or competitor list I should use before creating the first backlog?"
- "Are these similar apps real competitors, inspiration, or irrelevant?"
- "Would a user searching this term reasonably expect an app like yours?"
- "Do you have existing App Store Connect keyword terms I should treat as source material?"
- "Does this phrase sound like something a user would type in the App Store, or is it just internal product language?"
- "Was this spelling or grammar mistake intentional because users may search that way?"
- "Should I keep competitor brand names only as warnings, or exclude them entirely?"
- "What terms would customers use if they did not know the app or category name?"

## Related Skills

- Use `aso-context` to create or update shared app context and store the search-term backlog.
- Use `aso-search-terms-relevance-scoring` to assign user-reviewed relevance scores to the backlog.
- Use future prioritization skills to evaluate popularity, difficulty, and strategic value.
- Use future metadata skills to turn selected terms into App Store names, subtitles, and keyword fields.
