#!/usr/bin/env python3
import json, os, sys
BASE = "/Users/winslow/Projects/dan-business-path"

def stat_grid(stats):
    return '<div class="stat-grid">\n' + '\n'.join(
        f'<div class="stat"><div class="stat-value">{v}</div><div class="stat-label">{label}</div><div class="stat-source">{src}</div></div>'
        for v, label, src in stats
    ) + '\n</div>'

def ul(items):
    return '<ul>\n' + '\n'.join(f'<li>{x}</li>' for x in items) + '\n</ul>'

def expert(rows):
    return '<table><tr><th>Who</th><th>Key questions</th></tr>' + ''.join(
        f'<tr><td>{who}</td><td>{qs}</td></tr>' for who, qs in rows
    ) + '</table>'

def section(cfg):
    return f'''<h2>9. Market Size & Industry Data</h2>
{stat_grid(cfg['stats'])}
<p>{cfg['market_text']}</p>

<h2>10. Operator Reality</h2>
<div class="grid2"><div class="card green-flag"><h3>Where operators win</h3>
{ul(cfg['operator_wins'])}
</div><div class="card red-flag"><h3>Where owners lose money</h3>
{ul(cfg['operator_losses'])}
</div></div>

<h2>11. Competitive Landscape & Whitespace</h2>
{ul(cfg['competitive'])}

<h2>12. Dashboard Score Reality Check</h2>
<div class="grid2"><div class="card green-flag"><h3>Score confirmed ✓</h3>
{ul(cfg['score_confirmed'])}
</div><div class="card red-flag"><h3>Score caveats ⚠️</h3>
{ul(cfg['score_caveats'])}
</div></div>

<h2>13. Expert Call Plan</h2>
{expert(cfg['expert_plan'])}

<h2>14. Expert Calls</h2>'''

def inject(slug, cfg):
    p = os.path.join(BASE, slug + '.html')
    with open(p) as f: html = f.read()
    if '<h2>11. Competitive Landscape & Whitespace</h2>' in html:
        print(f'SKIP already augmented: {slug}')
        return os.path.getsize(p)
    markers = ['<h2>9. Expert Calls</h2>', '<h2>9. Expert Call Plan</h2>']
    replacement = section(cfg)
    for marker in markers:
        if marker in html:
            html = html.replace(marker, replacement, 1)
            html = html.replace('<h2>10. 30 / 60 / 90 Roadmap</h2>', '<h2>15. 30 / 60 / 90 Roadmap</h2>')
            with open(p, 'w') as f: f.write(html)
            size = os.path.getsize(p)
            print(f'OK {slug}: {size:,} bytes ({size/1024:.1f}KB)')
            return size
    raise SystemExit(f'No insertion marker found for {slug}')

configs = json.load(sys.stdin)
for slug, cfg in configs.items(): inject(slug, cfg)
