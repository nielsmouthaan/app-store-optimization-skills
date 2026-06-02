---
name: aso-localized-metadata-workflow
description: Runs the localized App Store optimization workflow for a chosen non-source language, country, region, storefront, or Apple ISO code. Use when a prompt names a target language, locale, country, region, translated keywords, localized search terms, or per-market app name, subtitle, and keywords. For deciding which localization to prioritize first, use aso-localization-prioritization. For primary/source metadata, use aso-metadata-workflow.
---

# ASO Localized Metadata Workflow

Use this skill as the primary entrypoint for App Store metadata optimization in an Apple-supported country or region and metadata language.

This workflow coordinates the specialist ASO skills with localization-specific guardrails. It uses source search terms as intent seeds, but localized terms must reflect how users in the target locale actually search.

If the user asks which country, region, language, or locale would have the highest organic search impact and has not chosen a target locale, use `aso-localization-prioritization` first. Return to this workflow after the user chooses a recommended locale.

## Non-Negotiable Rules

- Use `.agents/aso/context.md` for global app context and source-locale search terms.
- Use `.agents/aso/locales/<ISO code>/<language-slug>.md` for target-market language work.
- Do not duplicate the full source search-term backlog into localized workspaces.
- Use source terms as intent inspiration, not as strings to translate literally.
- Store a concise `Meaning` for each localized term so users who do not know the language can audit it.
- Fetch popularity and difficulty only for exact localized terms in the target App Store country or region.
- Derive any ASO tool region parameter from the workspace `ISO code` at tool-call time; do not store a separate stats region in the localized workspace.
- Count App Store keyword fields by UTF-8 bytes, not characters.
- Do not publish or update App Store Connect metadata unless the user explicitly asks for that action.

## Country And Language Setup

Before creating a localized workspace, determine the Apple `ISO code`, `Country or region`, and metadata `Language`.

Use `../../references/app-store-localizations.md` when suggesting or validating countries, regions, and supported metadata languages.

Suggestion order:

1. Explicit user-provided Apple ISO code, country/region, or metadata language.
2. Existing `.agents/aso/context.md` locale preferences or `## Locales` entries.
3. App Store Connect or local metadata files when available.
4. App Store URL country or region when available.
5. Target country/region or language mapped through the shared App Store localizations reference.

If the user names only a country or region, use Apple's default language for that ISO code and mention additional supported languages when useful.

If the user names only a language or language group, suggest separate workspaces for each relevant Apple ISO code instead of collapsing regions together. For example, German-speaking ASO should use separate workspaces for Germany, Austria, Switzerland, and Luxembourg when those markets are in scope.

Validate that the ISO code and language pair is supported by Apple before fetching statistics or generating metadata. If validation cannot be performed from available references and the pair is not obvious, ask the user to confirm the intended App Store country or region.

## Workspace Schema

Create or update one localized workspace per Apple ISO code and language:

```markdown
# ASO Locale Context: DEU (German)
*Last updated: YYYY-MM-DD*

**ISO code:** DEU
**Country or region:** Germany
**Language:** German

## Search Terms Backlog
| Search term | Meaning | Status | Relevance | Popularity | Difficulty | Stats source | Stats updated | Notes | Strategic score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| quittung scanner | receipt scanner | candidate |  |  |  |  |  | inspired by source intent: receipt scanner |  |

## Word Value Scores
| Word | Appearances | Total strategic score | Length | Value |
| --- | --- | --- | --- | --- |
```

Use only `ISO code`, `Country or region`, and `Language` as workspace header fields. Put uncertainty, original-intent references, local evidence, unresolved ASO tool-region derivation issues, and manual-review notes in `Notes`.

Also add or update the `## Locales` table in `.agents/aso/context.md`:

```markdown
| ISO code | Country or region | Language | Workspace | Notes |
| --- | --- | --- | --- | --- |
| DEU | Germany | German | .agents/aso/locales/DEU/german.md | German metadata |
```

## Workflow Overview

Run phases in this order:

1. Establish or update global app context with `aso-context`.
2. Choose and validate target `ISO code`, country or region, and language.
3. Create or update the localized workspace.
4. Identify localized search terms with `aso-search-terms-identification`.
5. Assign localized relevance with `aso-search-terms-relevance-scoring`.
6. Fetch target-region statistics with `aso-search-terms-statistics`.
7. Calculate localized scores with `aso-search-terms-scoring`.
8. Generate localized metadata drafts with `aso-metadata-generation`.

After every phase, summarize the target ISO code, country or region, language, localized workspace path, what changed, and the next required phase.

## Phase Guidance

### 1. Establish Global Context

Read `.agents/aso/context.md` first. If only legacy `.agents/aso-context.md` exists, use `aso-context` to migrate the next saved context to `.agents/aso/context.md`.

The global context should contain source app facts, source metadata, source search terms, source relevance, and original App Store Connect keyword field terms when available.

### 2. Identify Localized Search Terms

Use local search behavior as the primary target-locale evidence:

- target-language App Store autocomplete or ASO tool suggestions
- localized competitor names, subtitles, descriptions, screenshot text, and reviews
- user-provided native phrasing or support/review language
- target-language category terms, feature language, and jobs-to-be-done language
- source search terms as intent seeds

Do not translate the source backlog mechanically. A localized term is useful only when a real App Store user in the target region might search it while expecting this app.

For every localized term, store `Meaning` as a concise back-translation or explanation in a language the user understands.

### 3. Score Localized Relevance

Assign the same `1`-`5` relevance scale used by `aso-search-terms-relevance-scoring`.

Project relevance from source terms only when the localized term preserves the same App Store search intent. If the localized phrase has a different nuance, broader category, different user expectation, or uncertain idiom, score conservatively and add a compact note.

Agent-led review is the default. Ask the user only when ambiguity could materially change relevance, metadata placement, or whether a term should remain confirmed.

### 4. Fetch Localized Statistics

Use the localized workspace `ISO code`, not the source-region context, when fetching statistics. If the ASO tool requires a two-letter region parameter, derive it from the ISO code using `../../references/app-store-localizations.md` or a standard ISO 3166 lookup.

Fetch exact localized search terms. Do not translate terms during statistics fetching. Do not reuse popularity or difficulty values from another locale, language, or region.

If imported statistics were fetched for a different country or region than the workspace ISO code, treat them as incompatible unless the user explicitly wants exploratory comparison data outside the localized workflow.

### 5. Score And Generate Metadata

Use the existing strategic-score formula per localized workspace.

Generate app name, subtitle, and keywords for the target locale. Visible fields must read naturally for the target language. Keywords must fit the 100-byte App Store keyword limit.

Use `aso-metadata-generation` for localized drafts. It uses the same grouped variant structure as source-locale drafts, but the metadata table renames `Value` to `Localized value` and adds `Meaning` next to it.

For non-English locales, do not apply English plural, stemming, stop-word, or category-term assumptions unless target-language evidence supports the decision.

## Completion Report

End the workflow with:

- ISO code, country or region, and language
- localized workspace path
- number of localized candidate, confirmed, rejected, and scored terms
- statistics source and update date
- highest strategic localized terms and highest-value localized words
- metadata variant recommended or saved, including localized `Meaning` values or warnings when relevant
- field counts and coverage summary
- unresolved meaning, region, stale-statistics, byte-limit, or follow-up warnings

If metadata was only saved as a draft, state that App Store Connect was not updated.

## Related Skills

- Use `aso-context` to create or update global app context.
- Use `aso-localization-prioritization` to choose which metadata localization to target before this workflow.
- Use `aso-search-terms-identification` for localized search-term discovery.
- Use `aso-search-terms-relevance-scoring` for localized relevance.
- Use `aso-search-terms-statistics` for target-region popularity and difficulty.
- Use `aso-search-terms-scoring` for localized strategic and word value scores.
- Use `aso-metadata-generation` for localized metadata drafts.
