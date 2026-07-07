# Platforms

Use this reference when an ASO skill needs to interpret App Store Connect metadata platforms, concrete search surfaces, or tool-specific platform aliases.

## Core Terms

| Term | Meaning |
| --- | --- |
| `Platforms` | App Store Connect metadata platforms where app information and `Keywords` fields are managed. Use these values in `.agents/aso/context.md`. |
| Search surface | Concrete App Store ranking, statistics, or device surface used by a tool. Use only at tool-call time or when the user explicitly requests a preference. |
| Tool alias | The platform value required by a specific ASO tool or API. Map from `Platforms` or a search surface at tool-call time; do not store tool aliases as canonical context. |

## Platforms

Use only these values in the context `**Platforms:**` field:

| Platform | Notes |
| --- | --- |
| iOS | App Store Connect platform for iPhone and iPad apps. |
| macOS | App Store Connect platform for Mac apps. |
| tvOS | App Store Connect platform for Apple TV apps. |
| visionOS | App Store Connect platform for Apple Vision Pro apps. |

## Search Surfaces

Use search surfaces only for rankings, statistics, or tool parameters.

| Search surface | Platform | Typical tool aliases |
| --- | --- | --- |
| iPhone | iOS | `iphone`, `ios`, `software` |
| iPad | iOS | `ipad`, `iPadSoftware` |
| Mac | macOS | `mac`, `macos`, `desktopSoftware`, `macSoftware` |
| Apple TV | tvOS | `appletv`, `tvos` |
| Vision | visionOS | `vision`, `visionos` |

## Selection Rules

- `Platforms` determines which App Store Connect `Keywords` fields may be generated, saved, or published.
- Do not store a primary search surface by default.
- If an ASO tool requires an iPhone or iPad surface for iOS statistics or rankings and the user has not explicitly requested iPad, use iPhone.
- If the user explicitly requests iPad-based statistics or rankings, store `**Search surface preference:** iPad` in `.agents/aso/context.md` and reuse it for later statistics and ranking calls until the user changes it.
- Do not use `Search surface preference` to decide which `Keywords` fields exist. `Keywords` fields are based on `Platforms`.
