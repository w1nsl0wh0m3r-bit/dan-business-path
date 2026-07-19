# Consumer Brand Target Dashboard — Accuracy and Actionability Audit

**Date:** 2026-07-19  
**Scope:** `consumer-target-map.html`, its live ranked table, and the companion `consumer-porting-2026.html` thesis page  
**Decision standard:** named, operating, publicly evidenced opportunities with 1–10 units and a credible acquisition, JV, or rights path

## Executive verdict

The consolidated dashboard is now useful as a **research universe**, but the headline number should not be read as a target count. The audited page contains **238 records across 42 categories**. Only **26** clear the active-target gate; **142** are watch items and **70** are comps. The distinction matters: the prior page mixed named opportunities, operating comps, generic sourcing instructions, acquired assets, killed lanes, and large systems in one apparent pipeline.

The ranked table was the largest structural defect. It was a separate hardcoded list with stale unit counts/statuses and illustrative financial fields that could be mistaken for actual returns. It now renders directly from the same `TARGETS` records as the map, defaults to actionable consumer brands, and exposes evidence gaps and explicit comps instead of a synthetic “fastest money” ranking.

## Before / after

| Item | Before audit | After audit |
|---|---:|---:|
| Displayed universe | Stale “176 entries” subtitle; source described as 230 | 238 live records, counted at runtime |
| Active targets | Inflated by generic and unsupported rows | 26 gated active targets |
| Watch items | Mixed with targets | 142 |
| Comps / killed lanes | Mixed with targets | 70 |
| Publicly sourced records | Not surfaced | 168 (71%) |
| Records not publicly sourced | Not surfaced | 70 (48 unsupported + 22 internal-only) |
| Records without a usable unit count | Not surfaced | 32 |
| Pet records | Some remained visually live | All 25 are comps under the terminal pet-lane decision |
| Ranked table | Separate 30-row hardcoded dataset | Generated from the live universe |
| Financial ranking | Placeholder estimates presented comparatively | Removed; target economics are explicitly “not established” unless sourced |

Why 238 rather than 230: the consolidated source already contained five newly added records (PopUp Bagels, Baz Bagels, Federal Donuts, Mike’s Hot Honey, and Arcay Chocolates), and Jam Time was appended outside the base JSON. JOJU and Go Greek Yogurt were then added from the completed FDDIQ screen. A duplicate Sugar Shane’s record created during reconciliation was removed; the existing record was corrected instead.

## Material corrections executed

### 1. Governance and actionability

- Reserved `target` status for named, currently operating, publicly sourced 1–10-unit opportunities with conviction of at least 6.
- Demoted over-cap systems, acquired brands, generic franchisee classes, and unnamed lane hypotheses to comps or watch/sourcing instructions.
- Added explicit fields for `pipeline_type`, `evidence_state`, `next_action`, and `actionability_gate`.
- Converted the killed pet lane to comps with a narrow reopen rule; pet no longer inflates the pipeline.
- Rebuilt category filters and category counts dynamically so future additions cannot make the page headline stale.

### 2. Ranked-table reconciliation

- Removed the duplicate hardcoded brand dataset.
- Reconciled stale status and unit-count conflicts, including Jeff’s Bagel Run, ScandyCandy, Supermoon Bakehouse, Radio Bakery, Utopia, Third Culture, Sweet Hut, Sockerbit, Wanderlust Creamery, Saturday Morning/Swedish-candy names, and others surfaced by the audit.
- Replaced “Fastest Money” with **Top Evidence Gaps**. The former ranking depended on scenario placeholders, not verified target financials.
- Added filters for actionable names, all active targets, watch items, and explicit comps.

### 3. Important current-fact updates

| Name | Fix | Evidence basis | Implication |
|---|---|---|---|
| Jeff’s Bagel Run | 38 open shops; official locator lists 42 and company targets 50 | [Official locator](https://jeffsbagelrun.com/locations) | System benchmark / future franchisee-resale watch, not a 1–10-unit emerging-brand target |
| Ellianos Coffee | 85 stores | [Official July 2026 announcement](https://ellianos.com/blogs/blog/ellianos-coffee-now-open-in-regency-plaza-in-jacksonville-florida) | Comp only; far above mandate |
| Scooter’s Coffee | 900 stores | [Official February 2026 announcement](https://www.scooterscoffee.com/blog/post/900-stores-across-32-states-long-term-growth) | Comp only; source named franchisee resales separately |
| ScandyCandy | 3 open Florida stores; Sarasota in pipeline | [Official locator](https://scandycandy.store/pages/store-locator), [UTC Sarasota](https://utcsarasota.com/places/shop/scandycandy/) | JV watch; must prove repeat demand after novelty |
| Kids First Swim Schools | 21 locations across five states | [Official company page](https://kidsfirstswimschools.com/about/) | Comp; above mandate |
| SwimKids | Acquired by Emler | [Emler announcement](https://emlerswimschool.com/news/emler-swim-school-splashes-into-virginia-with-acquisition-of-swimkids-swim-schools/) | Transaction/operating comp only |
| LowCountry Swim School | One mobile operator | [Official site](https://lowcountryswimschool.com/) | Model mismatch; comp only |
| Sugar Shane’s | 3 stores, not 4; one canonical record | [Official site](https://sugarshanes.com/) | Watch until ownership/Founders Row scope is clear |

### 4. Missing high-signal names added

| Name | Current proof | Status | Required next step |
|---|---|---|---|
| JOJU | 6 live NYC locations | Target / JV candidate | Rebuild FDD Items 5–7, 19, and 20; prove manager-run four-wall economics. [Official locations](https://www.jojuny.com/locations) |
| Go Greek Yogurt | 4 live US locations, including Miami | Watch / franchise-rights screen | Reconstruct Item 19 cohorts and Boston/NY territory economics. [Official locations](https://gogreekyogurt.com/pages/locations) |

The rest of the 29-name FDDIQ screen was not bulk-added. Nineteen had unverified current live counts, and several had already grown above the 10-unit cap. Adding weakly verified names would increase the dashboard number without increasing decision value.

## What is actionable now

The dashboard’s decision queue should be read in this order:

1. **Starship Bagel** — finish the public proof-unit reconstruction; this is the best independent bagel path.
2. **Luxury repair acquisition screen** — Leather Spa, Rago Brothers, and Artbag lead; prove succession, craft-bench depth, mail-in throughput, and manager-run earnings.
3. **Jam Time** — reconstruct party-slot utilization, weekday economics, rent, and owner dependence.
4. **Layla Bagels** — advance only through a rights/economics/governance structure sprint.
5. **JOJU / Go Greek Yogurt** — fast-follow FDD and territory screens; neither has earned outreach yet.

## Remaining gaps and explicit deferrals

- **70 records are not publicly sourced:** 48 are unsupported and 22 rely only on internal source artifacts. They remain visible for research continuity but cannot rank as active targets.
- **32 records lack a verified unit count.** These should be resolved or archived during future lane-specific work.
- **Generic franchisee classes are not targets.** Scooter’s, BIGGBY, Tint World, and similar entries require a named 2–10-unit entity or package before promotion.
- **Bakery thesis:** not deferred; a separate July 19 thesis now exists at `reports/thesis-premium-bakery-platform-2026-07-19.md`. Its verdict is conditional: Cookie Society/Sunday Morning/Sugar Shane’s require manager-run economics and entry clarity before the lane moves ahead of bagels, luxury repair, or Jam Time.
- **No outreach was performed.** Founder, broker, FDD, and territory requests remain approval-gated.

## QA performed

- JavaScript syntax check passed with Node.
- Dataset audit passed: no duplicate IDs, no invalid active targets, all pet records are comps, and every active target clears the defined gate.
- The map and ranked table now consume the same live records.
- Companion thesis page was updated to remove stale pet/Jeff’s framing and incorporate luxury repair, Jam Time, JOJU, and Go Greek.

## Bottom line

The dashboard is now honest about what it is: **238 researched records, 26 active targets, and a short decision queue**. The most valuable change is not the eight net additions since the “230” snapshot. It is that filler, comps, and evidence gaps can no longer masquerade as actionable targets.
