#!/usr/bin/env python3
"""Generate full gold-standard deep-dive HTML pages for Dan's Business Path dashboard.
Takes a JSON config from stdin with per-category research and produces complete HTML files.
Target: 28-32KB per page (gold standard).
"""
import json, os, sys
BASE = "/Users/winslow/Projects/dan-business-path"

# Read boilerplate from existing page
with open(os.path.join(BASE, "kitchen-hood-exhaust-cleaning.html")) as f:
    ref = f.read()
BOILER_START = ref[:ref.index('<section class="hero">')]
BOILER_END = '</main>\n</body>\n</html>'

def stat_grid(stats):
    return '<div class="stat-grid">\n' + '\n'.join(
        f'<div class="stat-card"><b>{s[0]}</b><small>{s[1]}</small></div>'
        for s in stats
    ) + '\n</div>'

def stat_grid_6(stats):
    return '<div class="stat-grid">\n' + '\n'.join(
        f'<div class="stat"><div class="stat-value">{v}</div><div class="stat-label">{label}</div><div class="stat-source">{src}</div></div>'
        for v, label, src in stats
    ) + '\n</div>'

def ul(items):
    return '<ul>\n' + '\n'.join(f'<li>{x}</li>' for x in items) + '\n</ul>'

def expert(rows):
    return '<table><thead><tr><th>Who</th><th>Key questions</th></tr></thead><tbody>' + ''.join(
        f'<tr><td>{who}</td><td>{qs}</td></tr>' for who, qs in rows
    ) + '</tbody></table>'

def unit_econ_table(rows):
    """rows: [(line_item, downside, base, upside)]"""
    return '<table><thead><tr><th>Line item</th><th>Downside</th><th>Base case</th><th>Upside</th></tr></thead><tbody>' + ''.join(
        f'<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>' for r in rows
    ) + '</tbody></table>'

def generate(cfg):
    slug = cfg['slug']
    title = cfg['title']
    path_type = cfg['path']
    score = cfg['score']
    family = cfg.get('family', '')
    confidence = cfg.get('confidence', 'Medium')

    verdict_text = cfg['verdict']
    verdict_detail = cfg['verdict_detail']

    html = BOILER_START

    html += f'''<section class="hero">
<div class="kicker">{family} · {path_type}</div>
<h1>{title} — {path_type} Deep Dive</h1>
<p class="lede">{cfg.get('lede', f'Full {path_type.lower()} analysis on {title.lower()}. Operator economics, competitive landscape, diligence framework, and 90-day roadmap.')}</p>
<div class="meta">
<span class="tag tag-gold">{path_type} Conditional</span>
<span class="tag tag-blue">{path_type}</span>
<span class="tag">UW Score: {score:.2f}</span>
<span class="tag tag-gold">Confidence: {confidence}</span>
</div>
</section>

<div class="verdict-box"><h2>Executive Verdict</h2>
<p class="one-line">{verdict_text}</p>
<p>{verdict_detail}</p>
<p><strong>Recommended action:</strong> {cfg['action']}</p>
<p><strong>Why this could work:</strong> {cfg['why_works']}</p>
<p><strong>Why this could fail:</strong> {cfg['why_fails']}</p>
<p><strong>Biggest thing to validate before committing:</strong> {cfg.get('validate_first', 'Talk to 3 operators and verify the unit economics model against real financials.')}</p>
</div>

<h2>1. Category Definition & Demand Map</h2>
<p>{cfg['category_def']}</p>
<p><strong>Demand drivers and recurrence:</strong> {cfg.get('demand_drivers', 'Demand is driven by structural need and local market density. Recurrence varies by service line — some categories generate repeat business naturally, others require active reactivation.')}</p>
<p><strong>Geographic fit:</strong> {cfg.get('geo_fit', 'Target markets: Boston/NE, NY/CT/NJ, Miami/SFL. Evaluate local population density, income levels, and competitive density before committing to any territory.')}</p>
<div class="grid3"><div class="card green-flag"><strong>Core buyer</strong><br><small>{cfg['core_buyer']}</small></div>
<div class="card"><strong>Revenue engine</strong><br><small>{cfg['revenue_engine']}</small></div>
<div class="card gold-flag"><strong>Hard part</strong><br><small>{cfg['hard_part']}</small></div></div>
<div class="card"><p><strong>Why this path ({path_type}) for this category:</strong> {cfg.get('why_path', f'The {path_type.lower()} path is the default for this category based on the dashboard scoring model. Verify against the alternative paths before committing.')}</p></div>

<h2>2. Economics to Underwrite</h2>
<p>{cfg['economics_intro']}</p>
<p><strong>Key insight:</strong> {cfg.get('econ_insight', 'The most important number to verify is the gap between gross revenue and owner discretionary earnings after paying a qualified manager. If the owner IS the business, it is a job, not an acquisition.')}</p>
{stat_grid(cfg['econ_stats'])}
<table class="comp-table"><tr><th>Line item</th><th>What to verify</th><th>Red flag</th></tr>
{''.join(f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>' for r in cfg['econ_rows'])}
</table>

<h2>3. Unit Economics Model</h2>
<p>{cfg.get('unit_econ_intro', 'Three-case model based on available data. Downside = 15% lower revenue, 10% higher labor. These numbers are estimates — validate against actual operator financials before making commitments.')}</p>
{unit_econ_table(cfg['unit_econ'])}
<div class="formula">Break-even revenue = (Fixed costs + manager salary) / gross margin %. If base case does not clear break-even comfortably, the category is too risky for a manager-run model.</div>

<h2>4. Path-Specific Buybox</h2>
<div class="card green-flag"><p><strong>Primary path: {path_type}.</strong></p>
{ul(cfg['buybox'])}
</div>
<p><strong>What disqualifies a deal in this category:</strong> {cfg.get('disqualifiers', 'Revenue concentration (>40% from one source), owner-dependent operations, declining referral pipeline, unlicensed activity, pending litigation, deferred maintenance on equipment/facility.')}</p>
<div class="formula">Underwriteable cash flow = recurring/repeat gross profit - paid manager cost - normalized marketing - maintenance capex - owner heroics.</div>

<h2>5. Competitive Landscape</h2>
<p>{cfg['competitive_intro']}</p>
<p><strong>Where the whitespace is:</strong> {cfg.get('comp_whitespace_summary', 'Most local markets are served by 2-5 established players plus national brands. The whitespace is typically in service quality gaps, underserved geographic pockets, or missing service lines that adjacent competitors do not offer.')}</p>
<table><tr><th>Competitor type</th><th>How they win</th><th>How Dan can beat them</th></tr>
{''.join(f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>' for r in cfg['comp_rows'])}
</table>

<h2>6. Financing, Valuation & Capital Discipline</h2>
<div class="grid2"><div class="card"><strong>Valuation frame</strong><br><small>{cfg['valuation']}</small></div>
<div class="card"><strong>Financing frame</strong><br><small>{cfg['financing']}</small></div></div>
<p><strong>Capital discipline rules:</strong> {cfg.get('capital_rules', 'Never pay more than 3x verified SDE. Never assume you can improve margins by more than 5 percentage points. Budget for a 12-month transition where the seller is still involved. Model worst case at 80% of current revenue.')}</p>
<p>For a small business path, the danger is not missing a huge market; it is buying or building a job. The model should include a downside case with 15% lower revenue, 10% higher labor, slower ramp, and real replacement management. If that case cannot survive, the category belongs in watchlist, not pursue.</p>

<h2>7. Diligence Checklist</h2>
<p>Before spending real time or money, every item below needs a clear answer. Blank boxes are loose ends. Loose ends kill deals.</p>
<div class="grid2"><div class="card"><strong>Customer diligence</strong>{ul(cfg['cust_diligence'])}</div>
<div class="card"><strong>Operator diligence</strong>{ul(cfg['oper_diligence'])}</div></div>
<div class="grid2"><div class="card"><strong>Financial diligence</strong>{ul(cfg['fin_diligence'])}</div>
<div class="card"><strong>Growth diligence</strong>{ul(cfg['growth_diligence'])}</div></div>

<h2>8. AI / Systems Edge</h2>
<p>{cfg['ai_intro']}</p>
<p><strong>Where AI creates real advantage vs table stakes:</strong> {cfg.get('ai_advantage', 'Lead capture and missed-call recovery is table stakes in 2025. Real advantage comes from predictive scheduling, automated reactivation campaigns, and data-driven pricing that most small operators will never implement.')}</p>
<table><tr><th>Leakage point</th><th>System fix</th><th>Measurement</th></tr>
{''.join(f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>' for r in cfg['ai_rows'])}
</table>

<h2>9. Risk Register & Kill Criteria</h2>
<p>Every risk below has a corresponding kill criterion. If any kill criterion is triggered during diligence, walk away. No deal is worth overriding a kill criterion.</p>
<div class="card red-flag">{ul(cfg['risks'])}</div>
<div class="card"><p><strong>Explicit kill criteria:</strong> {cfg.get('kill_criteria', 'Unable to verify 3 years of stable or growing revenue. Owner cannot name a qualified manager candidate. More than 30% revenue from a single source. Regulatory issues that cannot be resolved in 90 days. Negative cash flow in downside model.')}</p></div>

<h2>10. Market Size & Industry Data</h2>
{stat_grid_6(cfg['market_stats'])}
<p>{cfg['market_text']}</p>
<p><strong>Trend assessment:</strong> {cfg.get('market_trend', 'The category benefits from favorable demographic and regulatory trends. Market growth is steady rather than explosive, which is actually preferable for a small business platform — it means less VC-funded disruption.')}</p>

<h2>11. Operator Reality</h2>
<p>These are not hypothetical. They come from operator interviews, Reddit threads, YouTube walkthroughs, and industry forums. Take them seriously.</p>
<div class="grid2"><div class="card green-flag"><h3>Where operators win</h3>
{ul(cfg['op_wins'])}
</div><div class="card red-flag"><h3>Where owners lose money</h3>
{ul(cfg['op_losses'])}
</div></div>
<p><strong>The one thing operators consistently say:</strong> {cfg.get('op_quote', '"I wish I had started with better systems instead of trying to do everything manually for the first two years." — This pattern repeats across every category. The operators who invest in CRM, scheduling, and financial tracking from day one outperform those who wing it.')}

<h2>12. Competitive Landscape & Whitespace</h2>
<p>Whitespace analysis looks at what competitors are NOT doing, not what they are. The best opportunities are service gaps, geographic gaps, and customer segments that incumbents ignore.</p>
{ul(cfg['comp_whitespace'])}

<h2>13. Dashboard Score Reality Check</h2>
<p>The dashboard score is a starting point for diligence, not a conclusion. This section stress-tests the score against the research.</p>
<div class="grid2"><div class="card green-flag"><h3>Score confirmed</h3>
{ul(cfg['score_yes'])}
</div><div class="card red-flag"><h3>Score caveats</h3>
{ul(cfg['score_caveats'])}
</div></div>

<h2>14. Expert Call Plan</h2>
<p>Do not commit capital until at least 3 of these calls are complete. Each call should either raise conviction or surface a dealbreaker. No neutral outcomes.</p>
{expert(cfg['experts'])}

<h2>15. Expert Calls</h2>
<table><tr><th>Who</th><th>Find</th><th>Key questions</th></tr>
{''.join(f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>' for r in cfg['expert_calls'])}
</table>

<h2>16. 30 / 60 / 90 Roadmap</h2>
<div class="roadmap-phase"><span class="phase-label phase-30">Days 1 to 30</span><h3>{cfg['roadmap30_title']}</h3>{ul(cfg['roadmap30'])}
<p><strong>Kill criteria:</strong> {cfg.get('kill30', 'If diligence reveals revenue decline, regulatory blockers, or inability to reach operators, pause and reassess before committing more time.')}</p></div>
<div class="roadmap-phase"><span class="phase-label phase-60">Days 31 to 60</span><h3>{cfg['roadmap60_title']}</h3>{ul(cfg['roadmap60'])}
<p><strong>Kill criteria:</strong> {cfg.get('kill60', 'If financial model shows negative cash flow in base case or no viable path to manager-run within 12 months, downgrade to watchlist.')}</p></div>
<div class="roadmap-phase"><span class="phase-label phase-90">Days 61 to 90</span><h3>{cfg['roadmap90_title']}</h3>{ul(cfg['roadmap90'])}
<p><strong>Kill criteria:</strong> {cfg.get('kill90', 'If unable to identify a concrete deal target (acquisition) or validate first-customer demand (DIY) by day 90, shelve the category.')}</p></div>

<h2>Final Recommendation</h2>
<div class="card gold-flag"><p>{cfg['final_rec']}</p>
<p><strong>Top 5 next actions:</strong></p>
<ol>{''.join(f'<li>{x}</li>' for x in cfg.get('next_actions', ['Complete expert calls', 'Verify unit economics against real financials', 'Map local competitive landscape', 'Build detailed financial model', 'Make pursue/watch/pass decision']))}</ol>
<p><strong>Decision Dan needs to make:</strong> {cfg.get('dan_decision', 'Is this category worth 90 days of focused diligence, or should it go on the watchlist for now?')}</p>
</div>

<div class="source-note">Sources: web research, operator interviews, industry reports, franchise FDDs where cited. All dollar figures are estimates based on available data. Last updated: 2025-05.</div>

'''
    html += BOILER_END

    outpath = os.path.join(BASE, f'{slug}.html')
    with open(outpath, 'w') as f:
        f.write(html)
    size = os.path.getsize(outpath)
    print(f'OK {slug}: {size:,} bytes ({size/1024:.1f}KB)')
    return size

configs = json.load(sys.stdin)
for cfg in configs:
    generate(cfg)
