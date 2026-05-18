# App Store Optimization Skills

Agent skill suite for App Store Optimization: research and prioritize keywords, generate localized metadata, and guide ASO workflows with shared app context.

## Purpose

This repository will become a multi-skill suite for turning ASO keyword research into App Store metadata. It should help agents:

- identify relevant App Store search terms and assess how well they fit the app
- research each term's popularity and ranking difficulty
- prioritize terms and individual words by their strategic value
- generate app names, subtitles, and keyword fields from the strongest keyword opportunities
- localize metadata using locale-specific keyword evidence

The intended outcome is a reusable skill suite that helps apps rank organically for relevant search terms and drive more downloads from users actively looking for an app like it.

## Skills

### aso-context

Internal foundation skill used by specialized skills and workflows to create or update `.agents/aso-context.md`, which captures app context and reusable ASO artifacts such as the search-term backlog. Users typically do not need to call this skill explicitly.

### aso-search-terms-identification

Identifies a broad single-language backlog of plausible App Store search-term candidates from app context, public listing/marketing sources, existing ASC keyword terms, competitor research, reviews, SEO/ASO tools, user input, brand terms, and phrase variants. It asks for key external sources before the first backlog and filters candidates for App Store search plausibility. Use this before relevance scoring, prioritization, or metadata generation.

### aso-search-terms-relevance-scoring

Assigns carefully user-reviewed 0-5 relevance scores to search terms in the shared ASO context, based on App Store search intent and how well the app satisfies that intent. Own-brand terms are treated as highly relevant. Use this after search-term identification and before later prioritization or metadata strategy work.

## Inspiration

This skill suite is inspired by the following MIT-licensed projects:

- Corey Haines's [Marketing Skills](https://github.com/coreyhaines31/marketingskills)  
  Copyright (c) 2025 Corey Haines
- Antoine van der Lee's [Xcode Build Optimization Agent Skill](https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill)  
  Copyright (c) 2026 Antoine van der Lee
