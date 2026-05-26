# Goal: Add 100 New Categories to Dan Business Path Dashboard

## Objective
Add 100 new business categories to the main dashboard at `/Users/winslow/Projects/dan-business-path/index.html`. The dashboard currently has 178 categories. After this, it will have 278.

## Source File
Read the definitive list here: `/Users/winslow/Projects/dan-business-path/definitive-100-new-categories.md`

This file contains all 100 categories with: name, Arena (Services or Multi-Unit), Family, and initial Vibe Score.

## What Each New Entry Needs

Every category in the dashboard JSON array has these fields. You must provide ALL of them for each new entry:

```json
{
  "Category": "Category name",
  "Arena": "Services" or "Multi-Unit",
  "Path": "DIY" or "Franchise" or "Acquisition",
  "Family": "Family name from the list",
  "UW Score": 0,
  "Vibe Score": <from the definitive list>,
  "Blended": 0,
  "PathFit": "High" or "Medium" or "Low",
  "Memo": "details/category-slug.html"
}
```

### Scoring Rules
- **UW Score**: Set to `0` for all new entries. These are "vibe scores" only — no underwriting has been done yet.
- **Vibe Score**: Use the value from the definitive list (range 2.5–3.8).
- **Blended**: Set to `0` (will auto-calculate when dashboard loads since UW is 0).
- **PathFit**: Your judgment based on category characteristics:
  - "High" if franchise-heavy, route-based, or acquisition-friendly with many brokers listing these
  - "Medium" if decent acquisition market but more fragmented
  - "Low" if mostly owner-operator, hard to scale, or niche
- **Path**: Best default path for Dan:
  - "Franchise" if major franchise ecosystems exist (e.g., car wash, haircut chain, tax prep)
  - "Acquisition" if broker listings are common and Dan could buy an existing operation
  - "DIY" if starting from scratch is realistic and common
- **Memo**: Generate a URL-safe slug from the category name, e.g., "Roofing repair company" → `"roofing-repair-company.html"`. Use lowercase, hyphens for spaces/special chars.

## Implementation Steps

1. **Read the current index.html** — extract the JSON array from the file (it's a massive single-line array embedded in the HTML).
2. **Read the definitive-100-new-categories.md** — get all 100 categories.
3. **Build 100 new JSON entries** following the schema above.
4. **Append all 100 entries to the existing JSON array** in index.html.
5. **DO NOT change any existing entries.** Only append new ones.
6. **DO NOT change any HTML, CSS, or JavaScript** outside the JSON array.
7. **Verify**: After editing, confirm the JSON parses cleanly and the table renders 278 rows.

## Critical Rules
- The JSON array is embedded in a single line in `index.html`. Use Python to safely parse and re-serialize it. Do NOT try to edit it by hand.
- Keep the array on a single line (minified) — same format as current.
- All 100 new entries should be appended at the END of the existing array.
- Do NOT create new HTML pages for these categories yet — just add them to the dashboard table.
- Test with: `python3 -c "import json; data=json.load(open('index.html').read().split('const categories = ')[1].split(';')[0]); print(len(data))"` after editing.

## Family Assignment Reference
Use these exact Family names (must match existing dashboard families):
- Auto categories → `"Automotive & Fleet"`
- Home Services trades → `"Home Services"`
- Cleaning/Restoration → `"Compliance & Safety"` (or `"Property & Outdoor"` for exterior cleaning)
- Moving/Storage/Logistics → `"Real Estate / Facilities"` (or `"B2B / Distribution"` for document/records)
- Senior Care → `"Senior & Accessibility"`
- Kids/Education → `"Kids & Education"`
- Professional Services → `"B2B / Distribution"`
- Beauty → `"Beauty & Aesthetics"`
- Pet → `"Pet Services"` or `"Health & Wellness"`
- Fitness → `"Sports & Recreation"`
- Food & Beverage → `"Food & Beverage"`

## Git
After successful edit and verification:
- `git add index.html`
- `git commit -m "Add 100 new categories to dashboard (278 total)"`
- `git push origin main`

## Success Criteria
- Dashboard has exactly 278 rows
- All 100 new categories appear in the table
- JSON parses without errors
- No existing categories were modified
- Site still renders correctly at https://w1nsl0wh0m3r-bit.github.io/dan-business-path/
