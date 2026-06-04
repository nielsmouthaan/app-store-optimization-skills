# App Store Search Metadata Evidence

Use this reference when an ASO skill needs to distinguish Apple-documented facts from practitioner-supported assumptions or unresolved App Store search claims.

## Evidence Labels

| Label | Use when |
| --- | --- |
| `Apple-documented` | Apple documents the field, limit, policy, or localization behavior. |
| `Practitioner-supported` | Reputable ASO practice or experiments support the guidance, but Apple does not publish it as a rule. |
| `Practitioner assumption` | The guidance is a plausible operational shortcut based on field practice, but evidence is limited. |
| `Unresolved` | Apple documentation is incomplete, conflicting, or silent, and practitioner sources disagree. |

## Indexed Metadata

Apple-documented indexed or searchable inputs for core app metadata:

- App name/title
- Subtitle
- Keyword field
- Primary category
- Company/developer name for branded findability

Apple also says primary and optional secondary categories are indexed, but Apple emphasizes primary category more clearly. Treat secondary category importance as less certain.

## Conversion-Oriented Fields

These fields can affect whether a search impression becomes a tap or install, but Apple does not document them as core keyword-ranking fields:

- Promotional text
- Description
- What's New
- Screenshots
- App previews

Use these fields as context for product language, clarity, and conversion. Do not use them as keyword buckets for App Store search metadata generation.

## Practitioner-Supported Drafting Rules

- Use app name, subtitle, then keyword field as a priority order for placement, but label this as practitioner-supported rather than Apple-documented.
- Avoid duplicate words across indexed fields; Apple discourages duplicates and practitioner evidence strongly supports avoiding them.
- Use the keyword field for unique remaining terms and efficient roots by default.
- Preserve phrases only when splitting would change meaning or when a confirmed high-value term justifies the byte cost.

## Unresolved Claims

- Apple does not publish exact relative weights for app name, subtitle, keyword field, and category.
- Apple documents both 100-character and 100-byte keyword limits in different places; use 100 bytes for implementation.
- Exact phrase-combination mechanics, especially across localizations, are not Apple-documented.
- Screenshot text and description semantics are not documented as direct App Store search text-relevance inputs.
