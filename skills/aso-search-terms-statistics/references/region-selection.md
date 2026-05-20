# Region Selection Reference

Use this reference to choose the App Store region for popularity and difficulty statistics when `.agents/aso-context.md` has a `Search language` but no `Search region`.

Apple's App Store localization reference is the authority for which languages are supported in which countries or regions:

https://developer.apple.com/help/app-store-connect/reference/app-information/app-store-localizations/

## Selection Rules

- User-provided `Search region` always wins.
- Store region codes as uppercase ISO 3166-1 alpha-2 codes, such as `US`, `NL`, or `DE`.
- Prefer the country or region where Apple treats the language as a default or primary localization.
- If the language has a regional variant, honor it: `English (UK)` -> `GB`, `French (Canada)` -> `CA`, `Portuguese (Brazil)` -> `BR`.
- If the language is shared across several major App Store regions and context gives no market clue, ask the user rather than silently picking a storefront.
- Use `US` only for unspecified English or when context clearly targets the United States.
- If the preferred region is unsupported by the selected tool, try another region that still makes sense for the language and app context. If no sensible fallback is clear, ask the user before fetching.

## Common Defaults

| Search language in context | Preferred region | Notes |
| --- | --- | --- |
| Arabic | SA | Use another Arabic-speaking region only when context identifies it. |
| Bangla | BD | Use `IN` if context targets India. |
| Catalan | ES | Catalan App Store localization maps to Spain. |
| Chinese, Simplified Chinese | CN | Use `SG` only when context targets Singapore. |
| Chinese Traditional, Traditional Chinese | TW | Use `HK` only when context targets Hong Kong. |
| Croatian | HR |  |
| Czech | CZ |  |
| Danish | DK |  |
| Dutch | NL | Use `BE` only when context targets Belgium. |
| English | US | Use a regional English variant when known. |
| English Australia | AU |  |
| English Canada | CA |  |
| English UK, English United Kingdom | GB |  |
| Finnish | FI |  |
| French | FR | Use `CA` for French Canada. |
| French Canada | CA |  |
| German | DE | Use `AT` or `CH` only when context targets Austria or Switzerland. |
| Greek | GR |  |
| Gujarati | IN |  |
| Hebrew | IL |  |
| Hindi | IN |  |
| Hungarian | HU |  |
| Indonesian | ID |  |
| Italian | IT |  |
| Japanese | JP |  |
| Kannada | IN |  |
| Korean | KR |  |
| Malay | MY |  |
| Malayalam | IN |  |
| Marathi | IN |  |
| Norwegian | NO |  |
| Odia | IN |  |
| Polish | PL |  |
| Portuguese | PT | Use `BR` only when context targets Brazil or Brazilian Portuguese. |
| Portuguese Brazil | BR |  |
| Portuguese Portugal | PT |  |
| Punjabi | IN | Use `PK` only when context targets Pakistan. |
| Romanian | RO |  |
| Russian | RU |  |
| Slovak | SK |  |
| Slovenian | SI |  |
| Spanish | ES |  |
| Spanish Mexico, Latin American Spanish | MX |  |
| Spanish Spain | ES |  |
| Swedish | SE |  |
| Tamil | IN |  |
| Telugu | IN |  |
| Thai | TH |  |
| Turkish | TR |  |
| Ukrainian | UA |  |
| Urdu | PK | Use `IN` if context targets India. |
| Vietnamese | VN |  |

## When In Doubt

Use the Apple reference page to confirm whether the language is available in the candidate country or region. If the language is available in several plausible regions and the app context does not identify a market, ask the user for `Search region` and save the answer in `.agents/aso-context.md`.
