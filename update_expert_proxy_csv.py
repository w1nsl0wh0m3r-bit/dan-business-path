import csv
from pathlib import Path

path = Path('/Users/winslow/.openclaw/workspace/research/2026-05-23 - Business Path Reality Check - Hermes Validation.csv')
rows = list(csv.DictReader(path.open(newline='', encoding='utf-8')))
new_cols = ['RedditSignal','YouTubeSignal','XSignal','ForumSignal','GlassdoorSignal','BrokerSignal','ExpertProxyVerdict']
fieldnames = list(rows[0].keys())
for c in new_cols:
    if c not in fieldnames:
        fieldnames.append(c)

signals = {
    'Backflow testing / cross-connection compliance': {
        'RedditSignal':'Supports: Reddit r/Irrigation/rPlumbing snippets cite $50-$100/test, 20/day theoretical throughput; testing easy quick money, repairs/replacements higher margin.',
        'YouTubeSignal':'Insufficient direct operator video found.',
        'XSignal':'Insufficient.',
        'ForumSignal':'Insufficient.',
        'GlassdoorSignal':'N/A.',
        'BrokerSignal':'Indirect support via route/acquisition thesis; no clean BBS detailed listing extracted.',
        'ExpertProxyVerdict':'supports'
    },
    'Kitchen hood / exhaust cleaning': {
        'RedditSignal':'Supports with caution: r/smallbusiness hood route netting ~$60k/year; commenters valued likely <$50k/$20k-$50k unless strategic buyer; r/sweatystartup snippet cites 30% revenue gain from pricing/new estimates.',
        'YouTubeSignal':'Supports: hood cleaning acquisition/operator videos; one interview cites acquisition of hood cleaning business for $928k; MFS video references six-figure revenue within <2 years.',
        'XSignal':'Insufficient.',
        'ForumSignal':'HOODZ/BizBuySell franchise presence; no complaint forum thread found.',
        'GlassdoorSignal':'Insufficient.',
        'BrokerSignal':'Supports: BizBuySell exhaust hood cleaning franchise listing with FF&E $68,587 and 5 FT employees surfaced.',
        'ExpertProxyVerdict':'supports'
    },
    'Grease trap pumping': {
        'RedditSignal':'Supports: r/sweatystartup threads cite ~$55k pumping truck startup, certifications, 45-minute pump jobs, 300+ gallon traps, route-density contract growth.',
        'YouTubeSignal':'Insufficient direct video found.',
        'XSignal':'Insufficient.',
        'ForumSignal':'Insufficient.',
        'GlassdoorSignal':'N/A.',
        'BrokerSignal':'Waste/route category support but no clean detailed grease listing extracted.',
        'ExpertProxyVerdict':'supports'
    },
    'Fire/life-safety inspections and extinguisher routes': {
        'RedditSignal':'Supports: r/smallbusiness buyer thread for one-man home-based extinguisher inspection business doing ~$300k revenue/year; r/firePE snippet says service/deficiency jobs average 35%-40% profit.',
        'YouTubeSignal':'Insufficient direct video found.',
        'XSignal':'Insufficient.',
        'ForumSignal':'Insufficient.',
        'GlassdoorSignal':'N/A.',
        'BrokerSignal':'Supports: BizBuySell fire suppression listings cite 95% recurring revenue and hundreds/thousands of accounts; another with 350 active repeating clients.',
        'ExpertProxyVerdict':'supports'
    },
    'Irrigation / sprinkler service': {
        'RedditSignal':'Supports: r/Irrigation thread says service side can make north of 30% operating income; start thread warns experience required.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient.',
        'ForumSignal':'N/A.',
        'GlassdoorSignal':'N/A.',
        'BrokerSignal':'Supports: BizBuySell MA irrigation listing $1.175M gross revenue/$206k SDE; sprinkler service listing asking $199k; established sprinkler/de-icing listing surfaced.',
        'ExpertProxyVerdict':'supports'
    },
    'Radon testing / mitigation': {
        'RedditSignal':'Supports with caution: r/radon/r/smallbusiness show startup interest and Angi/CAC struggle; recurring monitoring discussion emerging.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient.',
        'ForumSignal':'N/A.',
        'GlassdoorSignal':'N/A.',
        'BrokerSignal':'Indirect support only; financial model proxy claims $787k revenue/$226k EBITDA but low-confidence non-operator source.',
        'ExpertProxyVerdict':'supports'
    },
    'Swim school': {
        'RedditSignal':'Contradicts high score: r/smallbusiness buildout post flags >$1M capex, HVAC/dehumidification, giant-hole resale risk, staffing churn, permitting, 6%-8% royalty; commenter says franchise not worth it vs AdWords/referrals.',
        'YouTubeSignal':'Contradicts/weakens: review video says $2M/year but would not open; Acquisitions Anonymous swim-school acquisition review surfaced.',
        'XSignal':'Insufficient credible operator tweets.',
        'ForumSignal':'No UnhappyFranchisee/BlueMauMau thread found.',
        'GlassdoorSignal':'Contradicts: Goldfish Glassdoor snippets cite high manager/entry-level turnover, low pay, poor management; comp/benefits ~2.9/5.',
        'BrokerSignal':'Mixed: BizBuySell swim school with $434,509 gross/$247,830 SDE supports profitable resales; franchise resale at fraction of build cost flags greenfield risk.',
        'ExpertProxyVerdict':'contradicts'
    },
    'Girls/youth sports performance academy': {
        'RedditSignal':'Insufficient/mixed: $45k/month youth sports training hypothesis found but not verified; gymnastics thread says rec classes subsidize teams/profits.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient.',
        'ForumSignal':'N/A.',
        'GlassdoorSignal':'N/A.',
        'BrokerSignal':'Insufficient.',
        'ExpertProxyVerdict':'insufficient'
    },
    'Senior home safety modifications / aging-in-place retrofits': {
        'RedditSignal':'Insufficient/support demand: r/sweatystartup senior-proofing thread suggests safety consultant model; AgingParents confirms pain but no P&L.',
        'YouTubeSignal':'Supports demand: TruBlue/aging-in-place video frames $10k senior problem; no unit economics.',
        'XSignal':'Insufficient.',
        'ForumSignal':'N/A.',
        'GlassdoorSignal':'N/A.',
        'BrokerSignal':'Insufficient.',
        'ExpertProxyVerdict':'insufficient'
    },
    'Home accessibility / aging-in-place modifications': {
        'RedditSignal':'Insufficient/support demand: aging-in-place pain validated; no direct P&L.',
        'YouTubeSignal':'Supports demand via TruBlue/aging-in-place video but no numbers.',
        'XSignal':'Insufficient.',
        'ForumSignal':'FranchiseChatter/101 Mobility already supports adjacent franchise economics; no new complaint signal.',
        'GlassdoorSignal':'Insufficient.',
        'BrokerSignal':'Insufficient.',
        'ExpertProxyVerdict':'supports'
    },
    'Metal Supermarkets': {
        'RedditSignal':'Supports/mixed: r/metalworking complains high prices, validating convenience/gross-margin model; Facebook proxy says ~$1.7M revenue/$325k owner cash flow.',
        'YouTubeSignal':'Supports: multiple Metal Supermarkets franchisee story/interview videos found (franchisor-produced; no direct P&L snippets).',
        'XSignal':'Insufficient.',
        'ForumSignal':'FranchiseChatter FDD review exists and supports Item 19 analysis; no complaint forum found.',
        'GlassdoorSignal':'Insufficient.',
        'BrokerSignal':'Franchise resale/franchise pages found; no detailed cash-flow resale extracted.',
        'ExpertProxyVerdict':'supports'
    },
    'Pool service': {
        'RedditSignal':'Supports: r/pools/r/sweatystartup buying-route threads; snippets warn 1x annual revenue may be high and <$300 CAC possible in some markets.',
        'YouTubeSignal':'Supports: Acquired Minds video on buying pool cleaning business and 4x profits; revenue stages video surfaced.',
        'XSignal':'Insufficient.',
        'ForumSignal':'N/A.',
        'GlassdoorSignal':'N/A.',
        'BrokerSignal':'Strongly supports: BizBuySell 52 pool results; sample routes $6,152/mo recurring ask $73,824 CF $72,162; $21,440/mo recurring ask $257,142 CF $103,549; $1.105M pool safety company CF $415k.',
        'ExpertProxyVerdict':'supports'
    },
    'Pet wellness membership / Scenthound-style': {
        'RedditSignal':'Contradicts high score: r/Scenthound/local threads cite quality issues, profit/volume focus, membership cancellations, uneven stores.',
        'YouTubeSignal':'Mixed: Scenthound videos claim membership model and 4-5 year payback; likely franchise-sales bias.',
        'XSignal':'Insufficient; brand account only, no credible operator complaint tweets surfaced.',
        'ForumSignal':'FranchiseChatter 2025: $49,900 franchise fee, 6% royalty, up to 1.5% brand fund, local ad spend; confirms cost burden.',
        'GlassdoorSignal':'Contradicts: Scenthound 2.6/5 employee rating, comp/benefits 2.4/5.',
        'BrokerSignal':'Insufficient.',
        'ExpertProxyVerdict':'contradicts'
    },
    'Head spa / scalp wellness': {
        'RedditSignal':'Insufficient: employee/esthetician interest positive; spa-owner proxy mentions months with little/no income; no repeatable economics.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient.',
        'ForumSignal':'N/A.',
        'GlassdoorSignal':'Insufficient.',
        'BrokerSignal':'Anecdotal social/listing claims only; no validated broker P&L.',
        'ExpertProxyVerdict':'insufficient'
    },
    'Pickleball club': {
        'RedditSignal':'Strongly supports deprioritize: r/Pickleball Picklr FDD review cites $13.8M cumulative corporate net loss, $12.5M shareholder deficit, median club EBITDA $87k on $938k revenue before debt/tax/owner salary, worst club -$175k/year, best $567k on $1.8M.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient.',
        'ForumSignal':'No UnhappyFranchisee/BlueMauMau thread found; Reddit served as de facto operator forum.',
        'GlassdoorSignal':'Insufficient.',
        'BrokerSignal':'Insufficient in this pass.',
        'ExpertProxyVerdict':'supports'
    },
    'GLP-1 clinic / body composition clinic': {
        'RedditSignal':'Contradicts/weakens: r/EntrepreneurRideAlong GLP-1 telehealth operator says folded in 5 months; r/medicine cites $500/mo clinic charge; business thread on semaglutide failing surfaced.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient.',
        'ForumSignal':'N/A.',
        'GlassdoorSignal':'N/A.',
        'BrokerSignal':'Medspa/weight-loss broker proxies exist but not enough to offset regulatory/CAC risk.',
        'ExpertProxyVerdict':'contradicts'
    },
    'Medspa / injectables': {
        'RedditSignal':'Supports deprioritize: NYC medspa owner $480k revenue/$60k take-home; $25k-$30k monthly burn; 80%-90% room utilization; 500 patients/month; Groupon dependence.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient.',
        'ForumSignal':'N/A.',
        'GlassdoorSignal':'Insufficient brand-specific owner signal.',
        'BrokerSignal':'Mixed: BizBuySell medspa listings include asset-rich $220k ask/$45,995 CF, $1.5M Houston listing, social/broker proxies at 3.8x EBITDA; proves liquidity but not easy ops.',
        'ExpertProxyVerdict':'supports'
    },
    'Cookie / bakery / cinnamon roll concept': {
        'RedditSignal':'Supports low/Needs proof: Crumbl threads mention top stores $3M-$4M but majority barely breaking even; 4-5 year payback; oversaturation/slowing demand.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient.',
        'ForumSignal':'No relevant UnhappyFranchisee thread surfaced.',
        'GlassdoorSignal':'Insufficient.',
        'BrokerSignal':'Insufficient specific listing signal.',
        'ExpertProxyVerdict':'supports'
    },
    'Specialty coffee / espresso bar': {
        'RedditSignal':'Supports deprioritize: coffee owner threads warn about high failure/rent/labor; seller-finance/distress path exists.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient.',
        'ForumSignal':'N/A.',
        'GlassdoorSignal':'N/A.',
        'BrokerSignal':'Insufficient.',
        'ExpertProxyVerdict':'supports'
    },
    'Premium bagel / morning counter': {
        'RedditSignal':'Mixed/support current discount: bagel owner year 4 $450k gross/$1,264 daily sales/18% YoY growth; acquisition example $1.2M sales, $4,100 rent/mo, $265k payroll, ~$200k owner earnings, $600k ask.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient.',
        'ForumSignal':'N/A.',
        'GlassdoorSignal':'N/A.',
        'BrokerSignal':'Reddit acquisition example provides broker-like comps; no BBS detail extracted.',
        'ExpertProxyVerdict':'supports'
    },
    'Meal prep / prepared foods / family dinner pickup': {
        'RedditSignal':'Supports deprioritize despite revenue: examples $50k/month meal delivery and $700k-$800k annual Bay Area service; delivery platforms take ~30%, spoilage/churn hard.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient.',
        'ForumSignal':'N/A.',
        'GlassdoorSignal':'N/A.',
        'BrokerSignal':'Insufficient.',
        'ExpertProxyVerdict':'supports'
    },
    'Gatsby Glass / shower glass': {
        'RedditSignal':'Insufficient.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient; no credible operator tweet surfaced.',
        'ForumSignal':'No complaint forum found.',
        'GlassdoorSignal':'Insufficient.',
        'BrokerSignal':'Insufficient; FDDIQ remains primary evidence.',
        'ExpertProxyVerdict':'insufficient'
    },
    'Lash / brow studio': {
        'RedditSignal':'Supports caution: esthetics/lash franchise employees cite overwork; one job proxy $1,800-$2,000 after taxes every two weeks.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient for Amazing Lash franchise-owner complaints.',
        'ForumSignal':'No complaint forum found.',
        'GlassdoorSignal':'Supports caution: Amazing Lash manager comp/benefits around 3.0/5.',
        'BrokerSignal':'Insufficient.',
        'ExpertProxyVerdict':'supports'
    },
    'IV therapy / hydration': {
        'RedditSignal':'Insufficient direct operator signal.',
        'YouTubeSignal':'Insufficient.',
        'XSignal':'Insufficient for Prime IV complaints.',
        'ForumSignal':'No complaint forum found.',
        'GlassdoorSignal':'Insufficient.',
        'BrokerSignal':'Indirect medspa broker evidence only.',
        'ExpertProxyVerdict':'insufficient'
    }
}

for row in rows:
    vals = signals.get(row['Category'])
    if vals:
        for c in new_cols:
            row[c] = vals.get(c, '')
    else:
        for c in new_cols:
            row.setdefault(c, '')
        if not row['ExpertProxyVerdict']:
            row['ExpertProxyVerdict'] = 'insufficient'

with path.open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f'Updated {len(rows)} rows; columns now: {len(fieldnames)}')
print('Rows with any expert signal:', sum(1 for r in rows if any(r.get(c) for c in new_cols[:-1]) and r.get('ExpertProxyVerdict') != 'insufficient'))
