---
name: aso-context
description: Builds and refreshes shared app context for App Store metadata optimization workflows. Use when app context is missing, stale, incomplete, or needs facts from an App Store listing, marketing page, product docs, user input, competitors, or App Store Connect keyword terms.
---

# ASO Context

Create and maintain `.agents/aso/context.md`, which captures global app context and the source-locale ASO workspace that other skills reference so users do not repeat themselves.

The context should be compact, factual, and useful for later search-term identification plus relevance assignment and validation, statistics fetching, search term scoring, metadata generation, and localized ASO work.

Localized ASO work belongs in `.agents/aso/locales/<Locale>/context.md`, not in the global context file.

## Workflow

### 1. Check Existing Context

First, check whether `.agents/aso/context.md` exists.

If it exists:

- Read it before asking questions.
- Summarize what is already captured.
- Check whether it is sufficient for the current request.
- Continue without a user review gate when it already contains the needed app facts, primary locale, platforms, current metadata or documented metadata gaps, and source material for the requested downstream skill.
- Update only the parts affected by the current request, missing required fields, stale or contradictory source evidence, or newly available sources.
- Preserve user-confirmed facts unless new evidence clearly contradicts them.

If it does not exist:

- Draft it from the best available sources, show it to the user, and save `.agents/aso/context.md` only after approval.

Refresh existing context only when one of these applies:

- The user asks to refresh or change global app context.
- Current metadata, private App Store Connect keyword fields, categories, app facts, or source URLs are missing and needed for the current request.
- Existing source facts conflict with newer source evidence.
- Metadata-dependent work relies on context that appears stale, such as an old `*Last updated:*` date or known App Store Connect changes.
- A downstream skill cannot proceed because required context fields are absent.

When no refresh is needed, summarize the existing context and proceed. Do not ask the user to re-approve unchanged context.

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

For private App Store Connect metadata such as keyword fields, use available App Store Connect-capable tooling in a read-only way before asking the user to provide values manually. Useful options can include `asc`, the Helm CLI (`helm-asc`), the official App Store Connect API, or user-provided tooling. Prefer the relevant tool-specific skill, CLI help, or command discovery instead of hardcoded commands. If a tool is available but fails with an unclear error and the environment may be sandboxed, retry outside the sandbox when applicable and permitted before treating the source as unavailable. For read-only App Store Connect metadata commands, treat ambiguous App Store Connect `-50` validation errors in sandboxed environments as retry candidates before concluding the request, credentials, or locale are invalid. If automated retrieval still fails, ask once for the private values manually and continue with a documented source gap when useful.

Never write to App Store Connect through `asc`, the Helm CLI (`helm-asc`), the App Store Connect API, or another tool unless the user explicitly reviews and approves that write.

### 3. Populate From Sources

When using an **App Store URL**, extract what is publicly available:

- Name, subtitle, developer, primary category, and secondary category when available
- Description
- Visible screenshot text using OCR when possible
- Review themes and user language
- Competitors or similar apps, including links when available

After finding or receiving an App Store URL, try to capture the live App Store Connect keyword field terms for each relevant platform using available read-only App Store Connect-capable tooling, such as `asc`, the Helm CLI (`helm-asc`), the App Store Connect API, or user-provided tooling. These terms are not public, but they are important source material for ASO search-term work. If they cannot be retrieved automatically or provided by the user, continue with available sources and note the gap.

Use live App Store metadata as the default `## Metadata` > `### Current` baseline for app name, subtitle, and keyword fields. If App Store Connect also has staged metadata, do not store staged values as `### Current` unless the user explicitly asks to optimize the next release or approves generated metadata as current. When staged values differ and the difference matters for the current task, record one compact note in `## Source` or `### History`.

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

Before saving, show the drafted app context to the user and ask what is inaccurate, missing, misleading, or overemphasized. Briefly explain that search-term discovery uses this context as its source, so context that accurately reflects the app's purpose, audience, features, and positioning leads to better search terms and metadata recommendations.

Call out important source gaps and optional-but-useful fields that were expected, attempted, or relevant but unavailable. For example, if secondary category is not visible in available sources, mention that it is unavailable rather than silently implying the context is complete.

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

- Keep the file concise enough for other skills to read quickly, but preserve enough source-backed feature, audience, workflow, problem, jobs-to-be-done, and review language to support later search-term discovery.
- Prefer factual extraction over interpretation.
- Do not invent missing metadata, competitors, review themes, or screenshot text.
- Preserve keyword-rich phrases from source material when they are natural and accurate.
- Record important source gaps compactly in `## Source`, especially unavailable private keyword fields or App Store Connect fields that were expected, attempted, or relevant to the current workflow.
- Use screenshots as source material for app context using OCR text extraction.
- Summarize reviews into themes instead of copying long review text.
- Include competitor and similar app links when available; otherwise use plain app names.
- Store App Store categories as `**Primary category:**` and optional `**Secondary category:**`. Omit `**Secondary category:**` when it is unavailable, but mention it in the review or source gaps when it was expected, attempted, or relevant.
- Store one primary locale for the global backlog using Apple's metadata locale label, such as `Dutch` or `English (U.S.)`. Use `references/app-store-localizations.md` to validate or derive it.
- Do not store an Apple country or region ISO code as part of `Primary locale`. Store `Country or region preference` only when the user or clear source evidence explicitly overrides the default country or region derived from `references/app-store-localizations.md`.
- Store supported App Store Connect platforms in `**Platforms:**` using values from `references/platforms.md`, such as `iOS`, `macOS`, `tvOS`, or `visionOS`.
- Omit `**Search surface preference:**` unless the user explicitly asks to use a non-default search surface for statistics or rankings, such as iPad instead of iPhone for iOS.
- Store current metadata under `## Metadata` > `### Current`.
- Store live current keyword fields as platform-specific lines in `### Current`, such as `**Keywords (iOS):** term,term *(42/100 chars)*`. Omit platform keyword lines when they are unavailable. If the live fields cannot be retrieved and the user provides current values manually, store them in `### Current` and note the user-provided source compactly in `## Source`.
- Treat text inside `*(...)*` on metadata lines as an annotation. The stored metadata value is the text before the annotation.
- For localized metadata workspaces, put field meanings inside the same annotation when useful, such as `**Subtitle:** Rechnungen scannen *(18/30, scan invoices)*`.
- Store saved metadata iterations under `## Metadata` > `### History` only when the user explicitly saves a generated draft, provides an edited variant, approves current metadata, or publishes metadata. Do not store unsaved generated variants. When the user approves generated or edited metadata as current, update `### Current` through the metadata save flow rather than treating it as a fresh live ASC read.
- Keep history entries compact: a unique heading with date, status, and source; one short notes/guidance paragraph; then the saved metadata field lines. Use `Guidance:` in the paragraph when a user edit should affect later generations.
- Store localized workspaces in `## Locales` only after verifying the workspace file exists. Keep only the metadata locale, workspace path, optional country or region preference, and compact notes there; do not duplicate localized search terms in the global context. If a locale is planned but the workspace file does not exist yet, label it as `planned; workspace not created` in `Notes` and do not imply that localized context is ready.
- Use `.agents/aso/locales/<Locale>/context.md` for localized terms, relevance, statistics, scoring, current metadata, and metadata history.
- Use `candidate`, `confirmed`, or `rejected` for search-term backlog status values. Use `candidate` for unreviewed suggested or imported terms, `confirmed` for user-accepted terms in the usable ASO backlog, and `rejected` for terms the user does not want to use.
- Leave `Relevance` blank until `aso-search-terms-identification` assigns a user-approved integer score from `1` to `5`; keep it blank for rejected terms.
- Leave `Popularity`, `Difficulty`, `Stats country or region`, `Stats source`, and `Stats updated` blank until `aso-search-terms-statistics` obtains external statistics or normalizes user-provided Apple Ads Search Popularity. Keep them blank for rejected terms unless the user explicitly requests statistics for rejected terms. Store `Popularity` and `Difficulty` as validated `1`-`100` values. Use `Notes` for important compact statistics context, including Apple Ads normalization details.
- Leave `Strategic score` blank until `aso-search-terms-scoring` calculates it for confirmed terms with valid relevance from `1` to `5`, popularity, and difficulty values.
- Leave `## Word Value Scores` empty until `aso-search-terms-scoring` calculates derived word scores from confirmed terms with valid strategic scores.
- Preserve existing `## Metadata` `### History` entries unless explicitly updating them through `aso-metadata-generation`.
- Use `Notes` for compact context that helps later skills interpret a search term, such as source nuance, brand or competitor warnings, intentional spelling or grammar mistakes, long-tail variants, review language, questionable relevance, or user verification details.
- Preserve existing backlog columns and values unless the user approves a change. Later skills may add columns, but this skill must not drop them.
- Preserve rejected search terms when they prevent repeated suggestions.
- Update `*Last updated:*` whenever the file changes.
