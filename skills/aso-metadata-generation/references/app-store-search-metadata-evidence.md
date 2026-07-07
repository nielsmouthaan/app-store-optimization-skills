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
- `Keywords` field
- Primary category
- Company/developer name for branded findability

Apple also says primary and optional secondary categories are indexed, but Apple emphasizes primary category more clearly. Treat secondary category importance as less certain.

## Conversion-Oriented Fields

These fields can affect whether a search impression becomes a tap or install, but Apple does not document them as core search term ranking fields:

- Promotional text
- Description
- What's New
- Screenshots
- App previews

Use these fields as context for product language, clarity, and conversion. Do not use them as `Keywords` fields for App Store search metadata generation.

## Statistics Handling

- Treat third-party popularity and difficulty scores as source-defined estimates unless Apple documents otherwise.
- Store popularity and difficulty only as validated `1`-`100` planning inputs.
- Apple Ads Search Popularity on a user-provided `1`-`5` scale may be normalized for `Popularity` as `1 -> 5`, `2 -> 20`, `3 -> 40`, `4 -> 60`, and `5 -> 80`.
- Do not infer `Difficulty` from Apple Ads Search Popularity.
- Record normalization, stale data, source mismatch, seasonality, or other caveats compactly in backlog `Notes`; do not add separate evidence artifacts by default.

## Practitioner-Supported Drafting Rules

- Use app name, subtitle, then `Keywords` field as a priority order for placement, but label this as practitioner-supported rather than Apple-documented.
- Avoid duplicate words across indexed fields; Apple discourages duplicates and practitioner evidence strongly supports avoiding them.
- Use the `Keywords` field for unique remaining terms and efficient roots by default.
- Preserve phrases only when splitting would change meaning or when a confirmed high-value term justifies the character cost.

## Unresolved Claims

- Apple does not publish exact relative weights for app name, subtitle, `Keywords` field, and category.
- Apple documentation and ASO sources may use mixed character/byte wording for `Keywords` field limits; this skill suite uses 100 characters for implementation.
- Exact phrase-combination mechanics, especially across localizations, are not Apple-documented.
- Screenshot text and description semantics are not documented as direct App Store search text-relevance inputs.
