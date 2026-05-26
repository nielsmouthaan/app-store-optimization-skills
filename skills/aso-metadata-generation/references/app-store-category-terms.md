# App Store Category Terms

Use this list when evaluating category/free words in App Store metadata. Category terms are often low-priority candidate keywords because the app's category can already provide contextual relevance, but they may still be useful in visible metadata when they clarify the app.

## App Store Categories

```text
books
business
developer tools
education
entertainment
finance
food & drink
games
graphics & design
health & fitness
lifestyle
kids
magazines & newspapers
medical
music
navigation
news
photo & video
productivity
reference
safari extensions
shopping
social networking
sports
stickers
travel
utilities
weather
```

## Normalized Category Tokens

Use these single-word tokens after normalizing candidate metadata words. They make multi-word category names comparable to individual words in the app name, subtitle, and keywords. For example, `Health & Fitness` becomes `health` and `fitness`, and `Photo & Video` becomes `photo` and `video`.

```text
book
books
business
developer
developers
development
design
drink
education
educational
entertainment
finance
financial
fitness
food
game
games
graphics
health
kids
lifestyle
magazine
magazines
medical
music
navigation
news
newspaper
newspapers
photo
photos
productivity
reference
safari
shopping
social
sport
sports
sticker
stickers
tools
travel
utilities
utility
video
weather
```

## Games Subcategory Tokens

```text
action
adventure
board
card
family
music
puzzle
racing
role
playing
simulation
sports
strategy
```

## Usage Notes

- Do not automatically block category terms.
- Deprioritize category terms in keywords when stronger app-specific words are available.
- Allow category terms in app name or subtitle when they help users understand what the app is.
- Treat the app's own primary category as especially likely to be a free or low-priority keyword.
