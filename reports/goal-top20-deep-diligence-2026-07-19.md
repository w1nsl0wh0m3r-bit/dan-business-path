# GOAL: Top 20 Deep Diligence Sprint — Situation Room V2

## Mission
Apply `/sherlock` + `/ddacquire` grade OSINT and acquisition diligence to the Top 20 conviction targets from the Situation Room map. For each target, verify ownership, assess acquisition feasibility, model economics, and produce a decision-grade dossier. Update the map with findings.

## Context
The Situation Room V2 map has 175 scored targets. The Top 20 by conviction have been identified but lack deep diligence. Several may already be PE/VC-owned (instant kill). Others may have aging founders ready to sell (prime targets). We need to know which is which before Dan spends time on any of them.

## The Top 20

| # | Target | Category | Conviction |
|---|--------|----------|-----------|
| 1 | Leather Spa | Luxury Repair | 10 |
| 2 | The Cobblers | Luxury Repair | 10 |
| 3 | Starship Bagel | Bagels | 10 |
| 4 | Layla Bagels | Bagels | 10 |
| 5 | Jeff's Bagel Run | Bagels | 10 |
| 6 | Jeeves New York | Luxury Repair | 9 |
| 7 | Rago Brothers | Luxury Repair | 9 |
| 8 | 7 Brew | Drive-Thru Coffee | 9 |
| 9 | Othership | Social Bathhouse | 9 |
| 10 | Bathhouse NYC | Social Bathhouse | 9 |
| 11 | Sauna House | Social Bathhouse | 9 |
| 12 | Angie's Pet Spa | Pet Grooming | 8 |
| 13 | Yuppy Puppy Pet Spa | Pet Grooming | 8 |
| 14 | Bubbles Pet Spa | Pet Grooming | 8 |
| 15 | Found | GLP-1 Services | 8 |
| 16 | Prime IV | IV Hydration | 8 |
| 17 | Padel Haus | Padel | 8 |
| 18 | Reserve Padel | Padel | 8 |
| 19 | Skiptown | Pet Services | 7 |
| 20 | Cookie Society | Bakery | 7 |

## Diligence Protocol Per Target

### Phase 1: Blocking Check (ownership verification)
For each target, FIRST determine:
- Is it PE/VC backed? (search for "acquired", "private equity", "growth partner", "series A/B/C", "funding round")
- Is it publicly traded? (instant comp, not target)
- Is it a subsidiary of a larger entity?
- Is the founder still involved?

**Decision rule:** If PE/VC backed or publicly traded → downgrade to comp, stop detailed diligence.

### Phase 2: Entity & Infrastructure Recon
- Corporate entity filings (state registry)
- Domain/WHOIS analysis (infrastructure maturity = acquisition leverage)
- Email stack, hosting, tech stack
- Social media footprint (followers, posting cadence, engagement)
- Digital sophistication assessment

### Phase 3: Operating Intelligence
- Unit count verification (actual vs claimed)
- Revenue range estimation (public data, Foottraffic, review velocity, employee count)
- Employee sentiment (Glassdoor, Indeed, Reddit)
- Customer reviews (Google, Yelp, Trustpilot) — volume, recency, sentiment
- Litigation check (CourtListener, state courts, BBB)
- Founder background (LinkedIn, press, interviews)

### Phase 4: Acquisition Feasibility Assessment
- Is this business actually buyable? (founder age, distress signals, capital needs, expansion stalls)
- What's the likely asking price range?
- What's the acquisition path? (direct approach, broker, auction, franchisee)
- What's the fix-cost table? (infrastructure, operations, brand)
- What's the SBA 7(a) math? (price, down payment, debt service, CoC return)

### Phase 5: Verdict & Map Update
For each target, produce:
- **Verdict:** ACQUIRE / WATCH / PASS / COMP
- **Confidence:** High / Medium / Low
- **One-line why**
- **Next action** if ACQUIRE or WATCH
- **Updated conviction score** (may go up or down based on findings)

## Deliverables
1. Individual dossier per target (saved to workspace)
2. Summary comparison table
3. Updated Situation Room map with revised scores and new intelligence
4. Obsidian mirror of the summary report

## Execution Rules
- No outreach, no spend, no external messages, no logins
- All financial estimates are proxies labeled as such
- Prioritize blocking checks — kill PE-owned targets fast
- Use FDDIQ database for franchise brands (7 Brew, Jeff's Bagel Run, Prime IV, etc.)
- Cite every important claim
- Be skeptical — "looks good on paper" is not enough
