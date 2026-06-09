# AGENTS.md

Guidelines for AI agents working in this repository.

## Repository Overview

This repository is for **App Store Optimization Agent Skills** that follow the [Agent Skills specification](https://agentskills.io/specification.md). Skills install to `.agents/skills/` (the cross-agent standard).

- **Name**: App Store Optimization Skills
- **GitHub**: [nielsmouthaan/app-store-optimization-skills](https://github.com/nielsmouthaan/app-store-optimization-skills)
- **Creator**: Niels Mouthaan
- **License**: MIT

## Repository Structure

```text
app-store-optimization-skills/
├── skills/              # Agent Skills
│   └── skill-name/
│       └── SKILL.md     # Required skill file
├── AGENTS.md
├── LICENSE
└── README.md
```

## Build / Lint / Test Commands

**Skills** are content-only (no build step).

Verify manually:

- YAML frontmatter is valid
- `name` field matches directory name exactly
- `name` is 1-64 characters, lowercase alphanumeric and hyphens only
- `description` is 1-1024 characters

## Agent Skills Specification

Skills follow the [Agent Skills spec](https://agentskills.io/specification.md).

### Required Frontmatter

```yaml
---
name: skill-name
description: What this skill does and when to use it. Include trigger phrases.
---
```

### Frontmatter Field Constraints

| Field | Required | Constraints |
| --- | --- | --- |
| `name` | Yes | 1-64 chars, lowercase `a-z`, numbers, hyphens. Must match directory. |
| `description` | Yes | 1-1024 chars. Describe what it does and when to use it. |
| `license` | No | License name, if needed. |
| `metadata` | No | Key-value pairs such as author or version. |

### Name Field Rules

- Lowercase letters, numbers, and hyphens only
- Cannot start or end with hyphen
- No consecutive hyphens (`--`)
- Must match parent directory name exactly

### Optional Skill Directories

```text
skills/skill-name/
├── SKILL.md       # Required - main instructions
├── references/    # Optional - detailed docs loaded on demand
├── scripts/       # Optional - executable code
└── assets/        # Optional - templates or data files
```

## Writing Style Guidelines

### Structure

- Keep `SKILL.md` focused and concise.
- Use H2 (`##`) for main sections and H3 (`###`) for subsections.
- Use bullet points and numbered lists liberally.
- Use short paragraphs.
- Move long examples, schemas, and reference material out of `SKILL.md`.

### Tone

- Direct and instructional
- Professional but approachable
- Specific about inputs, outputs, and stopping conditions

### Formatting

- Use **bold** for key terms
- Use code blocks for examples and templates
- Use tables for reference data
- Avoid excessive emojis

### Clarity Principles

- Clarity over cleverness
- Specific over vague
- Active voice over passive
- One idea per section

### Description Field Best Practices

The `description` is critical for skill discovery.

Include:

1. What the skill does
2. When to use it (trigger phrases)
3. Related skills for scope boundaries, when relevant

```yaml
description: Research App Store keyword candidates with popularity and difficulty data. Use when the user provides search terms and wants measurable ASO keyword evidence. For metadata generation, use the aso-metadata-generation skill.
```

## Skill Suite Guidance

- Use source context fields consistently: `Primary locale` is the exact Apple metadata locale label, such as `Dutch` or `Spanish (Mexico)`. Do not include an ISO code in `Primary locale`.
- Treat Apple `ISO code` values from the localization reference as country or region identifiers for storefront-specific statistics, rankings, App Analytics, App Store URLs, or explicit user preferences; never use them as locale identifiers or locale folders.
- Derive the default country or region from the relevant skill-local `references/app-store-localizations.md` when a tool needs one. Store `Country or region preference` only when the user or clear source evidence explicitly overrides the default, similar to `Search surface preference`.
- Store localized ASO work under `.agents/aso/locales/<Apple locale label>/context.md`, for example `.agents/aso/locales/Spanish (Mexico)/context.md`.
- `Platforms` contains only App Store Connect metadata platforms (`iOS`, `macOS`, `tvOS`, `visionOS`). Derive platform/tool aliases from the relevant skill-local `references/platforms.md`.
- Treat iPhone, iPad, Mac, Apple TV, and Vision as search surfaces for statistics, rankings, or tool parameters, not as `Platforms` values. Do not store a search surface by default; store `Search surface preference` only when the user explicitly requests one.
- Treat app name and subtitle as shared metadata, and keywords as platform-specific. Draft or store keywords in `Keywords (iOS)`, `Keywords (macOS)`, etc.; do not silently reuse keyword stats, rankings, or drafts across platforms.
- Treat App Store keyword fields as 100-character limits per platform for this skill suite. Do not use byte counting for keyword fields, even when Apple documentation or other sources use mixed character/byte wording.
- Use `aso-context` as the foundation skill for capturing and storing reusable context and data, so agents do not repeat the same questions and can pass context and data between skills.
- Treat `aso-context` as an internal foundation skill in user-facing docs. Do not over-position it as the primary skill users should invoke directly; user-facing README examples should normally start with specialist skills such as search-term identification or relevance scoring.
- Specialist skills should check `.agents/aso/context.md` before starting. If it exists, use it as canonical app context. If it is missing or incomplete, invoke or recommend `aso-context` first.
- Use an `aso-*` prefix for ASO-specific skills so installed skills remain clearly namespaced.
- Use workflow skills, such as `aso-metadata-workflow` and `aso-localized-metadata-workflow`, as the primary entrypoint for workflows.
- Workflow skills should not duplicate specialist skill instructions. They should point to the relevant skill for each phase and pass along the required context or artifacts.
- Keep specialist skills independently useful when invoked directly.
- Use explicit artifacts between phases instead of relying on chat history.
- Skills must be independently installable. Any support file a skill needs at runtime must live inside that skill's folder.
- Use standard skill-local directories when applicable: `references/` for documentation, `scripts/` for executable helpers, and `assets/` for templates or static resources.
- Do not make installed skills depend on repository-level support files.

## README Updates

Update `README.md` whenever a skill is added, renamed, removed, or materially changed.

The README should stay user-facing and include only what is true for the current repository state:

- available skills and what each one does
- the primary user-facing specialist skills, with internal foundation skills described briefly when needed
- installation instructions only when explicitly requested by the user
- usage instructions only when explicitly requested by the user
- workflow overview once workflow skills exist
- acknowledgements and license notes

## Git Workflow

### Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat: add skill-name skill`
- `fix: improve clarity in skill-name`
- `docs: update README`
