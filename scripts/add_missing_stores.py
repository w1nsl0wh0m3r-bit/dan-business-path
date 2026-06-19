#!/usr/bin/env python3
"""Add 9 missing confirmed stores to swedish-candy-map.html TABLE_ROWS + MAP_PINS."""

import re, json
from urllib.parse import quote

MAP_PATH = 'swedish-candy-map.html'

with open(MAP_PATH) as f:
    html = f.read()

# Extract TABLE_ROWS
m = re.search(r'(const TABLE_ROWS\s*=\s*)(\[.*?\])(;)', html, re.DOTALL)
rows = json.loads(m.group(2))
print(f"Current rows: {len(rows)}")

max_rank = max(r['rank'] for r in rows)

def make_links(brand, address, slug):
    q = quote(f"{address} {brand}")
    return {
        "website": "",
        "maps": f"https://www.google.com/maps/search/?api=1&query={q}",
        "instagram": f"https://www.instagram.com/explore/search/keyword/?q={quote(brand)}",
        "detail": f"./swedish-candy/{slug}.html"
    }

new_rows = [
    # The Sweetish Fish — Chestnut Hill (verified open)
    {
        "rank": max_rank + 1,
        "brand": "The Sweetish Fish",
        "location": "Chestnut Hill MA",
        "address": "33 Boylston St Unit 3350 Chestnut Hill, MA 02467",
        "status": "verified open",
        "channel": "storefront",
        "cluster": "Boston/New England",
        "notes": "The Street Chestnut Hill mall; opened spring 2026",
        "links": make_links("The Sweetish Fish", "33 Boylston St Chestnut Hill MA", "the-sweetish-fish")
    },
    # The Sweetish Fish — Seaport (pop-up at The Current)
    {
        "rank": max_rank + 2,
        "brand": "The Sweetish Fish",
        "location": "Boston Seaport MA",
        "address": "100 Seaport Blvd Boston, MA 02210",
        "status": "verified open",
        "channel": "pop-up",
        "cluster": "Boston/New England",
        "notes": "Pop-up at The Current; Cape Cod natives",
        "links": make_links("The Sweetish Fish", "100 Seaport Blvd Boston MA", "the-sweetish-fish")
    },
    # The Pirate Candy Shop — Tampa (Hyde Park Village)
    {
        "rank": max_rank + 3,
        "brand": "The Pirate Candy Shop",
        "location": "Tampa FL",
        "address": "716 S Village Cir Tampa, FL 33606",
        "status": "verified open",
        "channel": "storefront",
        "cluster": "Florida",
        "notes": "Hyde Park Village; Tampa's first Swedish candy shop",
        "links": make_links("The Pirate Candy Shop", "716 S Village Cir Tampa FL", "the-pirate-candy-shop")
    },
    # The Pirate Candy Shop — St. Pete (opening summer 2026)
    {
        "rank": max_rank + 4,
        "brand": "The Pirate Candy Shop",
        "location": "St. Petersburg FL",
        "address": "689 Central Ave St. Petersburg, FL 33701",
        "status": "opening soon",
        "channel": "storefront",
        "cluster": "Florida",
        "notes": "Grand Central District; opening summer 2026",
        "links": make_links("The Pirate Candy Shop", "689 Central Ave St. Petersburg FL", "the-pirate-candy-shop")
    },
    # Sugar Moose Candy — Kaysville UT
    {
        "rank": max_rank + 5,
        "brand": "Sugar Moose Candy",
        "location": "Kaysville UT",
        "address": "85 Main St Kaysville, UT 84037",
        "status": "verified open",
        "channel": "storefront",
        "cluster": "Utah",
        "notes": "Original location; downtown Kaysville; 60+ varieties",
        "links": make_links("Sugar Moose Candy", "85 Main St Kaysville UT", "sugar-moose-candy")
    },
    # Sugar Moose Candy — Salt Lake City UT
    {
        "rank": max_rank + 6,
        "brand": "Sugar Moose Candy",
        "location": "Salt Lake City UT",
        "address": "1058 E 900 S Salt Lake City, UT 84105",
        "status": "verified open",
        "channel": "storefront",
        "cluster": "Utah",
        "notes": "Second location; 9th & 9th; opened June 2026",
        "links": make_links("Sugar Moose Candy", "1058 E 900 S Salt Lake City UT", "sugar-moose-candy")
    },
    # Swedish Moose Candy Co. — Provo UT
    {
        "rank": max_rank + 7,
        "brand": "Swedish Moose Candy Co.",
        "location": "Provo UT",
        "address": "Provo UT 84601",
        "status": "verified open",
        "channel": "storefront",
        "cluster": "Utah",
        "notes": "Utah County expansion; SLUG Mag profile",
        "links": make_links("Swedish Moose Candy Co.", "Provo UT", "swedish-moose-candy-co")
    },
    # Swedish Moose Candy Co. — American Fork UT
    {
        "rank": max_rank + 8,
        "brand": "Swedish Moose Candy Co.",
        "location": "American Fork UT",
        "address": "American Fork UT 84003",
        "status": "verified open",
        "channel": "storefront",
        "cluster": "Utah",
        "notes": "Utah County; near So Swede (same city)",
        "links": make_links("Swedish Moose Candy Co.", "American Fork UT", "swedish-moose-candy-co")
    },
    # The Sweetish Fish — Sandwich/Cape Cod (truck, founding location)
    {
        "rank": max_rank + 9,
        "brand": "The Sweetish Fish",
        "location": "Sandwich MA",
        "address": "Sandwich, MA 02563",
        "status": "seasonal/truck",
        "channel": "mobile",
        "cluster": "Boston/New England",
        "notes": "Cape Cod origin; candy truck; founders are Cape Cod natives",
        "links": make_links("The Sweetish Fish", "Sandwich MA", "the-sweetish-fish")
    },
]

# Append new rows
rows.extend(new_rows)

# Write back TABLE_ROWS
new_json = json.dumps(rows, indent=2, ensure_ascii=False)
html = html[:m.start(2)] + new_json + html[m.end(2):]

# Now check for MAP_PINS and add pins for the new stores
pin_match = re.search(r'(const MAP_PINS\s*=\s*)(\[.*?\])(;)', html, re.DOTALL)
if pin_match:
    pins = json.loads(pin_match.group(2))
    print(f"Current pins: {len(pins)}")
    
    new_pins = [
        {"brand": "The Sweetish Fish", "lat": 42.3218, "lng": -71.1662, "location": "Chestnut Hill MA"},
        {"brand": "The Sweetish Fish", "lat": 42.3522, "lng": -71.0434, "location": "Boston Seaport MA"},
        {"brand": "The Sweetish Fish", "lat": 41.7592, "lng": -70.4956, "location": "Sandwich MA"},
        {"brand": "The Pirate Candy Shop", "lat": 27.9370, "lng": -82.4734, "location": "Tampa FL"},
        {"brand": "The Pirate Candy Shop", "lat": 27.7713, "lng": -82.6590, "location": "St. Petersburg FL"},
        {"brand": "Sugar Moose Candy", "lat": 40.9821, "lng": -111.9388, "location": "Kaysville UT"},
        {"brand": "Sugar Moose Candy", "lat": 40.7489, "lng": -111.8650, "location": "Salt Lake City UT"},
        {"brand": "Swedish Moose Candy Co.", "lat": 40.2338, "lng": -111.6585, "location": "Provo UT"},
        {"brand": "Swedish Moose Candy Co.", "lat": 40.3772, "lng": -111.7957, "location": "American Fork UT"},
    ]
    
    pins.extend(new_pins)
    new_pins_json = json.dumps(pins, indent=2, ensure_ascii=False)
    html = html[:pin_match.start(2)] + new_pins_json + html[pin_match.end(2):]
    print(f"New pin count: {len(pins)}")

# Update any hardcoded counts in the HTML
html = re.sub(r'(\d+)\s*stores\s*across\s*\d+\s*brands', f'{len(rows)} stores across {len(set(r["brand"] for r in rows))} brands', html)
html = re.sub(r'(\d+)\s*mapped\s*stores', f'{len(rows)} mapped stores', html)

with open(MAP_PATH, 'w') as f:
    f.write(html)

# Count summary
brands = set(r['brand'] for r in rows)
print(f"\n✅ Done: {len(rows)} rows, {len(brands)} brands")
