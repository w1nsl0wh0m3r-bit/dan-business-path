#!/usr/bin/env python3
"""Upgrade all 31 Swedish candy comp profile pages with research data."""

import json
import os
import html as html_mod
from urllib.parse import quote as urlquote

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(BASE_DIR, "swedish-candy")

# Shared CSS (same across all existing pages)
CSS = """<style>
:root{--paper:#f4ead8;--paper2:#eadcc4;--ink:#252018;--muted:#766b5e;--line:rgba(62,49,32,.16);--blue:#315e72;--clay:#b86f4d;--sage:#6f80662;--gold:#b78b38;--card:rgba(255,251,241,.76)}
*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:"Space Grotesk",ui-sans-serif,system-ui,sans-serif;line-height:1.5;background:linear-gradient(180deg,var(--paper),var(--paper2));min-height:100dvh}.shell{max-width:1180px;margin:auto;padding:26px 24px 72px}nav{display:flex;justify-content:space-between;gap:16px;align-items:center;margin:0 0 36px;padding:10px;border:1px solid var(--line);border-radius:999px;background:rgba(255,251,241,.72)}nav a{color:var(--ink);text-decoration:none;font-size:13px;padding:8px 11px;border-radius:999px}h1{font-family:"Fraunces",Georgia,serif;font-size:clamp(2.4rem,5vw,4.6rem);line-height:.96;margin:12px 0 14px}h2{font-family:"Fraunces",Georgia,serif;font-size:1.8rem;line-height:1;margin:34px 0 12px}h3{margin:0 0 8px;font-size:1rem}.kicker{display:inline-flex;border:1px solid rgba(49,94,114,.18);background:rgba(255,251,241,.66);border-radius:999px;padding:8px 12px;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--blue);font-weight:700}.lede{max-width:880px;color:var(--muted);font-size:1.12rem}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:24px 0}.card,.panel{border:1px solid var(--line);border-radius:16px;background:var(--card);padding:16px}.card b{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:var(--blue);margin-bottom:6px}.card strong{font-size:1.16rem}.sections{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:18px}.panel ul{margin:0;padding-left:18px}.panel li{margin:0 0 7px}.note{border-left:4px solid var(--clay);padding:15px 18px;background:rgba(184,111,77,.09);border-radius:14px;color:var(--muted)}table{width:100%;border-collapse:collapse;background:rgba(255,251,241,.45);border:1px solid var(--line);border-radius:16px;overflow:hidden}th,td{padding:11px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;font-size:13px}th{font-size:10px;text-transform:uppercase;letter-spacing:.14em;color:var(--blue);background:rgba(255,251,241,.6)}td:first-child{font-weight:600}tr:last-child td{border-bottom:none}.links{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0}.links a{display:inline-block;padding:6px 14px;border:1px solid var(--line);border-radius:999px;font-size:12px;color:var(--blue);text-decoration:none;background:rgba(255,251,241,.6)}.links a:hover{background:rgba(49,94,114,.08)}.src{font-size:11px;color:var(--muted);margin-top:4px}
</style>"""

def esc(s):
    return html_mod.escape(str(s), quote=False)

def make_link(label, url):
    return f'<a href="{url}" target="_blank" rel="noopener">{esc(label)}</a>'

def make_panel(title, items, sources=None):
    """Generate a panel with bullet items and optional source links."""
    lis = "".join(f"<li>{item}</li>" for item in items)
    src = ""
    if sources:
        src_links = " · ".join(
            f'<a href="{url}" target="_blank" rel="noopener" class="src">{esc(label)}</a>'
            for label, url in sources
        )
        src = f'<div class="src">Sources: {src_links}</div>'
    return f'<div class="panel"><h3>{esc(title)}</h3><ul>{lis}</ul>{src}</div>'

def make_unit_table(units):
    """Generate the mapped unit records table."""
    rows_html = ""
    for u in units:
        loc = esc(u.get("location", ""))
        addr = esc(u.get("address", ""))
        rows_html += f"<tr><td>{loc}</td><td>{addr}</td></tr>"
    return (
        f'<table><thead><tr><th>Location</th><th>Address</th></tr></thead>'
        f"<tbody>{rows_html}</tbody></table>"
    )

def generate_page(brand):
    """Generate a single comp profile HTML page."""
    name = brand["name"]
    slug = brand["slug"]
    lede = brand["lede"]
    posture = brand["posture"]
    row_count = brand["rows"]
    markets = brand["markets"]
    confidence = brand["confidence"]
    links_html = brand["links_html"]
    panels = brand["panels"]
    units = brand["units"]

    # Build panels HTML
    panels_html = "".join(panels)

    # Build unit table
    unit_html = make_unit_table(units)

    # Diligence note
    diligence = brand.get("diligence_note", "")

    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(name)} | Swedish Candy Comp</title><meta name="description" content="Structured Swedish candy comp profile for {esc(name)}."><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">{CSS}
</style></head><body><main class="shell"><nav><b>Dan's Business Path</b><div><a href="../swedish-candy-map.html">Swedish Candy Map</a><a href="../emerging-multi-unit-pipeline.html">Pipeline</a></div></nav><span class="kicker">Swedish candy comp profile</span><h1>{esc(name)}</h1><p class="lede">{esc(lede)}</p><div class="grid"><div class="card"><b>Posture</b><strong>{esc(posture)}</strong></div><div class="card"><b>Rows</b><strong>{row_count}</strong></div><div class="card"><b>Markets</b><strong>{esc(markets)}</strong></div><div class="card"><b>Confidence</b><strong>{esc(confidence)}</strong></div></div><div class="links">{links_html}</div><section class="sections">{panels_html}</section><h2>Mapped Unit Records</h2>{unit_html}"""

    if diligence:
        page += f'<div class="note" style="margin-top:24px">{esc(diligence)}</div>'

    page += "</main></body></html>"
    return page


# Load unit data from TABLE_ROWS
import re

def load_units():
    """Load unit records from swedish-candy-map.html TABLE_ROWS."""
    map_path = os.path.join(BASE_DIR, "swedish-candy-map.html")
    with open(map_path) as f:
        html = f.read()
    m = re.search(r"const TABLE_ROWS = (\[.*?\]);", html, re.DOTALL)
    if not m:
        raise ValueError("Could not find TABLE_ROWS in map")
    rows = json.loads(m.group(1))
    from collections import defaultdict
    by_brand = defaultdict(list)
    for r in rows:
        by_brand[r["brand"]].append(r)
    return by_brand


def units_for(by_brand, brand_name):
    """Get unit records for a brand."""
    return [
        {"location": u.get("location", ""), "address": u.get("address", "")}
        for u in by_brand.get(brand_name, [])
    ]


def links_for(site=None, ig=None, maps=None):
    """Build links HTML."""
    parts = []
    if site:
        parts.append(make_link("Site", site))
    if ig:
        parts.append(make_link("IG", ig))
    if maps:
        for label, url in maps:
            parts.append(make_link(label, url))
    return "".join(parts)


def gm(query):
    """Google Maps link."""
    enc = urlquote(query, safe="")
    return f"https://www.google.com/maps/search/?api=1&query={enc}"
