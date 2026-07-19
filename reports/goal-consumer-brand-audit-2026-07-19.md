# GOAL: Consumer Brand Dashboard Audit & Gap Fill
## Created: 2026-07-19 | For: Winslow | Priority: High

---

## Objective

Review the consolidated consumer brand target dashboard (230 targets + ranked table) for accuracy, completeness, and actionability. Identify what needs to be added, fixed, or updated. Execute the fixes.

**Live dashboard:** https://w1nsl0wh0m3r-bit.github.io/dan-business-path/consumer-target-map.html
**Repo:** `/Users/winslow/Projects/dan-business-path/`
**Commit:** `6ef872c`

---

## Context — What Was Just Done

The dashboard was rapidly expanded across 3 sessions:
1. **Candy revival** (commit `ea33066`) — ScandyCandy conviction 3→7, unit counts corrected (ScandyCandy 1→4, BonBon 7, Saturday Candy 3, Sockerbit 3), Li-Lac Chocolates + Sweet Pete's added, candy thesis written
2. **Frozen dessert expansion** (commits `ada1c7b`, `849d829`) — Handel's, Crumbl multi-unit resale, Graeter's, McConnell's, Figo Il Gelato added. Froyo killed. Salt & Straw / Jeni's / Van Leeuwen killed (PE).
3. **Consolidation** (commit `6ef872c`) — 27 new targets from emerging pipeline added. Ranked consumer brand table (30 entries) added below the map.

**Total: 203 → 230 targets.**

---

## What to Review (5 Tracks)

### Track 1: Data Accuracy Audit
**Scope:** The 27 targets added from the emerging pipeline were bulk-imported with placeholder financials and estimated coordinates. Several may have wrong unit counts, stale status, or incorrect geocoding.

Check these specifically:
- **Unit counts** — Dan already flagged some are wrong. Spot-check the Swedish candy brands against current websites/Instagram. ScandyCandy was corrected from 1→4; others may be equally stale.
- **Status labels** — Several "watch" entries from the emerging pipeline may warrant "target" promotion (or vice versa). Apply the thesis filter: authentic founder-led, 1-10 units, NE/NYC/FL/DFW priority.
- **Geocoding** — Bulk import used city-level approximations. NYC entries should have precise neighborhood coordinates.
- **Conviction scores** — The 27 new entries all got default scores (3-4). Adjust based on thesis fit.

### Track 2: Completeness Gap Analysis
**Scope:** Cross-reference the dashboard against ALL source files to find consumer brands that should be on the board but aren't.

Sources to cross-check:
- `index.html` — 326-entry master CORPUS (filter for Family = "Consumer Food Brand", Arena = "Multi-Unit")
- `emerging-multi-unit-pipeline.html` — 161 entries (we pulled 27; are there more in priority markets?)
- `deep-dives/ice-cream-frozen-yogurt-shaved-ice.md` — verdict was "NO-GO" for ice cream; is this still right given Handel's addition?
- `deep-dives/premium-dessert-soft-serve-gelato.md` — verdict was "CONDITIONAL GO"; are all named brands on the dashboard?
- `swedish-candy/` directory — full comp profiles exist; are all mapped?
- Obsidian vault: `/Users/winslow/Documents/Business-Research/Business Transition Engine/` — any research not reflected?

### Track 3: Thesis Consistency Check
**Scope:** Dan has corrected scope THREE times in recent sessions. Verify every target on the dashboard fits the refined thesis:

**IN-SCOPE (keep):**
- Authentic founder-led consumer brands
- 1-10 units (small enough to acquire/control)
- Food/consumer categories: bagels, candy, gelato, ice cream, bakery, cookies, frozen dessert
- NE/NYC/FL primary, DFW secondary (others = watch/comp only)
- Real estate component = plus but not required
- High cash-on-cash potential

**OUT-OF-SCOPE (flag for removal or status downgrade):**
- PE-owned or PE-backed brands (7 Brew, Bathhouse, Othership, Padel Haus, etc. — already killed but verify no stragglers)
- Heavy industrial / B2B / route services (propane, HVAC, building materials)
- Car wash platforms, pet roll-ups, medspa roll-ups (too PE-focused)
- Brands outside priority markets with no expansion path to NE/NYC/FL/DFW
- Franchise systems >50 units unless franchisee-resale viable (Crumbl is the exception)

Flag any targets that don't fit. Don't delete — mark as `comp` or `killed` with a note.

### Track 4: Ranked Table Quality
**Scope:** The new table below the map has 30 entries. The original index.html had 20 ranked (with rank #4 missing — it was removed at some point). Check:

- Are the scores accurate? Several were carried over from the May/June analysis and may be stale.
- Should the table include MORE than 30? We have 230 targets on the map — the table only shows the curated top 30. Is that the right cutoff?
- Should the table pull live from TARGETS (the map data) instead of being a hardcoded BRAND_DATA array? Right now they're separate — if you update one, the other goes stale.
- Missing columns? Dan might want: founded year, founder name, est. revenue, last-known funding status.

### Track 5: Missing Thesis Work
**Scope:** Three thesis reports exist. Are there gaps?

Existing:
- `thesis-premium-bagel-platform-2026-07-19.md` ✓
- `thesis-premium-candy-platform-2026-07-19.md` ✓ (just written)
- `thesis-frozen-dessert-platform-2026-07-19.md` ✓ (just written)

Missing:
- **Bakery thesis** — we now have 12+ bakery targets (Cookie Society, Sunday Morning, Radio Bakery, Sweet Hut, Sugar Shane's, Third Culture, Supermoon, Lysée, Win Son, Mah-Ze-Dahr, La Cabra, etc.). No thesis written for this lane.
- **Coffee thesis** — Ellianos, Jeeves, Scooter's, BIGGBY are on the board. No thesis.
- **Priority market map** — which targets are actually in NE/NYC/FL/DFW vs elsewhere? A geographic concentration view.

---

## Execution Rules

1. **Fix as you go.** If you find a wrong unit count, fix it. Don't just flag it.
2. **Commit after each track.** Use clear commit messages.
3. **Update the table to pull from TARGETS live** rather than hardcoded BRAND_DATA if feasible — single source of truth.
4. **Don't add targets outside the thesis.** If you find something interesting but off-thesis, note it in a separate file, not the dashboard.
5. **Ask Dan only if** there's a genuine judgment call about scope. Otherwise use the refined thesis above.
6. **Backup before bulk edits.** `cp consumer-target-map.html consumer-target-map.html.bak-pre-audit-YYYYMMDD`

---

## Deliverables

1. **Audited dashboard** — corrected data, consistent thesis, accurate counts
2. **Gap log** — what was found missing and added (or noted for later)
3. **Updated ranked table** — accurate scores, live data if possible, right columns
4. **Bakery thesis** (if the lane warrants it — 12+ targets suggests yes)
5. **HANDOFF.md entry** summarizing what was fixed

---

## Acceptance Criteria

- [ ] Every target on the dashboard fits the refined consumer-brand thesis
- [ ] Unit counts spot-checked against current sources for top 20 targets
- [ ] No stale conviction scores on targets Dan would actually pursue
- [ ] Ranked table is accurate and ideally pulls from live TARGETS data
- [ ] Any bakery thesis gap is addressed (written or explicitly deferred with reason)
- [ ] All changes committed and pushed
- [ ] HANDOFF.md updated with summary
