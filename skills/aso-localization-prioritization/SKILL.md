---
name: aso-localization-prioritization
description: Prioritizes App Store product page metadata localizations for app name, subtitle, and keywords using territory funnel, monetization, retention, ratings, search opportunity, and evidence-quality signals. Use when the user asks which countries, regions, languages, locales, or App Store Connect localizations to target first. For generating localized metadata, use aso-localized-metadata-workflow.
---

# ASO Localization Prioritization

Act as an App Store metadata localization strategist. Help the user decide which Apple metadata locale should be prioritized first for App Store product page metadata.

This skill only prioritizes localizations for searchable App Store metadata: **app name, subtitle, and keywords**. It does not plan app translation, screenshots, app previews, description copy, onboarding, support, pricing, or market launch work.

Use broader business signals only to improve the metadata prioritization decision. Screenshots, pricing, support, legal, and in-app localization may be mentioned as risk or follow-up signals, but they are not this skill's output scope.

## Before Starting

Read `.agents/aso/context.md` first.

Use `../../references/app-store-localizations.md` to map territories, countries or regions, and languages to Apple-supported metadata locales and optional country or region preferences.

If `.agents/aso/context.md` is missing or lacks meaningful app context, invoke or recommend `aso-context` before continuing. Do not rank localizations without knowing what the app does.

If the user asks to generate metadata for a specific locale, use `aso-localized-metadata-workflow` instead. If the user asks which locale to do first or which locale has the highest potential impact, continue with this skill.

## Scope Rules

- Prioritize only App Store product page metadata localizations for app name, subtitle, and keywords.
- Do not recommend full app translation, screenshots, app previews, description localization, support localization, pricing changes, legal work, or broader go-to-market work as outputs from this skill.
- Use non-metadata signals only to explain priority, confidence, risk, or whether metadata localization is unlikely to solve the real problem.
- Do not create localized search-term backlogs, fetch keyword popularity or difficulty, score localized keywords, or generate localized metadata drafts.
- Do not treat a country or region as equivalent to a locale. Map every recommendation to an Apple metadata `Locale` and add `Country or region preference` only when the recommendation targets a non-default country or region for that locale.
- Do not store full localized keyword research in `.agents/aso/context.md`.
- Do not publish or update App Store Connect metadata.

## Data Inputs

Use whichever input route is available.

### User-Provided Data

If the user provides App Store Connect, App Analytics, or territory data, use it directly. Useful fields include:

- Territory or country or region
- Reporting window, ideally 90 or 180 days
- Impressions
- Product page views
- Conversion rate
- First-time downloads
- Source type, product page, campaign, or search/source notes
- Proceeds, paying users, proceeds per download, or other monetization signal
- Day 7 or Day 28 retention, deletions, crash rate, ratings, or review themes
- Search popularity, keyword difficulty, or competitor localization notes
- Market-size, iOS-share, or strategic-market notes
- Estimated localization cost or expected lift assumptions
- User-provided strategic notes

Ask only for missing data that materially changes the ranking. If the user cannot provide a metric, continue with the available data and mark the uncertainty.

### App Store Connect Data With asc

If `asc` is available and the user wants automatic data collection, use it to inspect or fetch App Store Connect and App Analytics data when possible. Use `asc-cli-usage` when available to understand current `asc` commands, flags, output formats, authentication, and pagination behavior.

If `asc` is unavailable, unauthenticated, lacks access, or analytics data is not ready, ask the user to provide App Store Connect or App Analytics territory data manually.

## Prioritization Lenses

Use qualitative priorities: `high`, `medium`, `low`, and `not enough data`. Also assign confidence as `high`, `medium`, or `low`.

Do not use fixed percentage weights by default. Prioritize with these lenses in order, using the simplest explanation that supports the recommendation.

1. **Existing untranslated demand with weak listing conversion.** Prefer locales where users already discover or view the app without localized metadata, but listing conversion is weak. Example: Germany has many product page views but a lower page-to-download rate than the app median, suggesting German metadata may improve conversion.
2. **Monetization quality and retention upside.** Move locales up when users in the territory pay, retain, and rate the app well. Move them down or add a risk flag when downloads are strong but retention, ratings, deletions, or crash performance suggest the product experience is the bottleneck. Example: Japan has lower traffic than Germany but stronger proceeds per download and Day 28 retention, so it can be the better first locale.
3. **Search demand and ranking feasibility.** Favor locales with relevant local-language search demand and realistic ranking difficulty. Example: Dutch terms such as category or feature phrases have useful popularity and manageable difficulty, while another market's terms are dominated by large competitors.
4. **Strategic market attractiveness.** Use external or user-provided strategy to break ties or justify cautious tests when internal data is sparse. Example: French (Canada) may matter because Canada is a strategic market and the app already has English Canada traction.
5. **Operational risk and evidence quality.** Lower confidence when data is sparse, stale, thresholded, mixed across platforms, or when legal, support, pricing, or in-app language risks make metadata-only localization less likely to succeed. Example: a large market with compliance complexity or only 60 product page views should not receive a confident high priority.

Do not treat missing values as zero.

When enough monetization data and explicit assumptions are available, optionally estimate ROI:

```text
Base page-to-download rate = First-time downloads / Product page views
New page-to-download rate = Base rate * (1 + expected conversion lift)
Additional product page views = Product page views * expected visibility lift
Incremental downloads = Product page views * (New rate - Base rate) + Additional product page views * New rate
New proceeds per download = Current proceeds per download * (1 + expected monetization lift)
Incremental proceeds for reporting window = Incremental downloads * New proceeds per download
Annual incremental proceeds = Incremental proceeds for reporting window * (365 / reporting window days)
Payback months = Estimated localization cost / (Annual incremental proceeds / 12)
```

Skip ROI when inputs are missing or assumptions would be invented. Use plain-language priority and confidence instead.

Use this guidance:

| Priority | Meaning |
| --- | --- |
| `high` | Strong evidence of metadata upside, clear Apple metadata locale, and no major risk that metadata is the wrong fix. |
| `medium` | Useful evidence or strategic fit, but one important signal is weak, missing, or risky. |
| `low` | Weak demand, weak business signal, unclear metadata upside, high risk, or better locales are available. |
| `not enough data` | Too little trustworthy data to prioritize responsibly. |

## Workflow

### 1. Review Context

Summarize the app context that affects localization priority:

- app category, use case, and source metadata
- source primary locale and platforms
- App Store URL and App Store Connect sources when available
- existing `## Locales` rows
- user-provided localization preferences or exclusions

Use `Platforms` from `.agents/aso/context.md` to understand which App Store Connect metadata platforms are in scope. If analytics or ASO data is platform-specific, do not mix data from different platforms in one prioritization result unless the user explicitly asks for a combined view and the limitation is noted.

### 2. Collect Or Inspect Territory Data

Use user-provided data first when present. If the user wants automatic collection and `asc` is available, use `asc`, guided by `asc-cli-usage` when available.

If neither route provides enough information, ask for a compact territory table. Do not guess from population size, general market reputation, or language popularity alone.

### 3. Map Territories To Metadata Localizations

For each promising territory, use `../../references/app-store-localizations.md` to choose the Apple metadata `Locale`.

When multiple territories point to the same metadata locale, summarize them together as affected storefronts in the recommendation. This is prioritization evidence only; downstream localized metadata work still uses one Apple metadata locale workspace.

If the territory's country or region differs from the locale's default country or region, set `Country or region preference` to the Apple country or region ISO code. If the territory matches the locale default, leave the preference blank.

If a recommendation is based on a group of storefronts that share a locale, leave `Country or region preference` blank unless the user explicitly targets one non-default country or region.

If a country or region has additional supported locales, mention them only when data, user preference, or local strategy makes them relevant. Do not automatically recommend every supported locale.

Examples:

- Spain defaults to `Spanish (Spain)`. Suggest `Catalan` only when evidence or user preference supports it.
- Mexico and many Latin American storefronts use `Spanish (Mexico)`, not `Spanish (Spain)`.
- Brazil uses `Portuguese (Brazil)`, not `Portuguese (Portugal)`.
- China mainland uses `Chinese (Simplified)`.
- US Spanish uses `Spanish (Mexico)` with `Country or region preference: USA`.
- `Spanish (Mexico)` and `Spanish (Spain)` are separate recommendations because their storefront coverage and vocabulary differ.

### 4. Rank Recommendations

Create a compact ranked list. Explain the recommendation in plain language. Keep it focused on whether app name, subtitle, and keywords should be localized for that Apple metadata locale and country or region when relevant.

If multiple locales are close, prefer the one with clearer search/source evidence or lower data uncertainty.

If conversion is acceptable but retention, ratings, deletions, crash rate, pricing, support, legal, or in-app language signals are weak, do not frame the locale as a clean metadata win. Rank it lower or add a risk flag that metadata may not be the main bottleneck.

### 5. Save Results

Save only a compact prioritization artifact at `.agents/aso/localization-prioritization.md`:

```markdown
# ASO Localization Prioritization
*Last updated: YYYY-MM-DD*

## Recommended Localizations
| Rank | Locale | Affected storefronts | Country or region preference | Priority | Confidence | Key evidence | Risk flags | Optional ROI/payback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | German | DEU |  | high | medium | strong Germany page views and weak listing conversion | keyword data missing | not calculated |

## Territory Signals
| Territory | Locale mapped | Impressions | Product page views | Conversion rate | First-time downloads | Proceeds/download | Retention/rating signal | Search/source notes | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
```

Also add or update compact rows in `.agents/aso/context.md` `## Locales` for recommended localizations:

```markdown
| Locale | Workspace | Country or region preference | Notes |
| --- | --- | --- | --- |
| German | .agents/aso/locales/German/context.md |  | recommended by aso-localization-prioritization; priority: high; confidence: medium |
```

When updating `## Locales`:

- Preserve existing notes unless they conflict with newer evidence.
- Do not create locale workspace files. `aso-localized-metadata-workflow` creates them after the user chooses a locale.
- Update `*Last updated:*` in changed files.

## Completion Report

End with:

- recommended localizations in priority order
- confidence, important data gaps, and risk flags
- saved artifact path
- `## Locales` rows added or updated
- next step: run `aso-localized-metadata-workflow` for a chosen locale

## Common Mistakes

- Ranking locales for full app translation instead of App Store metadata localization.
- Recommending screenshots, previews, descriptions, onboarding, pricing, legal, or support work as this skill's output instead of treating them as risk or follow-up signals.
- Treating missing data as zero.
- Choosing locales only from market size or language popularity.
- Treating one language as one market.
- Treating one country or region as one locale.
- Treating aggregated affected storefronts as a downstream workspace identity.
- Recommending every additional supported locale in a country or region by default.
- Producing precise ROI or scoring when assumptions would be invented.
- Generating localized metadata before the user chooses a target locale.

## Related Skills

- Use `aso-context` to create or update shared app context before ranking.
- Use `asc-cli-usage` to understand `asc` when fetching App Store Connect or App Analytics data.
- Use `aso-localized-metadata-workflow` after the user chooses a recommended locale.
