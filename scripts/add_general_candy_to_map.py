#!/usr/bin/env python3
"""Add general candy store layer to the Swedish candy map with toggle support."""

import json
import re

MAP_PATH = 'swedish-candy-map.html'

# General candy stores — Bucket B universe
GENERAL_CANDY_STORES = [
    # B1: National Chains
    {"brand": "IT'SUGAR", "location_name": "Times Square", "address": "20 E 14th St", "city": "New York", "state": "NY", "zip": "10003", "latitude": 40.7299, "longitude": -73.9886, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "NYC/Brooklyn", "notes": "~100+ stores nationally. BBX Capital. Filed Ch11 2020, emerged 2021."},
    {"brand": "IT'SUGAR", "location_name": "Lincoln Road", "address": "537 Lincoln Rd", "city": "Miami Beach", "state": "FL", "zip": "33139", "latitude": 25.7907, "longitude": -80.1319, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "South Florida", "notes": "Experiential 'sugartainment' format"},
    {"brand": "IT'SUGAR", "location_name": "Universal CityWalk", "address": "6000 Universal Blvd", "city": "Orlando", "state": "FL", "zip": "32819", "latitude": 28.4717, "longitude": -81.4639, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Florida Central", "notes": "Theme park location"},
    {"brand": "IT'SUGAR", "location_name": "Las Vegas Strip", "address": "3799 S Las Vegas Blvd", "city": "Las Vegas", "state": "NV", "zip": "89109", "latitude": 36.0917, "longitude": -115.1739, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Las Vegas", "notes": "Tourist/high-traffic"},
    {"brand": "IT'SUGAR", "location_name": "Garden State Plaza", "address": "1 Garden State Plaza", "city": "Paramus", "state": "NJ", "zip": "07652", "latitude": 40.9184, "longitude": -74.0759, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "NYC/Brooklyn", "notes": "Mall location"},
    {"brand": "IT'SUGAR", "location_name": "Scottsdale Fashion Square", "address": "7014 E Camelback Rd", "city": "Scottsdale", "state": "AZ", "zip": "85251", "latitude": 33.5021, "longitude": -111.9281, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Phoenix", "notes": "Premium mall"},
    
    {"brand": "Rocket Fizz", "location_name": "Reno (HQ area)", "address": "75 McCabe Dr", "city": "Reno", "state": "NV", "zip": "89511", "latitude": 39.4303, "longitude": -119.7899, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Reno/Tahoe", "notes": "~100+ franchise locations. Candy + soda. Nostalgia focus."},
    {"brand": "Rocket Fizz", "location_name": "Austin", "address": "301 S Lamar Blvd", "city": "Austin", "state": "TX", "zip": "78704", "latitude": 30.2599, "longitude": -97.7599, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Austin", "notes": "Independently owned franchise"},
    {"brand": "Rocket Fizz", "location_name": "Denver", "address": "2154 Larimer St", "city": "Denver", "state": "CO", "zip": "80205", "latitude": 39.7536, "longitude": -104.9942, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Denver", "notes": "Larimer Square"},
    
    # B2: Regional / Boutique
    {"brand": "Lolli & Pops", "location_name": "Stanford Shopping Center", "address": "660 Stanford Shopping Center", "city": "Palo Alto", "state": "CA", "zip": "94304", "latitude": 37.4432, "longitude": -122.1710, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Bay Area", "notes": "~25-35 stores. TerraMar Capital. Acquired Hammond's Candies Nov 2024."},
    {"brand": "Lolli & Pops", "location_name": "Rosedale Center", "address": "1595 Hwy 36 W", "city": "Roseville", "state": "MN", "zip": "55113", "latitude": 45.0180, "longitude": -93.1830, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Minneapolis", "notes": "Newly opened. Re-expansion phase."},
    {"brand": "Lolli & Pops", "location_name": "Eastview Mall", "address": "7979 Pittsford Palmyra Rd", "city": "Victor", "state": "NY", "zip": "14564", "latitude": 43.0256, "longitude": -77.4047, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Upstate NY", "notes": "Recently opened. Rochester area."},
    
    {"brand": "Dylan's Candy Bar", "location_name": "Upper East Side", "address": "1011 Third Ave", "city": "New York", "state": "NY", "zip": "10065", "latitude": 40.7610, "longitude": -73.9645, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "NYC/Brooklyn", "notes": "Flagship. ~$137M revenue (ZoomInfo). Founded by Dylan Lauren."},
    {"brand": "Dylan's Candy Bar", "location_name": "Los Angeles", "address": "189 The Grove Dr", "city": "Los Angeles", "state": "CA", "zip": "90036", "latitude": 34.0722, "longitude": -118.3578, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Los Angeles", "notes": "The Grove"},
    
    {"brand": "Sugarfina", "location_name": "World Trade Center", "address": "286 Greenwich St", "city": "New York", "state": "NY", "zip": "10007", "latitude": 40.7127, "longitude": -74.0116, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "NYC/Brooklyn", "notes": "8 stores remaining (was 38). SEC-reporting. Ch11 2020. Cautionary tale."},
    {"brand": "Sugarfina", "location_name": "Los Angeles", "address": "8607 Melrose Ave", "city": "Los Angeles", "state": "CA", "zip": "90069", "latitude": 34.0839, "longitude": -118.3763, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Los Angeles", "notes": "Premium gift candy. ~$61M revenue."},
    
    {"brand": "Hammond's Candies", "location_name": "Denver Factory", "address": "5735 Washington St", "city": "Denver", "state": "CO", "zip": "80216", "latitude": 39.7980, "longitude": -104.9410, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Denver", "notes": "Est. 1920. Factory tours. Acquired by Lolli & Pops Nov 2024."},
    
    # B3: Experiential
    {"brand": "Candytopia", "location_name": "Touring / Pop-up", "address": "Various", "city": "Varies", "state": "US", "zip": "", "latitude": 39.5, "longitude": -98.35, "status": "pop_up_or_cart", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "", "notes": "Ticketed experience. 3M+ guests. Candytopia 2.0 returning 2026. Not a store."},
    
    # B4: Independent
    {"brand": "Economy Candy", "location_name": "Lower East Side", "address": "108 Rivington St", "city": "New York", "state": "NY", "zip": "10002", "latitude": 40.7188, "longitude": -73.9862, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "NYC/Brooklyn", "notes": "Est. 1937. Family-owned. Already carries Bubs & Swedish gummies. 2,000+ SKUs."},
    {"brand": "Big Top Candy Shop", "location_name": "South Congress", "address": "1508 S Congress Ave", "city": "Austin", "state": "TX", "zip": "78704", "latitude": 30.2496, "longitude": -97.7494, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Austin", "notes": "Est. 2007. Retro/nostalgic candy."},
    {"brand": "Yummi Joy", "location_name": "Austin", "address": "1900 S Congress Ave", "city": "Austin", "state": "TX", "zip": "78704", "latitude": 30.2410, "longitude": -97.7501, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "Austin", "notes": "Toy Joy spinoff. General candy + novelty."},
    {"brand": "Bulk Candy Store", "location_name": "West Palm Beach", "address": "3001 Forest Hill Blvd", "city": "West Palm Beach", "state": "FL", "zip": "33406", "latitude": 26.6821, "longitude": -80.0900, "status": "verified_open", "category": "general_candy", "dan_posture": "general_candy", "market_cluster": "South Florida", "notes": "2 locations. $12.99/lb bulk. Ships nationwide."},
]

# Distinct colors for general candy brands (gray/slate spectrum — visually different from Swedish)
GENERAL_CANDY_COLORS = {
    "IT'SUGAR": "#dc2626",        # red
    "Rocket Fizz": "#7c3aed",      # violet (different from Lil Sweet Treat's purple)
    "Lolli & Pops": "#059669",     # emerald (different from Saturday Candy's green)
    "Dylan's Candy Bar": "#db2777", # pink-dark
    "Sugarfina": "#475569",        # slate
    "Hammond's Candies": "#92400e", # brown
    "Candytopia": "#7e22ce",       # purple-dark
    "Economy Candy": "#525252",    # neutral gray
    "Big Top Candy Shop": "#9333ea",
    "Yummi Joy": "#0d9488",
    "Bulk Candy Store": "#6b7280",
}

with open(MAP_PATH, 'r') as f:
    html = f.read()

# 1. Add general candy stores to STORES array
m = re.search(r'const STORES\s*=\s*(\[.*?\]);\s*\n', html, re.DOTALL)
if not m:
    print("ERROR: Could not find STORES array")
    exit(1)

existing_stores = json.loads(m.group(1))
current_count = len(existing_stores)

# Check if already added
existing_brands = set(s['brand'] for s in existing_stores)
if "IT'SUGAR" in existing_brands:
    print(f"General candy stores already present. Skipping.")
else:
    existing_stores.extend(GENERAL_CANDY_STORES)
    new_stores_json = json.dumps(existing_stores, ensure_ascii=False)
    html = html[:m.start(1)] + new_stores_json + html[m.end(1):]
    print(f"Added {len(GENERAL_CANDY_STORES)} general candy stores to STORES ({current_count} → {len(existing_stores)})")

# 2. Add general candy brand colors to BRAND_COLORS
m2 = re.search(r'const BRAND_COLORS\s*=\s*(\{.*?\});\s*\n', html, re.DOTALL)
if m2:
    existing_colors = json.loads(m2.group(1))
    for brand, color in GENERAL_CANDY_COLORS.items():
        if brand not in existing_colors:
            existing_colors[brand] = color
    new_colors_json = json.dumps(existing_colors, ensure_ascii=False)
    html = html[:m2.start(1)] + new_colors_json + html[m2.end(1):]
    print(f"Added {len(GENERAL_CANDY_COLORS)} general candy brand colors")

# 3. Update the toggle label
html = html.replace(
    '<label><input type="checkbox" id="show-excluded" /> Exclude / General Candy</label>',
    '<label><input type="checkbox" id="show-excluded" /> Show General Candy Stores</label>'
)

# 4. Update filter logic: show general_candy category when toggle is on
# Currently: if (s.dan_posture === 'exclude' && !se) return;
# Add: if (s.category === 'general_candy' && !se) return;
old_filter = "if (s.status === 'pop_up_or_cart' && !se) return;\n    if (s.dan_posture === 'exclude' && !se) return;"
new_filter = "if (s.status === 'pop_up_or_cart' && !se) return;\n    if (s.dan_posture === 'exclude' && !se) return;\n    if (s.category === 'general_candy' && !se) return;"
html = html.replace(old_filter, new_filter)

# 5. Add visual distinction: general candy markers get dashed border (square shape)
old_marker = """const marker = L.circleMarker([s.latitude, s.longitude], {
      radius: 8, fillColor: color, color: '#fff', weight: 1.5, opacity: 0.8, fillOpacity: 0.85
    });"""
new_marker = """const isGeneral = s.category === 'general_candy';
    const marker = L.circleMarker([s.latitude, s.longitude], {
      radius: isGeneral ? 7 : 8,
      fillColor: color,
      color: isGeneral ? '#252018' : '#fff',
      weight: isGeneral ? 2 : 1.5,
      opacity: 0.9,
      fillOpacity: isGeneral ? 0.6 : 0.85,
      dashArray: isGeneral ? '3,3' : null
    });"""
html = html.replace(old_marker, new_marker)

# 6. Update footer count
html = re.sub(
    r'\d+ total records, \d+ table rows, \d+ brands',
    f'{len(existing_stores)} total records, map includes general candy layer',
    html
)

with open(MAP_PATH, 'w') as f:
    f.write(html)

print(f"\n✅ Done: {len(existing_stores)} total stores in map")
print(f"General candy toggle: 'Show General Candy Stores' (off by default)")
print(f"Visual distinction: dashed dark border + smaller radius for general candy markers")
