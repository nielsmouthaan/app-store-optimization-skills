# App Store Optimization Skills

This suite contains agent skills for App Store Optimization (ASO). It helps you and your AI agents run structured, evidence-based ASO workflows.

The suite is maintained by Niels Mouthaan, the original founder of [ASO Suite](https://nielsmouthaan.dev/asosuite), a Mac-native ASO tool that was sold.

The current skills focus mainly on generating data-backed, ranking-affecting App Store metadata: app name, subtitle, and keywords. The workflow follows a methodology based on the [Advanced App Store Optimization Book](https://www.asoebook.com): identify a broad set of plausible search terms, collect popularity and difficulty statistics, calculate strategic scores, calculate per-word value, and draft metadata that aims to cover as many strategically useful search terms as possible.

For example, for a receipt-scanning app, the suite could generate metadata like:

- **Name:** Taxxy - Tax Receipt Scanner
- **Subtitle:** Invoices & Expense OCR
- **Keywords:** bookkeeping,deductions,vat,bills,records,audit,refunds,accountant,reimbursements,filing,claims

This suite is free to use. If you want to support ongoing maintenance, consider buying me a figurative coffee; thanks!

<p>
  <a href="https://buymeacoffee.com/nielsmouthaan">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="217" height="60">
  </a>
</p>

## Skills

This repository contains two workflow skills and several specialist skills used by those workflows. In normal use, start with a workflow skill. Use specialist skills directly only when you need a narrower task.

### `aso-metadata-workflow`

Runs the full ASO metadata optimization workflow for the app's primary or source metadata language. It coordinates a numbered five-phase flow:

1. `aso-context` establishes reusable source app context.
2. `aso-search-terms-identification` identifies a broad backlog of plausible App Store search-term candidates and assigns relevance scores based on App Store search intent and how well the app satisfies that intent.
3. `aso-search-terms-statistics` fetches external popularity and difficulty statistics for confirmed search terms. This requires an ASO tool such as [ASO Suite](https://nielsmouthaan.dev/asosuite) or [Astro](https://nielsmouthaan.dev/astro).
4. `aso-search-terms-scoring` calculates a strategic score for confirmed search terms and per-word value scores from those strategic scores.
5. `aso-metadata-generation` generates recommended metadata drafts for the shared app name, shared subtitle, and platform-specific keyword fields.

Use this workflow for the primary locale of the app.

### `aso-localized-metadata-workflow`

Use this workflow when you want to introduce or improve localized App Store metadata for another locale. It follows an explicit seven-phase flow for global context, locale validation, workspace setup, localized search-term identification, statistics, scoring, and metadata generation. It is the localized counterpart to `aso-metadata-workflow`, intended for metadata that should read naturally for local users instead of as a direct translation of the primary metadata.

### `aso-search-terms-rankings`

Tracks keyword rankings and ranking trends for confirmed search terms. This is useful after metadata changes go live, and it works well as a scheduled check.

The skill attempts to use ASO tools such as [ASO Suite](https://nielsmouthaan.dev/asosuite) or [Astro](https://nielsmouthaan.dev/astro) when available. If no supported tool is available, it can fall back to the less accurate iTunes Search API.

The suite also includes `aso-context` as an internal foundation skill for reusable app context. Users normally do not call it directly.

## Limitations

Most useful ASO data is not publicly available. Existing keyword fields, keyword popularity, difficulty, and accurate rankings usually require access to external systems.

This suite works best with:

- App Store Connect access, typically through agent-accessible tools such as [`asc`](https://github.com/rorkai/App-Store-Connect-CLI) or the CLI included with [Helm](https://helm-app.com).
- ASO statistics and ranking tools, preferably [ASO Suite](https://nielsmouthaan.dev/asosuite) or [Astro](https://nielsmouthaan.dev/astro).
- A capable AI model with strong reasoning.

## Installation

Installation instructions will be updated later.

## Usage

AI assistants usually discover and invoke skills from the prompt you provide. For best results, run these prompts in your app's repository so the agent can inspect the app's code, metadata files, and any existing ASO artifacts. You can also run the workflows elsewhere, but you will need to provide more context manually.

Example prompts:

- Use `aso-metadata-workflow` to optimize the App Store metadata of this app with the aim of increasing organic search discoverability in the primary region.
- Use `aso-localized-metadata-workflow` to optimize my App Store metadata for Spanish (Spain), with the aim of increasing organic search discoverability in regions where Spanish (Spain) is applicable.
- Use `aso-search-terms-rankings` to track current App Store keyword rankings for my confirmed search terms in the primary region on iPhone.
- Use `aso-search-terms-rankings` to determine whether updated metadata has resulted in better rankings for strategical keywords.

## Roadmap

App Store optimization goes beyond organic-search metadata. Future skill-suite extensions may cover:

- Removing dependencies on ASO tools for obtaining search-term statistics, with the goal of making agentic ASO entirely free
- Suggesting locales for metadata optimization based on evidence
- Metadata optimization for custom product pages
- Full product page analysis and localization, including screenshots and app previews
- Search Ads campaign analysis and recommendations

## Contribution

If you run into issues or have suggestions, open an issue. Pull requests are welcome when they follow `AGENTS.md` and stay within the scope of this skill suite.

## Acknowledgements

This skill suite uses a metadata-generation methodology based on the [Advanced App Store Optimization Book](https://www.asoebook.com).

It is inspired by the following MIT-licensed projects:

- Corey Haines's [Marketing Skills](https://github.com/coreyhaines31/marketingskills)  
  Copyright (c) 2025 Corey Haines
- Antoine van der Lee's [Xcode Build Optimization Agent Skill](https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill)  
  Copyright (c) 2026 Antoine van der Lee

Thanks to the maintainers and builders of community tools, including [ASO Suite](https://nielsmouthaan.dev/asosuite), [Astro](https://nielsmouthaan.dev/astro), [`asc`](https://github.com/rorkai/App-Store-Connect-CLI), and [Helm](https://helm-app.com).

Some links in this README or the skill implementations may be affiliate links.

## Copyright

See [LICENSE](LICENSE) for copyright and license information.
