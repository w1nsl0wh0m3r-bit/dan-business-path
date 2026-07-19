# Transition Signal Monitoring Framework
## Date: 2026-07-19 | Agent: Hermes

---

## Purpose
The deep diligence proved that **generational succession is the #1 acquisition signal**. Leather Spa (Carlos→David), Rago Brothers (4-gen), Jeeves (Jerry Pozniak), Artbag (closing after 90 yrs). We need systematic monitoring of transition signals across all 175 targets.

---

## Signal Taxonomy

### 🔴 STRONG SIGNALS (act immediately)
- Business listed for sale on BizBuySell, BusinessExits.com, Acquire.com, Empire Flippers
- Press announcement of closure/retirement ("after 40 years...")
- LLC dissolution or DBA change filed
- Founder death/illness (public record)
- Store hours reduced / reviews declining (operational distress)

### 🟡 MEDIUM SIGNALS (monitor, warm up relationship)
- Founder age 60+ (LinkedIn, public records)
- "Second generation" operating (succession uncertainty)
- No family member identified as successor
- Recent lease non-renewal signals
- Equipment aging (visible in store visits, reviews)

### 🟢 WEAK SIGNALS (build database)
- 20+ years operating history (approaching typical transition age)
- Single-location operator (limited scale = harder succession)
- No online booking/e-commerce (legacy operations)
- Owner active on social media but no succession content

---

## Monitoring Pipeline

### Layer 1: Automated (Daily/Weekly)
| Source | Signal | Cadence | Tool |
|--------|--------|---------|------|
| BizBuySell | "shoe repair" OR "bagel" OR "pet grooming" listings | Daily | RSS/email alert |
| BusinessExits.com | Category listings | Weekly | Manual scan |
| Google News alerts | "[brand name] closing" OR "retiring" OR "for sale" | Real-time | Google Alerts |
| LinkedIn | Founder tenure changes, new CEO announcements | Weekly | LinkedIn Sales Navigator |
| Yelp/Google reviews | Review velocity decline, hours changes | Weekly | Review tracking |

### Layer 2: Semi-Automated (Monthly)
| Source | Signal | Cadence |
|--------|--------|---------|
| State LLC/Corp filings | Dissolutions, officer changes | Monthly (state-by-state) |
| Local business journals | Retirement/closure announcements | Monthly scan |
| SSIA Classifieds (shoe repair) | Listings | Monthly |
| Franchise disclosure filings | New FDDs = growth = potential franchisee path | Annual |

### Layer 3: Manual/Relationship (Quarterly)
| Action | Cadence |
|--------|---------|
| Visit top 10 target locations | Quarterly (combine with travel) |
| Check in with founders (casual, non-transactional) | Quarterly |
| Attend industry trade shows | Annual |
| Monitor local press in target markets | Monthly |

---

## Implementation: Cron Job Concept

### Job 1: Business Listing Monitor (Daily)
```
Search BizBuySell + BusinessExits for:
- "shoe repair" OR "leather repair" OR "handbag repair"
- "bagel shop" OR "bagel bakery"
- "pet grooming" OR "dog grooming"
- "coffee shop" in target markets
Output: New listings to ESCALATIONS.md
```

### Job 2: News Signal Monitor (Real-time)
```
Google Alerts for:
- Each top-20 target brand name + "closing" / "retiring" / "for sale"
- "[target market] shoe repair retiring"
- "[target market] bagel shop for sale"
Output: Matches to NOW.md
```

### Job 3: Founder Age/Tenure Audit (Quarterly)
```
For each top-20 target:
- Check LinkedIn for founder age/role changes
- Check state filings for officer changes
- Check press for succession announcements
Output: Updated target profiles
```

---

## Immediate Actions

1. **Set up Google Alerts** for: Leather Spa, Rago Brothers, Starship Bagel, Layla Bagels, Jeeves NY, The Cobblers, Artbag, Cookie Society + "closing"/"retiring"/"for sale"
2. **Verify Artbag closing status** — is Madison Ave location actually closed? Is Coral Springs still operating? This is a live opportunity.
3. **Add BizBuySell RSS feeds** for target categories
4. **DFW fieldwork** (t904) — visit Starship, Cookie Society, Jeff's Bagel Run, observe operations, note equipment age and owner presence

---

## The Watchlist (Prioritized by Transition Signal Strength)

| Target | Signal Strength | Why |
|--------|----------------|-----|
| **Artbag** (NYC/FL) | 🔴 CRITICAL | Confirmed closing after 90 years. ACT NOW if interested. |
| **Leather Spa** (NYC) | 🟡 MEDIUM | 2nd-gen operator (David). Succession unclear. |
| **Rago Brothers** (NJ) | 🟡 MEDIUM | 4-gen family. 120+ years. Succession uncertainty. |
| **Jeeves NY** (NYC) | 🟡 MEDIUM | Jerry Pozniak acquired 2007. Son Zachary involved. |
| **Starship Bagel** (DFW) | 🟢 WEAK | Oren Salomon is at peak (just won Best Bagel). But growth pressure may create opening. |
| **Cookie Society** (DFW) | 🟢 WEAK | Founders active, growing. Long-term watch. |
