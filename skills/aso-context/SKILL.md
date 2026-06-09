---
name: aso-context
description: Builds and refreshes shared app context for App Store metadata optimization workflows. Use when app context is missing, stale, incomplete, or needs facts from an App Store listing, marketing page, product docs, user input, competitors, or App Store Connect keyword terms.
---

# ASO Context

Create and maintain `.agents/aso/context.md`, which captures global app context and the source-locale ASO workspace that other skills reference so users do not repeat themselves.

The context should be compact, factual, and useful for later search-term identification, relevance scoring, statistics fetching, search term scoring, metadata generation, and localized ASO work.

Localized ASO work belongs in `.agents/aso/locales/<Locale>/context.md`, not in the global context file.

## Workflow

### 1. Check Existing Context

First, check whether `.agents/aso/context.md` exists.

If it exists:

- Read it before asking questions.
- Summarize what is already captured.
- Update only the parts affected by the current request or newly available sources.
- Preserve user-confirmed facts unless new evidence clearly contradicts them.

If it does not exist:

- Create it from the best available sources.

### 2. Gather Sources

Ask for any source that can help build the context:

- App Store URL
- Marketing or landing page URL
- App Store Connect keyword field terms, grouped by platform when the app has more than one platform
- Local product docs, metadata files, README, or website copy
- User-provided app description
- Any additional source that may help search-term discovery, such as competitor lists, customer language, support requests, review exports, ASO tool exports, SEO tool exports, Apple Search Ads terms, or keyword research files

Ask once for missing high-value sources, then use whichever sources are available. If multiple sources are available, combine them. Record important source gaps instead of blocking progress.

If an App Store URL or marketing URL is provided, inspect it before deriving ASO context from local files alone. If the current environment cannot access the URL, ask the user to paste relevant copy and note the access gap.

### 3. Populate From Sources

When using an **App Store URL**, extract what is publicly available:

- Name, subtitle, developer, primary category, and secondary category when available
- Description
- Visible screenshot text using OCR when possible
- Review themes and user language
- Competitors or similar apps, including links when available

After finding or receiving an App Store URL, ask the user to provide the current App Store Connect keyword field terms for each relevant platform. These are not public, but they are important source material for ASO search-term work. If the user does not provide them, continue with available sources and note the gap.

When using a **marketing or landing page URL**, extract only ASO-useful context:

- Product description
- Features
- Use cases
- Solution to problem
- Keywords and app category language

When using **App Store Connect keyword field terms**, capture them as source material for search-term discovery under `## Metadata` `### Current` platform-specific `**Keywords (<platform>):**` lines. Do not treat them as automatically approved or final search terms.

When using **local files**, prefer sources that describe the app for users:

- App Store metadata files
- README files
- Landing page copy
- Product docs
- Release notes

Local files are useful context, but they are not a substitute for the public App Store listing or marketing page when those sources are available.

When using a **user description**, capture the user's wording directly where it may help later search term generation.

### 4. Verify The Draft

Before saving, show the drafted app context to the user and ask what is incorrect, missing, or misleading.

Iterate until the user is satisfied with the captured context.

### 5. Save The Context

After review and adjustment, create or update `.agents/aso/context.md` using this structure:

```markdown
# ASO App Context
*Last updated: YYYY-MM-DD*

## Source
**Primary locale:** Dutch
**Platforms:** iOS, macOS
**App Store URL:**
**Marketing URL:**
**Other sources:**

## Metadata
### Current

**Name:** Example App *(11/30)*
**Subtitle:** Example subtitle *(16/30)*
**Developer:** Example Studio
**Primary category:** Business
**Secondary category:** Productivity
**Keywords (iOS):** example,keyword,terms *(21/100 chars)*

### History

#### YYYY-MM-DD - Current - User Edited

User approved the current metadata. Guidance: keep the brand in the app name.

**Name:** Example App *(11/30)*
**Subtitle:** Example subtitle *(16/30)*
**Keywords (iOS):** example,keyword,terms *(21/100 chars)*

## Description


## Screenshots
-

## Use cases
-

## Features
-

## Solution to problem
-

## Reviews
-

## Competitors And Similar Apps
- [App name](https://apps.apple.com/...)

## Search Terms Backlog
| Search term | Source | Status | Relevance | Popularity | Difficulty | Stats country or region | Stats source | Stats updated | Notes | Strategic score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| example term | app description | candidate |  |  |  |  |  |  | feature phrase |  |

## Word Value Scores
| Word | Appearances | Total strategic score | Length | Value |
| --- | --- | --- | --- | --- |

## Locales
| Locale | Workspace | Country or region preference | Notes |
| --- | --- | --- | --- |
| German | .agents/aso/locales/German/context.md |  | target German metadata |
```

Omit unavailable sections when they add no value. For example, omit `## Reviews` for a pre-launch app with no public reviews.

## Writing Rules

- Keep the file concise enough for other skills to read quickly.
- Prefer factual extraction over interpretation.
- Do not invent missing metadata, competitors, review themes, or screenshot text.
- Preserve keyword-rich phrases from source material when they are natural and accurate.
- Use screenshots as source material for app context using OCR text extraction.
- Summarize reviews into themes instead of copying long review text.
- Include competitor and similar app links when available; otherwise use plain app names.
- Store App Store categories as `**Primary category:**` and optional `**Secondary category:**`. Omit `**Secondary category:**` when it is unavailable.
- Store one primary locale for the global backlog using Apple's metadata locale label, such as `Dutch` or `English (U.S.)`. Use `references/app-store-localizations.md` to validate or derive it.
- Do not store an Apple country or region ISO code as part of `Primary locale`. Store `Country or region preference` only when the user or clear source evidence explicitly overrides the default country or region derived from `references/app-store-localizations.md`.
- Store supported App Store Connect platforms in `**Platforms:**` using values from `references/platforms.md`, such as `iOS`, `macOS`, `tvOS`, or `visionOS`.
- Omit `**Search surface preference:**` unless the user explicitly asks to use a non-default search surface for statistics or rankings, such as iPad instead of iPhone for iOS.
- Store current metadata under `## Metadata` > `### Current`.
- Store current keyword fields as platform-specific lines in `### Current`, such as `**Keywords (iOS):** term,term *(42/100 chars)*`. Omit platform keyword lines when they are unavailable.
- Treat text inside `*(...)*` on metadata lines as an annotation. The stored metadata value is the text before the annotation.
- For localized metadata workspaces, put field meanings inside the same annotation when useful, such as `**Subtitle:** Rechnungen scannen *(18/30, scan invoices)*`.
- Store saved metadata iterations under `## Metadata` > `### History` only when the user explicitly saves a generated draft, provides an edited variant, approves current metadata, or publishes metadata. Do not store unsaved generated variants.
- Keep history entries compact: a unique heading with date, status, and source; one short notes/guidance paragraph; then the saved metadata field lines. Use `Guidance:` in the paragraph when a user edit should affect later generations.
- Store localized workspaces in `## Locales` when they exist. Keep only the metadata locale, workspace path, optional country or region preference, and compact notes there; do not duplicate localized search terms in the global context.
- Use `.agents/aso/locales/<Locale>/context.md` for localized terms, relevance, statistics, scoring, current metadata, and metadata history.
- Use `candidate`, `confirmed`, or `rejected` for search-term backlog status values. Use `candidate` for unreviewed suggested or imported terms, `confirmed` for user-accepted terms in the usable ASO backlog, and `rejected` for terms the user does not want to use.
- Leave `Relevance` blank until `aso-search-terms-relevance-scoring` assigns a user-approved integer score from `1` to `5`; keep it blank for rejected terms.
- Leave `Popularity`, `Difficulty`, `Stats country or region`, `Stats source`, and `Stats updated` blank until `aso-search-terms-statistics` obtains external statistics or normalizes user-provided Apple Ads Search Popularity. Keep them blank for rejected terms unless the user explicitly requests statistics for rejected terms. Store `Popularity` and `Difficulty` as validated `1`-`100` values. Use `Notes` for important compact statistics context, including Apple Ads normalization details.
- Leave `Strategic score` blank until `aso-search-terms-scoring` calculates it for confirmed terms with valid relevance from `1` to `5`, popularity, and difficulty values.
- Leave `## Word Value Scores` empty until `aso-search-terms-scoring` calculates derived word scores from confirmed terms with valid strategic scores.
- Preserve existing `## Metadata` `### History` entries unless explicitly updating them through `aso-metadata-generation`.
- Use `Notes` for compact context that helps later skills interpret a search term, such as source nuance, brand or competitor warnings, intentional spelling or grammar mistakes, long-tail variants, review language, questionable relevance, or user verification details.
- Preserve existing backlog columns and values unless the user approves a change. Later skills may add columns, but this skill must not drop them.
- Preserve rejected search terms when they prevent repeated suggestions.
- Update `*Last updated:*` whenever the file changes.
