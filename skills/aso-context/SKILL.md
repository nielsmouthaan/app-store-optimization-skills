---
name: aso-context
description: Provides, creates, and updates the context stored in `.agents/aso-context.md` that other skills may use for ASO purposes. Use when setting up ASO context, analyzing an App Store URL, analyzing a marketing or landing page URL, or performing ASO for an existing or pre-launch app.
---

# ASO Context

Create and maintain `.agents/aso-context.md`, which captures context that other skills reference so users do not repeat themselves.

The context should be compact, factual, and useful for later keyword research, search term ideation, metadata generation, and localization.

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
- Local product docs, metadata files, README, or website copy
- User-provided app description

Use whichever sources are available. If multiple sources are available, combine them.

### 3. Populate From Sources

When using an **App Store URL**, extract what is publicly available:

- Name, subtitle, developer, and category
- Description
- Visible screenshot text using OCR when possible
- Review themes and user language
- Competitors or similar apps, including links when available

When using a **marketing or landing page URL**, extract only ASO-useful context:

- Product description
- Features
- Use cases
- Solution to problem
- Keywords and app category

When using **local files**, prefer sources that describe the app for users:

- App Store metadata files
- README files
- Landing page copy
- Product docs
- Release notes

When using a **user description**, capture the user's wording directly where it may help later search term generation.

### 4. Ask Only For Useful Gaps

After drafting the context, ask for corrections or missing details only when they materially affect ASO work.

Good follow-up questions are narrow:

- "Is this the category you want to optimize for?"
- "Are any of these similar apps not real competitors?"
- "Which countries or languages should later ASO work focus on?"
- "Is any review or screenshot language misleading for the app?"

Avoid asking the user to complete a long questionnaire.

### 5. Save The Context

Create or update `.agents/aso-context.md` using this structure:

```markdown
# ASO App Context
*Last updated: YYYY-MM-DD*

## Source
**App Store URL:**
**Marketing URL:**
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
```

Omit unavailable sections when they add no value. For example, omit `## Reviews` for a pre-launch app with no public reviews.

## Writing Rules

- Keep the file concise enough for other skills to read quickly.
- Prefer factual extraction over interpretation.
- Do not invent missing metadata, competitors, review themes, or screenshot text.
- Preserve keyword-rich phrases from source material when they are natural and accurate.
- Summarize reviews into themes instead of copying long review text.
- Include competitor and similar app links when available; otherwise use plain app names.
- Update `*Last updated:*` whenever the file changes.
