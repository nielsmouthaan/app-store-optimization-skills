---
name: aso-metadata-performance-analysis
description: Analyzes post-publish performance of App Store metadata changes to app name, subtitle, and keywords. Use for metadata performance analysis, post-publish metadata evaluation, search discoverability impact, before/after metadata changes, organic search impact, or deciding whether metadata changes improved, hurt, or had no clear effect. Uses aso-search-terms-rankings for keyword ranking data.
---

# ASO Metadata Performance Analysis

Act as an ASO performance analyst. Evaluate whether a published metadata change improved, hurt, or had no clear effect on App Store search discoverability and downstream user quality.

This skill is an evaluation step. It does not generate metadata, collect keyword rankings directly, publish App Store Connect changes, or replace App Store Connect, App Analytics, Sales/Trends, Search Ads, or ranking data.

## Before Starting

Read `.agents/aso/context.md` first.

Use the source-locale context unless the user explicitly names a language, locale, country or region, storefront, or Apple country or region ISO code. For localized metadata, read the matching `.agents/aso/locales/<Locale>/context.md` workspace and save the analysis next to that workspace.

If app context is missing or incomplete:

- Invoke or recommend `aso-context` before continuing.
- Do not analyze metadata impact until the app, active locale, platforms, and relevant metadata are clear.

If the user asks only for keyword rankings, use `aso-search-terms-rankings`. If the user asks whether a metadata change improved performance, continue with this skill and use rankings as one evidence source.

## Data Sources

Use whichever trustworthy sources are available. Prefer automatic read-only collection when tools are available, then fall back to user-provided exports or pasted tables.

Useful data includes:

- App Store Connect or App Analytics acquisition data by source type.
- Sales/Trends App Units or commercial data.
- Search Ads impressions, taps, downloads, spend, conversion, keywords, search terms, Search Match, and impression share.
- Keyword ranking history from `.agents/aso/keyword-rankings.md` or `.agents/aso/locales/<Locale>/keyword-rankings.md`.
- User-provided ASO tool exports, App Store Connect exports, Search Ads exports, or analytics summaries.
- Release notes, major app releases, featuring, Product Page Optimization, Custom Product Pages, paid campaigns, pricing changes, outages, or external events.

When `asc` and `asc-cli-usage` are available, use them to obtain relevant App Store Connect, App Analytics, Sales/Trends, and Search Ads data before asking the user for manual exports.

If a source is unavailable, unauthenticated, stale, thresholded, or incomplete, continue with the available evidence and mark the confidence impact.

## Workflow

### 1. Define The Intervention

Identify the metadata change before looking at outcomes:

- app name, subtitle, and keyword fields changed
- platform, locale, country or region, and storefront scope
- previous values and new values
- intended target search terms or keyword clusters
- submission, approval, and visible-on-store timing when known
- other changes that could affect the same metrics

If the go-live date cannot be resolved, ask for it before drawing before/after conclusions.

### 2. Build Measurement Windows

Use these defaults unless the user gives a better design:

- **Baseline:** 28 days before the change, matched on weekdays when possible.
- **Washout:** skip the go-live day and incomplete analytics days.
- **Early readout:** 7 full days after washout.
- **Primary readout:** 14 full days after washout.
- **Stabilized readout:** 28 full days after washout.

For retention, proceeds per download, LTV proxy, or other cohort-quality metrics, allow extra time for the cohort to mature. If traffic is sparse, use a longer window or mark the result inconclusive instead of forcing a precise decision.

### 3. Analyze Search Performance First

Start with App Store search-source funnel metrics:

- impressions, preferably unique impressions
- product page views, preferably unique product page views
- first-time downloads, total downloads, or App Units
- conversion rate

Treat App Store Connect `App Store search` as potentially blended because search-result ads can contribute to it. Use Search Ads data to judge whether paid search could explain the movement. Search Ads data may be user-provided or obtained automatically through available tools such as `asc`.

Do not call a result purely organic unless Search Ads evidence, campaign records, or explicit user confirmation supports that conclusion. If Search Ads data is missing, analyze search-source performance but lower organic-attribution confidence.

### 4. Add Ranking And Downstream Evidence

Use keyword ranking data as a diagnostic signal:

- Read the relevant keyword ranking artifact when it exists.
- If ranking data is missing, stale, or not collected for the changed target terms, invoke or recommend `aso-search-terms-rankings`.
- Treat rankings as one signal, not the whole performance result.

Then check downstream guardrails when available:

- sessions and engagement
- D1, D7, D30, or available retention
- proceeds per download, revenue, paying users, or LTV proxy
- ratings, reviews, deletion signals, crashes, or quality issues
- major releases, featuring, product page changes, campaigns, or external events

### 5. Decide

Assign one decision label:

| Decision | Meaning |
| --- | --- |
| `better` | Primary search-source KPI improved meaningfully and guardrails do not show a serious downside. |
| `same` | Metrics are stable within practical bounds and there is no meaningful guardrail movement. |
| `poorer` | Primary search-source KPI or important guardrails worsened meaningfully. |
| `inconclusive` | Data is too sparse, confounded, stale, incomplete, or mixed to support a reliable decision. |

State confidence as `high`, `medium`, or `low`. Lower confidence when Search Ads data is missing, campaign changes overlap the metadata change, ranking data is absent, traffic is sparse, source data is thresholded, or other product/store changes overlap the measurement window.

## Saving Results

Save source-locale analyses to:

```text
.agents/aso/metadata-performance-analysis.md
```

Save localized analyses to:

```text
.agents/aso/locales/<Locale>/metadata-performance-analysis.md
```

Use this simple structure:

```markdown
# Metadata Performance Analysis
*Last updated: YYYY-MM-DD*

## Intervention

## Evidence

## Analysis

## Decision

## Next Steps
```

In `## Evidence`, summarize data sources, date ranges, search funnel metrics, ranking movement, Search Ads impact, and key data-quality caveats.

In `## Analysis`, explain what changed, whether paid search or other confounders could explain it, and whether downstream quality supports the result.

In `## Decision`, include the label, confidence, primary KPI, organic/paid confidence, and short rationale.

Preserve prior analysis entries unless the user explicitly asks to replace them. If updating the same intervention, update the existing entry instead of creating conflicting conclusions.

## Completion Report

End with:

- active source-locale or localized workspace
- artifact path updated
- intervention and measurement windows
- data sources used and important gaps
- search-source result, ranking signal, Search Ads impact, and guardrail summary
- decision label, confidence, and main reason
- next step, such as monitor longer, collect rankings, gather Search Ads data, revert, keep, or start a new metadata iteration

## Common Mistakes

- Treating keyword rankings as the complete performance evaluation.
- Calling App Store search-source movement organic without checking Search Ads evidence or confirming no paid search influence.
- Mixing App Store Connect downloads, Sales/Trends App Units, and installs without noting definition differences.
- Ignoring incomplete days, publication timing, or cohort maturation.
- Claiming causality from a simple before/after comparison when campaigns, releases, featuring, or product page changes overlap.
- Forcing a `better`, `same`, or `poorer` decision when evidence only supports `inconclusive`.

## Related Skills

- Use `aso-context` to create or update shared app context before analyzing impact.
- Use `asc-cli-usage` when `asc` is available for App Store Connect, App Analytics, Sales/Trends, or Search Ads data collection.
- Use `aso-search-terms-rankings` to collect or update keyword ranking data.
- Use `aso-metadata-generation` to create a new metadata iteration after analysis.
