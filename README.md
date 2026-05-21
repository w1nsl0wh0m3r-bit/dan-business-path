# Dan's Business Path Decision Dashboard

Static private dashboard for choosing between two arenas and three entry paths.

## Architecture

The dashboard is organized around Dan's actual opportunity set:

1. **Services** — route-based/local recurring businesses where the scarce assets are customer books, technicians, licenses, reviews, route density, and local trust. These usually skew **acquisition first**, **franchise second**, **DIY only selectively**.
2. **Multi-Unit** — consumer retail, food/beverage, education, wellness, specialty trade retail, and other repeatable unit concepts. These have more **DIY** potential because Dan can create the brand, site-selection logic, product, content, and operating playbook.

Within each arena, every opportunity is evaluated by entry path: **DIY / Build**, **Franchise**, or **Acquisition / Buy**.

## Updating

The catalog is embedded as JSON in `index.html`. Update rows directly or regenerate from research CSVs in `~/.openclaw/workspace/research/`.

## Local use

Open `index.html` directly in a browser. No build step, framework, or dependencies.

## Deployment

Commit locally and push only after Dan approves.
