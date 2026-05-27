# App Store Optimization Skills

Agent skill suite for App Store Optimization: orchestrate end-to-end metadata optimization, identify broad App Store search-term candidates, score keyword relevance, fetch external keyword statistics, calculate strategic priority scores, derive per-word metadata value scores, and generate App Store metadata drafts.

## Purpose

This repository provides ASO-focused agent skills that help agents:

- run a guided end-to-end App Store metadata optimization workflow with review stops
- identify a broad backlog of plausible App Store search terms
- score how well each search term fits the app and App Store search intent
- fetch validated external popularity and difficulty metrics for confirmed search terms
- calculate derived strategic scores for confirmed terms to guide metadata focus
- calculate per-word value scores to prioritize character-efficient metadata coverage
- generate App Store metadata variants from confirmed terms and word value scores

## Skills

### aso-metadata-workflow

Recommended user-facing entrypoint for a full App Store metadata optimization workflow. It guides the agent through app context, search-term identification, relevance scoring, statistics fetching, strategic scoring, word value scoring, and metadata generation with explicit review stops between phases.

### aso-context

Internal foundation skill used by the workflow and specialist skills. Users typically start with `aso-metadata-workflow` for a full optimization run or `aso-search-terms-identification` for a narrower keyword research task.

### aso-search-terms-identification

Identifies a broad single-language backlog of plausible App Store search-term candidates from app details, public listing or marketing sources, existing App Store Connect keyword terms, competitor research, reviews, user input, brand terms, and phrase variants. Use this before relevance scoring.

### aso-search-terms-relevance-scoring

Assigns user-reviewed `1`-`5` relevance scores to search terms, based on App Store search intent and how well the app satisfies that intent. Use this after search-term identification.

### aso-search-terms-statistics

Fetches external popularity and difficulty statistics for confirmed search terms and records them in the ASO context. Use this after relevance scoring and before strategic scoring or metadata placement. These values must come from tools such as ASO Suite or Astro; the agent should not infer them. Stats older than one month should be refreshed when possible.

### aso-search-terms-strategic-scoring

Calculates a derived `Strategic score` for confirmed search terms with approved relevance and fetched popularity and difficulty values. Use this after statistics fetching and before deciding which terms should receive metadata focus.

### aso-search-terms-word-value-scoring

Calculates derived per-word value scores from confirmed search terms and their `Strategic score` values. Use this after strategic scoring to identify individual words that cover the most strategic search-term value per metadata character.

### aso-metadata-generation

Generates single-locale App Store metadata drafts for app name, subtitle, and keywords from confirmed search terms, `Strategic score` values, and saved `Word Value Scores`. Use this after word value scoring to create metadata variants.

## Workflow

Use `aso-metadata-workflow` for a guided end-to-end optimization run. It coordinates the specialist skills in this order:

1. Use `aso-context` to create or verify the shared ASO context.
2. Use `aso-search-terms-identification` to build or expand the search-term backlog.
3. Use `aso-search-terms-relevance-scoring` to assign user-reviewed relevance scores.
4. Use `aso-search-terms-statistics` to fetch popularity and difficulty values for the relevant App Store region.
5. Use `aso-search-terms-strategic-scoring` to calculate strategic priority scores for confirmed terms.
6. Use `aso-search-terms-word-value-scoring` to calculate per-word metadata value scores from strategic scores.
7. Use `aso-metadata-generation` to generate App Store metadata drafts and compare coverage tradeoffs.

## Inspiration

This skill suite is inspired by the following MIT-licensed projects:

- Corey Haines's [Marketing Skills](https://github.com/coreyhaines31/marketingskills)
  Copyright (c) 2025 Corey Haines
- Antoine van der Lee's [Xcode Build Optimization Agent Skill](https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill)
  Copyright (c) 2026 Antoine van der Lee
