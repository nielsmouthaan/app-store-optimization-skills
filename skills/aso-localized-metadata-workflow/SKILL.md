---
name: aso-localized-metadata-workflow
description: Runs the localized App Store optimization workflow for a chosen non-source language, locale, country or region, storefront, or Apple country or region ISO code. Use when a prompt names a target language, locale, country or region, translated keywords, localized search terms, or per-market app name, subtitle, and keywords. For primary/source metadata, use aso-metadata-workflow.
---

# ASO Localized Metadata Workflow

Use this skill as the primary entrypoint for App Store metadata optimization in an Apple-supported metadata locale, with a derived country or region when storefront-specific statistics or rankings are needed.

This workflow coordinates the specialist ASO skills with localization-specific guardrails. It uses source search terms as intent seeds, but localized terms must reflect how users in the target locale actually search.

If the user has not chosen a target locale, ask them to choose the language, locale, country or region, storefront, or Apple country or region ISO code before starting localized metadata work.

## Non-Negotiable Rules

- Use `.agents/aso/context.md` for global app context and source-locale search terms.
- Use `.agents/aso/locales/<Locale>/context.md` for localized metadata work.
- Do not duplicate the full source search-term backlog into localized workspaces.
- Use source terms as intent inspiration, not as strings to translate literally.
- Treat localized metadata as research-led, not translation-led. Localized terms must come from target-locale search behavior, native vocabulary, or clear local evidence.
- Store a concise, natural `Meaning` for each localized term so users who do not know the language can audit it.
- Record localized review provenance in `Notes` so `confirmed` terms do not imply user approval unless the user actually approved them.
- Label localized current metadata baseline when current localized metadata exists; do not treat staged, user-provided, user-reported current, or unknown metadata as live.
- Choose a platform/statistics scope before fetching localized statistics; do not silently reuse evidence from one platform for another.
- Fetch popularity and difficulty only for exact localized terms in the target App Store country or region.
- Derive the country or region from the explicit request, saved `Country or region preference`, or locale default in `references/app-store-localizations.md`. Store a preference only when the default is overridden.
- For multi-region localized work, let `aso-search-terms-statistics` choose one primary scoring country or region and keep any secondary-region validation separate.
- Derive any tool country or region parameter at tool-call time; do not store the derived tool parameter as workspace state.
- Count App Store keyword fields by characters, not bytes.
- Do not publish or update App Store Connect metadata unless the user explicitly asks for that action.

## Locale And Country Or Region Setup

Before creating a localized workspace, determine the Apple metadata `Locale`. Determine a country or region only when the user names one, source evidence requires one, or a storefront-specific step needs statistics or rankings.

Use `references/app-store-localizations.md` when suggesting or validating metadata locales, country or region preferences, and supported App Store localizations.

Suggestion order:

1. Explicit user-provided metadata locale, language, country or region, or Apple country or region ISO code.
2. Existing `.agents/aso/context.md` locale preferences or `## Locales` entries.
3. App Store Connect or local metadata files when available.
4. App Store URL country or region when available.
5. Target country or region or language mapped through the shared App Store localizations reference.

If the user names only a country or region, use Apple's default metadata locale for that country or region and mention additional supported locales when useful.

If the user names only a language or language group, choose the matching Apple metadata locale and derive its default country or region from `references/app-store-localizations.md`. If the user explicitly targets a different country or region for that locale, store `Country or region preference`.

Validate that the locale is supported by Apple before generating metadata. Before fetching statistics or rankings, resolve the country or region in this order: explicit user request for the run, saved `Country or region preference`, default country or region for the active locale from `references/app-store-localizations.md`, then ask the user if no safe default exists.

## Cross-Localization

Cross-localization is optional advanced work. Use an additional Apple-supported locale for a territory only when the shared localization reference confirms support and local search evidence justifies the extra workspace.

When source-language query coverage matters, use the fallback assumption from `references/app-store-localizations.md`: storefront default metadata locale, then storefront additional supported locale(s), then the app primary/default locale when storefront-specific metadata is missing. Save a compact strategy note only when it affects keyword duplication or omission decisions.

By default, avoid duplicating keyword terms across locale workspaces for the same territory. If a term is repeated because the user wants a specific phrase or local evidence supports it, mark the reason in `Notes`. Treat exact phrase-combination behavior across locales as `Unresolved`; do not promise that words in different locale fields combine for ranking.

Example: for Germany, German terms belong in the German workspace. English terms usually belong in English (U.K.) if that workspace exists, or may be covered by the app primary/default locale such as English (U.S.) if no Germany-specific English metadata exists. Put English roots in German hidden keywords only when the user asks or evidence shows those English roots need German-locale keyword budget.

## Workspace Schema

Create or update one localized workspace per Apple metadata locale. Keep the workflow schema minimal and let specialist skills own their detailed table formats:

```markdown
# ASO App Context (German)
*Last updated: YYYY-MM-DD*

## Source
**Locale:** German
**Country or region preference:**

## Metadata

### Current

**Baseline:** live
**Name:** Belege für Steuern *(18/30, receipts for taxes)*
**Subtitle:** Rechnungen scannen *(18/30, scan invoices)*
**Keywords (iOS):** belege,steuern,scanner *(23/100 chars, receipts, taxes, scanner)*

### History

#### YYYY-MM-DD - Draft - Generated - Recommended

Generated by `aso-metadata-generation`. Guidance: prefer natural German tax/receipt wording over literal source-language translation.

**Name:** Belege für Steuern *(18/30, receipts for taxes)*
**Subtitle:** Rechnungen scannen *(18/30, scan invoices)*
**Keywords (iOS):** belege,steuern,scanner *(23/100 chars, receipts, taxes, scanner)*

## Search Terms Backlog

Use the localized backlog schema from `aso-search-terms-identification`.

## Word Value Scores

Use the word-value schema from `aso-search-terms-scoring`.
```

Use the localized workspace path, heading, and `## Source` values as the locale identity, such as `.agents/aso/locales/German/context.md` with `# ASO App Context (German)` and `**Locale:** German`. Add `Country or region preference` only when the user or clear source evidence explicitly overrides the default country or region for that locale. Use the same `## Metadata` `### Current` and `### History` model as the source context, with localized field meanings inside `*(...)*` annotations when useful.

Also add or update the `## Locales` table in `.agents/aso/context.md`:

```markdown
| Locale | Workspace | Country or region preference | Notes |
| --- | --- | --- | --- |
| German | .agents/aso/locales/German/context.md |  | German metadata |
```

## Workflow Overview

Run phases in this order:

1. Establish or update global app context with `aso-context`.
2. Choose and validate target metadata locale and optional country or region preference.
3. Create or update the localized workspace.
4. Identify localized search terms and assign and validate localized relevance with `aso-search-terms-identification`.
5. Fetch target country or region statistics with `aso-search-terms-statistics`, including platform/statistics scope.
6. Calculate localized scores with `aso-search-terms-scoring`.
7. Generate localized metadata drafts with `aso-metadata-generation`.

After every phase, summarize the target locale, localized workspace path, resolved or preferred country or region when relevant, what changed, and the next required phase.

## Phase Guidance

### Phase 1: Establish Global Context

Read `.agents/aso/context.md` first.

The global context should contain source app facts, primary locale, platforms, source metadata under `## Metadata` `### Current`, saved source metadata history, source search terms, source relevance, and original App Store Connect keyword field terms by platform when available.

### Phase 2: Choose And Validate Target Metadata Locale

Use `references/app-store-localizations.md` to validate the Apple metadata `Locale`, such as `German`, `French`, or `Spanish (Mexico)`.

If the user names only a country or region, choose Apple's default metadata locale for that country or region and mention additional supported locales when useful. If the user names a language or language group, choose the matching Apple metadata locale.

Resolve a country or region only when the user names one, saved context has a `Country or region preference`, source evidence requires one, or the next storefront-specific step needs statistics or rankings. Store `Country or region preference` only when the user or clear source evidence overrides the default country or region for that locale.

If the target country or region has additional supported locales that affect source-language query coverage, record a compact fallback strategy note in the localized workspace or global `## Locales` row. Do not create extra locale workspaces unless the user wants that locale or evidence justifies it.

### Phase 3: Create Or Update The Localized Workspace

Verify that `.agents/aso/locales/<Locale>/context.md` exists before treating a locale as ready for localized work. If the workspace is missing, create it using `## Workspace Schema`.

If dedicated localized App Store metadata exists, store it under `## Metadata` `### Current` with a compact `**Baseline:**` label and meaning annotations when useful. Prefer live metadata unless the user explicitly targets staged or next-release metadata. If live and staged values differ, record the chosen baseline and the difference compactly.

If no dedicated localized metadata exists yet, store a clear current-baseline note such as:

```markdown
### Current

No dedicated English (U.K.) metadata exists. Source English (U.S.) metadata may provide fallback coverage.
```

Add or update the global `## Locales` row only after the workspace file exists, or mark planned locales as `planned; workspace not created` in `Notes`.

### Phase 4: Identify Localized Search Terms And Assign And Validate Relevance

Use `aso-search-terms-identification` and pass these localization constraints. Use local search behavior as the primary target-locale evidence:

- target-language App Store autocomplete or ASO tool suggestions
- localized competitor names, subtitles, descriptions, screenshot text, and reviews
- user-provided native phrasing or support/review language
- target-language category terms, feature language, and jobs-to-be-done language
- source search terms as intent seeds

Do not translate the source backlog mechanically. A localized term is useful only when a real App Store user in the target locale and resolved country or region might search it while expecting this app.

If the localized run is part of a cross-localization strategy, keep the workspace focused on that locale and record duplicate-avoidance or intentional-overlap decisions in `Notes`.

For every localized term, store `Meaning` as a concise, natural back-translation or explanation in a language the user understands.

Project relevance from source terms only when the localized term preserves the same App Store search intent. If the localized phrase has a different nuance, broader category, different user expectation, or uncertain idiom, score conservatively and add a compact note.

Agent-led review is the default. Do the best possible review on behalf of the user, because the user may not understand the target language. Decide each localized term without user approval whenever reasonable: save it as `confirmed` when it appears to make sense as a target-locale App Store search for this app, save it as `candidate` when it is plausible but still uncertain, or save it as `rejected` when it is clearly unsuitable.

Ask the user or request native-speaker review only when, after best-effort analysis, it remains genuinely unclear whether the term makes sense and that uncertainty would materially affect downstream statistics, scoring, or metadata placement. Use `Notes` to mark review provenance with one of `review: agent-led`, `review: user-approved`, `review: native-approved`, or `review: needs native review`. When user or native-speaker approval is needed, show each localized term together with its `Meaning` and the reason it needs review.

### Phase 5: Fetch Localized Statistics

Use `aso-search-terms-statistics` to choose and summarize the platform/statistics scope before fetching statistics. Carry that scope and any platform evidence reuse warnings into `aso-metadata-generation`.

Use the active locale's resolved country or region, not the source context's country or region, when fetching statistics. Resolve it from the explicit request, saved `Country or region preference`, or locale default in `references/app-store-localizations.md`. If the ASO tool requires a two-letter country or region parameter, derive it from the resolved country or region ISO code using `references/app-store-localizations.md` or a standard ISO 3166 lookup.

For locales that matter across multiple countries or regions, use the statistics skill to keep one primary scoring country or region and any secondary validation separate. Carry important secondary-region conflicts forward as notes; do not mix secondary values into primary scoring.

Fetch exact localized search terms. Do not translate terms during statistics fetching. Do not reuse popularity or difficulty values from another locale or country or region. User-provided Apple Ads Search Popularity on a `1`-`5` scale may be normalized for `Popularity`, but it must not be used as `Difficulty`.

If imported statistics were fetched for a different country or region than the resolved country or region, treat them as incompatible unless the user explicitly wants exploratory comparison data outside the localized workflow.

### Phase 6: Calculate Localized Scores

Use `aso-search-terms-scoring` to calculate localized strategic scores and word value scores inside the active localized workspace.

### Phase 7: Generate Localized Metadata

Generate app name, subtitle, and platform keyword sections for the target locale. Visible fields must read naturally for the target language. Each generated keyword section must fit this suite's 100-character App Store keyword limit. Use portfolio balance so localized drafts do not overfit to only broad head terms or only long-tail terms.

Use `aso-metadata-generation` for one recommended localized draft. It uses the same grouped draft structure as source-locale drafts. When saved, localized metadata uses compact field annotations for counts and meanings, such as `*(18/30, scan invoices)`.

For non-English locales, do not apply English plural, stemming, stop-word, or category-term assumptions unless target-language evidence supports the decision.

After localized metadata goes live, recommend checking keyword rankings periodically with `aso-search-terms-rankings`.

## Completion Report

End the workflow with:

- locale and resolved or preferred country or region when relevant
- localized workspace path
- platform/statistics scope and any platform evidence reuse warnings
- primary scoring country or region and any important secondary-region validation notes
- number of localized candidate, confirmed, rejected, and scored terms
- localized review provenance mix and any terms still needing native review
- statistics source and update date
- highest strategic localized terms and highest-value localized words
- metadata draft recommended or saved, including localized `Meaning` values or warnings when relevant
- field counts and coverage summary
- unresolved meaning, country or region, stale-statistics, character-limit, or follow-up warnings

If metadata was only saved as a draft, state that App Store Connect was not updated.

## Related Skills

- Use `aso-context` to create or update global app context.
- Use `aso-search-terms-identification` for localized search-term discovery and relevance assignment.
- Use `aso-search-terms-statistics` for target country or region popularity and difficulty.
- Use `aso-search-terms-scoring` for localized strategic and word value scores.
- Use `aso-metadata-generation` for localized metadata drafts.
