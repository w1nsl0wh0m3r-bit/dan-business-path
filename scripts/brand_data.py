"""Brand research data for Swedish candy comp profiles — all 31 brands."""

# Each brand entry is a dict with keys matching the generate_page() function.
# Research compiled from web searches June 19, 2026.

BRANDS = []

# ──────────────────────────────────────────────────────────────────────────
# 1. SCANDYCANDY
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "ScandyCandy",
    "slug": "scandycandy",
    "lede": "Founder-led pure Swedish candy retailer in South Florida, founded 2024 by two brothers from Helsingborg. Fast viral growth — sold out in 9 days on opening. Now 3 locations + ecommerce.",
    "posture": "Target watch / proof-only",
    "rows": 3,
    "markets": "South Florida (Miami, Coral Gables, Palm Beach)",
    "confidence": "High",
    "links_html": "",  # filled at runtime
    "units": [],  # filled at runtime
    "diligence_note": "Strong founder authenticity (Swedish brothers, real cultural connection). Viral demand signal is real but young operation — inventory management is the weak spot (sold out in 9 days). Watch whether they can sustain foot traffic beyond the TikTok wave and manage supply chain. Key next question: unit economics and whether Palm Beach seasonal location converts to permanent.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 2. BONBON
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "BonBon",
    "slug": "bonbon",
    "lede": "Category-defining NYC Swedish candy retailer + ecommerce/wholesale. Founded 2017, 6 NYC-area stores, ~$10M revenue, 55 employees. The brand that sparked the TikTok Swedish candy craze.",
    "posture": "Comp / strategic-capital only",
    "rows": 6,
    "markets": "NYC/Brooklyn, Hamptons/Long Island",
    "confidence": "High",
    "links_html": "",
    "units": [],
    "diligence_note": "Market leader by revenue and store count. ~$10M revenue (RocketReach, Jan 2026). Not an acquisition target — too large and established. Strategic comp for benchmarking unit economics, pricing ($14/lb), and expansion playbooks.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 3. GO YUMMY
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Go Yummy",
    "slug": "go-yummy",
    "lede": "Family-run Swedish candy retailer in South Florida. CEO Willie King. 3 locations + online. Claims 'largest Swedish candy store in the US' at Boca Raton flagship with 400+ varieties.",
    "posture": "Target watch / comp",
    "rows": 3,
    "markets": "South Florida (Boca Raton, Fort Lauderdale, Palm Beach Gardens)",
    "confidence": "Medium-High",
    "links_html": "",
    "units": [],
    "diligence_note": "Closest comp to ScandyCandy in South Florida. Multi-unit operator with 3 locations. Key diligence: founder background (Willie King — Swedish connection?), unit economics, expansion pace. Direct head-to-head with ScandyCandy in overlapping markets.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 4. SATURDAY CANDY CO.
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Saturday Candy Co.",
    "slug": "saturday-candy-co",
    "lede": "Founder-led Swedish candy retailer on Long Island, NY. Founded by Julia Brandt, a Swedish immigrant from Setauket. Started online 2024, 3 brick-and-mortar locations by 2025-26.",
    "posture": "Target watch",
    "rows": 3,
    "markets": "Long Island, NY (Stony Brook, Sayville, Westhampton Beach)",
    "confidence": "High",
    "links_html": "",
    "units": [],
    "diligence_note": "Impressive multi-unit growth for a single founder (3 locations in ~18 months). Swedish-born founder with authentic cultural connection. Long Island is a distinct market from NYC — less competition. Key question: can the Long Island model port to other suburban markets?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 5. SWEETISH CANDY
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Sweetish Candy",
    "slug": "sweetish-candy",
    "lede": "Established Swedish candy retailer in Lancaster, PA. Founded 2019 by Tyler Graybeal (non-Swedish founder inspired by trip to Sweden). 2 stores + nationwide ecommerce + wholesale. Featured on NPR, NBC Today Show, Food & Wine.",
    "posture": "Comp / benchmark",
    "rows": 2,
    "markets": "Lancaster, PA + nationwide ecommerce",
    "confidence": "High",
    "links_html": "",
    "units": [],
    "diligence_note": "Proof that non-Swedish founders can build a legitimate Swedish candy business. Went from 30-50 online orders/day to 10,000+ during TikTok surge. Wholesale arm is a differentiator. Key comp for ecommerce economics and wholesale model.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 6. SOCKERBIT
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Sockerbit",
    "slug": "sockerbit",
    "lede": "Pioneer US Swedish candy retailer. Founded 2010 in LA by Florence Baras and Stefan Ernberg (a couple who met at a candy company in Europe). 1 active LA store + Pasadena coming soon. $1-5M revenue range.",
    "posture": "Comp / legacy benchmark",
    "rows": 3,
    "markets": "Los Angeles, CA",
    "confidence": "High",
    "links_html": "",
    "units": [],
    "diligence_note": "The original US Swedish candy store (2010). 14+ years of operating history. Smaller than BonBon but proven longevity. NYC location (Christopher St) closed — important data point on market viability outside LA. Key question: why didn't they scale faster in 14 years?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 7. LIL SWEET TREAT
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Lil Sweet Treat",
    "slug": "lil-sweet-treat",
    "lede": "Fastest-expanding candy retailer in the US. Founded Sept 2024 by Elly Ross (former big tech). 11 locations across 7 cities in <2 years. Multi-category (global candy, not Swedish-only). Viral TikTok presence with millions of views.",
    "posture": "Comp / scale benchmark",
    "rows": 11,
    "markets": "NYC, Boston, Chicago, DC, Philadelphia, San Francisco, Los Angeles",
    "confidence": "High",
    "links_html": "",
    "units": [],
    "diligence_note": "Not a pure Swedish candy play — global pick-and-mix. But the speed of expansion (11 locations in <2 years) is the benchmark for what's possible. Founded by a single young founder. Key question: unit economics and whether Swedish-only is a constraint or advantage vs. their broader approach.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 8. SWEDIE POP
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Swedie Pop",
    "slug": "swedie-pop",
    "lede": "Swedish candy retailer with 2 locations (Cerritos, CA mall + West Palm Beach, FL). Launched 2024 by 'two candy-obsessed moms.' Dual-coast presence.",
    "posture": "Comp",
    "rows": 2,
    "markets": "Cerritos, CA + West Palm Beach, FL",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Interesting dual-coast model. Two single-store locations in very different markets. Key question: is this one operator with 2 stores or 2 independent operators using same brand name?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 9. MUMS — THE SWEDISH CANDY CO.
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Mums — The Swedish Candy Co.",
    "slug": "mums-the-swedish-candy-co",
    "lede": "Swedish candy retailer + ecommerce in Northville, MI (metro Detroit). Claims '#1 Rated Swedish Candy Brand' and '200,000+ Mums Candy Lovers.' Active on Instagram and TikTok. Expanding to pop-ups (Plymouth Art in the Park 2026).",
    "posture": "Target watch",
    "rows": 1,
    "markets": "Northville, MI (metro Detroit) + ecommerce",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Single store but strong online/direct-to-consumer brand. '200,000+ candy lovers' claim is significant if real. Midwest market has less Swedish candy competition. Key question: what's the split between retail and online revenue?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 10. NANTASKET SWEETS BY SWEDES
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Nantasket Sweets By Swedes",
    "slug": "nantasket-sweets-by-swedes",
    "lede": "Swedish-born founder Maria Stolt's candy store. Opened Christmas Eve 2020 on Nantasket Beach in Hull, MA. Now expanding to Boston's Charles Street. Women-owned, only Swedish-woman-owned candy store on the east coast.",
    "posture": "Target watch",
    "rows": 2,
    "markets": "Hull, MA + Boston (Charles St, opening soon)",
    "confidence": "High",
    "links_html": "",
    "units": [],
    "diligence_note": "Authentic Swedish woman-owned operation with 5+ years history. Expanding from beach town to Boston proper. Key comp for understanding second-location economics in New England. Differentiated by homemade fudge and caramels alongside Swedish candy.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 11. SODT
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Sodt",
    "slug": "sodt",
    "lede": "Scandinavian candy shop in Portland, ME, founded by co-owner Nikoline Østergaard. Opened May 2025. Second location opening summer 2026 in Freeport, ME. Curated Scandinavian sweets (not just Swedish).",
    "posture": "Target watch",
    "rows": 2,
    "markets": "Portland, ME + Freeport, ME (opening summer 2026)",
    "confidence": "High",
    "links_html": "",
    "units": [],
    "diligence_note": "Authentic Scandinavian founder (Danish/Norwegian name). Portland→Freeport expansion is a logical retail corridor (Freeport = outlet destination). Two-store model in small Maine market is a good template for tier-2 New England cities.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 12. MADELEINE'S CANDY SHOP
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Madeleine's Candy Shop",
    "slug": "madeleine-s-candy-shop",
    "lede": "Swedish candy shop in Boston's South End. Founded by Madeleine Brason, a former clinical researcher. Opened Feb 2025 to lines down the block. Swedish-inspired with a mix of everything.",
    "posture": "Comp",
    "rows": 1,
    "markets": "Boston South End",
    "confidence": "High",
    "links_html": "",
    "units": [],
    "diligence_note": "Single-location, non-Swedish founder (former clinical researcher). Strong opening demand (lines down the block). Not Swedish-only — broader candy concept. Key question: is this a template for non-Swedish founders or an outlier?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 13. SWEDISH MOOSE CANDY CO.
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Swedish Moose Candy Co.",
    "slug": "swedish-moose-candy-co",
    "lede": "Swedish candy chain in Utah. Founded by Simonsen and Mård-Castman. Multiple Utah locations (American Fork, St. George, Provo). Expanding aggressively in the Utah market.",
    "posture": "Target watch / comp",
    "rows": 1,
    "markets": "Utah (American Fork, St. George, Provo)",
    "confidence": "Medium-High",
    "links_html": "",
    "units": [],
    "diligence_note": "Multi-unit operator in a unique market (Utah — strong Scandinavian heritage, family-oriented culture). Swedish-connected founders. Key comp for understanding non-coastal market dynamics. Multiple locations in a single metro is a different expansion model than coastal city-hopping.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 14. SO SWEDE
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "So Swede",
    "slug": "so-swede",
    "lede": "Swedish candy shop in American Fork, UT. Co-founded by Olive Redd. Opened June 2025. Shopify ecommerce + single brick-and-mortar. Covered by Deseret News.",
    "posture": "Comp",
    "rows": 1,
    "markets": "American Fork, UT",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Competes directly with Swedish Moose in American Fork/Utah Valley. Single location. Key question: how does the Utah market support multiple Swedish candy operators in the same town?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 15. VÄNNEST
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Vännest",
    "slug": "vannest",
    "lede": "Swedish candy store in NYC West Village. Grand opening March 28, 2026. Viral on social media with lines out the door. On the same block as Candy King and near other Swedish candy competitors.",
    "posture": "Comp / market saturation signal",
    "rows": 1,
    "markets": "NYC West Village (Bleecker St)",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "New entrant in an already crowded West Village Swedish candy corridor (Candy King at 306 Bleecker, Vännest at 253 Bleecker, plus nearby competitors). Key signal: this block is becoming the epicenter of Swedish candy competition. Notable for market saturation analysis.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 16. KÄNDI
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Kändi",
    "slug": "kandi",
    "lede": "Swedish candy retailer in Los Angeles with 3 locations (Studio City, Santa Monica, Century City coming soon). Positioned as premium Swedish candy destination.",
    "posture": "Comp",
    "rows": 3,
    "markets": "Los Angeles, CA (Studio City, Santa Monica, Century City)",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Multi-unit LA operator with 3 locations. Direct competitor to Sockerbit in the LA market. Key question: founder background and whether they're Swedish-connected or inspired operators.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 17. GOODIS
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Goodis",
    "slug": "goodis",
    "lede": "Ecommerce-only Swedish candy brand based in Bergen County, NJ. Co-founded by Nemrud Kurt with Swedish family connections. Launched late 2024. 313+ products. Featured on Swedish national TV (TV4). Expanding to Europe.",
    "posture": "Comp / ecommerce benchmark",
    "rows": 1,
    "markets": "Online (Carlstadt, NJ) + expanding to Europe",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Pure ecommerce play — no physical stores. 313+ products is the largest catalog we've found. International expansion to Europe is notable. Key comp for understanding online-only economics vs. brick-and-mortar.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 18. CANDY KING (CLOETTA)
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Candy King (Cloetta)",
    "slug": "candy-king-cloetta",
    "lede": "Corporate-owned Swedish candy giant's first US flagship. CandyKing was founded in Stockholm 1984, operates hundreds of European locations, owned by Cloetta (Stockholm Stock Exchange). NYC West Village flagship opened Dec 6, 2025.",
    "posture": "Comp / exclude (corporate)",
    "rows": 1,
    "markets": "NYC West Village (Bleecker St)",
    "confidence": "High",
    "links_html": "",
    "units": [],
    "diligence_note": "Major corporate entrant with deep resources. Not an acquisition target. Key strategic signal: Cloetta's investment validates the US market but also increases competitive pressure on independents. Their pricing and format set benchmarks.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 19. ALL ABOARD CANDY
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "All Aboard Candy",
    "slug": "all-aboard-candy",
    "lede": "Swedish candy shop in Philadelphia's Rittenhouse Square. Co-founded by childhood besties Emily Grossman and Alyssa Bonventure. Opened June 2025. Built through social media before brick-and-mortar.",
    "posture": "Comp",
    "rows": 1,
    "markets": "Philadelphia, PA (Rittenhouse Square)",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Social-media-first launch model. Non-Swedish founders. Philadelphia is an untapped market for Swedish candy. Key question: foot traffic sustainability and whether single-location model is profitable in Rittenhouse rent environment.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 20. BIG TOP CANDY SHOP
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Big Top Candy Shop",
    "slug": "big-top-candy-shop",
    "lede": "Retro candy shop on South Congress in Austin, TX. Opened 2007 by owner Brandon Hodge. Not Swedish-only — nostalgic/retro candy store that carries Swedish candy (including Moomin-branded). Long-standing Austin institution.",
    "posture": "Comp / exclude (not Swedish-pure)",
    "rows": 1,
    "markets": "Austin, TX (South Congress)",
    "confidence": "High",
    "links_html": "",
    "units": [],
    "diligence_note": "Not a Swedish candy concept — retro/nostalgic candy store. 18+ years operating on South Congress. Included as geographic comp only. Swedish candy is a product line, not the core concept.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 21. BOUNOM EMPORIUM
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "BouNom Emporium",
    "slug": "bounom-emporium",
    "lede": "Swedish candy shop in Avon, CT. Owned by Khamla (also owner of BouNom Bakery nearby). Described as 'only shop dedicated to Swedish candy in Connecticut.' Gilded age candy shop aesthetic.",
    "posture": "Comp",
    "rows": 1,
    "markets": "Avon, CT",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Only dedicated Swedish candy shop in Connecticut. Cross-ownership with bakery is interesting (synergy model). Key question: is the bakery a better business than the candy shop, and is this a dual-concept play?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 22. CONFETTI BLOSSOM
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Confetti Blossom",
    "slug": "confetti-blossom",
    "lede": "Swedish candy shop in Minneapolis skyway system (LaSalle Plaza). New entrant in the Minnesota market. Pop-up and event presence including holiday markets.",
    "posture": "Comp",
    "rows": 1,
    "markets": "Minneapolis, MN (skyway level)",
    "confidence": "Low-Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Very little public information available. Minneapolis skyway location is unusual (office worker traffic, not street retail). Key question: is this a sustainable retail model or a pop-up experiment?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 23. NIKKI'S CANDY
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Nikki's Candy",
    "slug": "nikki-s-candy",
    "lede": "Swedish candy store in Reno, NV. Founded by Nikki (inspired by personal story). Grand opening Oct 28, 2025 in Smithridge Shopping Center. Active social media presence.",
    "posture": "Comp",
    "rows": 1,
    "markets": "Reno, NV",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "First-mover in Reno market — no other Swedish candy stores in Nevada. Personal-story-driven founding. Key question: can Reno support a Swedish candy store, and is this a replicable tier-3 market opportunity?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 24. NECTAR CANDY CO.
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Nectar Candy Co.",
    "slug": "nectar-candy-co",
    "lede": "Swedish candy cart/pop-up operator in Pittsburgh, PA. Mobile candy cart model — not a fixed brick-and-mortar. Active on Instagram with pop-up locations.",
    "posture": "Comp / format alternative",
    "rows": 1,
    "markets": "Pittsburgh, PA (mobile/pop-up)",
    "confidence": "Low-Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Cart/pop-up model is a lower-capital entry format. Interesting for testing market demand before committing to a lease. Key question: what are the economics of a mobile candy cart vs. fixed retail?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 25. SWEDISH CANDY CULTURE
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Swedish Candy Culture",
    "slug": "swedish-candy-culture",
    "lede": "Swedish candy retailer in Fort Worth, TX. Co-owned by Crimson Nathanson. 200+ varieties of imported candy. Also operates a candy truck for events. Dallas-Fort Worth market.",
    "posture": "Comp",
    "rows": 1,
    "markets": "Fort Worth, TX (DFW metro)",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "DFW market entry. Candy truck for events alongside brick-and-mortar is a dual-revenue model. Key question: is DFW a viable Swedish candy market, and what's the store-vs-truck revenue split?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 26. SUGAR MOOSE CANDY
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Sugar Moose Candy",
    "slug": "sugar-moose-candy",
    "lede": "Swedish candy store in Kaysville, UT, with second location in Salt Lake City (9th & 9th). Part of the Utah Swedish candy cluster alongside Swedish Moose and So Swede.",
    "posture": "Comp",
    "rows": 1,
    "markets": "Utah (Kaysville + Salt Lake City)",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Third Swedish candy brand in Utah market. Two locations. Key question: what is it about Utah that supports 3+ Swedish candy operators? Likely Scandinavian heritage + family-oriented culture + lower rent.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 27. SWEETISH FISH (THE)
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "The Sweetish Fish",
    "slug": "the-sweetish-fish",
    "lede": "Swedish candy concept founded by Cape Cod natives Savanna Vaughn and Cara Crupi-Dulmaine. Started as candy truck on Route 6A in Sandwich, MA (June 2025). Now at The Street Chestnut Hill and Seaport pop-ups. Non-Swedish founders inspired by NYC candy trend.",
    "posture": "Comp",
    "rows": 1,
    "markets": "Cape Cod, MA + Chestnut Hill, MA + Boston Seaport",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Truck-to-brick-and-mortar pipeline is a viable capital-efficient entry. Non-Swedish founders. Cape Cod origin with Boston expansion. Key question: is the truck or the mall kiosk the better unit economics?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 28. SWEDISH CANDY LAND
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Swedish Candy Land",
    "slug": "swedish-candy-land",
    "lede": "Online-only Swedish candy retailer based in Ulricehamn, Sweden. Ships worldwide. Founded by Daniel Johansson. Ecommerce-only with blog and fast worldwide shipping.",
    "posture": "Comp / exclude (Swedish-based)",
    "rows": 1,
    "markets": "Online (Ulricehamn, Sweden) — ships to US",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Swedish-based ecommerce operation shipping to the US. Not a US retail acquisition target. Included as comp for understanding the import/supply chain side. Key question: could this be a supplier relationship rather than a competitor?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 29. TO THE MOON
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "To The Moon",
    "slug": "to-the-moon",
    "lede": "Candy shop in Wilton Manors/Fort Lauderdale, FL. Carries Swedish candy alongside other candy types and Dubai chocolate bars. Not Swedish-only — general candy retailer. Named after The Honeymooners TV show.",
    "posture": "Comp / exclude (not Swedish-pure)",
    "rows": 1,
    "markets": "Wilton Manors/Fort Lauderdale, FL",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "General candy retailer, not a Swedish candy concept. 287 Yelp reviews suggest good traffic. Included for geographic comp in the Fort Lauderdale market where Go Yummy and Swedie Pop also operate.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 30. TROLLEY CAR SWEETS & TREATS
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Trolley Car Sweets & Treats",
    "slug": "trolley-car-sweets-and-treats",
    "lede": "Scandinavian candy shop in Richmond, VA (Fan District, Strawberry Street). New entrant. Taking over former Idle Hands space. Covered by Richmond Times-Dispatch.",
    "posture": "Comp",
    "rows": 1,
    "markets": "Richmond, VA (Fan District)",
    "confidence": "Low-Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "First-mover in Richmond market. Very little public information. Key question: is Richmond a viable Swedish candy market? Lower rent and growing food scene could be favorable.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 31. YUMMI JOY
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Yummi Joy",
    "slug": "yummi-joy",
    "lede": "Austin candy store — spinoff of Toy Joy (iconic Austin toy store). Owned by Dorshelle Meyer. Carries Swedish candy alongside European-style candy, vegan ice cream, and fudge. Not Swedish-only.",
    "posture": "Comp / exclude (not Swedish-pure)",
    "rows": 1,
    "markets": "Austin, TX (N Lamar Blvd)",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Part of established Austin retailer ecosystem (Toy Joy). Swedish candy is one product line among many. Key comp for understanding how existing candy retailers are incorporating Swedish candy vs. dedicated Swedish concepts.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 32. HEJ HEJ
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Hej Hej",
    "slug": "hej-hej",
    "lede": "Swedish hot dog and candy pop-up in San Francisco (Cortland Ave). Founded by Steven B (founder of Swedish hot dog pop-up). Expanded from hot dogs to Swedish candy. Active on social media, featured in SF Standard.",
    "posture": "Comp / format alternative",
    "rows": 1,
    "markets": "San Francisco, CA (Cortland Ave)",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Dual-concept (Swedish hot dogs + candy) is unique. Pop-up model in SF. Key question: is the candy a supplement to the food or a standalone business? Different value proposition from pure candy retail.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 33. LILLA SWEDISH CANDY
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Lilla Swedish Candy",
    "slug": "lilla-swedish-candy",
    "lede": "Husband-and-wife team (Nic Jansson and Holly Berrigan) from Whately, MA. Founded online 2025 (lillacandy.co, TikTok @lillacandy). Opening brick-and-mortar in Thornes Marketplace, Northampton, MA in summer 2026.",
    "posture": "Comp / early-stage comp",
    "rows": 1,
    "markets": "Northampton, MA (Thornes Marketplace, opening July 2026)",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Online-to-brick-and-mortar pipeline. Thornes Marketplace is a well-known indie retail destination. Third business for this couple (experienced operators). Key comp for understanding small-market New England viability.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 34. MILLIE'S SWEDISH CANDY
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Millie's Swedish Candy",
    "slug": "millie-s-swedish-candy",
    "lede": "Swedish candy company opening in College Park, Orlando, FL (June 13, 2026). Previously operated as pop-up at Dora Mae Jewelry during holiday events. Part of the Orlando food scene expansion.",
    "posture": "Comp",
    "rows": 1,
    "markets": "Orlando, FL (College Park)",
    "confidence": "Low-Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Pop-up-to-store model in Orlando. Very little public information on founders or scale. Key question: is Orlando a viable market and what's the background of the operator?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 35. SUKKER BABY
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Sukker Baby",
    "slug": "sukker-baby",
    "lede": "Scandinavian candy brand (not just Swedish). Retail presence at The Edit in Toronto. Ecommerce + retail. Mentioned alongside Sockerbit as a Scandinavian (not Swedish-only) candy brand.",
    "posture": "Comp / exclude (Canadian-based)",
    "rows": 1,
    "markets": "Toronto, Canada + online",
    "confidence": "Low",
    "links_html": "",
    "units": [],
    "diligence_note": "Canadian operation. Not a US acquisition target. Included as comp for understanding the broader North American Scandinavian candy market. Key question: are they planning US expansion?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 36. SÖTSAK
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Sötsak",
    "slug": "sotsak",
    "lede": "Swedish candy store opening in Highland Village, Houston, TX. 'Sötsak' means 'sweet thing' in Swedish. New entrant in the Texas market. Limited public information pre-opening.",
    "posture": "Comp / watch",
    "rows": 1,
    "markets": "Houston, TX (Highland Village, opening soon)",
    "confidence": "Low",
    "links_html": "",
    "units": [],
    "diligence_note": "Pre-opening. Houston is a large, diverse market with no established Swedish candy presence. Highland Village is a premium retail destination. Key question: who's behind this and what's their go-to-market strategy?",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 37. THE PIRATE CANDY SHOP
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "The Pirate Candy Shop",
    "slug": "the-pirate-candy-shop",
    "lede": "Not surfaced in public sources reviewed. May be a local candy shop with minimal online presence.",
    "posture": "Unknown",
    "rows": 1,
    "markets": "Unknown",
    "confidence": "Low",
    "links_html": "",
    "units": [],
    "diligence_note": "Could not find public information on this brand. May need direct research or removal from the universe if unverified.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 38. KARAMELLER
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Karameller",
    "slug": "karameller",
    "lede": "Not surfaced in public sources reviewed. May be a local candy shop with minimal online presence.",
    "posture": "Unknown",
    "rows": 1,
    "markets": "Unknown",
    "confidence": "Low",
    "links_html": "",
    "units": [],
    "diligence_note": "Could not find public information on this brand. May need direct research or removal from the universe if unverified.",
    "panels": [],
})

# ──────────────────────────────────────────────────────────────────────────
# 39. SWEDISH CRAVE
# ──────────────────────────────────────────────────────────────────────────
BRANDS.append({
    "name": "Swedish Crave",
    "slug": "swedish-crave",
    "lede": "Swedish candy review/affiliate site (swedishcrave.com) that publishes detailed store reviews. Not a candy retailer — it's a content/review site covering the Swedish candy market.",
    "posture": "Exclude (media/content site)",
    "rows": 1,
    "markets": "Online",
    "confidence": "Medium",
    "links_html": "",
    "units": [],
    "diligence_note": "Not a retail operation. Content/review site. Should be excluded from retail comp analysis but is a valuable intelligence source on the competitive landscape.",
    "panels": [],
})
