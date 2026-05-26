# Goal: Next 30 Ranked Deep Dives (Research → MD → HTML)

## Objective
Produce deep-dive investment memos for the next 30 highest-ranked categories on the Dan Business Path dashboard that don't already have completed deep dives. Save each as markdown, then merge into the corresponding live HTML page on the GitHub Pages site.

## Current State
- Dashboard: 178 categories (soon 278 after 100 additions)
- Completed deep dives: ~30 categories already have .md files in `deep-dives/` and merged HTML pages
- This goal covers the NEXT 30 by rank that lack deep dives

## Process Per Category

### Step 1: Identify the 30
The 30 categories are already identified (sorted by Score field in the JSON, skipping those with existing `.md` files in `/Users/winslow/Projects/dan-business-path/deep-dives/`):

1. Distressed franchise portfolio acquisition
2. Candy/import snacks ecommerce to retail
3. Drive-thru coffee kiosk
4. Self-storage / portable storage
5. Men's health / hair restoration / TRT clinic
6. Bubble tea / boba
7. Breakfast sandwich / egg concept
8. Asian bakery / Korean bakery / mochi donut
9. Trade workwear / women skilled trades workwear
10. PayMore / electronics resale
11. Gymnastics / ninja / movement academy
12. AED inspection / battery-pad replacement
13. AI compliance admin layer for route businesses
14. GLP-1 clinic / body composition clinic
15. Specialty restoration contractor
16. Specialty coffee / espresso bar
17. Waxing studio
18. Blinds / window coverings
19. Handyman / home repair subscription
20. Senior home safety modifications / aging-in-place retrofits
21. Luxury home specialty systems maintenance
22. Tacos / burritos / bowl concept
23. Pilates / barre boutique fitness
24. Facial bar
25. Acne / skin clinic
26. Pizza slice / Roman / Detroit pizza
27. Home electrification / heat pump retrofit concierge
28. Massage studio
29. Lighting showroom
30. Flooring / tile / surfaces showroom

### Step 2: Research & Write Markdown
For each category, produce a deep-dive memo saved as `/Users/winslow/Projects/dan-business-path/deep-dives/<slug>.md`.

**Required sections (use this exact structure):**

```markdown
# [Category Name] — Deep Dive Investment Memo

## Verdict: GO / NO-GO / CONDITIONAL
[1-2 sentence bottom line with reasoning]

## 1. Category Definition & Demand Map
- What is this business? (2-3 sentences)
- Who are the customers? (B2B vs B2C split)
- Demand drivers: what makes this recurring or growing?
- Geographic relevance: NE (Boston/NE, NY/CT/NJ), SFL, or national
- Market size: cite sources or label as "estimate" — NO fake precision

## 2. Economics to Underwrite
| Metric | Typical Range | Source |
|--------|--------------|--------|
| Revenue per unit | $X-$Y | [source] |
| SDE / EBITDA margin | X%-Y% | [source] |
| Average ticket / job | $X-$Y | [source] |
| Customer frequency | X times/year | [source] |
| Route density potential | [assessment] | [source] |
| Recurring revenue % | X%-Y% | [source] |
| SBA financeable? | Yes/No | [source] |

## 3. Unit Economics Model (Three-Case)

| Case | Revenue | SDE | SDE Margin | Entry Price | Multiple | Cash-on-Cash Year 1 |
|------|---------|-----|-----------|-------------|----------|---------------------|
| Bear | | | | | 3.0-3.5x | |
| Base | | | | | 3.5-4.0x | |
| Bull | | | | | 4.0-4.5x | |

**Key assumptions:**
- Entry multiples: 3-4.5x SDE at Dan's scale ($200-500K SDE). NOT 8-10x.
- SBA 7(a): 10-year term, ~11% rate (2026), 10% down
- Cash-on-cash = (SDE - debt service) / down payment
- Operator partner: Dan can hire/partner with an operator — don't penalize lack of direct experience

## 4. Path-Specific Buybox
What makes a GOOD acquisition target in this category?
- Revenue range:
- SDE range:
- Years in business:
- Route density / customer count:
- Key assets to verify:
- Red flags to avoid:

What makes a good FRANCHISE candidate?
- Top 3-5 franchise brands with typical franchise fee + royalty
- FDD highlight: item 19 financials if available
- Unit economics from franchise disclosure

## 5. Competitive Landscape
- Top 5-10 competitors or roll-ups active in this space
- PE activity: who's consolidating?
- Fragmentation level: how many mom-and-pops vs chains?
- Moat: what protects margins? (certifications, relationships, equipment, compliance)

## 6. Financing, Valuation & Capital Discipline
- Typical deal structure (asset vs stock, earnout, seller note)
- SBA eligibility and typical loan terms
- Down payment required at Dan's scale
- Payback period at base case
- honest multiple arbitrage: ~3x in → 4x out at this scale

## 7. 90-Day Roadmap (If Dan Pursues This)
- Phase 1 (Days 1-30): Market mapping, broker outreach, franchise FDD requests
- Phase 2 (Days 31-60): Operator partner search, financial modeling, site visits
- Phase 3 (Days 61-90): LOI on first target or franchise signing decision

## 8. Kill Criteria
What would make this a NO-GO?
- [specific negative signals that would kill the thesis]

## Sources
[All URLs and data sources cited throughout]
```

### Step 3: Merge into HTML Page
For each completed markdown, merge the content into the corresponding live HTML page.

**File mapping:**
- The HTML filename should match the `Memo` field from the dashboard JSON
- If the HTML page doesn't exist yet, create one using the existing template structure (copy from any existing deep-dive HTML page in the repo — same CSS/layout/nav)
- If the HTML page exists but has template content, replace template text with real research
- **DO NOT change CSS, classes, layout, or JavaScript** — only text content

**Verification per page:**
- Page loads without errors
- Title and meta description are category-specific (not generic)
- All 8 sections have real data (no "TBD" or placeholder text)
- Numbers in tables are specific (not ranges without context)

### Step 4: Save to Obsidian
Copy each completed `.md` file to:
`/Users/winslow/Documents/Business-Research/Business Transition Engine/Business Path Deep Dives/<slug>.md`

### Step 5: Git Commit & Push
After each batch of ~5-10 completed and merged pages:
```bash
cd /Users/winslow/Projects/dan-business-path
git add .
git commit -m "Deep dives batch N: [category names]"
git push origin main
```

## Execution Strategy
- Work in batches of 5 categories
- Use subagents for parallel research (one subagent per batch of 5)
- Each subagent handles: research → write .md → merge into HTML → verify
- After all batches complete, do a single Obsidian save pass and final git push

### Batch Assignments:
**Batch 1 (categories 1-5):** Distressed franchise portfolio, candy/import snacks, drive-thru coffee kiosk, self-storage, men's health/TRT clinic
**Batch 2 (categories 6-10):** Bubble tea/boba, breakfast sandwich/egg, Asian bakery/mochi donut, trade workwear, PayMore/electronics resale
**Batch 3 (categories 11-15):** Gymnastics/ninja academy, AED inspection, AI compliance admin, GLP-1 clinic, specialty restoration
**Batch 4 (categories 16-20):** Specialty coffee, waxing studio, blinds/window coverings, handyman subscription, senior home safety mods
**Batch 5 (categories 21-25):** Luxury home systems, tacos/burritos, pilates/barre, facial bar, acne/skin clinic
**Batch 6 (categories 26-30):** Pizza slice, home electrification/heat pump, massage studio, lighting showroom, flooring/tile showroom

## Research Rules
- **All market size claims must cite sources** or say "estimate" — no fake precision
- **Exit multiples: 3-4.5x SDE** at Dan's scale. Never 8-10x unless citing a specific proven franchise resale.
- **Dan CAN partner with an operator** — don't penalize lack of direct operating experience
- **Two Avenue framework in mind:**
  - Avenue 1: Operator partnership + recurring revenue
  - Avenue 2: High cash-on-cash, fast payback consumer business
- **NE focus**: Boston/NE primary, NY/CT/NJ secondary, SFL tertiary
- **No outreach to operators, brokers, or sellers** — research only
- **Score reality checks must be honest** — not self-affirming

## Quality Bar
- Each memo should have 8-15 specific data points with sources
- Unit economics must include real dollar amounts (not just percentages)
- Competitive landscape must name real companies and PE firms
- If data is unavailable for a category, say so explicitly — don't fabricate

## Working Directory
`/Users/winslow/Projects/dan-business-path`

## Completion Criteria
- 30 new `.md` files in `deep-dives/`
- 30 HTML pages created or updated with real research content
- All saved to Obsidian
- All committed and pushed to GitHub
- Dashboard site renders correctly with all new pages linked
