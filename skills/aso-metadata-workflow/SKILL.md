---
name: aso-metadata-workflow
description: Runs the end-to-end App Store optimization workflow for the app's primary or source metadata language. Use for full primary listing optimization, organic search metadata work, or coordinating context, keyword research, relevance scoring, statistics, strategic scoring, and metadata drafts. For other languages, countries or regions, use aso-localized-metadata-workflow.
---

# ASO Metadata Workflow

Use this skill as the primary entrypoint for end-to-end App Store metadata optimization for organic search discoverability in the primary/source locale.

For requests involving another language, locale, country or region, or storefront, use `aso-localized-metadata-workflow` instead.

This workflow coordinates the specialist ASO skills. It owns sequencing, prerequisites, review gates, and handoffs. It does not replace specialist skill instructions.

## Non-Negotiable Rules

- Use `.agents/aso/context.md` as the single workflow artifact and handoff file.
- Keep localized work in `.agents/aso/locales/<Locale>/context.md` through `aso-localized-metadata-workflow`; do not run multi-locale work inside this source workflow.
- Read the relevant specialist skill before executing each phase, then follow that skill's workflow.
- Do not duplicate formulas, scoring rubrics, metadata field rules, or table schemas from specialist skills.
- Stop for user review before saving user-judgment inputs: app context, search-term backlog, relevance scores, and final metadata choices.
- Do not estimate popularity or difficulty. They must come from an external ASO statistics source.
- Do not generate metadata drafts until confirmed terms have strategic scores and word value scores.
- Do not publish or update App Store Connect metadata unless the user explicitly asks for that action.

## Workflow Overview

Run phases in this order:

1. Establish app context with `aso-context`.
2. Identify search terms with `aso-search-terms-identification`.
3. Validate relevance with `aso-search-terms-relevance-scoring`.
4. Fetch statistics with `aso-search-terms-statistics`.
5. Calculate search term scores with `aso-search-terms-scoring`.
6. Generate metadata drafts with `aso-metadata-generation`.

After every phase, summarize:

- the phase completed
- what changed in `.agents/aso/context.md`
- blockers or source gaps
- the next required review or phase

## Phase 0: Establish Context

Use `aso-context` when `.agents/aso/context.md` is missing, stale, incomplete, or contradicted by new source material.

The context must identify, when available:

- primary locale and optional country or region preference
- App Store Connect platforms
- App Store URL
- marketing URL
- App Store Connect keyword field terms by platform
- app metadata, use cases, features, reviews, and competitors

Stop after drafting or updating the context. Ask the user to confirm what is incorrect, missing, or misleading before treating the context as ready for search-term work.

## Phase 1: Identify Search Terms

Use `aso-search-terms-identification` to create or expand the search-term backlog.

Before proceeding, confirm that the backlog is broad enough for later scoring and includes plausible App Store search phrases, source notes, and useful variants.

Stop after presenting proposed terms. Let the user accept, reject, correct, or add terms before saving or moving to relevance scoring. Save accepted terms as `confirmed`, rejected terms as `rejected`, and unreviewed suggestions or imports as `candidate`. Preserve rejected terms so future runs do not suggest them again.

## Phase 2: Validate Relevance

Use `aso-search-terms-relevance-scoring` to assign user-reviewed `1`-`5` relevance scores to confirmed terms.

Relevance is a user-judgment input for all later prioritization. Stop before saving scores and require explicit user approval or corrections to the relevance groups.

After approved scores are saved, continue only with confirmed terms.

## Phase 3: Fetch Statistics

Use `aso-search-terms-statistics` to fetch popularity and difficulty for confirmed terms.

Use the primary locale from context, or let the statistics skill derive or ask for it according to its locale-selection rules.

Before continuing, let the statistics skill show confirmed terms with missing statistics or statistics more than one month old. If the user declines to refresh outdated statistics, continue only with a stale-statistics warning.

Stop if:

- no statistics source is available
- credentials are missing
- usage limits are reached
- the primary locale is unresolved
- the statistics tool cannot be accessed

Do not estimate or infer missing popularity or difficulty values. Report the blocker and the missing upstream requirement.

## Phase 4: Calculate Search Term Scores

Use `aso-search-terms-scoring` after confirmed terms have valid relevance, popularity, and difficulty values.

This phase is deterministic. It may save derived strategic scores and word value scores once prerequisites are satisfied, but it must not change relevance, statistics, statuses, notes, or metadata placement.

If no confirmed terms are eligible, stop and report which upstream input is missing.

## Phase 5: Generate Metadata Drafts

Use `aso-metadata-generation` after strategic scores and word value scores exist.

Generate metadata variants and coverage analysis for the active source locale. Stop after presenting grouped variants, warnings, coverage tradeoffs, and the recommended option.

Save a draft, update current context metadata, or publish to App Store Connect only when the user explicitly approves the relevant save or publish action.

After metadata goes live, recommend checking keyword rankings periodically with `aso-search-terms-rankings`, then using `aso-metadata-performance-analysis` to evaluate broader search-source performance, Search Ads impact, and downstream guardrails.

## Review Gates

Use these gates to decide whether the workflow can continue:

| Gate | Required user or tool confirmation | Next phase |
| --- | --- | --- |
| Context approved | User confirms app context and source gaps are acceptable | Search-term identification |
| Backlog approved | User accepts, rejects, corrects, or adds proposed terms; accepted terms are saved as `confirmed` | Relevance scoring |
| Relevance approved | User explicitly approves or corrects relevance groups | Statistics fetching |
| Statistics available | External source provides validated popularity and difficulty for the target country or region, or the user accepts stale statistics with a warning | Search term scoring |
| Search term scores saved | Eligible confirmed terms have derived strategic scores and word value scores are saved in context | Metadata generation |
| Metadata choice approved | User approves a draft, current metadata update, or publish action | Save or publish according to `aso-metadata-generation` |

## Completion Report

End the workflow with a compact report:

- primary locale and platforms
- number of backlog terms, confirmed terms, rejected terms, and scored terms
- statistics source and update date
- highest strategic terms and highest-value words
- metadata variant recommended or saved
- field counts and coverage summary
- unresolved source gaps, warnings, or follow-up tests

If metadata was only saved as a draft, state that App Store Connect was not updated.

## Related Skills

- Use `aso-context` to create or update shared app context.
- Use `aso-search-terms-identification` to create or expand the search-term backlog.
- Use `aso-search-terms-relevance-scoring` to assign user-reviewed relevance scores.
- Use `aso-search-terms-statistics` to fetch popularity and difficulty.
- Use `aso-search-terms-scoring` to calculate derived strategic scores and per-word value scores.
- Use `aso-metadata-generation` to generate and save metadata drafts.
- Use `aso-metadata-performance-analysis` after metadata changes go live to evaluate post-publish impact.
- Use `aso-localized-metadata-workflow` for localized metadata optimization tied to a specific country or region.
