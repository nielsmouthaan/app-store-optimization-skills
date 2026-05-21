# App Store Optimization Skills

Agent skill suite for App Store Optimization: identify broad App Store search-term candidates, score keyword relevance, fetch external keyword statistics, calculate strategic priority scores, and derive per-word metadata value scores.

## Purpose

This repository provides ASO-focused agent skills that help agents:

- identify a broad backlog of plausible App Store search terms
- score how well each search term fits the app and App Store search intent
- fetch external popularity and difficulty metrics for search terms
- calculate derived strategic scores for confirmed terms to guide metadata focus
- calculate per-word value scores to prioritize character-efficient metadata coverage

## Skills

### aso-context

Internal foundation skill used by the specialist skills. Users typically start with `aso-search-terms-identification` instead of invoking this directly.

### aso-search-terms-identification

Identifies a broad single-language backlog of plausible App Store search-term candidates from app details, public listing or marketing sources, existing App Store Connect keyword terms, competitor research, reviews, user input, brand terms, and phrase variants. Use this before relevance scoring.

### aso-search-terms-relevance-scoring

Assigns user-reviewed `1`-`5` relevance scores to search terms, based on App Store search intent and how well the app satisfies that intent. Use this after search-term identification.

### aso-search-terms-statistics

Fetches external popularity and difficulty statistics for non-rejected search terms and records them in the ASO context. Use this after relevance scoring and before strategic scoring or metadata placement. These values must come from tools such as ASO Suite or Astro; the agent should not infer them.

### aso-search-terms-strategic-scoring

Calculates a derived `Strategic score` for confirmed search terms with approved relevance and fetched popularity and difficulty values. Use this after statistics fetching and before deciding which terms should receive metadata focus.

### aso-search-terms-word-value-scoring

Calculates derived per-word value scores from confirmed search terms and their `Strategic score` values. Use this after strategic scoring to identify individual words that cover the most strategic search-term value per metadata character.

## Workflow

1. Use `aso-search-terms-identification` to build or expand the search-term backlog.
2. Use `aso-search-terms-relevance-scoring` to assign user-reviewed relevance scores.
3. Use `aso-search-terms-statistics` to fetch popularity and difficulty values for the relevant App Store region.
4. Use `aso-search-terms-strategic-scoring` to calculate strategic priority scores for confirmed terms.
5. Use `aso-search-terms-word-value-scoring` to calculate per-word metadata value scores from strategic scores.

## Inspiration

This skill suite is inspired by the following MIT-licensed projects:

- Corey Haines's [Marketing Skills](https://github.com/coreyhaines31/marketingskills)
  Copyright (c) 2025 Corey Haines
- Antoine van der Lee's [Xcode Build Optimization Agent Skill](https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill)
  Copyright (c) 2026 Antoine van der Lee
