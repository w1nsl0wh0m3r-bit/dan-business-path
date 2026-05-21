# Dan's Business Path Decision Dashboard

Static private dashboard for choosing between **Services** and **Multi-Unit** business arenas, then selecting the right entry path: **DIY / Build**, **Franchise**, or **Acquisition / Buy**.

## Design direction

The page is intentionally styled like a clean strategy placemat / drawing board: warm paper, graphite ink, muted blueprint blue, clay accents, tactile cards, and filterable catalog tables. It should feel like something worth revisiting weekly, not a generic web dashboard.

## Architecture

1. **Services** — route-based/local recurring businesses where the scarce assets are customer books, technicians, licenses, reviews, route density, and local trust. Usually acquisition-first, franchise-second, DIY only selectively.
2. **Multi-Unit** — consumer retail, food/beverage, education, wellness, specialty trade retail, and repeatable unit concepts. More DIY potential because Dan can create the brand, site-selection logic, product, content, and operating playbook.

Within each arena, every opportunity is evaluated by entry path.

## Updating

The catalog is embedded as JSON in `index.html`. Update rows directly or regenerate from research CSVs in `~/.openclaw/workspace/research/`.

## Local use

Open `index.html` directly in a browser. No build step, framework, or dependencies beyond optional Google Fonts.

## Deployment

Commit locally and push only after Dan approves.
