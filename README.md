# App Store Optimization Skills

Agent skill suite for App Store Optimization: orchestrate end-to-end metadata optimization, identify broad App Store search-term candidates, score keyword relevance, fetch external keyword statistics, calculate derived search-term scores, generate App Store metadata drafts, track keyword rankings, and localize ASO work per locale and region.

## Purpose

This repository provides ASO-focused agent skills that help agents:

- run a guided end-to-end App Store metadata optimization workflow with review stops
- identify a broad backlog of plausible App Store search terms
- score how well each search term fits the app and App Store search intent
- fetch validated external popularity and difficulty metrics for confirmed search terms
- calculate derived strategic scores and per-word value scores for confirmed terms
- track keyword rankings over time for later performance evaluation
- prioritize which App Store product page metadata localizations to target first
- generate auditable App Store metadata variants with grouped fields, counts, coverage, and notes
- optimize localized metadata in region-correct per-locale workspaces with localized values and adjacent user-readable meanings

## Skills

### aso-metadata-workflow

Recommended user-facing entrypoint for a full source-locale App Store metadata optimization workflow. It guides the agent through app context, search-term identification, relevance scoring, statistics fetching, search-term scoring, and metadata generation with explicit review stops between phases.

### aso-localized-metadata-workflow

Recommended user-facing entrypoint for optimizing metadata in another language, locale, country, storefront, region, or Apple ISO code. It suggests and validates Apple-supported country/language pairs, creates workspaces under `.agents/aso/locales/<ISO code>/`, uses source terms as intent seeds instead of literal translations, derives ASO tool regions only when needed, and generates localized metadata drafts with `Meaning` lines for generated values.

### aso-localization-prioritization

Recommended user-facing entrypoint for deciding which App Store product page metadata localizations to prioritize first for organic search impact. It uses App Store Connect/App Analytics data from the user or `asc` when available, maps territories to Apple-supported metadata localizations, and saves a compact prioritization artifact. It is limited to prioritizing app name, subtitle, and keywords; it does not plan full app translation.

### aso-context

Internal foundation skill used by the workflow and specialist skills. It stores global/source context in `.agents/aso/context.md`. Users typically start with `aso-metadata-workflow` for a full source-locale optimization run, `aso-localization-prioritization` to decide which metadata localization to target first, `aso-localized-metadata-workflow` for a chosen localized metadata target, or `aso-search-terms-identification` for a narrower keyword research task.

### aso-search-terms-identification

Identifies a broad single-language or localized backlog of plausible App Store search-term candidates from app details, public listing or marketing sources, existing App Store Connect keyword terms, competitor research, reviews, user input, brand terms, local search behavior, and phrase variants. Use this before relevance scoring.

### aso-search-terms-relevance-scoring

Assigns `1`-`5` relevance scores to search terms, based on App Store search intent and how well the app satisfies that intent. Source-locale relevance is user-reviewed; localized relevance uses back-translated meanings and agent-led review by default, asking the user when ambiguity matters. Use this after search-term identification.

### aso-search-terms-statistics

Fetches external popularity and difficulty statistics for confirmed search terms and records them in the active ASO context or locale workspace. Use this after relevance scoring and before search-term scoring or metadata placement. These values must come from tools such as ASO Suite or Astro; the agent should not infer them. Stats older than one month should be refreshed when possible, and localized stats must match the target region.

### aso-search-terms-rankings

Tracks keyword rankings and trends for confirmed search terms. Use this for periodic ranking checks, post-publish evaluation, or monitoring whether metadata changes improved keyword performance.

### aso-search-terms-scoring

Calculates derived `Strategic score` values for confirmed search terms and derived per-word value scores from those strategic scores. Use this after relevance scoring and statistics fetching to prioritize terms and identify individual words that cover the most strategic search-term value per metadata character.

### aso-metadata-generation

Generates source-locale or localized App Store metadata drafts for shared app name, shared subtitle, and platform-specific keyword sections from confirmed search terms, `Strategic score` values, and saved `Word Value Scores`. Use this after search-term scoring to create metadata variants. Drafts use grouped variant blocks with app name/subtitle sections, `Keywords (<platform>)` sections, counts, coverage, and notes. Keyword fields are counted against Apple's 100-byte limit per platform.

## Artifacts

- Global/source context: `.agents/aso/context.md`
- Source-locale keyword rankings: `.agents/aso/keyword-rankings.md`
- Localization prioritization: `.agents/aso/localization-prioritization.md`
- Localized workspaces: `.agents/aso/locales/<ISO code>/<language-slug>.md`
- Localized keyword rankings: `.agents/aso/locales/<ISO code>/<language-slug>-keyword-rankings.md`
- Shared App Store localizations reference: `references/app-store-localizations.md`
- Shared platform terminology reference: `references/platforms.md`

## Workflow

Use `aso-metadata-workflow` for a guided end-to-end source-locale optimization run. It coordinates the specialist skills in this order:

1. Use `aso-context` to create or verify the shared ASO context.
2. Use `aso-search-terms-identification` to build or expand the search-term backlog.
3. Use `aso-search-terms-relevance-scoring` to assign user-reviewed relevance scores.
4. Use `aso-search-terms-statistics` to fetch popularity and difficulty values for the relevant primary locale.
5. Use `aso-search-terms-scoring` to calculate strategic priority scores and per-word metadata value scores.
6. Use `aso-metadata-generation` to generate App Store metadata drafts and compare coverage tradeoffs.

Use `aso-localization-prioritization` when deciding which App Store product page metadata localization to target first. Use `aso-localized-metadata-workflow` when optimizing a chosen locale or region. It follows the same specialist sequence, but first validates the Apple ISO code and metadata language, then writes terms, relevance, statistics, scoring, and drafts to the matching localized workspace.

After publishing metadata changes, use `aso-search-terms-rankings` periodically to check keyword rankings for later performance evaluation. Prefer ASO Suite (https://nielsmouthaan.dev/asosuite) or Astro (https://nielsmouthaan.dev/astro).

## Inspiration

This skill suite is inspired by the following MIT-licensed projects:

- Corey Haines's [Marketing Skills](https://github.com/coreyhaines31/marketingskills)
  Copyright (c) 2025 Corey Haines
- Antoine van der Lee's [Xcode Build Optimization Agent Skill](https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill)
  Copyright (c) 2026 Antoine van der Lee
