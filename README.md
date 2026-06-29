# App Store Optimization Skills

Agent skill suite for App Store Optimization: orchestrate end-to-end metadata optimization, identify and relevance-score broad App Store search-term candidates, fetch external keyword statistics, calculate derived search-term scores, generate App Store metadata drafts, track keyword rankings, analyze post-publish metadata performance, and localize ASO work per Apple metadata locale and country or region.

## Purpose

This repository provides ASO-focused agent skills that help agents:

- run a guided end-to-end App Store metadata optimization workflow with review stops
- identify a broad backlog of plausible App Store search terms and score how well each term fits the app and App Store search intent
- fetch validated external popularity and difficulty metrics for confirmed search terms
- calculate derived strategic scores and per-word value scores for confirmed terms
- track keyword rankings over time with the current App Store version as one post-publish evidence source
- analyze whether published metadata changes improved, hurt, or had no clear effect on search discoverability
- prioritize which App Store product page metadata localizations to create or refresh using funnel, revenue, retention, ratings, search, and evidence-quality signals
- generate an auditable recommended App Store metadata draft with grouped fields, counts, coverage, warnings, and notes, then save approved choices in compact metadata history
- optimize localized metadata in Apple-locale workspaces with localized values, compact field-meaning annotations, and derived country or region targets for statistics and rankings

## Skills

### aso-metadata-workflow

Recommended user-facing entrypoint for a full source-locale App Store metadata optimization workflow. It guides the agent through app context, search-term identification plus relevance assignment and validation, statistics fetching, search-term scoring, and metadata generation with explicit review stops where user judgment is needed.

### aso-localized-metadata-workflow

Recommended user-facing entrypoint for optimizing metadata in another language, locale, country or region, storefront, or Apple country or region ISO code. It suggests and validates Apple-supported metadata locales, creates workspaces under `.agents/aso/locales/<Locale>/context.md`, uses source terms as intent seeds instead of literal translations, derives countries or regions only when needed, and generates localized metadata drafts with compact meaning annotations for saved values.

### aso-localization-prioritization

Recommended user-facing entrypoint for deciding which App Store product page metadata localizations to create or refresh first for app name, subtitle, and keywords. It uses App Store Connect/App Analytics data from the user or available App Store Connect-capable tools, such as `asc`, the Helm CLI (`helm-asc`), the App Store Connect API, or user-provided tooling, inspects existing localized metadata when available, maps territories to Apple-supported metadata localizations, and ranks new-localization and existing-locale refresh opportunities with funnel, monetization, retention, ratings, search-opportunity, and evidence-quality signals. It does not plan full app translation or broader market launch work.

### aso-context

Internal foundation skill used by the workflow and specialist skills. It stores global/source context in `.agents/aso/context.md`, including private App Store Connect keyword fields when they are available and documented source gaps when they are not. Users typically start with `aso-metadata-workflow` for a full source-locale optimization run, `aso-localization-prioritization` to decide which metadata localization to create or refresh first, `aso-localized-metadata-workflow` for a chosen localized metadata target, or `aso-search-terms-identification` for a narrower keyword research task.

### aso-search-terms-identification

Identifies a broad single-language or localized backlog of plausible App Store search-term candidates from app details, public listing or marketing sources, existing App Store Connect keyword terms, competitor research, reviews, user input, brand terms, local search behavior, and phrase variants. It also assigns `1`-`5` relevance scores based on App Store search intent and how well the app satisfies that intent. Source-locale relevance is user-reviewed; localized relevance uses back-translated meanings and agent-led review by default, asking the user when ambiguity matters.

### aso-search-terms-statistics

Fetches external popularity and difficulty statistics for confirmed search terms and records them in the active ASO context or locale workspace. Use this after search terms have approved relevance scores and before search-term scoring or metadata placement. These values must come from tools such as ASO Suite or Astro, compatible user-provided exports, or normalized Apple Ads Search Popularity for popularity only; the agent should not infer them from unrelated metrics. Stats older than one month should be refreshed when possible, and localized stats must match the resolved country or region.

### aso-search-terms-rankings

Tracks keyword rankings and trends for confirmed search terms, including the current App Store version for each saved ranking run. Use this for periodic ranking checks or monitoring search-term position movement after metadata changes.

### aso-metadata-performance-analysis

Analyzes whether published App Store metadata changes improved, hurt, or had no clear effect on search discoverability and downstream quality. It uses App Store Connect, App Analytics, Sales/Trends, Search Ads, and keyword ranking evidence when available.

### aso-search-terms-scoring

Calculates derived `Strategic score` values for confirmed App Store search terms and derived per-word value scores from those strategic scores. Use this after search terms have relevance scores and statistics to prioritize terms and identify individual words that cover the most strategic search-term value per metadata character.

### aso-metadata-generation

Generates one recommended source-locale or localized App Store metadata draft for shared app name, shared subtitle, and platform-specific keyword fields from confirmed search terms, `Strategic score` values, saved `Word Value Scores`, current metadata, ranking evidence when available, and saved metadata history guidance. Use this after search-term scoring to create a metadata draft and coverage analysis. Review output uses grouped draft sections with counts, recommendation rationale, coverage, warnings, and notes; explicit saves append compact entries under `## Metadata` `### History`, and current approvals update `## Metadata` `### Current`.

## Artifacts

- Global/source context with `## Metadata` `### Current` and `### History`: `.agents/aso/context.md`
- Source-locale keyword rankings: `.agents/aso/keyword-rankings.md`
- Source-locale metadata performance analysis: `.agents/aso/metadata-performance-analysis.md`
- Localization prioritization: `.agents/aso/localization-prioritization.md`
- Localized workspaces with the same compact metadata current/history model: `.agents/aso/locales/<Locale>/context.md`
- Localized keyword rankings: `.agents/aso/locales/<Locale>/keyword-rankings.md`
- Localized metadata performance analysis: `.agents/aso/locales/<Locale>/metadata-performance-analysis.md`
## Workflow

Use `aso-metadata-workflow` for a guided end-to-end source-locale optimization run. It coordinates the specialist skills in this order:

1. Use `aso-context` to create or verify the shared ASO context.
2. Use `aso-search-terms-identification` to build or expand the search-term backlog and assign user-reviewed relevance scores.
3. Use `aso-search-terms-statistics` to fetch popularity and difficulty values for the relevant primary locale.
4. Use `aso-search-terms-scoring` to calculate strategic priority scores and per-word metadata value scores.
5. Use `aso-metadata-generation` to generate a recommended App Store metadata draft, review coverage tradeoffs, and save approved drafts, edits, current choices, or published snapshots under metadata history.

Use `aso-localization-prioritization` when deciding which App Store product page metadata localization to create or refresh first. It stays metadata-first, but can use revenue, retention, ratings, search, existing localized metadata, and risk signals to avoid prioritizing a locale where metadata is unlikely to be the main bottleneck. Use `aso-localized-metadata-workflow` when optimizing a chosen locale or country or region. It follows the same specialist sequence, but first validates the Apple metadata locale, derives or stores a country or region only when needed, then writes terms, relevance, statistics, scoring, and saved metadata history to the matching localized workspace.

After publishing metadata changes, use `aso-search-terms-rankings` periodically to collect ranking evidence, then use `aso-metadata-performance-analysis` to evaluate broader search-source performance, Search Ads impact, and downstream guardrails.

## Roadmap

Future skill-suite extensions may cover adjacent App Store discoverability work that is outside the current metadata workflow:

- Custom product page keyword strategy
- Promoted In-App Purchase and In-App Event discoverability
- Full product page localization, including screenshots and app previews

## Inspiration

This skill suite is inspired by the following MIT-licensed projects:

- Corey Haines's [Marketing Skills](https://github.com/coreyhaines31/marketingskills)
  Copyright (c) 2025 Corey Haines
- Antoine van der Lee's [Xcode Build Optimization Agent Skill](https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill)
  Copyright (c) 2026 Antoine van der Lee
