---
name: aso-metadata-workflow
description: Runs the end-to-end App Store optimization workflow for the app's primary or source metadata language. Use for full primary listing optimization, organic search metadata work, or coordinating context, search-term identification, relevance assignment and validation, statistics, strategic scoring, and metadata drafts. For other languages, countries or regions, use aso-localized-metadata-workflow.
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
- Do not publish, update, or otherwise write to App Store Connect through the [Helm CLI](https://nielsmouthaan.nl/helm) (`helm-asc`), `asc`, the App Store Connect API, or another tool unless the user explicitly reviews and approves that action.

## Workflow Overview

Run phases in this order:

1. Establish app context with `aso-context`.
2. Identify search terms and assign and validate relevance with `aso-search-terms-identification`.
3. Fetch statistics with `aso-search-terms-statistics`.
4. Calculate search term scores with `aso-search-terms-scoring`.
5. Generate metadata drafts with `aso-metadata-generation`.

After every phase, summarize:

- the phase completed
- what changed in `.agents/aso/context.md`
- blockers or source gaps
- the next required review or phase

At each user review gate, briefly explain why the review matters, what to check, examples of useful corrections, and what will be saved or used after approval.

## Phase 0: Establish Context

Use `aso-context` when `.agents/aso/context.md` is missing, stale, incomplete, or contradicted by new source material.

The context must identify, when available:

- primary locale and optional country or region preference
- App Store Connect platforms
- App Store URL
- marketing URL
- App Store Connect keyword field terms by platform
- app metadata under `## Metadata` `### Current`, compact saved metadata `### History`, primary category, secondary category, use cases, features, reviews, and competitors

Private App Store Connect metadata collection and source-gap handling belong to `aso-context`; follow that skill instead of duplicating retrieval steps here.

Stop after drafting or updating the context. Ask the user to confirm what is incorrect, missing, or misleading before treating the context as ready for search-term work. If no approved context exists yet, keep the draft in the response until approval.

## Phase 1: Identify Search Terms And Assign And Validate Relevance

Use `aso-search-terms-identification` to create or expand the search-term backlog and assign user-reviewed `1`-`5` relevance scores.

Before proceeding, confirm that the backlog is broad enough for later scoring, includes plausible App Store search phrases, source notes, useful variants, and approved relevance groups.

Stop after presenting proposed terms grouped by relevance. Let the user accept, reject, correct, add terms, or move terms between relevance groups before saving. Save accepted terms as `confirmed` with approved `Relevance`, rejected terms as `rejected` without relevance, and explicitly undecided suggestions or imports as `candidate` without relevance. Preserve rejected terms so future runs do not suggest them again.

After approved terms and relevance scores are saved, continue only with confirmed terms.

## Phase 2: Fetch Statistics

Use `aso-search-terms-statistics` to fetch popularity and difficulty for confirmed terms. User-provided Apple Ads Search Popularity on a `1`-`5` scale may be normalized for `Popularity`, but it must not be used as `Difficulty`.

Use the primary locale from context, or let the statistics skill derive or ask for it according to its locale-selection rules.

When all requested statistics are fetched, validated, and fresh enough for the run, continue to search term scoring without a user review gate. If any requested statistic is missing, pending, stale, incompatible, or unusable after the fetch attempt, require a user decision before continuing.

Stop and require user intervention if:

- no statistics source is available
- credentials are missing
- usage limits are reached
- the primary locale is unresolved
- the statistics tool cannot be accessed

Do not estimate or infer missing popularity or difficulty values beyond the statistics skill's explicit Apple Ads Search Popularity normalization. Report the blocker and the missing upstream requirement.

## Phase 3: Calculate Search Term Scores

Use `aso-search-terms-scoring` after confirmed terms have valid relevance, popularity, and difficulty values.

This phase is deterministic. It may save derived strategic scores and word value scores once prerequisites are satisfied, but it must not change relevance, statistics, statuses, notes, or metadata placement.

If no confirmed terms are eligible, stop and report which upstream input is missing.

## Phase 4: Generate Recommended Metadata Draft

Use `aso-metadata-generation` after strategic scores and word value scores exist.

Generate one recommended metadata draft and coverage analysis for the active source locale. Stop after presenting grouped draft sections, recommendation rationale, portfolio tradeoffs, warnings, and coverage tradeoffs.

Save a draft, update current context metadata, or publish to App Store Connect only when the user explicitly approves the relevant save or publish action. Saved drafts, user-edited drafts, current approvals, and published snapshots are recorded under `## Metadata` `### History`; only explicit current approvals or successful publishes update `## Metadata` `### Current`.

After metadata goes live, recommend checking keyword rankings periodically with `aso-search-terms-rankings`.

## Review Gates

Use these gates to decide whether the workflow can continue:

| Gate | Required user or tool confirmation | Next phase |
| --- | --- | --- |
| Context approved | User confirms app context and source gaps are acceptable | Search-term identification plus relevance assignment and validation |
| Search terms and relevance approved | User accepts, rejects, corrects, adds, or moves proposed terms between relevance groups; accepted terms are saved as `confirmed` with `Relevance` | Statistics fetching |
| Statistics available | External source provides complete validated popularity and difficulty for the target country or region, with Apple Ads normalization allowed for popularity only; incomplete statistics require a user decision before continuing | Search term scoring |
| Search term scores saved | Eligible confirmed terms have derived strategic scores and word value scores are saved in context | Metadata generation |
| Metadata choice approved | User approves a draft history save, current metadata update, or publish action | Save to `## Metadata` `### History`, and update `### Current` only for current approvals or successful publishes |

## Completion Report

End the workflow with a compact report:

- primary locale and platforms
- number of backlog terms, confirmed terms, rejected terms, and scored terms
- statistics source and update date
- highest strategic terms and highest-value words
- metadata draft recommended or saved, including whether a history entry was appended or current metadata was updated
- field counts and coverage summary
- unresolved source gaps, warnings, or follow-up tests

If metadata was only saved as a draft, state that App Store Connect was not updated.

## Related Skills

- Use `aso-context` to create or update shared app context.
- Use `aso-search-terms-identification` to create or expand the search-term backlog and assign user-reviewed relevance scores.
- Use `aso-search-terms-statistics` to fetch popularity and difficulty.
- Use `aso-search-terms-scoring` to calculate derived strategic scores and per-word value scores.
- Use `aso-metadata-generation` to generate a recommended metadata draft and save approved drafts, edits, current choices, or published snapshots.
- Use `aso-localized-metadata-workflow` for localized metadata optimization tied to a specific country or region.
