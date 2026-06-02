---
name: aso-localization-prioritization
description: Prioritizes App Store product page metadata localizations for organic search impact. Use when the user asks which countries, regions, languages, locales, or App Store Connect localizations to target first for app name, subtitle, and keywords based on App Store Connect, App Analytics, asc, or user-provided territory data. For generating localized metadata, use aso-localized-metadata-workflow.
---

# ASO Localization Prioritization

Act as an App Store metadata localization strategist. Help the user decide which App Store product page metadata localizations are most likely to improve organic search discoverability.

This skill only prioritizes localizations for searchable App Store metadata: **app name, subtitle, and keywords**. It does not plan app translation, screenshots, app previews, description copy, onboarding, support, pricing, or market launch work.

## Before Starting

Read `.agents/aso/context.md` first.

Use `../../references/app-store-localizations.md` to map territories, countries, regions, and languages to Apple-supported metadata localization pairs.

If `.agents/aso/context.md` is missing or lacks meaningful app context, invoke or recommend `aso-context` before continuing. Do not rank localizations without knowing what the app does.

If the user asks to generate metadata for a specific locale, use `aso-localized-metadata-workflow` instead. If the user asks which locale to do first or which locale has the highest potential impact, continue with this skill.

## Scope Rules

- Prioritize only App Store product page metadata localizations for app name, subtitle, and keywords.
- Do not recommend full app translation, screenshots, app previews, description localization, support localization, or broader go-to-market work.
- Do not create localized search-term backlogs, fetch keyword popularity or difficulty, score localized keywords, or generate localized metadata drafts.
- Do not treat a country as equivalent to a language. Map every recommendation to an Apple `ISO code`, country or region, and metadata `Language`.
- Do not store full localized keyword research in `.agents/aso/context.md`.
- Do not publish or update App Store Connect metadata.

## Data Inputs

Use whichever input route is available.

### User-Provided Data

If the user provides App Store Connect, App Analytics, or territory data, use it directly. Useful fields include:

- Territory or country/region
- Impressions
- Product page views
- Conversion rate
- First-time downloads
- Source type or search/source notes
- User-provided strategic notes

Ask only for missing data that materially changes the ranking. If the user cannot provide a metric, continue with the available data and mark the uncertainty.

### App Store Connect Data With asc

If `asc` is available and the user wants automatic data collection, use it to inspect or fetch App Store Connect and App Analytics data when possible. Use `asc-cli-usage` when available to understand current `asc` commands, flags, output formats, authentication, and pagination behavior.

If `asc` is unavailable, unauthenticated, lacks access, or analytics data is not ready, ask the user to provide App Store Connect or App Analytics territory data manually.

## Prioritization Criteria

Use qualitative priorities: `high`, `medium`, `low`, and `not enough data`.

Consider:

- **Existing demand:** impressions, product page views, first-time downloads, or other territory-level interest.
- **Metadata upside:** high impressions with weak product page views, or high product page views with weak conversion, may indicate product page metadata opportunity.
- **Search/source signal:** App Store Search or other discoverability-source evidence is stronger than unrelated traffic.
- **Strategic preference:** user-provided target markets, priority regions, or exclusions.
- **Localization fit:** whether Apple supports a clear metadata language for the target country or region.
- **Data uncertainty:** missing, stale, low-volume, thresholded, or ambiguous data lowers confidence.

Do not treat missing values as zero.

Use this guidance:

| Priority | Meaning |
| --- | --- |
| `high` | Strong territory evidence, clear metadata-localization pair, and plausible organic search upside. |
| `medium` | Some useful evidence or strategic fit, but one important signal is weak or missing. |
| `low` | Weak demand, weak business signal, unclear upside, or better locales are available. |
| `not enough data` | Too little trustworthy territory data to prioritize responsibly. |

## Workflow

### 1. Review Context

Summarize the app context that affects localization priority:

- app category, use case, and source metadata
- active source search language, region, and platform
- App Store URL and App Store Connect sources when available
- existing `## Locales` rows
- user-provided localization preferences or exclusions

Use the active `Platform` from `.agents/aso/context.md` for the full prioritization run. If the platform is missing and the available data clearly belongs to one platform, note that assumption and update context when saving. If the platform is ambiguous, ask the user before comparing territory data. Do not mix analytics or ASO data from different platforms in one prioritization result.

### 2. Collect Or Inspect Territory Data

Use user-provided data first when present. If the user wants automatic collection and `asc` is available, use `asc`, guided by `asc-cli-usage` when available.

If neither route provides enough information, ask for a compact territory table. Do not guess from population size, general market reputation, or language popularity alone.

### 3. Map Territories To Metadata Localizations

For each promising territory, use `../../references/app-store-localizations.md` to choose the Apple `ISO code`, country or region, and metadata `Language`.

If a country has additional supported languages, mention them only when data, user preference, or local strategy makes them relevant. Do not automatically recommend every supported language.

Examples:

- Spain defaults to `ESP` / `Spanish (Spain)`. Suggest `Catalan` only when evidence or user preference supports it.
- Mexico uses `MEX` / `Spanish (Mexico)`, not `Spanish (Spain)`.
- Brazil uses `BRA` / `Portuguese (Brazil)`, not `Portuguese (Portugal)`.
- China mainland uses `CHN` / `Simplified Chinese`.

### 4. Rank Recommendations

Create a compact ranked list. Explain the recommendation in plain language. Keep it focused on whether app name, subtitle, and keywords should be localized for that App Store country/language pair.

If multiple locales are close, prefer the one with clearer search/source evidence or lower data uncertainty.

### 5. Save Results

Save only a compact prioritization artifact at `.agents/aso/localization-prioritization.md`:

```markdown
# ASO Localization Prioritization
*Last updated: YYYY-MM-DD*

## Recommended Localizations
| Rank | ISO code | Country or region | Language | Priority | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | DEU | Germany | German | high | strong impressions and weak conversion; keyword data missing |

## Territory Signals
| Territory | Impressions | Product page views | Conversion rate | First-time downloads | Source/search notes | Notes |
| --- | ---: | ---: | ---: | ---: | --- | --- |
```

Also add or update compact rows in `.agents/aso/context.md` `## Locales` for recommended localizations:

```markdown
| ISO code | Country or region | Language | Workspace | Notes |
| --- | --- | --- | --- | --- |
| DEU | Germany | German | .agents/aso/locales/DEU/german.md | recommended by aso-localization-prioritization; priority: high |
```

When updating `## Locales`:

- Preserve existing notes unless they conflict with newer evidence.
- Do not create locale workspace files. `aso-localized-metadata-workflow` creates them after the user chooses a locale.
- Update `*Last updated:*` in changed files.

## Completion Report

End with:

- recommended localizations in priority order
- important data gaps or uncertainty
- saved artifact path
- `## Locales` rows added or updated
- next step: run `aso-localized-metadata-workflow` for a chosen locale

## Common Mistakes

- Ranking locales for full app translation instead of App Store metadata localization.
- Recommending screenshots, previews, descriptions, onboarding, or support work from this skill.
- Treating missing data as zero.
- Choosing locales only from market size or language popularity.
- Treating one language as one market.
- Recommending every additional supported language in a country by default.
- Generating localized metadata before the user chooses a target locale.

## Related Skills

- Use `aso-context` to create or update shared app context before ranking.
- Use `asc-cli-usage` to understand `asc` when fetching App Store Connect or App Analytics data.
- Use `aso-localized-metadata-workflow` after the user chooses a recommended locale.
