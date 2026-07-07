# App Store Localizations

Use this reference when an ASO skill needs to choose or validate an App Store metadata locale, derive a default country or region for storefront-specific statistics or rankings, or derive a tool country or region parameter.

Apple's App Store localization reference is the authority:

https://developer.apple.com/help/app-store-connect/reference/app-information/app-store-localizations/

Apple separates two concepts:

| Concept | Meaning for ASO skills |
| --- | --- |
| Metadata locale | The Apple-supported app information language/locale label, such as `Dutch`, `Spanish (Mexico)`, or `Chinese (Simplified)`. Use this as the locale identity and workspace folder name. |
| Country or region ISO code | The storefront/territory code from Apple's table, such as `NLD`, `MEX`, or `USA`. Use this only when statistics, rankings, App Analytics, App Store URLs, or user instructions require a country or region. |
| App Store Connect locale code | The API localization code, such as `nl-NL`, `es-ES`, or `zh-Hant`. Use this only when App Store Connect metadata tooling requires a locale code. |
| Tool country or region parameter | A tool-specific value, often a two-letter country code such as `NL`, `MX`, or `US`. Derive it at call time; do not store it as locale identity. |

## Supported Metadata Locales

Apple lists these supported app information languages and locales:

`Arabic`, `Bangla`, `Catalan`, `Chinese (Simplified)`, `Chinese (Traditional)`, `Croatian`, `Czech`, `Danish`, `Dutch`, `English (Australia)`, `English (Canada)`, `English (U.K.)`, `English (U.S.)`, `Finnish`, `French`, `French (Canada)`, `German`, `Greek`, `Gujarati`, `Hebrew`, `Hindi`, `Hungarian`, `Indonesian`, `Italian`, `Japanese`, `Kannada`, `Korean`, `Malay`, `Malayalam`, `Marathi`, `Norwegian`, `Odia`, `Polish`, `Portuguese (Brazil)`, `Portuguese (Portugal)`, `Punjabi`, `Romanian`, `Russian`, `Slovak`, `Slovenian`, `Spanish (Mexico)`, `Spanish (Spain)`, `Swedish`, `Tamil`, `Telugu`, `Thai`, `Turkish`, `Ukrainian`, `Urdu`, `Vietnamese`.

Use exact Apple locale labels for locale identity and folder names. If Apple's country or region table uses a shortened label such as `English (US)` or `Simplified Chinese`, normalize it to the supported metadata locale label above, such as `English (U.S.)` or `Chinese (Simplified)`.

## App Store Connect Locale Codes

Use these codes only when App Store Connect metadata tooling asks for a locale code. They were cross-checked against an App Store Connect locale catalog on 2026-07-02. If a tool rejects a code, verify against the current tool or App Store Connect response before changing the workspace locale label.

| Metadata locale | App Store Connect locale code |
| --- | --- |
| Arabic | `ar-SA` |
| Bangla | `bn-BD` |
| Catalan | `ca` |
| Chinese (Simplified) | `zh-Hans` |
| Chinese (Traditional) | `zh-Hant` |
| Croatian | `hr` |
| Czech | `cs` |
| Danish | `da` |
| Dutch | `nl-NL` |
| English (Australia) | `en-AU` |
| English (Canada) | `en-CA` |
| English (U.K.) | `en-GB` |
| English (U.S.) | `en-US` |
| Finnish | `fi` |
| French | `fr-FR` |
| French (Canada) | `fr-CA` |
| German | `de-DE` |
| Greek | `el` |
| Gujarati | `gu-IN` |
| Hebrew | `he` |
| Hindi | `hi` |
| Hungarian | `hu` |
| Indonesian | `id` |
| Italian | `it` |
| Japanese | `ja` |
| Kannada | `kn-IN` |
| Korean | `ko` |
| Malay | `ms` |
| Malayalam | `ml-IN` |
| Marathi | `mr-IN` |
| Norwegian | `no` |
| Odia | `or-IN` |
| Polish | `pl` |
| Portuguese (Brazil) | `pt-BR` |
| Portuguese (Portugal) | `pt-PT` |
| Punjabi | `pa-IN` |
| Romanian | `ro` |
| Russian | `ru` |
| Slovak | `sk` |
| Slovenian | `sl-SI` |
| Spanish (Mexico) | `es-MX` |
| Spanish (Spain) | `es-ES` |
| Swedish | `sv` |
| Tamil | `ta-IN` |
| Telugu | `te-IN` |
| Thai | `th` |
| Turkish | `tr` |
| Ukrainian | `uk` |
| Urdu | `ur-PK` |
| Vietnamese | `vi` |

## Workspace Naming

Use one workspace per metadata locale:

```text
.agents/aso/locales/<Locale>/context.md
```

Examples:

```text
.agents/aso/locales/German/context.md
.agents/aso/locales/Dutch/context.md
.agents/aso/locales/English (U.K.)/context.md
.agents/aso/locales/English (U.S.)/context.md
.agents/aso/locales/Spanish (Mexico)/context.md
.agents/aso/locales/Spanish (Spain)/context.md
.agents/aso/locales/Catalan/context.md
```

Localized ranking artifacts live next to the locale workspace:

```text
.agents/aso/locales/<Locale>/search-term-rankings.md
```

## Source Locale Format

Store the source metadata locale as the Apple locale label only:

```markdown
**Primary locale:** Dutch
```

Store a country or region only when the user explicitly requests one or source evidence clearly requires a non-default country or region:

```markdown
**Country or region preference:** BEL
```

Do not store any ISO-code-plus-locale value as a locale identity.

## Country Or Region Resolution

When a statistics or rankings skill needs a storefront country or region, resolve it in this order:

1. Explicit user request for the current run.
2. Saved `Country or region preference`.
3. Default country or region for the active metadata locale from this reference.
4. Ask the user if no safe default is listed.

Use a saved `Country or region preference` only when the user or source evidence explicitly overrides the locale default, similar to `Search surface preference`.

## Default Country Or Region By Locale

This table is for ASO skill defaults, not App Store Connect's `Default language` column. Every listed country or region is grounded in Apple's localization table. When the user explicitly names another Apple-supported country or region for the locale, store it as `Country or region preference`.

| Metadata locale | Default country or region | Other Apple-supported countries or regions |
| --- | --- | --- |
| Arabic | SAU | DZA, BHR, EGY, IRQ, JOR, KWT, LBN, LBY, MRT, MAR, OMN, QAT, TUN, ARE, USA, YEM |
| Bangla | IND |  |
| Catalan | ESP |  |
| Chinese (Simplified) | CHN | SGP, USA |
| Chinese (Traditional) | TWN | HKG, MAC, USA |
| Croatian | HRV | BIH, MNE, SRB |
| Czech | CZE |  |
| Danish | DNK |  |
| Dutch | NLD | BEL, SUR |
| English (Australia) | AUS | NZL |
| English (Canada) | CAN |  |
| English (U.K.) | GBR | AFG, ALB, DZA, AGO, AIA, ATG, ARG, ARM, AUS, AUT, AZE, BHS, BHR, BRB, BLR, BEL, BLZ, BEN, BMU, BTN, BOL, BIH, BWA, BRA, VGB, BRN, BGR, BFA, KHM, CMR, CPV, CYM, TCD, CHL, CHN, COL, COD, COG, CRI, CIV, HRV, CYP, CZE, DNK, DMA, DOM, ECU, EGY, SLV, EST, SWZ, FJI, FIN, FRA, GAB, GMB, GEO, DEU, GHA, GRC, GRD, GTM, GNB, GUY, HND, HKG, HUN, ISL, IND, IDN, IRQ, IRL, ISR, ITA, JAM, JOR, KAZ, KEN, XKS, KWT, KGZ, LAO, LVA, LBN, LBR, LBY, LTU, LUX, MAC, MDG, MWI, MYS, MDV, MLI, MLT, MRT, MUS, MEX, FSM, MDA, MNG, MNE, MSR, MAR, MOZ, MMR, NAM, NRU, NPL, NLD, NZL, NIC, NER, NGA, MKD, NOR, OMN, PAK, PLW, PAN, PNG, PRY, PER, PHL, POL, PRT, QAT, KOR, ROU, RUS, RWA, STP, SAU, SEN, SRB, SYC, SLE, SGP, SVK, SVN, SLB, ZAF, ESP, LKA, KNA, LCA, VCT, SUR, SWE, CHE, TWN, TJK, TZA, THA, TON, TTO, TUN, TUR, TKM, TCA, UGA, UKR, ARE, URY, UZB, VUT, VEN, VNM, YEM, ZMB, ZWE |
| English (U.S.) | USA | JPN |
| Finnish | FIN |  |
| French | FRA | DZA, BEL, BEN, BFA, KHM, CMR, TCD, COD, COG, CIV, EGY, GAB, GNB, GUY, LAO, LBN, LUX, MDG, MLI, MRT, MUS, MAR, NER, RWA, SEN, SYC, CHE, TTO, TUN, USA, VUT |
| French (Canada) | CAN |  |
| German | DEU | AUT, LUX, CHE |
| Greek | GRC | CYP |
| Gujarati | IND |  |
| Hebrew | ISR |  |
| Hindi | IND |  |
| Hungarian | HUN |  |
| Indonesian | IDN |  |
| Italian | ITA | CHE |
| Japanese | JPN |  |
| Kannada | IND |  |
| Korean | KOR | USA |
| Malay | MYS |  |
| Malayalam | IND |  |
| Marathi | IND |  |
| Norwegian | NOR |  |
| Odia | IND |  |
| Polish | POL |  |
| Portuguese (Brazil) | BRA | USA |
| Portuguese (Portugal) | PRT |  |
| Punjabi | IND |  |
| Romanian | ROU |  |
| Russian | RUS | UKR, USA |
| Slovak | SVK |  |
| Slovenian | SVN |  |
| Spanish (Mexico) | MEX | ARG, BLZ, BOL, CHL, COL, CRI, DOM, ECU, SLV, GTM, HND, NIC, PAN, PRY, PER, USA, URY, VEN |
| Spanish (Spain) | ESP |  |
| Swedish | SWE |  |
| Tamil | IND |  |
| Telugu | IND |  |
| Thai | THA |  |
| Turkish | TUR | CYP |
| Ukrainian | UKR | RUS |
| Urdu | PAK | IND |
| Vietnamese | VNM | USA |

## Country Or Region Table

Apple's country or region table has these fields:

| Apple field | Meaning for ASO skills |
| --- | --- |
| `ISO code` | Storefront/statistics/ranking country or region. Do not use it as the locale identity or workspace folder. |
| `Country or region` | Human-readable market name from Apple. Do not store this when the ISO code is enough. |
| `Default language` | The default metadata locale for that country or region. |
| `Additional supported language(s)` | Other metadata locales Apple supports in that country or region. |

Common rows used by these skills:

| ISO code | Default metadata locale | Additional metadata locales |
| --- | --- | --- |
| AUT | German | English (U.K.) |
| AUS | English (Australia) | English (U.K.) |
| BEL | English (U.K.) | Dutch, French |
| BRA | Portuguese (Brazil) | English (U.K.) |
| CAN | English (Canada) | French (Canada) |
| CHE | German | English (U.K.), French, Italian |
| CHN | Chinese (Simplified) | English (U.K.) |
| DEU | German | English (U.K.) |
| ESP | Spanish (Spain) | Catalan, English (U.K.) |
| FRA | French | English (U.K.) |
| GBR | English (U.K.) |  |
| ITA | Italian | English (U.K.) |
| JPN | Japanese | English (U.S.) |
| KOR | Korean | English (U.K.) |
| LUX | English (U.K.) | French, German |
| MEX | Spanish (Mexico) | English (U.K.) |
| NLD | Dutch | English (U.K.) |
| PRT | Portuguese (Portugal) | English (U.K.) |
| SWE | Swedish | English (U.K.) |
| USA | English (U.S.) | Arabic, Chinese (Simplified), Chinese (Traditional), French, Korean, Portuguese (Brazil), Russian, Spanish (Mexico), Vietnamese |

## Storefront Locale Fallback Assumption

Use this ASO planning assumption when deciding whether source-language search terms need coverage in a localized metadata workspace:

1. Prefer the storefront's default metadata locale.
2. Then use additional metadata locales Apple supports for that storefront.
3. Then assume the app's primary/default metadata locale can provide fallback coverage when storefront-specific metadata is missing.

This is a practical planning model based on Apple's supported storefront locales and app primary-language behavior, not an Apple-documented guarantee that search terms rank in this exact order or combine across locale fields. Validate important assumptions with ranking evidence when possible.

Examples:

- Germany (`DEU`): plan German first, English (U.K.) as supported secondary English coverage, then the app primary/default locale such as English (U.S.) if German or English (U.K.) metadata is missing.
- Netherlands (`NLD`): plan Dutch first, English (U.K.) as supported secondary English coverage, then the app primary/default locale if needed.
- Japan (`JPN`): plan Japanese first, English (U.S.) as supported secondary English coverage, then the app primary/default locale if different.

## Tool Country Or Region Derivation

Some ASO tools use two-letter country or region parameters while Apple lists three-letter ISO codes on the localization page. Derive the tool parameter when needed; do not store it as workspace state.

Common examples:

| Apple country or region ISO code | Tool parameter |
| --- | --- |
| AUT | AT |
| AUS | AU |
| BEL | BE |
| BRA | BR |
| CAN | CA |
| CHE | CH |
| CHN | CN |
| CZE | CZ |
| DEU | DE |
| DNK | DK |
| ESP | ES |
| FIN | FI |
| FRA | FR |
| GBR | GB |
| GRC | GR |
| HRV | HR |
| IDN | ID |
| IND | IN |
| ISR | IL |
| ITA | IT |
| JPN | JP |
| KOR | KR |
| MEX | MX |
| MYS | MY |
| NLD | NL |
| NOR | NO |
| PAK | PK |
| POL | PL |
| PRT | PT |
| ROU | RO |
| RUS | RU |
| SVK | SK |
| SVN | SI |
| SWE | SE |
| THA | TH |
| TUR | TR |
| TWN | TW |
| UKR | UA |
| USA | US |
| VNM | VN |

If the needed mapping is not in this reference, use a standard ISO 3166 lookup. If still uncertain, ask before fetching statistics or rankings.

## Prompt Resolution Examples

- `draft metadata for Germany` -> locale `German`, workspace `.agents/aso/locales/German/context.md`; derive `DEU`, then `DE` only when a statistics or ranking tool needs it.
- `draft metadata for German-speaking countries or regions` -> locale `German`; use `DEU` by default, or store `Country or region preference` such as `AUT`, `CHE`, or `LUX` when the user chooses a specific country or region.
- `draft metadata for US Spanish` -> locale `Spanish (Mexico)`, workspace `.agents/aso/locales/Spanish (Mexico)/context.md`, with `Country or region preference: USA`.
- `draft metadata for Spain` -> locale `Spanish (Spain)`, workspace `.agents/aso/locales/Spanish (Spain)/context.md`; mention `Catalan` only when evidence or user preference supports it.
