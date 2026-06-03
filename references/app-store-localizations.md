# App Store Localizations

Use this reference when an ASO skill needs to choose or validate an App Store country or region, metadata language, localized workspace path, or ASO tool region parameter.

Apple's App Store localization reference is the authority for supported metadata languages by country or region:

https://developer.apple.com/help/app-store-connect/reference/app-information/app-store-localizations/

Apple's table is organized as:

| Apple field | Meaning for ASO skills |
| --- | --- |
| `ISO code` | Durable App Store country/region identifier. Use this to organize localized workspaces. |
| `Country or region` | Human-readable target market name. |
| `Default language` | First language to use when the user names only the country or region. |
| `Additional supported language(s)` | Other metadata languages Apple supports in that country or region. |

## Workspace Naming

Use Apple's `ISO code` first, then one file per Apple language label:

```text
.agents/aso/locales/<ISO code>/<language-slug>.md
```

Examples:

```text
.agents/aso/locales/DEU/german.md
.agents/aso/locales/DEU/english-uk.md
.agents/aso/locales/USA/english-us.md
.agents/aso/locales/USA/spanish-mexico.md
.agents/aso/locales/ESP/spanish-spain.md
.agents/aso/locales/ESP/catalan.md
```

Slug language labels by lowercasing, removing punctuation, and replacing spaces or parenthetical qualifiers with hyphens. Examples: `English (U.K.)` -> `english-uk`, `Spanish (Mexico)` -> `spanish-mexico`.

## Source Locale Format

Use the same Apple `ISO code` and language labels for the source context:

```markdown
**Primary locale:** NLD (Dutch)
```

If a tool requires a two-letter country or region parameter, derive it from the ISO code at tool-call time.

## Selection Rules

- Explicit user-provided `ISO code` and Apple language label always win when the pair exists in Apple's table.
- If the user names a country or region, use that row's default language unless the user asks for another supported language.
- If the user names a country or region with several supported languages, mention the additional options when useful, but do not optimize all of them unless asked.
- If the user names a language group instead of a country, suggest one workspace per App Store country or region where that language is a default or supported language and fetch statistics separately for each country or region.
- Use existing `.agents/aso/context.md` locale preferences, `## Locales`, App Store Connect metadata, local metadata files, or App Store URL country clues as stronger evidence than defaults.
- Validate country/region and language pairs against Apple's table before fetching statistics or drafting metadata.
- Do not store a separate stats region in localized workspaces. If an ASO tool requires an ISO 3166-1 alpha-2 region parameter, derive it from the workspace `ISO code` at tool-call time.

## Tool Region Derivation

Some ASO tools use two-letter country or region codes while Apple lists three-letter ISO codes on the localization page. Derive the tool parameter when needed; do not store it as workspace state.

Common examples:

| ISO code | Tool region |
| --- | --- |
| AUT | AT |
| BEL | BE |
| CAN | CA |
| CHE | CH |
| DEU | DE |
| ESP | ES |
| FRA | FR |
| GBR | GB |
| JPN | JP |
| MEX | MX |
| NLD | NL |
| USA | US |

If the needed mapping is not in this reference, use a standard ISO 3166 lookup or the agent's country-code knowledge. If still uncertain, ask before fetching statistics.

## Common Country And Language Rows

This table covers the common ASO targets and examples the skills should resolve without asking. For other countries or regions, consult Apple's localization reference.

| ISO code | Country or region | Default language | Additional supported language(s) |
| --- | --- | --- | --- |
| AUT | Austria | German | English (U.K.) |
| AUS | Australia | English (Australia) | English (U.K.) |
| BEL | Belgium | English (U.K.) | Dutch, French |
| BRA | Brazil | Portuguese (Brazil) | English (U.K.) |
| CAN | Canada | English (Canada) | French (Canada) |
| CHE | Switzerland | German | English (U.K.), French, Italian |
| CHN | China mainland | Simplified Chinese | English (U.K.) |
| DEU | Germany | German | English (U.K.) |
| ESP | Spain | Spanish (Spain) | Catalan, English (U.K.) |
| FRA | France | French | English (U.K.) |
| GBR | United Kingdom | English (U.K.) |  |
| ITA | Italy | Italian | English (U.K.) |
| JPN | Japan | Japanese | English (US) |
| KOR | South Korea | Korean | English (U.K.) |
| LUX | Luxembourg | English (U.K.) | French, German |
| MEX | Mexico | Spanish (Mexico) | English (U.K.) |
| NLD | Netherlands | Dutch | English (U.K.) |
| PRT | Portugal | Portuguese (Portugal) | English (U.K.) |
| SWE | Sweden | Swedish | English (U.K.) |
| USA | United States | English (US) | Arabic, Chinese (Simplified), Chinese (Traditional), French, Korean, Portuguese (Brazil), Russian, Spanish (Mexico), Vietnamese |

## Prompt Resolution Examples

- `draft metadata for Germany` -> `.agents/aso/locales/DEU/german.md`; use German search terms and derive `DE` only when the statistics tool needs it.
- `draft metadata for German-speaking regions` -> suggest separate German workspaces for `DEU`, `AUT`, `CHE`, and `LUX`; fetch statistics separately per ISO code.
- `draft metadata for US Spanish` -> `.agents/aso/locales/USA/spanish-mexico.md`; use Spanish (Mexico) search terms and derive `US` for statistics tools.
- `draft metadata for Spain` -> `.agents/aso/locales/ESP/spanish-spain.md`; mention Catalan and English (U.K.) as optional additional supported languages.
