---
name: aso-context
description: Provides, creates, and updates the context stored in `.agents/aso-context.md` that other skills may use for ASO purposes. Use when setting up ASO context, analyzing an App Store URL, analyzing a marketing or landing page URL, or performing ASO for an existing or pre-launch app.
---

# ASO Context

Create and maintain `.agents/aso-context.md`, which captures context that other skills reference so users do not repeat themselves.

The context should be compact, factual, and useful for later search-term identification, keyword research, metadata generation, and localization.

## Workflow

### 1. Check Existing Context

First, check whether `.agents/aso-context.md` exists.

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
- App Store Connect keyword field terms
- Local product docs, metadata files, README, or website copy
- User-provided app description
- Any additional source that may help search-term discovery, such as competitor lists, customer language, support requests, review exports, ASO tool exports, SEO tool exports, Apple Search Ads terms, or keyword research files

Use whichever sources are available. If multiple sources are available, combine them.

If an App Store URL or marketing URL is provided, inspect it before deriving ASO context from local files alone. If the current environment cannot access the URL, ask the user to paste relevant copy and note the access gap.

### 3. Populate From Sources

When using an **App Store URL**, extract what is publicly available:

- Name, subtitle, developer, and category
- Description
- Visible screenshot text using OCR when possible
- Review themes and user language
- Competitors or similar apps, including links when available

After finding or receiving an App Store URL, explicitly ask the user to provide the current App Store Connect keyword field terms. These are not public, but they are important source material for ASO search-term work. Continue only after the user provides them or explicitly says to skip them.

When using a **marketing or landing page URL**, extract only ASO-useful context:

- Product description
- Features
- Use cases
- Solution to problem
- Keywords and app category

When using **App Store Connect keyword field terms**, capture them as source material for search-term discovery. Do not treat them as automatically approved or final search terms.

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

After review and adjustment, create or update `.agents/aso-context.md` using this structure:

```markdown
# ASO App Context
*Last updated: YYYY-MM-DD*

## Source
**Search language:** English, unless otherwise specified.
**App Store URL:**
**Marketing URL:**
**App Store Connect keywords:**
**Other sources:**

## Metadata
**Name:**
**Subtitle:**
**Developer:**
**Category:**

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
| Search term | Source | Status | Notes |
| --- | --- | --- | --- |
| example term | app description | candidate | feature phrase |
```

Omit unavailable sections when they add no value. For example, omit `## Reviews` for a pre-launch app with no public reviews.

## Writing Rules

- Keep the file concise enough for other skills to read quickly.
- Prefer factual extraction over interpretation.
- Do not invent missing metadata, competitors, review themes, or screenshot text.
- Preserve keyword-rich phrases from source material when they are natural and accurate.
- Summarize reviews into themes instead of copying long review text.
- Include competitor and similar app links when available; otherwise use plain app names.
- Store one active search language for the backlog; default to English when unspecified.
- Use `candidate`, `confirmed`, or `rejected` for search-term backlog status values.
- Use `Notes` for compact context that helps later skills interpret a search term, such as source nuance, brand or competitor warnings, intentional spelling or grammar mistakes, long-tail variants, review language, questionable relevance, or user verification details.
- Preserve rejected search terms when they prevent repeated suggestions.
- Update `*Last updated:*` whenever the file changes.
