---
name: aso-context
description: Builds and refreshes shared app context for App Store metadata optimization workflows. Use when app context is missing, stale, incomplete, or needs facts from an App Store listing, marketing page, product docs, user input, competitors, or App Store Connect keyword terms.
---

# ASO Context

Create and maintain `.agents/aso/context.md`, which captures global app context and the source-locale ASO workspace that other skills reference so users do not repeat themselves.

The context should be compact, factual, and useful for later search-term identification, relevance scoring, statistics fetching, search term scoring, metadata generation, and localized ASO work.

Localized ASO work belongs in `.agents/aso/locales/<ISO code>/<language-slug>.md`, not in the global context file.

## Workflow

### 1. Check Existing Context

First, check whether `.agents/aso/context.md` exists.

If it exists:

- Read it before asking questions.
- Summarize what is already captured.
- Update only the parts affected by the current request or newly available sources.
- Preserve user-confirmed facts unless new evidence clearly contradicts them.

If it does not exist but legacy `.agents/aso-context.md` exists:

- Read the legacy file as the current context.
- On the next save, write the updated context to `.agents/aso/context.md`.
- Do not delete the legacy file unless the user explicitly asks.

If neither context file exists:

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

- Name, subtitle, developer, and category
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
- Keywords and app category

When using **App Store Connect keyword field terms**, capture them as source material for search-term discovery under platform-specific `Keywords (<platform>)` sections. Do not treat them as automatically approved or final search terms.

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
**Primary locale:** NLD (Dutch)
**Platforms:** iOS, macOS
**App Store URL:**
**Marketing URL:**
**Other sources:**
**Localization preferences:**

## Metadata
**Name:**
**Subtitle:**
**Developer:**
**Category:**

## Current Keywords
### Keywords (iOS)

### Keywords (macOS)

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
| Search term | Source | Status | Relevance | Popularity | Difficulty | Stats region | Stats source | Stats updated | Notes | Strategic score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| example term | app description | candidate |  |  |  |  |  |  | feature phrase |  |

## Word Value Scores
| Word | Appearances | Total strategic score | Length | Value |
| --- | --- | --- | --- | --- |

## Locales
| ISO code | Country or region | Language | Workspace | Notes |
| --- | --- | --- | --- | --- |
| DEU | Germany | German | .agents/aso/locales/DEU/german.md | target German metadata |
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
- Store one primary locale for the global backlog using Apple's App Store localization `ISO code` and language label, such as `NLD (Dutch)` or `USA (English (US))`. Use `../../references/app-store-localizations.md` to validate or derive it.
- Store supported App Store Connect platforms in `**Platforms:**` using values from `../../references/platforms.md`, such as `iOS`, `macOS`, `tvOS`, or `visionOS`.
- Omit `**Search surface preference:**` unless the user explicitly asks to use a non-default search surface for statistics or rankings, such as iPad instead of iPhone for iOS.
- Store current keyword fields in `## Current Keywords` with one `### Keywords (<platform>)` section per relevant platform.
- Store localized workspaces in `## Locales` when they exist. Keep only the Apple ISO code, country or region, language, workspace path, and compact notes there; do not duplicate localized search terms in the global context.
- Use `.agents/aso/locales/<ISO code>/<language-slug>.md` for localized terms, relevance, statistics, scoring, and metadata drafts.
- Use `candidate`, `confirmed`, or `rejected` for search-term backlog status values. Use `candidate` for unreviewed suggested or imported terms, `confirmed` for user-accepted terms in the usable ASO backlog, and `rejected` for terms the user does not want to use.
- Leave `Relevance` blank until `aso-search-terms-relevance-scoring` assigns a user-approved integer score from `1` to `5`; keep it blank for rejected terms.
- Leave `Popularity`, `Difficulty`, `Stats region`, `Stats source`, and `Stats updated` blank until `aso-search-terms-statistics` obtains external statistics; keep them blank for rejected terms unless the user explicitly requests statistics for rejected terms. Store `Popularity` and `Difficulty` as validated `1`-`100` values. Use `Notes` for important compact statistics context.
- Leave `Strategic score` blank until `aso-search-terms-scoring` calculates it for confirmed terms with valid relevance, popularity, and difficulty values.
- Leave `## Word Value Scores` empty until `aso-search-terms-scoring` calculates derived word scores from confirmed terms with valid strategic scores.
- Preserve existing `## Metadata Drafts` sections unless explicitly updating them through `aso-metadata-generation`.
- Use `Notes` for compact context that helps later skills interpret a search term, such as source nuance, brand or competitor warnings, intentional spelling or grammar mistakes, long-tail variants, review language, questionable relevance, or user verification details.
- Preserve existing backlog columns and values unless the user approves a change. Later skills may add columns, but this skill must not drop them.
- Preserve rejected search terms when they prevent repeated suggestions.
- Update `*Last updated:*` whenever the file changes.
