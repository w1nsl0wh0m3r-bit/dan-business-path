# Dan's Business Path Decision Dashboard

Static private dashboard for choosing between **Services** and **Multi-Unit** business arenas, then selecting the right entry path: **DIY / Build**, **Franchise**, or **Acquisition / Buy**.

Live page: <https://w1nsl0wh0m3r-bit.github.io/dan-business-path/>

## Current product direction

This is now meant to be a weekly **decision cockpit**, not just a ranked catalog. The top of the page should answer:

1. What is on the active shortlist?
2. What stage is each idea in?
3. What did Dan/Winslow/Hermes do last?
4. What changed since the last review?
5. Which rankings are suspect because the idea/path scores disagree?

The full 179-row universe remains reference material below the cockpit. On 2026-05-22, a gap scan against Obsidian brainstorming added 15 missing categories across compliance micro-routes, property/estate services, resilience services, and distressed acquisition theses, then 6 niche DIY/build-testable categories and 10 trend/buzz-sourced categories with score support.

## Architecture

1. **Services** — route-based/local recurring businesses where the scarce assets are customer books, technicians, licenses, reviews, route density, and local trust. Usually acquisition-first, franchise-second, DIY only selectively.
2. **Multi-Unit** — consumer retail, food/beverage, education, wellness, specialty trade retail, and repeatable unit concepts. More DIY potential because Dan can create the brand, site-selection logic, product, content, and operating playbook.

Within each arena, every opportunity is evaluated by entry path.

## Operating fields

The original catalog fields remain embedded in `index.html`, but the cockpit normalizes them into operating concepts:

- **Status**: collapsed to `Pursue / Screen / Watch / Kill` for filtering. Micro-statuses stay in the row detail.
- **Diligence stage**: `None → Researching → Calling → LOI/Term → Dead`.
- **Shortlist**: local star flag. Defaults to Pursue items and high-scoring eligible items.
- **This week’s action**: local text note for what happened last.
- **Memo / notes link**: local URL/path field for diligence docs.
- **Score gap flag**: highlights entries where Overall Score `<3.0` but selected path fit `>=4`; these are “easy to do, not necessarily worth doing.”
- **Path logic flag**: highlights entries where `BestPath=Acquisition` but `Acquisition <= 2`.
- **Metric rationale hover**: each 1–5 sub-score now has a hover tooltip explaining what the score means and pulling the most relevant row rationale — thesis, why, geography, AI edge, financing risk, or kill criteria.

Cockpit state is stored in browser `localStorage` under `danBusinessPathCockpit.v1`; it is not yet synced back to the repo.

## Scoring model

Each row has 12 attractiveness metrics scored 1–5:

- demand_quality
- growth_tailwinds
- recurrence_frequency
- unit_economics
- financeability
- scaling_ease
- competitive_whitespace
- ai_digital_value_add
- target_geography_fit
- dan_fit
- exit_upside
- downside_protection

Path fit is separate:

- `DIY`
- `Franchise`
- `Acquisition`
- `PathFitSubtotal`
- `SelectedPathFit`

`OverallScore`/`Score` should represent category attractiveness independent of path. `SelectedPathFit` should represent whether the recommended path is actually executable.

## Updating

The catalog is embedded as JSON in `index.html`. Update rows directly for now or regenerate from research CSVs in `~/.openclaw/workspace/research/`.

Recommended next refactor: extract the embedded catalog to `catalog.json`, CSS to `style.css`, and cockpit/rendering logic to `app.js`. Keep the current single-file version until deployment constraints are confirmed because direct `file://` use does not reliably support `fetch()`.

## Local use

Open `index.html` directly in a browser. No build step, framework, or dependencies beyond optional Google Fonts.

## Deployment

Commit locally and push only after Dan approves.
