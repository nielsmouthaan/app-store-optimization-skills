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

Internal foundation skill used by specialized skills and workflows to create or update `.agents/aso-context.md`, which captures context that other skills reference so users do not repeat themselves. Users typically do not need to call this skill explicitly.

## Inspiration

This skill suite is inspired by the following MIT-licensed projects:

- Corey Haines's [Marketing Skills](https://github.com/coreyhaines31/marketingskills)  
  Copyright (c) 2025 Corey Haines
- Antoine van der Lee's [Xcode Build Optimization Agent Skill](https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill)  
  Copyright (c) 2026 Antoine van der Lee
