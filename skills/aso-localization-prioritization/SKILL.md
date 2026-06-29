---
name: aso-localization-prioritization
description: Prioritizes App Store product page metadata localization opportunities for app name, subtitle, and keywords, including new localizations and refreshes of existing localized metadata, using territory funnel, monetization, retention, ratings, search opportunity, and evidence-quality signals. Use when the user asks which countries, regions, languages, locales, existing App Store Connect localizations, or metadata refreshes to create or refresh first. For generating localized metadata, use aso-localized-metadata-workflow.
---

# ASO Localization Prioritization

Act as an App Store metadata localization strategist. Help the user decide which Apple metadata locale should be created or refreshed first for App Store product page metadata.

This skill only prioritizes localization opportunities for searchable App Store metadata: **app name, subtitle, and keywords**. It covers both new metadata localizations and updates to already localized metadata. It does not plan app translation, screenshots, app previews, description copy, onboarding, support, pricing, or market launch work.

Use broader business signals only to improve the metadata prioritization decision. Screenshots, pricing, support, legal, and in-app localization may be mentioned as risk or follow-up signals, but they are not this skill's output scope.

## Before Starting

Read `.agents/aso/context.md` first.

Use `references/app-store-localizations.md` to map territories, countries or regions, and languages to Apple-supported metadata locales and optional country or region preferences.

If `.agents/aso/context.md` is missing or lacks meaningful app context, invoke or recommend `aso-context` before continuing. Do not rank localizations without knowing what the app does.

If the user asks to generate or update metadata for a specific locale, use `aso-localized-metadata-workflow` instead. If the user asks which locale to create, refresh, do first, or which locale has the highest potential impact, continue with this skill.

## Scope Rules

- Prioritize only App Store product page metadata localization opportunities for app name, subtitle, and keywords.
- Do not recommend full app translation, screenshots, app previews, description localization, support localization, pricing changes, legal work, or broader go-to-market work as outputs from this skill.
- Use non-metadata signals only to explain priority, confidence, risk, or whether metadata localization is unlikely to solve the real problem.
- Do not create localized search-term backlogs, fetch keyword popularity or difficulty, score localized keywords, or generate localized metadata drafts.
- Do not treat a country or region as equivalent to a locale. Map every recommendation to an Apple metadata `Locale` and add `Country or region preference` only when the recommendation targets a non-default country or region for that locale.
- Do not store full localized keyword research in `.agents/aso/context.md`.
- Do not publish or update App Store Connect metadata.

## Data Inputs

Use whichever input route is available.

### User-Provided Data

If the user provides App Store Connect, App Analytics, Sales, ratings, reviews, or territory data, use it directly. Useful fields include:

- Territory or country or region
- Reporting window, ideally 90 or 180 days
- Existing App Store Connect localization status
- Current localized app name, subtitle, and keyword fields by platform
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

### App Store Connect Data With Tools

If the user wants automatic data collection, use available App Store Connect-capable tools in a read-only way to inspect or fetch App Store Connect, App Analytics, Sales, ratings, and review data when possible. Useful options can include `asc`, the Helm CLI (`helm-asc`), the App Store Connect API, or user-provided tooling. Use relevant tool-specific skills such as `asc-cli-usage` or `helm-asc` when available, or use CLI help and command discovery to understand current commands, flags, output formats, authentication, and pagination behavior.

When available, use App Store Connect-capable tools or user-provided App Store Connect exports to inspect existing metadata localizations and current localized app name, subtitle, and keyword fields by platform. Treat this as read-only evidence for whether the opportunity is a new localization or an existing-localization refresh.

If tooling is unavailable, unauthenticated, lacks access, or analytics data is not ready, ask the user to provide App Store Connect or App Analytics territory data manually.

## Opportunity Types

Assign one opportunity type to every recommendation:

| Opportunity type | Meaning |
| --- | --- |
| `new-localization` | The Apple metadata locale is missing, defaulted, untranslated, or not meaningfully localized. |
| `refresh-existing` | The Apple metadata locale already exists, but performance or metadata evidence suggests app name, subtitle, or keywords may be under-optimized. |
| `monitor` | Data is too sparse, mixed, or inconclusive to justify new metadata work or a refresh now. |

## Prioritization Lenses

Use qualitative priorities: `high`, `medium`, `low`, and `not enough data`. Also assign confidence as `high`, `medium`, or `low`.

Do not use fixed percentage weights by default. Prioritize with these lenses in order, using the simplest explanation that supports the recommendation.

1. **New-localization demand with weak listing conversion.** Prefer locales where users already discover or view the app through fallback-language metadata, but listing conversion is weak. Example: Brazil has many product page views, weak page-to-download rate, and no Portuguese (Brazil) metadata, suggesting new localized metadata may improve visibility or conversion.
2. **Existing-localization refresh opportunity.** Prefer already localized locales where conversion, search-source performance, rankings, page engagement, or revenue efficiency underperform the app median, source locale, peer benchmark, or comparable territories. Strengthen the case when current metadata has quality flags such as untranslated or defaulted fields, a generic subtitle, empty or weak keyword fields, source-language keyword reuse, stale terms, or poor local vocabulary fit.
3. **Monetization quality and retention upside.** Move locales up when users in the territory pay, retain, and rate the app well. Move them down or add a risk flag when downloads are strong but retention, ratings, deletions, or crash performance suggest the product experience is the bottleneck. Example: Japan has lower traffic than Germany but stronger proceeds per download and Day 28 retention, so it can be the better first locale.
4. **Search demand and ranking feasibility.** Favor locales with relevant local-language search demand and realistic ranking difficulty. Example: Dutch terms such as category or feature phrases have useful popularity and manageable difficulty, while another market's terms are dominated by large competitors.
5. **Strategic market attractiveness.** Use external or user-provided strategy to break ties or justify cautious tests when internal data is sparse. Example: French (Canada) may matter because Canada is a strategic market and the app already has English Canada traction.
6. **Operational risk and evidence quality.** Lower confidence when data is sparse, stale, thresholded, mixed across platforms, or when legal, support, pricing, or in-app language risks make metadata-only localization less likely to succeed. Example: a large market with compliance complexity or only 60 product page views should not receive a confident high priority.

Do not treat missing values as zero.

### Optional Diagnostic Score

Use a diagnostic score only when enough comparable data exists. The score is decision support, not a replacement for priority and confidence. Always show the factor evidence when using a score, and skip scoring when inputs are sparse, stale, or not comparable. When scoring, assign rough `0`-`100` evidence scores to each factor.

```text
Diagnostic score =
  demand and funnel volume * 0.25
+ metadata underperformance gap * 0.25
+ monetization quality * 0.20
+ retention and quality guardrails * 0.15
+ search and keyword opportunity * 0.10
+ strategic and operational fit * 0.05
```

Use the score to explain tradeoffs, not to overrule risk flags. A locale with a good score but weak retention, ratings, deletions, crashes, support, legal, pricing, or in-app language signals should be ranked lower or marked as risky because metadata may not be the main bottleneck.

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

- primary category, secondary category, use case, and source metadata
- source primary locale and platforms
- App Store URL and App Store Connect sources when available
- existing `## Locales` rows
- existing locale workspace summaries when available
- known current localized metadata fields when available
- user-provided localization preferences or exclusions

Use `Platforms` from `.agents/aso/context.md` to understand which App Store Connect metadata platforms are in scope. If analytics or ASO data is platform-specific, do not mix data from different platforms in one prioritization result unless the user explicitly asks for a combined view and the limitation is noted.

### 2. Collect Or Inspect Localization And Territory Data

Use user-provided data first when present. If the user wants automatic collection and App Store Connect-capable tooling is available, use it in a read-only way, guided by relevant tool-specific skills such as `asc-cli-usage` or `helm-asc` when available.

Collect or inspect:

- existing App Store Connect metadata localizations
- current app name, subtitle, and keyword fields by localized platform
- territory funnel, monetization, retention, ratings, review, and quality data
- source type, search, ranking, competitor, or benchmark notes when available
- existing `.agents/aso/context.md` `## Locales` rows and localized workspace notes

If neither route provides enough information, ask for a compact localization and territory table. Do not guess from population size, general market reputation, or language popularity alone.

### 3. Map Territories To Metadata Localizations

For each promising territory, use `references/app-store-localizations.md` to choose the Apple metadata `Locale`.

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

Create a compact ranked list. Explain the recommendation in plain language. Keep it focused on whether app name, subtitle, and keywords should be newly localized or refreshed for that Apple metadata locale and country or region when relevant.

If multiple locales are close, prefer the one with clearer search/source evidence or lower data uncertainty.

If conversion is acceptable but retention, ratings, deletions, crash rate, pricing, support, legal, or in-app language signals are weak, do not frame the locale as a clean metadata win. Rank it lower or add a risk flag that metadata may not be the main bottleneck.

### 5. Save Results

Save only a compact prioritization artifact at `.agents/aso/localization-prioritization.md`:

```markdown
# ASO Localization Prioritization
*Last updated: YYYY-MM-DD*

## Recommended Localizations
| Rank | Locale | Affected storefronts | Country or region preference | Opportunity type | Existing metadata status | Priority | Confidence | Diagnostic score | Key evidence | Underperformance reason | Risk flags | Optional ROI/payback | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | German | DEU |  | refresh-existing | localized metadata exists | high | medium | not calculated | strong Germany page views and weak listing conversion | current keywords appear stale | keyword data missing | not calculated | run aso-localized-metadata-workflow for German |

## Localization Inventory
| Locale | Existing status | Current metadata notes | Data source | Notes |
| --- | --- | --- | --- | --- |
| German | localized metadata exists | app name localized; subtitle generic; iOS keywords stale | App Store Connect | candidate refresh |

## Territory Signals
| Territory | Locale mapped | Existing metadata status | Impressions | Product page views | Conversion rate | First-time downloads | Proceeds/download | Retention/rating signal | Search/source notes | Comparison notes |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
```

Also add or update compact rows in `.agents/aso/context.md` `## Locales` for recommended localizations:

```markdown
| Locale | Workspace | Country or region preference | Notes |
| --- | --- | --- | --- |
| German | .agents/aso/locales/German/context.md |  | recommended by aso-localization-prioritization; action: refresh-existing; priority: high; confidence: medium |
```

When updating `## Locales`:

- Preserve existing notes unless they conflict with newer evidence.
- Do not create locale workspace files. `aso-localized-metadata-workflow` creates them after the user chooses a locale.
- Update `*Last updated:*` in changed files.

## Completion Report

End with:

- recommended localizations in priority order
- opportunity type for each recommendation
- confidence, important data gaps, and risk flags
- diagnostic score only when enough comparable data exists
- saved artifact path
- `## Locales` rows added or updated
- next step: run `aso-localized-metadata-workflow` for a chosen locale

## Common Mistakes

- Ranking locales for full app translation instead of App Store metadata localization.
- Recommending screenshots, previews, descriptions, onboarding, pricing, legal, or support work as this skill's output instead of treating them as risk or follow-up signals.
- Treating missing data as zero.
- Choosing locales only from market size or language popularity.
- Ignoring existing localized metadata that underperforms and only recommending missing localizations.
- Treating current localized metadata as good just because App Store Connect has fields filled in.
- Treating one language as one market.
- Treating one country or region as one locale.
- Treating aggregated affected storefronts as a downstream workspace identity.
- Recommending every additional supported locale in a country or region by default.
- Producing precise ROI or scoring when assumptions would be invented.
- Generating localized metadata before the user chooses a target locale.

## Related Skills

- Use `aso-context` to create or update shared app context before ranking.
- Use relevant tool-specific skills such as `asc-cli-usage` or `helm-asc` when fetching App Store Connect or App Analytics data through CLI tools.
- Use `aso-localized-metadata-workflow` after the user chooses a recommended locale.
