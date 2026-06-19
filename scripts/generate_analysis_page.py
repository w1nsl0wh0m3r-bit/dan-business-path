#!/usr/bin/env python3
"""Generate the Swedish Candy Analysis page: reconciliation, taxonomy, scorecard, landed-cost model, Utah appendix."""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSS = """
:root{--paper:#f4ead8;--paper2:#eadcc4;--ink:#252018;--muted:#766b5e;--line:rgba(62,49,32,.16);--blue:#315e72;--clay:#b86f4d;--sage:#6f8066;--gold:#b78b38;--card:rgba(255,251,241,.76);--green:#4a7c3e;--red:#a8423a;--amber:#c4923a}
*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:"Space Grotesk",ui-sans-serif,system-ui,sans-serif;line-height:1.55;background:linear-gradient(180deg,var(--paper),var(--paper2));min-height:100dvh}
.shell{max-width:1180px;margin:auto;padding:26px 24px 72px}
nav{display:flex;justify-content:space-between;gap:16px;align-items:center;margin:0 0 36px;padding:10px;border:1px solid var(--line);border-radius:999px;background:rgba(255,251,241,.72)}
nav a{color:var(--ink);text-decoration:none;font-size:13px;padding:8px 11px;border-radius:999px}
h1{font-family:"Fraunces",Georgia,serif;font-size:clamp(2.0rem,4.5vw,3.8rem);line-height:.96;margin:12px 0 14px}
h2{font-family:"Fraunces",Georgia,serif;font-size:1.7rem;line-height:1.1;margin:44px 0 14px}
h3{margin:0 0 6px;font-size:1.05rem;font-weight:600}
h4{margin:18px 0 6px;font-size:.95rem;font-weight:600;color:var(--blue)}
.kicker{display:inline-flex;border:1px solid rgba(49,94,114,.18);background:rgba(255,251,241,.66);border-radius:999px;padding:8px 12px;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--blue);font-weight:700}
.lede{max-width:880px;color:var(--muted);font-size:1.1rem;margin-bottom:24px}
.card{border:1px solid var(--line);border-radius:16px;background:var(--card);padding:18px;margin:14px 0}
.card.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.card b{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:var(--blue);margin-bottom:4px}
.card strong{font-size:1.1rem}
.note{border-left:4px solid var(--clay);padding:15px 18px;background:rgba(184,111,77,.09);border-radius:14px;color:var(--muted);margin:14px 0}
.note.blue{border-left-color:var(--blue);background:rgba(49,94,114,.06)}
.note.green{border-left-color:var(--green);background:rgba(74,124,62,.06)}
.note.red{border-left-color:var(--red);background:rgba(168,66,58,.06)}
table{width:100%;border-collapse:collapse;background:rgba(255,251,241,.45);border:1px solid var(--line);border-radius:16px;overflow:hidden;margin:14px 0}
th{padding:10px;border-bottom:1px solid var(--line);text-align:left;font-size:10px;text-transform:uppercase;letter-spacing:.12em;color:var(--blue);background:rgba(255,251,241,.7)}
td{padding:9px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;font-size:13px}
td:first-child{font-weight:600}
tr:last-child td{border-bottom:none}
.badge{display:inline-block;padding:2px 9px;border-radius:999px;font-size:10px;font-weight:700;letter-spacing:.04em}
.b-pure{background:rgba(49,94,114,.12);color:var(--blue)}
.b-general{background:rgba(184,111,77,.12);color:var(--clay)}
.b-ecom{background:rgba(183,139,56,.12);color:var(--gold)}
.b-ghost{background:rgba(118,107,94,.12);color:var(--muted)}
.score{display:inline-block;width:28px;height:28px;border-radius:50%;text-align:center;line-height:28px;font-weight:700;font-size:12px;color:#fff}
.s-high{background:var(--green)}
.s-med{background:var(--amber)}
.s-low{background:var(--red)}
.s-na{background:var(--muted)}
.bucket-list{list-style:none;padding:0;margin:0}
.bucket-list li{padding:8px 0;border-bottom:1px solid var(--line);font-size:13px;display:flex;justify-content:space-between;align-items:center}
.bucket-list li:last-child{border-bottom:none}
.store-count{font-weight:700;color:var(--blue);font-size:12px}
.footnote{font-size:11px;color:var(--muted);margin-top:6px}
.footnote a{color:var(--blue);text-decoration:none}
@media(max-width:768px){.card.grid4{grid-template-columns:repeat(2,1fr)}}
"""

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Swedish Candy Analysis | Dan's Business Path</title><meta name="description" content="Universe reconciliation, taxonomy, acquisition scorecard, landed-cost model, and Utah cluster analysis for the US Swedish candy market."><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet"><style>{CSS}</style></head><body><main class="shell">
<nav><b>Dan's Business Path</b><div><a href="swedish-candy-map.html">Swedish Candy Map</a><a href="emerging-multi-unit-pipeline.html">Pipeline</a><a href="index.html">Home</a></div></nav>
<span class="kicker">Swedish candy · analysis layer</span>
<h1>Market Analysis &amp; Acquisition Framework</h1>
<p class="lede">Universe reconciliation, competitive taxonomy, acquisition scorecard for the top operators, a landed-cost / unit-economics model, and the Utah cluster appendix. This page sits on top of the <a href="swedish-candy-map.html">store map</a> and <a href="swedish-candy/scandycandy.html">comp profiles</a> — it does not modify them.</p>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<h2>1. Universe Reconciliation</h2>
<!-- ═══════════════════════════════════════════════════════════════════ -->

<div class="card grid4">
<div><b>Live Map Rows</b><strong>60</strong></div>
<div><b>Audit Universe</b><strong>71</strong></div>
<div><b>Delta</b><strong>+11 records</strong></div>
<div><b>Action</b><strong>Reconcile before scoring</strong></div>
</div>

<p>The live site map (<a href="swedish-candy-map.html">swedish-candy-map.html</a>) runs on a 60-row / 31-brand baseline (commit 10c9320). The June 19 exhaustive re-audit identified 71 records across ~38 brands. The 11-record gap comes from stores confirmed in research but not yet added to the live TABLE_ROWS:</p>

<table>
<thead><tr><th>Brand</th><th>Missing Stores</th><th>Evidence</th><th>On Comp Page?</th></tr></thead>
<tbody>
<tr><td>The Sweetish Fish</td><td>Chestnut Hill MA, Seaport MA, Sandwich MA (truck)</td><td>Cape News, WBZ-TV, Boston.com, official site</td><td>✅ Page exists (0 map rows)</td></tr>
<tr><td>The Pirate Candy Shop</td><td>Tampa FL, St. Petersburg FL</td><td>Delta report: "Tampa + St. Pete confirmed"</td><td>✅ Page exists (0 map rows)</td></tr>
<tr><td>Sugar Moose Candy</td><td>Kaysville UT, Salt Lake City UT (9th &amp; 9th)</td><td>Instagram (@wasatcheats), "SLC IS NOW OPEN"</td><td>✅ Page exists (0 map rows)</td></tr>
<tr><td>Swedish Moose Candy Co.</td><td>Provo UT, American Fork UT (2 additional beyond St. George)</td><td>SLUG Mag profile, Explore Utah Valley</td><td>✅ Page exists (1 of 3 stores mapped)</td></tr>
<tr><td>Lil Sweet Treat</td><td>Hoboken NJ (announced Apr 2026)</td><td>Hoboken Girl, Instagram</td><td>✅ May already be in 11 rows</td></tr>
<tr><td>Swedie Pop</td><td>Cerritos CA (Los Cerritos Center mall)</td><td>Indeed job posting, official site</td><td>✅ Already on map</td></tr>
</tbody>
</table>

<div class="note blue"><strong>Recommendation:</strong> Add the 7 confirmed missing stores (Sweetish Fish ×3, Pirate ×2, Sugar Moose ×2) and 2 Swedish Moose additional locations to the live map TABLE_ROWS in a future patch. This brings the map to 69 rows. The remaining 2 records (Hoboken announced, Swedie Pop already present) explain the remaining gap. Do NOT update posture labels or scoring on the live site until this reconciliation is merged.</div>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<h2>2. Competitive Taxonomy</h2>
<!-- ═══════════════════════════════════════════════════════════════════ -->

<p>The 71-record universe mixes very different business models. Splitting into 4 buckets clarifies who's actually an acquisition candidate vs. who's a different animal entirely.</p>

<h3>Bucket A — Pure-Play Swedish Candy Storefronts</h3>
<p class="footnote">Dedicated Swedish/Scandinavian candy retail. Pick-and-mix wall is the core concept. Scoreable as acquisition targets.</p>
<div class="card">
<ul class="bucket-list">
<li>BonBon <span class="store-count">6 stores</span></li>
<li>Lil Sweet Treat <span class="store-count">11 stores</span></li>
<li>ScandyCandy <span class="store-count">3 stores</span></li>
<li>Go Yummy <span class="store-count">3 stores</span></li>
<li>Saturday Candy Co. <span class="store-count">3 stores</span></li>
<li>Sockerbit <span class="store-count">2 open + 1 coming</span></li>
<li>Kändi <span class="store-count">2 open + 1 coming</span></li>
<li>Sweetish Candy <span class="store-count">2 stores</span></li>
<li>Swedish Moose Candy Co. <span class="store-count">3 stores (UT)</span></li>
<li>Nantasket Sweets By Swedes <span class="store-count">1 + 1 coming</span></li>
<li>Sodt <span class="store-count">1 + 1 coming</span></li>
<li>Saturday Candy Co. <span class="store-count">3 stores</span></li>
<li>Vännest <span class="store-count">1 store</span></li>
<li>So Swede <span class="store-count">1 store (UT)</span></li>
<li>Sugar Moose Candy <span class="store-count">2 stores (UT)</span></li>
<li>Madeleine's Candy Shop <span class="store-count">1 store</span></li>
<li>Mums — The Swedish Candy Co. <span class="store-count">1 store</span></li>
<li>Nikki's Candy <span class="store-count">1 store</span></li>
<li>BouNom Emporium <span class="store-count">1 store</span></li>
<li>All Aboard Candy <span class="store-count">1 store</span></li>
<li>Swedish Candy Culture <span class="store-count">1 store</span></li>
<li>Lilla Swedish Candy <span class="store-count">1 coming</span></li>
<li>Millie's Swedish Candy <span class="store-count">1 store</span></li>
<li>Sötsak <span class="store-count">1 coming</span></li>
<li>Trolley Car Sweets &amp; Treats <span class="store-count">1 store</span></li>
<li>Confetti Blossom <span class="store-count">1 store</span></li>
<li>Swedie Pop <span class="store-count">2 stores</span></li>
<li>The Sweetish Fish <span class="store-count">3 formats (truck/mall/pop-up)</span></li>
<li>The Pirate Candy Shop <span class="store-count">2 stores</span></li>
<li>Hej Hej <span class="store-count">1 pop-up (dual-concept: hot dogs + candy)</span></li>
</ul>
</div>

<h3>Bucket B — General Candy Stores (Carry Swedish as a Category)</h3>
<p class="footnote">Swedish candy is a product line, not the concept. Not acquisition targets for a Swedish candy thesis, but useful for understanding how existing retailers incorporate the category.</p>
<div class="card">
<ul class="bucket-list">
<li>Big Top Candy Shop <span class="store-count">1 store — retro/nostalgic (Austin TX, est. 2007)</span></li>
<li>Yummi Joy <span class="store-count">1 store — Toy Joy spinoff (Austin TX)</span></li>
<li>To The Moon <span class="store-count">1 store — general candy + Dubai chocolate (FL)</span></li>
</ul>
</div>

<h3>Bucket C — Ecommerce / Importers / Content</h3>
<p class="footnote">No physical storefront. Different business model — logistics/brand/media, not retail. Not acquisition targets for storefront retail, but potential suppliers or strategic threats.</p>
<div class="card">
<ul class="bucket-list">
<li>Goodis <span class="store-count">313+ SKUs, ecommerce only (Carlstadt NJ)</span></li>
<li>Swedish Candy Land <span class="store-count">Online, ships worldwide from Sweden</span></li>
<li>Swedish Crave <span class="store-count">Content/review site — not a store</span></li>
<li>Candy King (Cloetta) <span class="store-count">Corporate — 1 US flagship, hundreds in Europe</span></li>
</ul>
</div>

<h3>Bucket D — Ghosts / Unverified</h3>
<p class="footnote">Zero public footprint. May be real stores with no web presence, data errors, or closed. Recommend removal from the active universe until verified.</p>
<div class="card">
<ul class="bucket-list">
<li>Karameller <span class="store-count">No public information found</span></li>
<li>Sukker Baby <span class="store-count">Toronto-based — excluded from US scope</span></li>
</ul>
</div>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<h2>3. Acquisition Scorecard — Top 12 Pure-Play Operators</h2>
<!-- ═══════════════════════════════════════════════════════════════════ -->

<p>Scored on 5 dimensions, each rated 1–5. Higher = more attractive as an acquisition or partnership target. Scores are directional — they encode what's publicly knowable, not actual financials.</p>

<div class="note blue"><strong>Scoring criteria:</strong><br>
<strong>Scale (1–5):</strong> Store count + revenue signals. 1 = single store, 5 = 6+ stores or $10M+ revenue.<br>
<strong>Growth Velocity (1–5):</strong> Expansion speed. 1 = static, 5 = 3+ stores in <2 years.<br>
<strong>Market Position (1–5):</strong> First-mover advantage, market dominance. 1 = follower, 5 = category-defining.<br>
<strong>Sellability (1–5):</strong> How likely the founder would sell. Based on founder age, solo vs. team, fatigue signals. 1 = unlikely, 5 = strong signals.<br>
<strong>Cleanliness (1–5):</strong> How well-understood the business is. 1 = opaque, 5 = transparent operations, press coverage, clear financials.</p>

<table>
<thead><tr>
<th>Rank</th><th>Brand</th><th>Stores</th>
<th>Scale</th><th>Growth</th><th>Position</th><th>Sellability</th><th>Clean</th>
<th>Total</th><th>Posture</th>
</tr></thead>
<tbody>

<tr><td>1</td><td>BonBon</td><td>6</td>
<td><span class="score s-high">5</span></td><td><span class="score s-med">3</span></td><td><span class="score s-high">5</span></td><td><span class="score s-low">2</span></td><td><span class="score s-high">4</span></td>
<td><strong>19</strong></td><td><span class="badge b-pure">Comp / benchmark</span></td></tr>

<tr><td>2</td><td>Lil Sweet Treat</td><td>11</td>
<td><span class="score s-high">5</span></td><td><span class="score s-high">5</span></td><td><span class="score s-high">4</span></td><td><span class="score s-med">3</span></td><td><span class="score s-med">3</span></td>
<td><strong>20</strong></td><td><span class="badge b-pure">Comp / scale benchmark</span></td></tr>

<tr><td>3</td><td>ScandyCandy</td><td>3</td>
<td><span class="score s-med">3</span></td><td><span class="score s-high">5</span></td><td><span class="score s-med">3</span></td><td><span class="score s-med">3</span></td><td><span class="score s-med">3</span></td>
<td><strong>17</strong></td><td><span class="badge b-pure">Target watch</span></td></tr>

<tr><td>4</td><td>Saturday Candy Co.</td><td>3</td>
<td><span class="score s-med">3</span></td><td><span class="score s-high">4</span></td><td><span class="score s-med">3</span></td><td><span class="score s-high">4</span></td><td><span class="score s-med">3</span></td>
<td><strong>17</strong></td><td><span class="badge b-pure">Target watch</span></td></tr>

<tr><td>5</td><td>Go Yummy</td><td>3</td>
<td><span class="score s-med">3</span></td><td><span class="score s-med">3</span></td><td><span class="score s-med">3</span></td><td><span class="score s-med">3</span></td><td><span class="score s-low">2</span></td>
<td><strong>14</strong></td><td><span class="badge b-pure">Comp</span></td></tr>

<tr><td>6</td><td>Sockerbit</td><td>2+1</td>
<td><span class="score s-med">3</span></td><td><span class="score s-low">2</span></td><td><span class="score s-high">4</span></td><td><span class="score s-med">3</span></td><td><span class="score s-high">4</span></td>
<td><strong>16</strong></td><td><span class="badge b-pure">Comp / legacy benchmark</span></td></tr>

<tr><td>7</td><td>Kändi</td><td>2+1</td>
<td><span class="score s-med">3</span></td><td><span class="score s-med">3</span></td><td><span class="score s-low">2</span></td><td><span class="score s-low">2</span></td><td><span class="score s-low">2</span></td>
<td><strong>12</strong></td><td><span class="badge b-pure">Comp</span></td></tr>

<tr><td>8</td><td>Sweetish Candy</td><td>2</td>
<td><span class="score s-med">3</span></td><td><span class="score s-low">2</span></td><td><span class="score s-med">3</span></td><td><span class="score s-med">3</span></td><td><span class="score s-high">4</span></td>
<td><strong>15</strong></td><td><span class="badge b-pure">Comp / ecommerce benchmark</span></td></tr>

<tr><td>9</td><td>Swedish Moose Candy Co.</td><td>3</td>
<td><span class="score s-med">3</span></td><td><span class="score s-med">3</span></td><td><span class="score s-med">3</span></td><td><span class="score s-med">3</span></td><td><span class="score s-low">2</span></td>
<td><strong>14</strong></td><td><span class="badge b-pure">Target watch (UT)</span></td></tr>

<tr><td>10</td><td>Nantasket Sweets</td><td>1+1</td>
<td><span class="score s-low">2</span></td><td><span class="score s-med">3</span></td><td><span class="score s-low">2</span></td><td><span class="score s-high">4</span></td><td><span class="score s-med">3</span></td>
<td><strong>14</strong></td><td><span class="badge b-pure">Target watch (NE)</span></td></tr>

<tr><td>11</td><td>Sodt</td><td>1+1</td>
<td><span class="score s-low">2</span></td><td><span class="score s-med">3</span></td><td><span class="score s-low">2</span></td><td><span class="score s-med">3</span></td><td><span class="score s-med">3</span></td>
<td><strong>13</strong></td><td><span class="badge b-pure">Target watch (NE)</span></td></tr>

<tr><td>12</td><td>Mums</td><td>1</td>
<td><span class="score s-low">2</span></td><td><span class="score s-low">2</span></td><td><span class="score s-low">2</span></td><td><span class="score s-med">3</span></td><td><span class="score s-low">2</span></td>
<td><strong>11</strong></td><td><span class="badge b-pure">Comp</span></td></tr>

</tbody>
</table>

<div class="note"><strong>Read this table carefully.</strong> Lil Sweet Treat scores highest (20/25) but is not a pure Swedish candy play — it's global pick-and-mix. BonBon (19/25) is the category leader but likely too large/expensive to acquire. The most interesting acquisition candidates are <strong>ScandyCandy (17)</strong> and <strong>Saturday Candy Co. (17)</strong> — both founded by Swedish-connected operators, both growing fast, both at a size where a deal is conceivable. <strong>Nantasket Sweets (14)</strong> scores lower on scale/position but highest on sellability (4/5) — a solo female founder who's been running it for 5+ years may be the most likely to actually take a call.</div>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<h2>4. Landed-Cost / Unit Economics Model</h2>
<!-- ═══════════════════════════════════════════════════════════════════ -->

<p class="lede">The single most important unanswered question: does the math work? A Swedish candy store is fundamentally an import logistics business with a retail front. The cost structure depends entirely on <strong>how you source the candy</strong>.</p>

<h3>Two Sourcing Paths</h3>

<div class="card">
<h4>Path A — Direct Import (FCL, self-managed)</h4>
<p>Buy full pallets/containers directly from Swedish manufacturers (Bubs, Malaco, Fazer, Candy People). You own customs clearance, warehousing, and distribution. This is what BonBon and Sweetish likely do.</p>
<table>
<thead><tr><th>Cost Component</th><th>Per Lb</th><th>Notes / Source</th></tr></thead>
<tbody>
<tr><td>Brand wholesale (Bubs/Malaco, case)</td><td>$3.50</td><td>Triangulated from Swedish retail (~$3.65/lb at 90 SEK/kg) less ~40% grocery margin. Brand case pricing higher than grocery wholesale due to branded packaging.</td></tr>
<tr><td>Export packing &amp; palletizing</td><td>$0.15</td><td>Standard export pallet prep</td></tr>
<tr><td>Ocean freight (FCL, Gothenburg → NYC)</td><td>$0.10</td><td>~$1,800 per 20ft container, ~18,000 lb candy per container (FreightAmigo, Freightos 2026 rates)</td></tr>
<tr><td>Insurance (0.5%)</td><td>$0.02</td><td>Marine cargo insurance</td></tr>
<tr><td><strong>CIF value at US port</strong></td><td><strong>$3.77</strong></td><td>Sum of above</td></tr>
<tr><td>US import duty — HTS 1704.90 (12.2%)</td><td>$0.46</td><td>Sugar confectionery, not containing cocoa. General/MFN rate for EU goods. <a href="https://hts.usitc.gov/search?query=1704.90.90.00">USITC HTS lookup</a></td></tr>
<tr><td>MPF + HMF fees</td><td>$0.02</td><td>Merchandise processing + harbor maintenance</td></tr>
<tr><td>Customs broker</td><td>$0.03</td><td>Per-shipment brokerage</td></tr>
<tr><td>Inland transport + warehousing</td><td>$0.30</td><td>Port to warehouse, cold/dry storage, pick/pack</td></tr>
<tr><td><strong>Total landed cost</strong></td><td><strong>$4.58</strong></td><td></td></tr>
<tr><td>Shrink / waste / spoilage (5%)</td><td>$0.23</td><td>Open-bin display waste, expired product</td></tr>
<tr><td><strong>Effective COGS per lb</strong></td><td style="color:var(--green);font-weight:700">$4.81</td><td></td></tr>
<tr><td>Retail price per lb</td><td>$14.00</td><td>Market standard (BonBon, ScandyCandy, most stores)</td></tr>
<tr><td><strong>Gross margin per lb</strong></td><td style="color:var(--green);font-weight:700;font-size:15px">$9.19 (65.6%)</td><td></td></tr>
</tbody>
</table>
</div>

<div class="card">
<h4>Path B — Via US Distributor (DDP delivered)</h4>
<p>Buy from US-based distributors like ScandiWholesale, SweedsCandy, SwedishCandyWholesale, or Swedelicious. They handle import, customs, and freight. You pay a premium but avoid operational complexity. This is what most small/single-store operators do.</p>
<table>
<thead><tr><th>Cost Component</th><th>Per Lb</th><th>Notes / Source</th></tr></thead>
<tbody>
<tr><td>US distributor wholesale (avg of observed prices)</td><td>$8.40</td><td>From SwedishCandyWholesale.com actual prices: Bubs Skulls $9.59/lb, Happy Flowers $7.14/lb, avg across 7 SKUs = $8.40/lb (see 25-SKU model below)</td></tr>
<tr><td>Inbound freight (domestic)</td><td>$0.30</td><td>Ground shipping from distributor warehouse</td></tr>
<tr><td><strong>Effective COGS per lb</strong></td><td style="color:var(--red);font-weight:700">$8.70</td><td></td></tr>
<tr><td>Shrink / waste / spoilage (5%)</td><td>$0.44</td><td></td></tr>
<tr><td><strong>Net COGS per lb</strong></td><td style="color:var(--red);font-weight:700">$9.14</td><td></td></tr>
<tr><td>Retail price per lb</td><td>$14.00</td><td></td></tr>
<tr><td><strong>Gross margin per lb</strong></td><td style="color:var(--red);font-weight:700;font-size:15px">$4.86 (34.7%)</td><td></td></tr>
</tbody>
</table>
</div>

<div class="note red"><strong>The spread is massive.</strong> Direct import yields 66% gross margin vs. 35% through a distributor. On a store selling 200 lb/week (10,400 lb/year), that's <strong>$44K/year</strong> in gross profit difference. At 3 stores doing 600 lb/week, the spread is <strong>$131K/year</strong>. Direct import isn't an optimization — it's the difference between a viable business and a marginal one. The operational complexity (customs, freight forwarding, working capital, warehouse) is the barrier to entry that protects margins.</div>

<h3>25-SKU Price Model — Actual Distributor Prices</h3>
<p class="footnote">Prices from SwedishCandyWholesale.com and SwedishSweetsWholesale.com (June 2026). Direct-import estimates based on model above (~55% of distributor price = landed cost).</p>

<table>
<thead><tr>
<th>SKU</th><th>Brand</th><th>Category</th>
<th>Bag (kg)</th><th>Distributor $</th>
<th>$/lb (dist.)</th>
<th>Est. direct import $/lb</th>
<th>Margin @ $14 (direct)</th>
</tr></thead>
<tbody>
<tr><td>Sour Dizzy Skull</td><td>Bubs</td><td>Foam / sour</td><td>2.6</td><td>$54.99</td><td>$9.59</td><td>$5.27</td><td>62%</td></tr>
<tr><td>Wild Foamy Strawberry Pomegranate Oval</td><td>Bubs</td><td>Foam</td><td>2.8</td><td>$61.90</td><td>$10.04</td><td>$5.52</td><td>61%</td></tr>
<tr><td>Sour Foam Rombs Tutti Frutti</td><td>Bubs</td><td>Foam / sour</td><td>2.6</td><td>$54.99</td><td>$9.59</td><td>$5.27</td><td>62%</td></tr>
<tr><td>Sour Fruity Pear Mini</td><td>Bubs</td><td>Gummy / sour</td><td>2.6</td><td>$49.99</td><td>$8.72</td><td>$4.80</td><td>66%</td></tr>
<tr><td>Giant Sour Skulls</td><td>Bubs</td><td>Foam / sour</td><td>3.2</td><td>$61.50</td><td>$8.72</td><td>$4.80</td><td>66%</td></tr>
<tr><td>Banana Bubs (Foamy)</td><td>Bubs</td><td>Foam</td><td>2.8</td><td>$58.40</td><td>$9.47</td><td>$5.21</td><td>63%</td></tr>
<tr><td>Happy Flowers</td><td>Astra Sweets</td><td>Gummy</td><td>2.5</td><td>$39.35</td><td>$7.14</td><td>$3.93</td><td>72%</td></tr>
<tr><td>Bubs Pick-N-Mix (½lb bag ×12)</td><td>Bubs</td><td>Assorted</td><td>2.7</td><td>$89.88</td><td>$7.49</td><td>$4.12</td><td>71%</td></tr>
<tr><td>1kg Mixed Assortment</td><td>Various</td><td>Pick &amp; Mix</td><td>1.0</td><td>$17.49</td><td>$7.94</td><td>$4.37</td><td>69%</td></tr>
<tr><td>Bubs Pick-N-Mix (100 lb pallet)</td><td>Bubs</td><td>Bulk pallet</td><td>45.4</td><td>$1,999</td><td>$6.40</td><td>$3.52</td><td>75%</td></tr>
<tr><td>Malaco Fish (est.)</td><td>Malaco/Cloetta</td><td>Gummy</td><td>2.5</td><td>~$42</td><td>$7.62</td><td>$4.19</td><td>70%</td></tr>
<tr><td>Fazer Tutti Frutti (est.)</td><td>Fazer</td><td>Foam</td><td>2.5</td><td>~$44</td><td>$7.98</td><td>$4.39</td><td>69%</td></tr>
<tr><td>Candy People Mini Gummy (est.)</td><td>Candy People</td><td>Gummy</td><td>2.5</td><td>~$40</td><td>$7.26</td><td>$3.99</td><td>71%</td></tr>
<tr><td>Salty Licorice (est.)</td><td>Malaco</td><td>Licorice</td><td>2.5</td><td>~$46</td><td>$8.34</td><td>$4.59</td><td>67%</td></tr>
<tr><td>Salmiak Licorice (est.)</td><td>Fazer</td><td>Licorice</td><td>2.5</td><td>~$48</td><td>$8.71</td><td>$4.79</td><td>66%</td></tr>
<tr><td>Cola Bottle Gummies (est.)</td><td>Various</td><td>Gummy</td><td>2.5</td><td>~$41</td><td>$7.44</td><td>$4.09</td><td>71%</td></tr>
<tr><td>Fizzy Sour Worms (est.)</td><td>Various</td><td>Gummy / sour</td><td>2.5</td><td>~$43</td><td>$7.80</td><td>$4.29</td><td>69%</td></tr>
<tr><td>Chocolate-covered Marshmallow (est.)</td><td>Various</td><td>Chocolate</td><td>2.0</td><td>~$38</td><td>$8.62</td><td>$4.74</td><td>66%</td></tr>
<tr><td>Raspberry Gummy (est.)</td><td>Malaco</td><td>Gummy</td><td>2.5</td><td>~$42</td><td>$7.62</td><td>$4.19</td><td>70%</td></tr>
<tr><td>Pomegranate Gummy (est.)</td><td>Bubs</td><td>Gummy</td><td>2.5</td><td>~$45</td><td>$8.16</td><td>$4.49</td><td>68%</td></tr>
<tr><td>Foam Hearts (est.)</td><td>Candy People</td><td>Foam</td><td>2.5</td><td>~$39</td><td>$7.08</td><td>$3.89</td><td>72%</td></tr>
<tr><td>Sour Apple Rings (est.)</td><td>Various</td><td>Gummy / sour</td><td>2.5</td><td>~$42</td><td>$7.62</td><td>$4.19</td><td>70%</td></tr>
<tr><td>Toffee Caramels (est.)</td><td>Malaco</td><td>Caramel</td><td>2.0</td><td>~$40</td><td>$9.07</td><td>$4.99</td><td>64%</td></tr>
<tr><td>Jelly Rings (est.)</td><td>Fazer</td><td>Gummy</td><td>2.5</td><td>~$41</td><td>$7.44</td><td>$4.09</td><td>71%</td></tr>
<tr><td>Dry-Roasted Almond Choc (est.)</td><td>Various</td><td>Chocolate</td><td>2.0</td><td>~$42</td><td>$9.53</td><td>$5.24</td><td>63%</td></tr>
</tbody>
</table>
<p class="footnote">Items marked (est.) are reasonable estimates based on category pricing patterns from observed distributor prices. Direct-import estimates use the model: landed cost ≈ 55% of distributor price (distributor adds ~45% margin for their import/freight/warehousing/profit). Actual costs vary by brand, volume, and negotiation.</p>

<h3>Store-Level Unit Economics</h3>

<div class="card">
<h4>Pro-forma: Single Store — Moderate Traffic (est. 150 lb/week)</h4>
<table>
<thead><tr><th>Line Item</th><th>Direct Import</th><th>Via Distributor</th></tr></thead>
<tbody>
<tr><td>Weekly volume</td><td>150 lb</td><td>150 lb</td></tr>
<tr><td>Revenue/week @ $14/lb</td><td>$2,100</td><td>$2,100</td></tr>
<tr><td>Annual revenue</td><td>$109,200</td><td>$109,200</td></tr>
<tr><td>COGS/lb</td><td>$4.81</td><td>$9.14</td></tr>
<tr><td>Annual COGS</td><td>$37,500</td><td>$71,200</td></tr>
<tr><td><strong>Gross profit</strong></td><td style="color:var(--green)"><strong>$71,700 (65.7%)</strong></td><td style="color:var(--red)"><strong>$38,000 (34.8%)</strong></td></tr>
<tr><td>Rent (est. 1,200 SF @ $45/SF)</td><td>$54,000</td><td>$54,000</td></tr>
<tr><td>Labor (2 PT @ $18/hr)</td><td>$67,000</td><td>$67,000</td></tr>
<tr><td>Utilities + insurance + POS</td><td>$18,000</td><td>$18,000</td></tr>
<tr><td>Marketing / content</td><td>$12,000</td><td>$12,000</td></tr>
<tr><td><strong>Total opex</strong></td><td><strong>$151,000</strong></td><td><strong>$151,000</strong></td></tr>
<tr><td><strong>Net operating income</strong></td><td style="color:var(--red)"><strong>−$79,300</strong></td><td style="color:var(--red)"><strong>−$113,000</strong></td></tr>
</tbody>
</table>
<div class="note red"><strong>This doesn't work at 150 lb/week.</strong> A single store needs ~400+ lb/week to break even, and that's with direct import. At distributor pricing, the math may never work for a standalone single store.</div>
</div>

<div class="card">
<h4>Pro-forma: Single Store — High Traffic (est. 400 lb/week)</h4>
<table>
<thead><tr><th>Line Item</th><th>Direct Import</th><th>Via Distributor</th></tr></thead>
<tbody>
<tr><td>Weekly volume</td><td>400 lb</td><td>400 lb</td></tr>
<tr><td>Annual revenue</td><td>$291,200</td><td>$291,200</td></tr>
<tr><td>Annual COGS</td><td>$100,000</td><td>$190,000</td></tr>
<tr><td><strong>Gross profit</strong></td><td style="color:var(--green)"><strong>$191,200 (65.7%)</strong></td><td style="color:var(--amber)"><strong>$101,200 (34.8%)</strong></td></tr>
<tr><td>Opex (same as above)</td><td>$151,000</td><td>$151,000</td></tr>
<tr><td><strong>Net operating income</strong></td><td style="color:var(--green)"><strong>+$40,200</strong></td><td style="color:var(--red)"><strong>−$49,800</strong></td></tr>
</tbody>
</table>
</div>

<div class="card">
<h4>Pro-forma: 3-Store Operator (est. 1,000 lb/week total)</h4>
<table>
<thead><tr><th>Line Item</th><th>Direct Import</th></tr></thead>
<tbody>
<tr><td>Annual revenue</td><td>$728,000</td></tr>
<tr><td>Annual COGS (3 stores)</td><td>$250,000</td></tr>
<tr><td><strong>Gross profit</strong></td><td style="color:var(--green)"><strong>$478,000 (65.7%)</strong></td></tr>
<tr><td>Rent (3 stores)</td><td>$140,000</td></tr>
<tr><td>Labor (6 PT + 1 manager)</td><td>$230,000</td></tr>
<tr><td>Utilities + insurance + POS</td><td>$48,000</td></tr>
<tr><td>Marketing + shared warehouse</td><td>$35,000</td></tr>
<tr><td><strong>Total opex</strong></td><td><strong>$453,000</strong></td></tr>
<tr><td><strong>Net operating income</strong></td><td style="color:var(--green)"><strong>+$25,000</strong></td></tr>
</tbody>
</table>
</div>

<div class="note green"><strong>The economics only work at scale with direct import.</strong> A 3-store operator doing 1,000 lb/week total with direct import is barely cash-flow positive ($25K NOI) before owner comp. To generate $75-100K in owner income, you need either higher per-store volume (500+ lb/week each) or 5+ stores. This explains why BonBon (6 stores, ~$10M revenue) is the only clearly profitable operator — they have the scale to make direct import work and amortize fixed costs.</div>

<h4>Key Variable: Pounds Per Week Per Store</h4>
<p class="footnote">The entire thesis hinges on this number. 200 lb/week is a store doing ~28 customers/day at 1 lb each. 400 lb/week is ~57 customers/day. These are plausible for a viral location (TikTok-driven foot traffic) but unproven for steady-state operation post-hype.</p>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<h2>5. Utah Cluster Appendix</h2>
<!-- ═══════════════════════════════════════════════════════════════════ -->

<p>Three Swedish candy brands competing in the same Utah metro (American Fork, Provo, Kaysville, Salt Lake City, St. George) is genuinely unusual. The question is <em>why</em>.</p>

<div class="card">
<h4>The Operators</h4>
<table>
<thead><tr><th>Brand</th><th>Locations</th><th>Founder</th><th>Opened</th></tr></thead>
<tbody>
<tr><td>Swedish Moose Candy Co.</td><td>St. George, Provo, American Fork</td><td>Simonsen &amp; Mård-Castman (Swedish-connected)</td><td>2024–25</td></tr>
<tr><td>So Swede</td><td>American Fork</td><td>Olive Redd</td><td>June 2025</td></tr>
<tr><td>Sugar Moose Candy</td><td>Kaysville, Salt Lake City</td><td>Unknown</td><td>2024–25</td></tr>
</tbody>
</table>
</div>

<h4>Possible Structural Drivers</h4>
<div class="card">
<ol style="padding-left:18px;line-height:1.8">
<li><strong>Scandinavian heritage:</strong> Utah has a significant Scandinavian-American population due to 19th-century Mormon migration from Sweden, Denmark, and Norway. Cultural affinity for Nordic products is higher than typical US markets.</li>
<li><strong>LDS culture and candy:</strong> Mormon culture emphasizes family activities, and the LDS Word of Wisdom discourages alcohol/coffee/tea — making candy and sweets a more central social/lifestyle category than in secular markets. "Saturday candy" (<em>lördagsgodis</em>) maps naturally onto LDS family night traditions.</li>
<li><strong>Low rent / low labor costs:</strong> Utah County (American Fork, Provo) has significantly lower retail rent than NYC, LA, or South Florida. A store that's marginal in Manhattan may be profitable in American Fork.</li>
<li><strong>Founder ecosystem:</strong> The founders may know each other — Swedish Moose and So Swede are both in American Fork. One may have inspired (or spun off from) the other.</li>
<li><strong>TikTok timing:</strong> All three launched in 2024–25, right at the peak of the Swedish candy TikTok wave. They're riding the same trend simultaneously in a market where barriers to entry are low.</li>
</ol>
</div>

<div class="note blue"><strong>Take:</strong> The Utah cluster is likely driven by a combination of Scandinavian cultural affinity + LDS family-candy culture + low barriers to entry. It's worth monitoring as a <em>template for secondary-market viability</em> — if Swedish candy works in American Fork, UT (pop. 33,000), it can work in similar family-oriented, lower-cost markets. But 3 brands competing in the same metro is also a saturation signal. The cluster will likely consolidate to 1–2 survivors.</div>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<h2>Methodology &amp; Sources</h2>
<!-- ═══════════════════════════════════════════════════════════════════ -->

<div class="card">
<h4>Landed-Cost Model Sources</h4>
<ul style="padding-left:18px;line-height:1.7">
<li><strong>Swedish domestic retail:</strong> Reddit r/sweden lösgodis pricing (79.80–90 SEK/kg), Instagram creator content</li>
<li><strong>US distributor wholesale:</strong> SwedishCandyWholesale.com actual prices (7 SKUs, June 2026), SwedishSweetsWholesale.com ($17.49/kg)</li>
<li><strong>US import duty:</strong> HTS 1704.90.90.00 — 12.2% general rate (<a href="https://hts.usitc.gov">USITC</a>)</li>
<li><strong>Ocean freight:</strong> FreightAmigo ($1,600–$1,900 per 20ft, Northern Europe → US East Coast)</li>
<li><strong>Duty-free option:</strong> HTS 1704.90 "Special: Free" may apply under certain trade preferences — not assumed in this model</li>
<li><strong>US wholesale ecosystem:</strong> ScandiWholesale (DDP), SweedsCandy (pallets/containers), Swedelicious (1,370+ SKUs, 30+ brands direct from Sweden)</li>
</ul>
<h4>Scorecard Sources</h4>
<ul style="padding-left:18px;line-height:1.7">
<li>Store counts and locations: Live map TABLE_ROWS + June 19 delta report</li>
<li>Revenue estimates: RocketReach (BonBon ~$10M), ZoomInfo (Sockerbit $1–5M)</li>
<li>Founder profiles: News articles, Instagram, press features (see individual <a href="swedish-candy/scandycandy.html">comp profiles</a>)</li>
<li>Sellability scores: Directional estimates based on founder age, solo vs. team, operating history, and growth stage</li>
</ul>
<p class="footnote">All financial figures are estimates and directional models, not verified financials. The landed-cost model should be validated against actual quotes from Swedish manufacturers and freight forwarders before any investment decision.</p>
</div>

<div class="note"><strong>Next steps if this lane stays alive:</strong></p>
<ol style="padding-left:18px;line-height:1.8">
<li><strong>Validate the model:</strong> Get actual FCL quotes from Bubs/Malaco/Fazer and a freight forwarder. The $4.81/lb direct-import COGS is the linchpin.</li>
<li><strong>Get real volume data:</strong> Sit outside BonBon's Allen St store with a clicker for a day. How many customers? How many pounds per customer?</li>
<li><strong>Pick 3–5 targets and do real diligence:</strong> ScandyCandy, Saturday Candy, Nantasket Sweets are the best candidates by score + sellability + size. Founder outreach → P&L review → lease terms → supplier relationships.</li>
<li><strong>Stress-test trend durability:</strong> 18 months into the TikTok wave. Is traffic steady, declining, or still growing? Compare Q2 2026 foot traffic to Q4 2025.</li>
</ol>
</div>

</main></body></html>"""

out_path = os.path.join(BASE_DIR, "swedish-candy-analysis.html")
with open(out_path, "w") as f:
    f.write(page)
print(f"Generated {out_path} ({len(page):,} bytes)")
