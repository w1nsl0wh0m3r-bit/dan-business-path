# Dan's Business Path Decision Dashboard

Static private dashboard for choosing between **Services** and **Multi-Unit** business arenas, then selecting the right entry path: **DIY / Build**, **Franchise**, or **Acquisition / Buy**.

Live page: <https://w1nsl0wh0m3r-bit.github.io/dan-business-path/>

## Pages

### index.html — Strategy Dashboard
The main catalog and ranking surface. Sections from top to bottom:

1. **Arenas** — Services vs Multi-Unit posture definitions
2. **2×3 Matrix** — which entry path fits each arena
3. **Strategic Take** — current priority wedge and narrative
4. **Highest-Ranked Opportunities** — top 15 from live DATA (posture-aware, suppresses DefaultRankEligible=false)
5. **Full Category Universe** — filterable table (arena, path, market, search) with expandable score drawers
6. **Ranked by Arena + Path** — reference view: top 10 per cell

All ranking sections derive from the embedded `DATA` array at runtime. The hardcoded table rows in the HTML serve as fallback content before JS loads and are replaced by `render()`.


### underwriting.html — Economic Underwriting Dashboard
Separate diligence-grade version for vetting categories economically. It keeps the 179-row universe but re-sorts around `UnderwritingScore` and `UnderwritingVerdict`, with proof/risk columns for unit economics, recurrence, financeability, downside, path fit, theme tags, and economic detail drawers. This is the decision-quality view for “what would need to be true?” rather than browsing themes.

### operating.html — Operating Layer (Weekly Cockpit)
Separate page focused on weekly operating decisions, not catalog browsing. Features:

- **Shortlist** — starred items from across the catalog
- **Pipeline lanes** — None → Researching → Calling → LOI/Term → Dead
- **Per-card controls** — diligence stage, weekly action note, memo link
- **Stats bar** — shortlist count, status distribution, gap flags, logic flags
- **Dynamic change log** — shows last-touched items and live flag counts
- **Back-links** — each card links to the full detail view on index.html

Cockpit state is stored in browser `localStorage` under `danBusinessPathCockpit.v1`.

## Current product direction

This is a weekly **decision cockpit**, not just a ranked catalog. The operating layer (operating.html) answers:

1. What is on the active shortlist?
2. What stage is each idea in?
3. What did Dan do last?
4. What changed since the last review?
5. Which rankings are suspect because the idea/path scores disagree?

The full 179-row universe remains reference material in index.html.

## Architecture

1. **Services** — route-based/local recurring businesses where the scarce assets are customer books, technicians, licenses, reviews, route density, and local trust. Usually acquisition-first, franchise-second, DIY only selectively.
2. **Multi-Unit** — consumer retail, food/beverage, education, wellness, specialty trade retail, and repeatable unit concepts. More DIY potential because Dan can create the brand, site-selection logic, product, content, and operating playbook.

Within each arena, every opportunity is evaluated by entry path.

## Operating fields

The original catalog fields remain embedded in `index.html`, but the cockpit normalizes them into operating concepts:

- **Status**: collapsed to `Pursue / Screen / Watch / Kill` for filtering. Micro-statuses stay in the row detail.
- **Diligence stage**: `None → Researching → Calling → LOI/Term → Dead`.
- **Shortlist**: local star flag. Defaults to Pursue items and high-scoring eligible items.
- **This week's action**: local text note for what happened last.
- **Memo / notes link**: local URL/path field for diligence docs.
- **Score gap flag**: highlights entries where Overall Score `<3.0` but selected path fit `>=4`; these are "easy to do, not necessarily worth doing."
- **Path logic flag**: highlights entries where `BestPath=Acquisition` but `Acquisition <= 2`.
- **Metric rationale hover**: each 1–5 sub-score has a hover tooltip explaining what the score means and pulling the most relevant row rationale — thesis, why, geography, AI edge, financing risk, or kill criteria. On mobile, tap to expand.

Cockpit state is stored in browser `localStorage` under `danBusinessPathCockpit.v1`; it is not synced back to the repo.

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

`OverallScore`/`Score` represents category attractiveness independent of path. `SelectedPathFit` represents whether the recommended path is actually executable. Both fields should always be equal (`Score` is kept for backward compatibility).

## DATA consistency

Both `index.html` and `operating.html` embed the full DATA array. When updating categories or scores, **both files must be updated together.** The recommended refactor (extract to `catalog.json`) remains deferred because `file://` use does not reliably support `fetch()`.

## Updating

The catalog is embedded as JSON in both HTML files. Update rows directly for now or regenerate from research CSVs in `~/.openclaw/workspace/research/`.

## Local use

Open `index.html` directly in a browser. No build step, framework, or dependencies beyond optional Google Fonts.

## Deployment

Commit locally and push. GitHub Pages serves from the default branch.

## Changelog

- **2026-05-22**: Product-quality pass. Synced DATA across both files (operating.html was stale with 179/179 score mismatches). Fixed render() sort to use `OverallScore||Score`. Fixed rank() display. Added mobile scroll hints on catalog table. Made operating.html change log dynamic. Added back-links from cockpit cards to catalog detail. Updated stale copy (category count, footer date).
