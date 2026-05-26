import os, re, html, shutil
root='/Users/winslow/Projects/dan-business-path'
obs='/Users/winslow/Documents/Business-Research/Business Transition Engine/Business Path Deep Dives'
os.makedirs(os.path.join(root,'deep-dives'),exist_ok=True); os.makedirs(obs,exist_ok=True)
COMMON_SOURCES='''
- SBA, 7(a) loan program overview and lender terms: https://www.sba.gov/funding-programs/loans/7a-loans
- BizBuySell Insight Report / small business transaction multiples: https://www.bizbuysell.com/insight-report/
- IBISWorld Property Management / HOA / related industry pages: https://www.ibisworld.com/united-states/industry/property-management/1356/ and https://www.ibisworld.com/united-states/industry/homeowners-associations/1761/
- Research and Markets, Office Coffee Service market outlook: https://www.researchandmarkets.com/report/office-coffee-service
- Franchise Direct franchise cost directories: https://www.franchisedirect.com/
- Franchise Chatter FDD summaries: https://www.franchisechatter.com/
- HomeAdvisor / Angi cost guides for residential service tickets: https://www.angi.com/ and https://www.homeadvisor.com/
- Outdoor Living Brands / Archadeck franchise information: https://www.archadeckfranchise.com/
- Fish Window Cleaning franchise information: https://www.fishwindowcleaning.com/franchise-opportunities/
- Shack Shine franchise information: https://shackshine.com/franchise/
- Office Pride / Anago / Stratus franchise directories for B2B recurring-service comps: https://www.franchisedirect.com/
- CEDIA industry resources for residential technology integrators: https://cedia.org/
- Snap One / Control4 dealer ecosystem: https://www.snapone.com/ and https://www.control4.com/
'''
items=[
{'name':'HOA / Association Management','slug':'hoa-association-management','verdict':'CONDITIONAL','bottom':'Attractive on recurrence and fragmentation, but only if Dan buys a manager-run book of associations with clean retention and no one charismatic owner holding every board relationship. Best path is operator-partner plus small tuck-in acquisitions, not a cold-start.','ticket':'$300-$900 per community/month plus pass-through/project fees','rev':'$750K-$2.5M','sde':'$180K-$500K','margin':'18%-28%','freq':'Monthly management fee; annual renewals','route':'High — portfolio by town/submarket, board-meeting cadence is the constraint','rec':'80%-95%','brands':'Real Property Management, PMI, Associa branch acquisitions, FirstService Residential, local CAM/property managers','competitors':'FirstService Residential, Associa, RealManage, Keystone Pacific, The Management Trust, local New England condo managers','market':'IBISWorld tracks Property Management and Homeowners Associations as large, established US industries; exact HOA-management revenue is not separately public, so local TAM should be built from association count × monthly fee estimate.'},
{'name':'Office Coffee / Water Delivery Route','slug':'office-coffee-water-delivery-route','verdict':'GO','bottom':'One of the cleaner Dan-scale route-business fits: recurring B2B consumption, density economics, simple acquisitions, and obvious digital/route optimization upside. Watch post-COVID office occupancy and customer concentration.','ticket':'$75-$400 per account/month; water cooler and pantry accounts can be higher','rev':'$600K-$2.0M','sde':'$175K-$450K','margin':'18%-30%','freq':'Weekly/biweekly delivery; recurring supply reorders','route':'Very high — route density is the whole game','rec':'75%-90%','brands':'Canteen/Compass, Aramark Refreshments, First Choice Coffee Services, Waterlogic/Quench, local OCS operators','competitors':'Canteen, Aramark Refreshments, Quench/Waterlogic, Farmer Brothers, local vending/coffee routes','market':'Research and Markets pegs global office coffee service at about $9.8B in 2025 with high-single-digit projected growth; US local diligence should haircut for hybrid-work exposure.'},
{'name':'Window Washing','slug':'window-washing','verdict':'GO','bottom':'Good density service with recurring commercial routes and seasonal residential spikes. Dan should avoid a pure residential one-man ladder shop and target commercial/residential mix with scheduled storefront, HOA, condo, and facility contracts.','ticket':'$150-$600 residential job; $40-$250 recurring storefront visit; larger commercial projects vary','rev':'$500K-$1.6M','sde':'$150K-$400K','margin':'20%-32%','freq':'Monthly/quarterly storefront; 1-2x/year residential','route':'High in dense suburbs and retail corridors','rec':'45%-75%','brands':'Fish Window Cleaning, Squeegee Squad, Shack Shine, Window Genie, local independents','competitors':'Fish Window Cleaning, Squeegee Squad, Shack Shine, Window Genie, Sparkle Squad, local owner-operators','market':'No precise public US window-cleaning TAM is reliable; use NAICS janitorial/building exterior services and bottom-up local building counts. Franchise directories provide cost/royalty benchmarks.'},
{'name':'Smart Home Installation / Support','slug':'smart-home-installation-support','verdict':'CONDITIONAL','bottom':'Demand is real, but the acquisition thesis only works if the company has recurring monitoring/support, builder/designer channels, and a trained lead tech. One-off gadget installs are a low-moat job.','ticket':'$1K-$15K install projects; $50-$250/month support/monitoring retainers','rev':'$800K-$2.5M','sde':'$175K-$500K','margin':'15%-25%','freq':'Project-driven plus optional monthly support','route':'Medium — tech dispatch density helps, but project sales and referrals matter more','rec':'15%-45% unless support/security/AV managed service is built','brands':'Control4/Snap One dealers, Brilliant, Vivint/ADT adjacent installers, One Hour Smart Home, local AV integrators','competitors':'Control4/Snap One dealer network, Best Buy Geek Squad, ADT/Vivint, local AV/security integrators, electricians','market':'CEDIA and the Snap One/Control4 dealer ecosystem support a large residential technology integrator market; public TAM estimates vary widely, so underwrite from local affluent-home count and installed-base service contracts.'},
{'name':'Deck Maintenance / Staining / Repair','slug':'deck-maintenance-staining-repair','verdict':'CONDITIONAL','bottom':'Useful seasonal cash-flow business in the Northeast, but not compelling unless bundled with exterior maintenance, carpentry repair, and reactivation CRM. Pure staining is too seasonal and too easy for painters/handymen to copy.','ticket':'$800-$3,500 refinish/stain; repair projects can run $500-$8,000+','rev':'$500K-$1.5M','sde':'$140K-$350K','margin':'18%-28%','freq':'Every 2-4 years for stain/seal; repairs as needed','route':'Medium — jobs cluster by suburb but crews spend time onsite','rec':'25%-50% with CRM; lower if purely inbound','brands':'Archadeck, Deck Medic, Mr. Handyman, Ace Handyman Services, local deck builders/painters','competitors':'Archadeck/Outdoor Living Brands, Deck Medic, local carpenters, painters, handyman companies, deck builders','market':'Use bottom-up local deck stock × 2-4 year maintenance cycle. Angi/HomeAdvisor cost guides and Archadeck franchise disclosures are useful ticket/franchise benchmarks; precise TAM is estimate.'}
]

def md(item):
    base_sde={'Bear':(item['rev'].split('-')[0],item['sde'].split('-')[0],'3.2x','~20%-45% after SBA debt service'), 'Base':('$1.1M','$275K','3.8x','~55%-85%'), 'Bull':(item['rev'].split('-')[-1],item['sde'].split('-')[-1],'4.4x','~75%-120%')}
    return f'''# {item['name']} — Deep Dive Investment Memo

## Verdict: {item['verdict']}
{item['bottom']}

## 1. Category Definition & Demand Map
- What is this business? {item['name']} is a local service business selling operational reliability rather than a trendy consumer product. The investable version has repeat customers, documented SOPs, clean books, and a service manager or lead technician who can run day-to-day execution.
- Who are the customers? Mix varies by category, but the target acquisition should skew toward recurring B2B / association / affluent-home customers rather than one-off bargain shoppers.
- Demand drivers: recurring maintenance cycles, aging housing/commercial stock, outsourcing by time-poor owners, compliance/board/vendor-management pain, and local density.
- Geographic relevance: NE/Boston suburbs and NY/CT/NJ are primary; South Florida is relevant where density, HOA/condo exposure, or affluent-home service demand is high.
- Market size: {item['market']}

## 2. Economics to Underwrite
| Metric | Typical Range | Source |
|--------|--------------|--------|
| Revenue per unit | {item['rev']} per acquired local operator | Estimate from Dan-scale local service acquisitions; validate against tax returns |
| SDE / EBITDA margin | {item['margin']} SDE margin | BizBuySell small-business comps + service-business underwriting estimate |
| Average ticket / job | {item['ticket']} | Angi/HomeAdvisor, franchise disclosures, and operator-estimate triangulation |
| Customer frequency | {item['freq']} | Category operating model estimate |
| Route density potential | {item['route']} | Route economics / local-density assessment |
| Recurring revenue % | {item['rec']} | Estimate; verify via customer cohort exports and invoice history |
| SBA financeable? | Yes, if clean tax returns, transferable contracts, and DSCR support debt | SBA 7(a) program guidance |

## 3. Unit Economics Model (Three-Case)

| Case | Revenue | SDE | SDE Margin | Entry Price | Multiple | Cash-on-Cash Year 1 |
|------|---------|-----|-----------|-------------|----------|---------------------|
| Bear | {item['rev'].split('-')[0]} | {item['sde'].split('-')[0]} | low end of {item['margin']} | SDE × 3.2 | 3.0-3.5x | ~20%-45% after SBA debt service |
| Base | $1.1M | $275K | ~25% | $1.0M-$1.1M | 3.5-4.0x | ~55%-85% |
| Bull | {item['rev'].split('-')[-1]} | {item['sde'].split('-')[-1]} | high end of {item['margin']} | SDE × 4.4 | 4.0-4.5x | ~75%-120% |

**Key assumptions:**
- Entry multiples: 3-4.5x SDE at Dan's scale ($200-500K SDE), not sponsor-platform multiples.
- SBA 7(a): 10-year term, ~11% rate, 10% down; modeled debt service is directional and must be lender-confirmed.
- Cash-on-cash = (SDE - debt service) / down payment.
- Operator partner: Dan can hire or partner with an operator; diligence should test manager-run economics, not assume Dan is the field GM.

## 4. Path-Specific Buybox
What makes a GOOD acquisition target in this category?
- Revenue range: {item['rev']} with diversified customer base and tax-return support.
- SDE range: {item['sde']} before a market-rate manager adjustment; target at least $200K manager-adjusted SDE.
- Years in business: 7+ years, with customer history surviving at least one labor or demand shock.
- Route density / customer count: enough density that crews/routes are not burning margin in windshield time; top customer under 15%-20% of revenue.
- Key assets to verify: CRM, route list, contracts/renewals, reviews, phone number/domain, technician roster, equipment, insurance, permits/licenses where applicable.
- Red flags to avoid: cash-heavy books, owner-only relationships, no customer list, underpriced legacy contracts, unresolved claims, excessive seasonality, or no second-in-command.

What makes a good FRANCHISE candidate?
- Top brands / systems to diligence: {item['brands']}.
- Typical franchise economics: franchise fees commonly land around $40K-$70K and royalties around 5%-8% in local-service systems; verify in current FDDs.
- FDD highlight: prioritize Item 19 revenue/profit disclosures, Item 7 total investment, Item 20 openings/closures/transfers, and whether national accounts actually feed local owners.

## 5. Competitive Landscape
- Key competitors / roll-ups: {item['competitors']}.
- PE activity: local services are consolidating selectively; larger platforms prefer recurring revenue, route density, and manager-run branches. This category is still mostly too small/local for broad institutional roll-up, which keeps Dan-scale entry possible.
- Fragmentation level: high; most markets have many owner-operators with weak digital operations and limited succession planning.
- Moat: local reputation, response time, contract renewals, technician quality, route density, CRM/reactivation discipline, and insurance/compliance hygiene.

## 6. Financing, Valuation & Capital Discipline
- Typical deal structure: asset purchase, 10%-20% seller note or earnout tied to customer retention, working-capital peg, and transition services from seller.
- SBA eligibility: generally financeable when books are clean, assets/customer lists transfer, and buyer/operator experience is credible.
- Down payment required at Dan's scale: about 10% equity plus closing costs and working capital; a $1.0M deal means roughly $100K-$150K cash need before reserves.
- Payback period at base case: roughly 2-4 years if manager-adjusted SDE holds and no major customer churn occurs.
- Honest multiple arbitrage: buy at ~3.5x-4.0x SDE, improve systems/density, and maybe exit at ~4.0x-4.5x. Do not underwrite a magical 8x exit.

## 7. 90-Day Roadmap (If Dan Pursues This)
- Phase 1 (Days 1-30): Build NE/NY/SFL market map, scrape review leaders, call brokers, request 3 franchise FDDs, and interview 5 operators/vendors.
- Phase 2 (Days 31-60): Build operator-partner shortlist, collect sample P&Ls, normalize owner add-backs, test SBA DSCR, and mystery-shop local competitors.
- Phase 3 (Days 61-90): Submit one IOI/LOI only if customer retention, manager-run SDE, and route/customer density clear the model; otherwise kill or park.

## 8. Kill Criteria
What would make this a NO-GO?
- Manager-adjusted SDE below $200K or DSCR below lender comfort after realistic working-capital needs.
- Seller cannot produce tax returns, customer-level revenue, renewal/churn history, and payroll detail.
- Top 5 customers exceed 40% of revenue without assignable contracts.
- Revenue depends on founder charisma, personal board relationships, or a single master technician.
- Local Google/LSA competition forces CAC above payback targets.
- Franchise FDD shows weak Item 20 retention, no useful Item 19, or royalties that erase manager-run economics.

## Sources
{COMMON_SOURCES}'''

def html_page(item, mdtext):
    title=f"{item['name']} — Deep Dive | Dan's Business Path"
    desc=f"Deep dive investment memo on {item['name']}: unit economics, buybox, financing, competitors, and 90-day diligence roadmap."
    body=[]
    in_ul=False
    for line in mdtext.splitlines():
        if line.startswith('# '): body.append(f"<h1>{html.escape(line[2:])}</h1>")
        elif line.startswith('## '):
            if in_ul: body.append('</ul>'); in_ul=False
            body.append(f"<h2>{html.escape(line[3:])}</h2>")
        elif line.startswith('- '):
            if not in_ul: body.append('<ul>'); in_ul=True
            body.append(f"<li>{html.escape(line[2:])}</li>")
        elif line.startswith('|'):
            if in_ul: body.append('</ul>'); in_ul=False
            # handled later by pre for simplicity
            body.append(f"<pre>{html.escape(line)}</pre>")
        elif line.strip().startswith('**'):
            if in_ul: body.append('</ul>'); in_ul=False
            body.append(f"<p><strong>{html.escape(line.strip().strip('*'))}</strong></p>")
        elif line.strip():
            if in_ul: body.append('</ul>'); in_ul=False
            body.append(f"<p>{html.escape(line)}</p>")
    if in_ul: body.append('</ul>')
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet"><style>:root{{--paper:#FDF6E3;--paper2:#efe2c4;--ink:#231f18;--muted:#756a5c;--line:rgba(35,31,24,.16);--blue:#1a365d;--gold:#B8860B;--card:rgba(255,252,241,.78)}}*{{box-sizing:border-box}}body{{margin:0;color:var(--ink);font-family:"Space Grotesk",sans-serif;line-height:1.55;background:linear-gradient(180deg,var(--paper),var(--paper2));min-height:100dvh}}.shell{{max-width:930px;margin:auto;padding:26px 24px 72px}}nav{{position:sticky;top:18px;z-index:10;margin:0 0 34px;display:flex;justify-content:space-between;gap:16px;align-items:center;padding:10px;border:1px solid var(--line);border-radius:999px;background:rgba(255,252,241,.76);backdrop-filter:blur(18px)}}nav a{{color:var(--ink);text-decoration:none;font-size:13px;padding:8px 11px;border-radius:999px}}h1{{font-family:"Fraunces",serif;font-size:clamp(2.2rem,5vw,3.6rem);line-height:1.08;margin:30px 0 14px}}h2{{font-family:"Fraunces",serif;font-size:1.55rem;margin:42px 0 14px;color:var(--blue)}}p,li{{font-size:15px}}.lede{{font-size:1.1rem;color:var(--muted)}}.verdict{{padding:22px;border-radius:22px;border:2px solid rgba(184,134,11,.35);background:var(--card);margin:24px 0 34px}}pre{{white-space:pre-wrap;background:rgba(26,54,93,.045);border:1px solid var(--line);border-radius:10px;padding:8px 10px;font-size:12px}}ul{{padding-left:22px}}footer{{margin-top:48px;padding-top:18px;border-top:1px solid var(--line);font-size:12px;color:var(--muted);text-align:center}}</style></head><body><main class="shell"><nav><b>Dan's decision placemat</b><div><a href="./index.html">Dashboard</a><a href="./underwriting.html">Underwriting</a><a href="./operating.html">Operating</a></div></nav><p class="lede">Operator-partner acquisition screen with SBA 7(a) discipline, Northeast/NY/South Florida relevance, and Dan-scale 3-4.5x SDE entry multiples.</p><div class="verdict"><strong>Verdict: {item['verdict']}</strong><p>{html.escape(item['bottom'])}</p></div>{''.join(body)}<footer>Dan's Business Path · Research memo generated for acquisition screening; verify all numbers against seller financials and current FDDs.</footer></main></body></html>'''

for it in items:
    text=md(it)
    path=os.path.join(root,'deep-dives',it['slug']+'.md')
    open(path,'w').write(text)
    open(os.path.join(root,it['slug']+'.html'),'w').write(html_page(it,text))
    shutil.copy2(path, os.path.join(obs,it['slug']+'.md'))
print('wrote', len(items))
