# GOAL: Candy & Bagel Lane Revival — 4-Track Execution
## Date: 2026-07-19 | Owner: Hermes | Status: Executing

---

## Context

Dan's consumer multi-unit thesis centers on authentic founder-led food brands. Two lanes are priority: **bagels** (strong, 5 targets at conviction 8-10) and **candy** (dormant since June 19 PASS, now being revived). The main dashboard (`consumer-target-map.html`) has STALE candy unit counts — the dedicated candy map (`swedish-candy-map.html`) has 73 stores across 35 brands with full research, but the main map hasn't been synced.

Existing research assets:
- `swedish-candy-map.html` — 73 stores, 35 brands, live on GitHub Pages
- `swedish-candy-analysis.html` — full acquisition scorecard, landed-cost model, competitive taxonomy
- `swedish-candy/` — 39 comp profile pages with founder/origin/news/revenue data
- Reference docs: `swedish-candy-comp-profiles.md`, `us-candy-retail-landscape.md`, `swedish-candy-map-build.md`

## The 4 Tracks

### Track 1: Revive ScandyCandy
- ScandyCandy is at conviction 3 in the main dashboard — stale from June 19 PASS
- Actual data: 4 locations (Coconut Grove, Coral Gables, Palm Beach, Sarasota coming), founded 2024 by Calle & Wille Olsen (brothers from Helsingborg), viral demand (sold out in 9 days), SFL priority market
- Re-research current status, traffic, social growth, expansion signals
- Upgrade conviction if warranted, update main dashboard entry

### Track 2: Sync candy unit counts across dashboard
- Main dashboard has wrong counts: ScandyCandy (says 1, actual 4), BonBon (says 6-7, actual 7), Saturday Candy (says 2, actual 3), Sockerbit (says 2, actual 3)
- Lil Sweet Treat (12 units!) is entirely missing from main dashboard
- Pull correct counts from swedish-candy-map.html TABLE_ROWS and update consumer-target-map.html TARGETS array

### Track 3: Expand beyond Swedish candy — US artisan/specialty candy in NE/FL/DFW
- Research chocolatiers, artisan taffy/caramel/toffee, gummy/confection DTC, specialty candy retail
- Focus on founder-led, multi-unit, NE/NYC/FL/DFW
- Add qualified targets to main dashboard

### Track 4: Add FL + NE bagel targets
- Bagel lane is DFW/LA-heavy (Starship, Layla). Need authentic FL and NE bagel brands
- Research and add to dashboard

## Acceptance Criteria

1. ScandyCandy entry updated with current data + appropriate conviction
2. All candy entries in main dashboard have correct unit counts matching the candy map
3. At least 5 new non-Swedish candy targets researched and added (if qualified candidates exist)
4. At least 3 new FL/NE bagel targets researched and added (if qualified candidates exist)
5. Candy thesis report written (parallel to `thesis-premium-bagel-platform-2026-07-19.md`)
6. All changes committed and pushed
