---
title: Situation Room Board Surgery
date: 2026-07-19
status: complete
tags:
  - business-transition
  - situation-room
  - target-pipeline
---

# Situation Room Board Surgery — 2026-07-19

## Decision

The board is now an operator pipeline rather than a flat list of things that look interesting. The original embedded universe contained 175 entries across 27 categories; the party-first kids sprint subsequently imported Jam Time from prior research, bringing the live board to 176 entries: 60 active targets, 73 watch items and 43 operating comps. The prior hardcoded cards incorrectly showed 85 / 56 / 34 even though the embedded dataset actually contained 77 / 58 / 40 before this review.

The reduction to 60 active targets is intentional. Generic lane hypotheses, unnamed franchisee clusters, over-cap chains and stale internal-only pet names no longer count as actionable companies. The strongest current lanes remain visible, but category evidence is no longer confused with something Dan can pursue.

Dashboard: `/Users/winslow/Projects/dan-business-path/consumer-target-map.html`

Rollback copy: `/Users/winslow/Projects/dan-business-path/consumer-target-map.html.bak-sprint5-20260719`

## What changed

| Change | Before | After | Operator implication |
|---|---:|---:|---|
| Total universe | 175 embedded records | 176 pipeline entries | No records silently deleted; Jam Time imported from prior research |
| Active targets | 77 actual / 85 displayed | 60 actual and displayed | Generic, weak and over-cap entries removed from active count; Jam Time added |
| Watch | 58 actual / 56 displayed | 73 actual and displayed | Hypotheses and unverified names stay visible without masquerading as deals |
| Comps | 40 actual / 34 displayed | 43 actual and displayed | Bathhouse, Play Street Museum and Hyper Kidz moved to benchmark status |
| Publicly sourced | Not displayed | 145 / 176 (82%) | Evidence gap is now explicit |
| Needs public evidence | Not displayed | 31 | 20 unsupported plus 11 internal-only records |
| Pipeline classification | None | Eight explicit types | Separates acquisitions, JVs, rights, comps, watches and sourcing instructions |
| Next action | Inconsistent | Present on all 175 entries | Every live row has a concrete gate or sourcing instruction |

## Material judgment calls

1. **Bathhouse is a comp, not a target.** Its institutional capital and flagship build profile make it useful proof of demand but a poor fit for Dan's entry constraints. Sauna House and Urban Sweat remain JV/watch candidates.
2. **Dedicated padel remains gated.** Ultra Padel was demoted from target to watch. Epic remains a potential JV only if a real-estate/operator advantage appears.
3. **Luxury repair remains actionable.** Leather Spa, The Cobblers, Rago Brothers and Cobbler Concierge were normalized to their actual service footprint and classified as acquisition or JV candidates.
4. **Generic concepts no longer inflate the target count.** GLP-1 meal delivery, bottle-shop/sober-bar concepts, independent drive-through coffee, generic yoga/barre, IV lounges and IV/med-spa hybrids are watch-level sourcing instructions until a named 2–10-unit company is found.
5. **Internal-only pet names were demoted.** Poochies Dallas, Paws Fur Grooming Mobile, UrbanWagz, Puptown, Woofinwaggle and Brandyapple require current public verification before returning to active status. Happy K-9 was corrected to two locations with a public source and remains an acquisition screen.
6. **Bagel facts were refreshed.** Layla is now three Los Angeles locations; Starship and Layla have public sources and explicit JV gates.
7. **Party-first kids was corrected after the dedicated sprint.** Jam Time was imported as a four-unit Greater Boston acquisition/JV screen. Play Street Museum (30+) and Hyper Kidz (18+) were corrected and moved to comps because they violate the 1–10-unit mandate.

## Classification rules

- `acquisition_target`: named operating company where buying the entity or assets is the plausible entry.
- `jv_candidate`: named operator where territory, licensing, development or operating partnership is the likely structure.
- `franchise_rights`: a named franchise or franchisee-entity path, not a generic category.
- `operating_target`: named company that passes the current active screen but whose entry structure is not yet resolved.
- `watchlist`: named company or concept that needs a gating fact before diligence.
- `operating_comp`: proof point retained for economics, buzz or format comparison; not counted as actionable.
- `lane_hypothesis` / `sourcing_instruction`: a research direction that must produce a named 2–10-unit operator.

## Evidence-state rules

- `verified_public`: at least one recorded HTTP(S) source. This confirms that a public evidence trail exists; it does not certify every field.
- `internal_only`: the only evidence is a prior internal memo or non-link note.
- `unsupported`: no source is recorded in the embedded dataset.

This distinction matters: the 82% sourced score is a coverage measure, not a claim that 82% of all operating facts are freshly verified. Unit counts and ownership can still change and should be refreshed before outreach.

## Test evidence

| Test | Result | Evidence |
|---|---|---|
| Runtime dataset reconciles | Pass | 176 unique records after one audited import; no duplicate IDs or names |
| Inline JavaScript syntax | Pass | `new Function()` compile test |
| Dynamic status reconciliation | Pass | 60 target / 73 watch / 43 comp = 176 |
| Evidence reconciliation | Pass | 145 public / 11 internal / 20 unsupported = 176 |
| Browser render | Pass | 176 table rows rendered in Chrome from local file |
| Evidence filter | Pass | Unsupported filter returns 20 rows |
| Target filter | Pass | Target filter returns 61 rows |
| Corrected facts | Pass | Browser shows Layla 3, Happy K-9 2 and Leather Spa 7 footprint points |
| Source rendering | Pass | HTTP sources render as links; internal notes render as plain text |
| Rollback path | Pass | Pre-surgery HTML copy retained beside dashboard |

## Residual gaps

- Twenty records have no recorded source and eleven rely only on internal research. They are visible in the red evidence queue rather than silently trusted.
- Several financial fields remain directional proxies with low or medium confidence; this sprint fixed pipeline semantics, not every underwriting assumption.
- `last_verified` is only populated where the record already carried an update date. A future sourcing pass should timestamp individual facts, not merely records.
- The dashboard is a single-file artifact with manual overrides. A future refactor should move the dataset and audit log into separate structured files, but that is not required to use the board now.

## Next action

Use the evidence filter as the cleanup queue. Do not add any new “target” unless it is a named company with public evidence, an explicit pipeline type and a concrete next action. The next business sprint should use this stricter standard when screening party-first kids/family operators.
