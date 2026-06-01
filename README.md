# App Store Optimization Skills

Agent skill suite for App Store Optimization: orchestrate end-to-end metadata optimization, identify broad App Store search-term candidates, score keyword relevance, fetch external keyword statistics, calculate derived search-term scores, generate App Store metadata drafts, and localize ASO work per locale and region.

## Purpose

This repository provides ASO-focused agent skills that help agents:

- run a guided end-to-end App Store metadata optimization workflow with review stops
- identify a broad backlog of plausible App Store search terms
- score how well each search term fits the app and App Store search intent
- fetch validated external popularity and difficulty metrics for confirmed search terms
- calculate derived strategic scores and per-word value scores for confirmed terms
- generate App Store metadata variants from confirmed terms and word value scores
- optimize localized metadata in region-correct per-locale workspaces

## Skills

### aso-metadata-workflow

Recommended user-facing entrypoint for a full source-locale App Store metadata optimization workflow. It guides the agent through app context, search-term identification, relevance scoring, statistics fetching, search-term scoring, and metadata generation with explicit review stops between phases.

### aso-localized-metadata-workflow

Recommended user-facing entrypoint for optimizing metadata in another language, locale, country, storefront, region, or Apple ISO code. It suggests and validates Apple-supported country/language pairs, creates workspaces under `.agents/aso/locales/<ISO code>/`, uses source terms as intent seeds instead of literal translations, derives ASO tool regions only when needed, and generates localized metadata drafts.

### aso-context

Internal foundation skill used by the workflow and specialist skills. It stores global/source context in `.agents/aso/context.md`. Users typically start with `aso-metadata-workflow` for a full source-locale optimization run, `aso-localized-metadata-workflow` for localized metadata, or `aso-search-terms-identification` for a narrower keyword research task.

### aso-search-terms-identification

Identifies a broad single-language or localized backlog of plausible App Store search-term candidates from app details, public listing or marketing sources, existing App Store Connect keyword terms, competitor research, reviews, user input, brand terms, local search behavior, and phrase variants. Use this before relevance scoring.

### aso-search-terms-relevance-scoring

Assigns `1`-`5` relevance scores to search terms, based on App Store search intent and how well the app satisfies that intent. Source-locale relevance is user-reviewed; localized relevance uses back-translated meanings and agent-led review by default, asking the user when ambiguity matters. Use this after search-term identification.

### aso-search-terms-statistics

Fetches external popularity and difficulty statistics for confirmed search terms and records them in the active ASO context or locale workspace. Use this after relevance scoring and before search-term scoring or metadata placement. These values must come from tools such as ASO Suite or Astro; the agent should not infer them. Stats older than one month should be refreshed when possible, and localized stats must match the target region.

### aso-search-terms-scoring

Calculates derived `Strategic score` values for confirmed search terms and derived per-word value scores from those strategic scores. Use this after relevance scoring and statistics fetching to prioritize terms and identify individual words that cover the most strategic search-term value per metadata character.

### aso-metadata-generation

Generates source-locale or localized App Store metadata drafts for app name, subtitle, and keywords from confirmed search terms, `Strategic score` values, and saved `Word Value Scores`. Use this after search-term scoring to create metadata variants. Keyword fields are counted against Apple's 100-byte limit.

## Artifacts

- Global/source context: `.agents/aso/context.md`
- Localized workspaces: `.agents/aso/locales/<ISO code>/<language-slug>.md`
- Shared App Store localizations reference: `references/app-store-localizations.md`

## Workflow

Use `aso-metadata-workflow` for a guided end-to-end source-locale optimization run. It coordinates the specialist skills in this order:

1. Use `aso-context` to create or verify the shared ASO context.
2. Use `aso-search-terms-identification` to build or expand the search-term backlog.
3. Use `aso-search-terms-relevance-scoring` to assign user-reviewed relevance scores.
4. Use `aso-search-terms-statistics` to fetch popularity and difficulty values for the relevant App Store region.
5. Use `aso-search-terms-scoring` to calculate strategic priority scores and per-word metadata value scores.
6. Use `aso-metadata-generation` to generate App Store metadata drafts and compare coverage tradeoffs.

Use `aso-localized-metadata-workflow` when optimizing another locale or region. It follows the same specialist sequence, but first suggests and validates the Apple ISO code and metadata language, then writes terms, relevance, statistics, scoring, and drafts to the matching localized workspace.

## Inspiration

This skill suite is inspired by the following MIT-licensed projects:

- Corey Haines's [Marketing Skills](https://github.com/coreyhaines31/marketingskills)
  Copyright (c) 2025 Corey Haines
- Antoine van der Lee's [Xcode Build Optimization Agent Skill](https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill)
  Copyright (c) 2026 Antoine van der Lee
