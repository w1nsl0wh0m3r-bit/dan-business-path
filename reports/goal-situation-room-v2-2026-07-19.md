# GOAL: Situation Room V2 — Harden, Rank, Expand

## Mission
Transform the 152-entry consumer target map from a list into a decision-grade diligence tool. Add scoring, financial modeling, urgency tracking, and 5 missing buzzy high-cash-on-cash lanes. Make the dashboard self-explanatory for Dan.

## Context
The current map (consumer-target-map.html) has 152 targets across 22 categories. It was just expanded from 112→152 by applying Winslow's t904 senior-operator review. But it's still a flat list with no scoring, no financial data, no timing urgency, and 5 major buzzy categories completely missing.

## Deliverables

### 1. SCORING SYSTEM (add to every target)
Add these fields to each target entry:
- `conviction_score` (1-10): How well does this fit Dan's profile + thesis?
- `cash_on_cash_potential` (1-5): Likelihood of >25% annual cash-on-cash return
- `time_to_revenue` (months): How fast could this generate cash flow?
- `entry_difficulty` (1-5): 1=easy (write a check), 5=hard (build from scratch)
- `check_size` ($K): Estimated capital required for first meaningful position
- `urgency` (high/medium/low): Is there a closing window? (founder aging, distress, capital need, category inflection)

Scoring rubric for conviction_score:
- 9-10: Dan could do this tomorrow, fits all criteria, high return potential
- 7-8: Strong fit, one question mark
- 5-6: Interesting but needs more diligence
- 3-4: Comp or watch, not ready
- 1-2: Park

### 2. FINANCIAL PROXY MODEL (for top 30 targets)
For each of the top 30 by conviction_score, add:
- `est_revenue_low` / `est_revenue_high` ($K/yr per unit)
- `est_margin_pct` (gross margin %)
- `est_sde_range` ($K low-high per unit)
- `est_capex_per_unit` ($K)
- `est_payback_months` (simple payback)
- `model_confidence` (low/medium/high)

### 3. FIVE MISSING BUZZY HIGH-RETURN LANES

#### Lane 8: GLP-1 / Weight-Loss Adjacent Services
The single biggest consumer health shift of our lifetime. 15%+ of US adults on GLP-1 drugs by 2027. The drug makers capture the pharmacology, but the SERVICES around GLP-1 — nutrition coaching, muscle-preservation training, body-contouring/loose-skin services, meal delivery, psychological support — are wide open. Dan could acquire or build a tech-enabled service layer.
- Targets: weight-loss coaching platforms, body-contouring/med-spa operators, GLP-1-adjacent nutrition services, muscle-preservation fitness concepts, meal-delivery services targeting GLP-1 users
- Why high CoC: massive demand wave, low service infrastructure, recurring membership model, affluent user base
- Why ground floor: the services layer barely exists — most GLP-1 patients get the drug and zero support

#### Lane 9: Non-Alcoholic / "Sober Social" Bars & Bottle Shops
Gen Z drinking at historic lows. NA beverage market exploding. NA bottle shops and sober bars are appearing in NYC, LA, Austin. Social infrastructure for the sober-curious is a real white-space — the "third place" without alcohol.
- Targets: NA bottle shops (Boisson successor, wilderness of NA brands), sober bars (Listen Bar, Getaway-style), NA-bev cafes, adaptogen/functional beverage bars
- Why high CoC: low COGS (NA bevs are cheap), high margin on mocktails, membership model, cultural tailwind
- Why ground floor: almost zero national operators; category just crossed from niche to mainstream

#### Lane 10: Drive-Thru Premium Coffee
7 Brew (244% growth, Blackstone-backed), 7 Brew, Dutch Bros, Ellianos. The drive-thru coffee model is the highest-unit-economics QSR format. 7 Brew is growing insanely fast but you can still get territories. Low capex, daily repeat, high margin, scalable.
- Targets: 7 Brew franchisee/area dev, Dutch Bros franchisee economics, Ellianos territories, independent drive-thru coffee operators, Smileans/Scooter's franchisee
- Why high CoC: $300-600K capex, $1.5-2.5M revenue, 20-30% margins, 18-30 month payback
- Why ground floor: 7 Brew is pre-national; you can still get major territories

#### Lane 11: Pilates Reformer / Boutique Fitness Resales
Pilates reformer market: $7.65B (2025) → $16.81B (2035). Club Pilates has 800+ units. But the opportunity is acquiring independent studios or franchisee clusters. Reformer equipment is the moat ($5-15K per reformer × 10-15 per studio). Membership model, affluent demographic, recurring revenue.
- Targets: independent Pilates reformer studios (2-5 unit), Club Pilates franchisee clusters, Solidcore/SLT franchisee-adjacent, boutique barre/Pilates hybrids
- Why high CoC: $200-400K all-in, $400-700K revenue, 30%+ margins, 24-36mo payback
- Why ground floor: thousands of independent studios with aging founders, franchisee succession

#### Lane 12: IV Hydration & Recovery Lounges
IV hydration market $2.8B (2025), growing fast. Prime IV at 208 locations, $100M revenue. Fusions, IVme, Hydrafinity. The model is simple: nurse + space + supplies + memberships. Low capex, recurring revenue, wellness positioning, affluent demographic. Can be bolted onto med-spa or gym.
- Targets: Prime IV franchisee, independent IV lounges, Hydrafinity, IV/med-spa hybrids, recovery lounge concepts
- Why high CoC: $190-630K all-in, $500K-1M+ revenue, high margins on the actual IV (supplies are cheap), 18-30mo payback
- Why ground floor: only ~500-800 locations nationally; thousands of markets unserved

### 4. RANKING TABLE
After scoring all 152+ targets, produce a force-ranked table:
- Top 20 by conviction_score
- Top 10 by cash_on_cash_potential × time_to_revenue (fastest money)
- Top 10 by urgency (closing windows)
- Bottom 20 to kill/cut (lowest conviction + lowest return)

### 5. MAP UX ENHANCEMENTS
Add to the HTML dashboard:
- Sortable table view (by conviction, by CoC, by urgency, by check size)
- Filter by category AND status AND check_size range
- Color-coded conviction scores (green 8-10, yellow 5-7, red 1-4)
- "Top 20" and "Kill List" quick-filter buttons
- Summary cards at top: Total targets, Avg conviction, Avg check size, # high-urgency
- Compact card view vs map view toggle

### 6. DATA QUALITY PASS
For every target with `model_confidence: low`, flag it with a visible badge. No target should have empty buzz_signals, sources, or first_diligence after this pass.

## Execution Rules
- No outreach, no spend, no external messages, no logins
- All financial estimates are PROXIES, not diligence — label as such
- Backup before changes
- Save final report to workspace + Obsidian mirror
- Commit and push
