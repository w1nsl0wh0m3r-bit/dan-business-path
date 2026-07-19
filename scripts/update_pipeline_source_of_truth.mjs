import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";

const repo = path.resolve(import.meta.dirname, "..");
const workspace = "/Users/winslow/.openclaw/workspace";
function csv(name) {
  const p = path.join(workspace, "research", name);
  const code = "import csv,json,sys; print(json.dumps(list(csv.DictReader(open(sys.argv[1], newline='')))))";
  return JSON.parse(execFileSync("python3", ["-c", code, p], { encoding: "utf8", maxBuffer: 1024 * 1024 * 20 }));
}

const top20Raw = csv("2026-06-18-consumer-product-brand-top20-ranking.csv").slice(0, 20);
const corpus = csv("2026-06-18-systematic-consumer-product-brand-corpus.csv");
const operators = csv("2026-06-18-v2-named-multi-unit-operator-universe-final.csv");
const proof = csv("2026-06-18-named-multi-unit-operator-proof-sprint-25.csv");

function splitUrls(value = "") {
  return String(value)
    .split(/[;\s]+/)
    .map((u) => u.trim())
    .filter(Boolean)
    .map((u) => /^https?:\/\//i.test(u) ? u : (/^[a-z0-9.-]+\.[a-z]{2,}(\/.*)?$/i.test(u) ? `https://${u}` : ""))
    .filter(Boolean);
}

function linkSet(name, geography, sourceUrls = "") {
  const urls = splitUrls(sourceUrls);
  const website = urls.find((u) => !/instagram\.com|facebook\.com|linkedin\.com|yelp\.com|bizjournals\.com|prnewswire\.com|wikipedia\.org|google\.com/i.test(u)) || urls[0] || "";
  const instagram = urls.find((u) => /instagram\.com/i.test(u)) || `https://www.instagram.com/explore/search/keyword/?q=${encodeURIComponent(name)}`;
  const maps = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(`${name} ${geography || ""}`.trim())}`;
  return { website, maps, instagram };
}

const top20 = top20Raw.map((r) => {
  const brand = r.brand;
  const overrides = {
    "Wanderlust Creamery": {
      posture: "Diligence gate",
      next: "Confirm the FB capital ask is current; request 24-month store P&L, debt, leases, cash/AP/tax status, use of proceeds, pipeline capex, and last-13-week sales/labor/COGS.",
      risk: "Could be working-capital stress or closed-store losses; no valuation talk before numbers."
    },
    "Starship Bagel": {
      posture: "DFW proof sprint",
      next: "Mystery-shop Lewisville, Downtown Dallas, and North Dallas; test central production quality, traffic, sellout cadence, wholesale/catering, and manager-run economics.",
      risk: "Founder/product dependence and whether North Dallas performs like the flagship."
    },
    "Cookie Society": {
      posture: "DFW proof sprint",
      next: "Mystery-shop all five stores; validate traffic by daypart, corporate gifting/catering, staffing, and 30% haircut economics.",
      risk: "Crumbl/boutique-cookie category pressure and dessert-cycle volatility."
    },
    "Botolino Gelato": {
      posture: "DFW proof sprint",
      next: "Visit Greenville, Preston Hollow, Bishop Arts, and Plano; test production scalability, off-peak demand, cakes/pints/catering, and founder dependence.",
      risk: "Seasonal frozen-dessert economics and Carlo/product dependence."
    },
    "ScandyCandy": {
      posture: "Watch-only after Swedish candy downgrade",
      next: "Do not approach now. Track 6-12 month demand decay, BUBS/Sockerbit mass retail pressure, copycat openings, and any founder-fatigue/distress signal.",
      risk: "Category scarcity is compressing as BUBS and Sockerbit go mass retail; specialty-store moat is thin."
    },
    "Jeff's Bagel Run": {
      posture: "Pass on brand acquisition",
      next: "Only evaluate as franchisee/area-developer path if Dan opts into operator build; use FDD and territory-rights diligence.",
      risk: "PE-backed brand acquisition is unrealistic for Dan."
    }
  };
  const o = overrides[brand] || {};
  return {
    rank: Number(r.final_rank),
    brand,
    category: r.category,
    market: r.geography,
    units: r.estimated_units_verified,
    score: r.total_score,
    posture: o.posture || r.dan_entry_path || "Watch / compare",
    why: r.why_ranked_here,
    next: o.next || r.next_deep_dive_questions,
    risk: o.risk || r.key_risk,
    links: linkSet(brand, r.geography, r.source_urls)
  };
});

const corpusRows = corpus.map((r) => ({
  rank: Number(r.rank),
  name: r.name,
  category: r.category,
  subcategory: r.subcategory,
  geography: r.geography,
  units: r.estimated_units,
  status: r.status,
  entry: r.dan_entry_path,
  caveat: r.key_caveat,
  proof: r.first_proof_question,
  links: linkSet(r.name, r.geography, r.source_urls)
}));

const operatorRows = operators.slice(0, 60).map((r) => ({
  rank: Number(r.rank),
  name: r.name,
  category: r.category,
  geography: r.geography,
  units: r.estimated_unit_count,
  status: r.target_status,
  entry: r.entry_path,
  risk: r.kill_risk,
  question: r.first_diligence_question,
  links: linkSet(r.name, r.geography, r.source_urls)
}));

const proofRows = proof.map((r) => ({
  rank: Number(r.proof_rank),
  name: r.name,
  category: r.category,
  geography: r.geography,
  units: r.verified_or_estimated_unit_count,
  status: r.proof_status,
  change: r.rank_change,
  entry: r.dan_entry_path,
  question: r.first_diligence_question,
  notes: r.notes,
  links: linkSet(r.name, r.geography, r.source_urls)
}));

const statusCounts = proofRows.reduce((acc, r) => {
  acc[r.status] = (acc[r.status] || 0) + 1;
  return acc;
}, {});

function j(value) {
  return JSON.stringify(value).replaceAll("</", "<\\/");
}

const html = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Emerging Multi-Unit Pipeline | Dan's Business Path</title>
<meta name="description" content="Dan's source-of-truth emerging multi-unit and consumer brand pipeline, updated through the July 19 Situation Room review.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{--paper:#f4ead8;--paper2:#eadcc4;--ink:#252018;--muted:#766b5e;--line:rgba(62,49,32,.16);--blue:#315e72;--blue2:#dfeaf0;--clay:#b86f4d;--sage:#6f8062;--gold:#b78b38;--card:rgba(255,251,241,.74);--shadow:0 30px 90px rgba(80,59,34,.16)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;color:var(--ink);font-family:"Space Grotesk",ui-sans-serif,system-ui,sans-serif;line-height:1.5;background:radial-gradient(circle at 14% -6%,rgba(184,111,77,.22),transparent 34%),radial-gradient(circle at 88% 6%,rgba(49,94,114,.18),transparent 30%),linear-gradient(180deg,var(--paper),var(--paper2));min-height:100dvh}body:after{content:"";position:fixed;inset:0;pointer-events:none;opacity:.12;mix-blend-mode:multiply;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 240 240' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.7' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='240' height='240' filter='url(%23n)' opacity='.5'/%3E%3C/svg%3E")}
.shell{max-width:1320px;margin:auto;padding:26px 24px 72px}nav{position:sticky;top:18px;z-index:10;width:min(1080px,100%);margin:0 auto 46px;display:flex;justify-content:space-between;gap:16px;align-items:center;padding:10px;border:1px solid rgba(62,49,32,.14);border-radius:999px;background:rgba(255,251,241,.72);backdrop-filter:blur(18px);box-shadow:0 18px 50px rgba(80,59,34,.12)}nav b{padding-left:12px}.links{display:flex;gap:6px;flex-wrap:wrap}.links a{color:var(--ink);text-decoration:none;font-size:13px;padding:8px 11px;border-radius:999px}.links a:hover{background:rgba(49,94,114,.09)}
.kicker{display:inline-flex;gap:8px;align-items:center;border:1px solid rgba(49,94,114,.18);background:rgba(255,251,241,.66);border-radius:999px;padding:8px 12px;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--blue);font-weight:700}.kicker:before{content:"";width:7px;height:7px;border-radius:99px;background:var(--clay)}h1{font-family:"Fraunces",Georgia,serif;font-weight:650;font-size:clamp(3rem,6.5vw,7rem);line-height:.9;letter-spacing:-.055em;max-width:1120px;margin:18px 0 22px}h2{font-family:"Fraunces",Georgia,serif;font-weight:650;font-size:clamp(2rem,4vw,4.1rem);letter-spacing:-.04em;line-height:.95;margin:0 0 20px}h3{font-size:22px;margin:0 0 9px;letter-spacing:-.02em}.lede{max-width:940px;color:var(--muted);font-size:clamp(1.05rem,1.8vw,1.32rem)}section{padding:42px 0}.grid2{display:grid;grid-template-columns:1fr 1fr;gap:18px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.grid5{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}.card{border:1px solid var(--line);border-radius:22px;background:var(--card);padding:22px;box-shadow:inset 0 1px 0 rgba(255,255,255,.78)}.hero-card{border:1px solid rgba(49,94,114,.2);border-radius:32px;background:linear-gradient(135deg,rgba(255,251,241,.9),rgba(223,234,240,.56));padding:28px;box-shadow:var(--shadow)}p,li{color:var(--muted)}.tag{display:inline-block;margin:4px 4px 0 0;padding:6px 9px;border-radius:999px;border:1px solid var(--line);font-size:12px;color:var(--ink);background:rgba(255,255,255,.36)}.pill{display:inline-block;border-radius:999px;padding:4px 8px;font-size:11px;font-weight:800}.go,.advance{background:rgba(111,128,98,.14);color:var(--sage)}.watch{background:rgba(183,139,56,.16);color:#765402}.kill,.demote{background:rgba(184,111,77,.12);color:var(--clay)}.comp{background:rgba(49,94,114,.12);color:var(--blue)}.note{border-left:4px solid var(--clay);padding:15px 18px;background:rgba(184,111,77,.09);border-radius:16px;color:var(--muted)}
.metric{padding:18px;border:1px solid var(--line);border-radius:18px;background:rgba(255,251,241,.6)}.metric strong{display:block;font-family:"Fraunces",Georgia,serif;font-size:34px;line-height:1;color:var(--blue)}.stack{display:grid;grid-template-columns:130px 1fr 170px;gap:14px;align-items:start;padding:16px 0;border-bottom:1px solid var(--line)}.stack:last-child{border-bottom:0}.ranknum{font-family:"Fraunces",Georgia,serif;color:var(--gold);font-size:28px;line-height:1}.brand{font-weight:800;color:var(--ink)}.external-links{display:flex;flex-wrap:wrap;gap:6px;min-width:156px}.external-links a{display:inline-flex;align-items:center;border:1px solid var(--line);border-radius:999px;padding:5px 8px;background:rgba(255,255,255,.36);color:var(--blue);font-size:11px;font-weight:800;text-decoration:none}.external-links a:hover{background:rgba(49,94,114,.1)}.controls{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0}.controls input,.controls select{font:inherit;background:rgba(255,251,241,.8);border:1px solid var(--line);border-radius:999px;padding:10px 13px;color:var(--ink)}.controls input{min-width:280px}.table-shell{overflow:auto;border:1px solid var(--line);border-radius:20px;background:rgba(255,251,241,.5)}table{width:100%;border-collapse:collapse;min-width:1320px}th,td{padding:12px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;font-size:13px}th{font-size:10px;text-transform:uppercase;letter-spacing:.14em;color:var(--blue);background:rgba(49,94,114,.06)}tr:last-child td{border-bottom:0}.source{font-size:12px;color:var(--muted);border-top:1px dashed var(--line);padding-top:18px}footer{padding:36px 0;color:var(--muted);font-size:13px}@media(max-width:900px){.shell{padding:16px}.grid2,.grid3,.grid5{grid-template-columns:1fr}nav{position:relative;border-radius:24px;align-items:flex-start;flex-direction:column}.stack{grid-template-columns:1fr}.controls input{min-width:100%;width:100%}h1{font-size:3rem}table{min-width:1120px}}
</style>
</head>
<body>
<main class="shell">
<nav><b>Dan's source-of-truth pipeline</b><div class="links"><a href="./index.html">Dashboard</a><a href="./consumer-target-map.html">Situation Room</a><a href="#corpus">Full List</a><a href="#operators">Operators</a><a href="./operating.html">Operating</a></div></nav>

<section class="hero-card">
<span class="kicker">Source of truth - updated 2026-07-19</span>
<h1>Emerging multi-unit and consumer brand pipeline.</h1>
<p class="lede">This page supersedes the stale June 12 45-candidate view. It now opens directly into the full consumer-brand sourcing universe, with corrected operator context, proof-sprint rerating, July 4 lane validation, and the July 19 Situation Room cleanup and expansion.</p>
<span class="tag">${corpus.length} consumer brand corpus rows</span><span class="tag">45 scored ranking candidates retained in source files</span><span class="tag">${operators.length} corrected named-operator rows</span><span class="tag">${proof.length} proof-sprint rows</span><span class="tag">152 Situation Room entries</span><span class="tag">No outreach / no spend</span>
</section>

<section>
<h2>Board counts.</h2>
<div class="grid5">
<div class="metric"><strong>${corpus.length}</strong><span>consumer corpus rows</span></div>
<div class="metric"><strong>45</strong><span>scored ranking candidates</span></div>
<div class="metric"><strong>${corpus.filter((r) => r.category === "Frozen Dessert").length}</strong><span>frozen dessert rows</span></div>
<div class="metric"><strong>${operators.length}</strong><span>named-operator v2 rows</span></div>
<div class="metric"><strong>${proof.length}</strong><span>proof sprint rows</span></div>
</div>
</section>

<section id="corpus">
<h2>Full ${corpus.length}-row consumer brand corpus.</h2>
<p class="note">This is the full sourcing universe, not proofed diligence. Rows can be targets, watch names, or comps. Use it to find lanes and candidates, then require proof sprint work before action.</p>
<div class="controls"><input id="corpusSearch" placeholder="Search corpus..."><select id="corpusStatus"><option value="All">All statuses</option></select><select id="corpusCategory"><option value="All">All categories</option></select></div>
<div class="table-shell"><table><thead><tr><th>Rank</th><th>Name</th><th>Links</th><th>Category</th><th>Subcategory</th><th>Geography</th><th>Units</th><th>Status</th><th>Dan entry path</th><th>Caveat</th><th>First proof question</th></tr></thead><tbody id="corpusBody"></tbody></table></div>
</section>

<section id="operators">
<h2>Named multi-unit operator universe / proof sprint.</h2>
<div class="grid2">
<div class="card"><h3>Universe correction</h3><p>The original 150-row pass was useful lane ideation, but too category-heavy. The v2 deliverable is the corrected named-operator universe: ${operators.length} actual businesses/operators that can be proofed.</p></div>
<div class="card"><h3>Proof sprint result</h3><p>${Object.entries(statusCounts).map(([k,v]) => `${v} ${k}`).join(" / ")}. Biggest fixes: AquaKids killed/rebranded, SwimKids acquired, Kids First too scaled, LowCountry mobile, and specialty auto moved above swim schools.</p></div>
</div>
<h3>Proof sprint rows</h3>
<div class="controls"><input id="proofSearch" placeholder="Search proof sprint..."><select id="proofStatus"><option value="All">All proof statuses</option></select></div>
<div class="table-shell"><table><thead><tr><th>Proof rank</th><th>Name</th><th>Links</th><th>Category</th><th>Geography</th><th>Units</th><th>Status</th><th>Rank change</th><th>Entry path</th><th>First diligence question</th><th>Notes</th></tr></thead><tbody id="proofBody"></tbody></table></div>
<h3 style="margin-top:34px">Top named-operator universe rows</h3>
<div class="controls"><input id="operatorSearch" placeholder="Search operator universe..."><select id="operatorStatus"><option value="All">All statuses</option></select></div>
<div class="table-shell"><table><thead><tr><th>Rank</th><th>Name</th><th>Links</th><th>Category</th><th>Geography</th><th>Units</th><th>Status</th><th>Entry path</th><th>Kill risk</th><th>First diligence question</th></tr></thead><tbody id="operatorBody"></tbody></table></div>
</section>

<section>
<h2>July 19 Situation Room: cleanup, expansion, and sharper queues.</h2>
<div class="note" style="margin-bottom:24px"><b>Posted 2026-07-19.</b> A senior-operator scrub separated actual acquisition/JV targets from comps, franchise systems, acquired businesses, nonprofits, and over-scaled platforms. The dedicated map was expanded from 112 audited entries to 152 tracked entries, and its stale hard-coded headline was replaced with live counts.</div>
<div class="grid3">
<div class="card"><h3>Bagels stay #1</h3><p>Prioritize Layla rights/JV diligence, Starship proof-unit economics, and Jeff's Bagel Run franchisee/area-development returns. Treat Utopia as a quality comp, not a near-term control target.</p></div>
<div class="card"><h3>Pet gets narrower</h3><p>Bias to grooming, hygiene, self-wash, memberships, and micro-acquisition density. Facility-heavy boarding/daycare assets remain selective-buy resale cases, not the lead thesis.</p></div>
<div class="card"><h3>Kids gets smaller-box</h3><p>Party-first play, STEM/maker birthdays, and venue-light programming outrank generic activity or dedicated swim greenfield. Mature hosted or resale swim remains selective.</p></div>
</div>
<div class="grid2" style="margin-top:18px">
<div class="card"><h3>New-lane sprint</h3><p>Ranked discovery lanes are social bathhouse / sauna-cold plunge clubs, padel, and luxury repair / restoration. These are research queues, not approach-now recommendations.</p></div>
<div class="card"><h3>Live map and evidence</h3><p><a href="./consumer-target-map.html">Open the 152-entry Situation Room map</a>. The supporting review is in <code>reports/situation-room-review-2026-07-19.md</code>; the public map was independently verified against the local 70 target / 49 watch / 33 comp distribution.</p></div>
</div>
</section>

<section>
<h2>July 4 Sprint: Lane Re-Rating & New Target Maps</h2>
<div class="note" style="margin-bottom:24px"><b>Posted 2026-07-05.</b> Four lanes were validated against current sources, lane verdicts were issued, and three new target-map artifacts were produced. The underlying corpus/operator tables remain the June source data; the sprint adds directional verdicts and bounded validation maps.</div>
<div class="grid2">
<div class="card"><h3>Lane verdicts</h3><p><span class="pill advance">ADVANCE</span> youth sports / kids enrichment &nbsp; <span class="pill watch">WATCH</span> pet wellness &nbsp; <span class="pill watch">COMPLIANCE WEDGE</span> BERDO &nbsp; <span class="pill kill">KILL</span> GLP-1 local operators for a first sprint.</p></div>
<div class="card"><h3>Artifacts</h3><p>40-target multi-lane map, 25-operator youth-sports map, 150-record BERDO list with 40 enriched records, and a BERDO exposure-scan / rescue-offer packet.</p></div>
</div>
<div class="card" style="margin-top:18px"><h3>Source files</h3><p><code>research/2026-07-04-consumer-proof-sprint-final-recommendation.md</code> · <code>research/2026-07-04-consumer-proof-sprint-target-map.md</code> · <code>research/2026-07-04-youth-sports-operator-map.csv</code> · <code>research/2026-07-04-berdo-validation-target-list.csv</code></p></div>
</section>

<section>
<h2>Update discipline.</h2>
<div class="card source">
<p><b>Canonical public URL:</b> https://w1nsl0wh0m3r-bit.github.io/dan-business-path/emerging-multi-unit-pipeline.html</p>
<p><b>Update rule:</b> after every material proof sprint, deep dive batch, or action-plan rerating, update this page first. Scratch files in the OpenClaw workspace are not the dashboard of record.</p>
<p><b>Data sources:</b> consumer corpus, top-20 ranking/action-plan files used for posture context, v2 named-operator universe, named-operator proof sprint 25, Swedish candy commoditization review, June 19 frozen-yogurt chain addendum, July 4 consumer proof sprint, and July 19 Situation Room review/map.</p>
<p><b>Repeatable build:</b> run <code>node scripts/update_pipeline_source_of_truth.mjs</code> from the repo root.</p>
</div>
</section>

<footer>Private working page. Source-of-truth dashboard generated from workspace research artifacts on 2026-07-19.</footer>
</main>

<script>
const TOP20 = ${j(top20)};
const CORPUS = ${j(corpusRows)};
const OPERATORS = ${j(operatorRows)};
const PROOF = ${j(proofRows)};
const esc = (v) => String(v ?? "").replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const norm = (v) => String(v ?? "").toLowerCase();
const pill = (v) => {
  const s = norm(v);
  const cls = s.includes("advance") || s.includes("diligence") || s.includes("proof") ? "go" : s.includes("watch") ? "watch" : s.includes("comp") || s.includes("pass") ? "comp" : s.includes("kill") || s.includes("demote") ? "kill" : "watch";
  return '<span class="pill ' + cls + '">' + esc(v || "watch") + '</span>';
};
const linkButtons = (links = {}) => '<div class="external-links">' +
  (links.website ? '<a href="' + esc(links.website) + '" target="_blank" rel="noopener">Site</a>' : '') +
  (links.maps ? '<a href="' + esc(links.maps) + '" target="_blank" rel="noopener">Map</a>' : '') +
  (links.instagram ? '<a href="' + esc(links.instagram) + '" target="_blank" rel="noopener">IG</a>' : '') +
  '</div>';
function options(sel, rows, key) {
  sel.innerHTML += [...new Set(rows.map(r => r[key]).filter(Boolean))].sort().map(v => '<option>' + esc(v) + '</option>').join("");
}
function renderTable(rows, body, cells) {
  body.innerHTML = rows.map(r => '<tr>' + cells.map(fn => '<td>' + fn(r) + '</td>').join("") + '</tr>').join("");
}
function textFilter(rows, query, keys) {
  const q = norm(query);
  return rows.filter(r => !q || keys.some(k => norm(r[k]).includes(q)));
}
const corpusSearch = document.getElementById("corpusSearch"), corpusStatus = document.getElementById("corpusStatus"), corpusCategory = document.getElementById("corpusCategory"), corpusBody = document.getElementById("corpusBody");
options(corpusStatus, CORPUS, "status"); options(corpusCategory, CORPUS, "category");
function renderCorpus() {
  const rows = textFilter(CORPUS, corpusSearch.value, ["name","category","subcategory","geography","status","entry","caveat","proof"]).filter(r => (corpusStatus.value === "All" || r.status === corpusStatus.value) && (corpusCategory.value === "All" || r.category === corpusCategory.value));
  renderTable(rows, corpusBody, [r=>esc(r.rank), r=>'<span class="brand">'+esc(r.name)+'</span>', r=>linkButtons(r.links), r=>esc(r.category), r=>esc(r.subcategory), r=>esc(r.geography), r=>esc(r.units), r=>pill(r.status), r=>esc(r.entry), r=>esc(r.caveat), r=>esc(r.proof)]);
}
const proofSearch = document.getElementById("proofSearch"), proofStatus = document.getElementById("proofStatus"), proofBody = document.getElementById("proofBody");
options(proofStatus, PROOF, "status");
function renderProof() {
  const rows = textFilter(PROOF, proofSearch.value, ["name","category","geography","status","entry","question","notes"]).filter(r => proofStatus.value === "All" || r.status === proofStatus.value);
  renderTable(rows, proofBody, [r=>esc(r.rank), r=>'<span class="brand">'+esc(r.name)+'</span>', r=>linkButtons(r.links), r=>esc(r.category), r=>esc(r.geography), r=>esc(r.units), r=>pill(r.status), r=>esc(r.change), r=>esc(r.entry), r=>esc(r.question), r=>esc(r.notes)]);
}
const operatorSearch = document.getElementById("operatorSearch"), operatorStatus = document.getElementById("operatorStatus"), operatorBody = document.getElementById("operatorBody");
options(operatorStatus, OPERATORS, "status");
function renderOperators() {
  const rows = textFilter(OPERATORS, operatorSearch.value, ["name","category","geography","status","entry","risk","question"]).filter(r => operatorStatus.value === "All" || r.status === operatorStatus.value);
  renderTable(rows, operatorBody, [r=>esc(r.rank), r=>'<span class="brand">'+esc(r.name)+'</span>', r=>linkButtons(r.links), r=>esc(r.category), r=>esc(r.geography), r=>esc(r.units), r=>pill(r.status), r=>esc(r.entry), r=>esc(r.risk), r=>esc(r.question)]);
}
[[corpusSearch,corpusStatus,renderCorpus],[corpusCategory,corpusCategory,renderCorpus],[proofSearch,proofStatus,renderProof],[operatorSearch,operatorStatus,renderOperators]].forEach(([a,b,fn]) => { a.addEventListener("input",fn); b.addEventListener("input",fn); });
renderCorpus(); renderProof(); renderOperators();
</script>
</body>
</html>
`;

fs.writeFileSync(path.join(repo, "emerging-multi-unit-pipeline.html"), html);
console.log(`Updated emerging-multi-unit-pipeline.html with ${corpus.length} corpus rows, ${top20.length} top ranks, ${operators.length} operators, ${proof.length} proof rows.`);
