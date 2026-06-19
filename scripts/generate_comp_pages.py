#!/usr/bin/env python3
"""Generate all 31 Swedish candy comp profile pages with research data."""

import json
import os
import html as html_mod
from urllib.parse import quote as urlquote
from collections import defaultdict
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(BASE_DIR, "swedish-candy")

# ─── Brand Research Data ───────────────────────────────────────────────────
# Structured research for each brand. Each entry has:
#   founder, origin, news, social, revenue, openings, diligence

BRANDS = {
    "ScandyCandy": {
        "slug": "scandycandy",
        "lede": "Founder-led pure Swedish candy retailer in South Florida, founded 2024 by two brothers from Helsingborg. Viral opening (sold out in 9 days). Now 3 open locations + UTC Sarasota coming soon + ecommerce.",
        "posture": "Target watch / proof-only",
        "markets": "South Florida (Miami, Coral Gables, Palm Beach)",
        "confidence": "High",
        "site": "https://scandycandy.store/",
        "ig": "https://www.instagram.com/explore/search/keyword/?q=ScandyCandy",
        "founder": [
            "Founded 2024 by brothers <strong>Calle Olsen</strong> (23) and <strong>Wille Olsen</strong> (21) from Helsingborg, Sweden.",
            "Moved to US to study and play soccer in Los Angeles before relocating to Miami.",
            "Registered in Florida Feb 27, 2025 as Foreign LLC (filing #M25000002966).",
            "Founder-led, no known outside investors. Full-time operation.",
        ],
        "origin": [
            "From Helsingborg, a coastal city in southern Sweden ~20 min ferry from Denmark.",
            "Started as online-only side project in 2024 while brothers were students in LA.",
            "Moved to Miami after finding LA regulatory environment difficult for food retail.",
            "Core concept: Swedish <em>lördagsgodis</em> (Saturday candy) tradition — weekly pick-and-mix.",
        ],
        "news": [
            "Aug 9, 2025: Coral Gables flagship opened at 241 Miracle Mile — 100+ person lines, 300 customers got $30 credit.",
            "Aug 18, 2025: Forced to close temporarily after selling entire inventory in 9 days. Covered by Miami New Times.",
            "Aug 30, 2025: Reopened with restocked shelves.",
            "Nov 1, 2025: Palm Beach seasonal location opened at Royal Poinciana Plaza.",
            "Dec 2025: SACC Florida membership spotlight feature.",
            "June 2026: UTC Sarasota tenant page and Bradenton Herald report ScandyCandy is coming to The Mall at University Town Center; job postings list store roles at 140 University Town Center Dr.",
        ],
        "social": [
            "Instagram: active, growing (handle not publicly confirmed in search results).",
            "Viral TikTok coverage from Miami-area creators and food influencers.",
            "Miami Herald feature quoted Wille Olsen (age 21).",
        ],
        "revenue": [
            "Not publicly disclosed. No third-party revenue estimates available.",
            "Scale signal: sold entire store inventory in 9 days — strong demand signal.",
            "3 open physical locations + UTC Sarasota announced + online store + warehouse.",
            "Pricing: ~$14-16/lb pick-and-mix (standard for market).",
        ],
        "openings": [
            "Current: Coral Gables (flagship), Coconut Grove, Palm Beach (seasonal).",
            "Opening announced: The Mall at University Town Center, 140 University Town Center Dr, Sarasota, FL.",
            "Palm Beach is seasonal pop-up inside The Current at Royal Poinciana Plaza.",
            "No announced expansion beyond South Florida yet.",
        ],
        "diligence": "Strong founder authenticity. Viral demand is real but operation is young (founded 2024, first store Aug 2025). Inventory management is the weak spot. Watch whether foot traffic sustains beyond TikTok wave. Key question: unit economics and whether seasonal Palm Beach converts to permanent.",
    },
    "BonBon": {
        "slug": "bonbon",
        "lede": "Category-defining NYC Swedish candy retailer + ecommerce/wholesale. Founded 2017, 6 mapped open stores plus Greenwich CT announced, ~$10M revenue estimate, 55 employees. The brand that sparked the TikTok Swedish candy craze.",
        "posture": "Comp / strategic-capital only",
        "markets": "NYC/Brooklyn, Hamptons/Long Island",
        "confidence": "High",
        "site": "https://bonbonnyc.com/",
        "ig": "https://www.instagram.com/bonbonnyc_/",
        "founder": [
            "Founded 2017 by three Swedish friends: <strong>Selim Adira</strong>, <strong>Robert Persson</strong>, and <strong>Leonard (Leo) Schaltz</strong>.",
            "Robert and Selim went to high school together in Malmö, Sweden. Met Leo in NYC ~10 years prior.",
            "Pre-candy backgrounds: finance, shipping, nightlife, restaurant management (Marcus Samuelsson's Aquavit/Red Rooster), event production at UN.",
            "Corporate entity: BonBon — A Swedish Candy Co. NYC-based headquarters.",
        ],
        "origin": [
            "First store opened early 2018 on Allen Street, Lower East Side, NYC.",
            "Concept: 160+ kinds of Scandinavian candy, pick-and-mix by weight ($14/lb).",
            "Expanded methodically over 7 years from 1 to 6 locations.",
            "Added soft serve ice cream and branded merchandise.",
        ],
        "news": [
            "2019: Observer feature interview with all three founders.",
            "2024: TikTok viral explosion — went from ~50 orders/day to 1,000+ overnight (Today Show coverage).",
            "BuzzFeed feature: 'often-sold-out candy store ships over 1,000 orders a day.'",
            "2025-26: Opened Sag Harbor (Hamptons), Upper East Side, Williamsburg locations.",
            "6 retail locations confirmed on FAQ page as of 2026.",
            "Spring 2026: Greenwich Girl / BonBon social snippets say BonBon is opening at 12 West Putnam Avenue, Greenwich, CT in summer 2026.",
        ],
        "social": [
            "Instagram: <strong>71.9K followers</strong> (@bonbonnyc_) as of mid-2026.",
            "TikTok: @bonbonnyc — significant following (Today Show cited viral growth).",
            "Featured in BuzzFeed, Today Show, Eater, Observer, Serious Eats.",
        ],
        "revenue": [
            "RocketReach estimate: <strong>~$10.3M annual revenue</strong> (Jan 2026).",
            "Crustdata: <strong>55 employees</strong> as of Jan 2026, growing 31% YoY.",
            "ZoomInfo: $1M-$5M range (likely outdated/pre-TikTok surge).",
            "1,000+ orders/day during peak TikTok period (2024).",
            "Pricing: $14/lb pick-and-mix + pre-packaged products.",
            "Label as directional estimate — no audited financials public.",
        ],
        "openings": [
            "Current: 6 mapped open locations — Allen St (LES), Degraw St (Red Hook), Sag Harbor, Lexington Ave (UES), Greenwich Ave (West Village), Driggs Ave (Williamsburg).",
            "Opening announced: Greenwich, CT at 12 West Putnam Avenue, summer 2026.",
            "Growing ecommerce business shipping nationwide.",
            "Careers email active (careers@bonbonnyc.com) — team growing.",
        ],
        "diligence": "Market leader by revenue and store count. ~$10M revenue. Not an acquisition target — too large and established. Strategic comp for benchmarking unit economics, pricing ($14/lb), and expansion playbooks.",
    },
    "Go Yummy": {
        "slug": "go-yummy",
        "lede": "Family-run Swedish candy retailer in South Florida. CEO Willie King. 3 locations + online. Claims 'largest Swedish candy store in the US' at Boca Raton with 400+ varieties.",
        "posture": "Target watch / comp",
        "markets": "South Florida (Boca Raton, Fort Lauderdale, Palm Beach Gardens)",
        "confidence": "Medium-High",
        "site": "https://goyummyusa.com/",
        "ig": "https://www.instagram.com/goyummyswedishcandy",
        "founder": [
            "Family-run operation. CEO: <strong>Willie King</strong> (interviewed on Instagram).",
            "Swedish connection not yet confirmed — may be inspired operator rather than Swedish-born.",
            "Co-founder/owner Amelia King identified on Instagram (Amelia's Swedish Candy Truck).",
        ],
        "origin": [
            "Opened Boca Raton location fall 2025 — 400+ varieties of imported Swedish candy.",
            "Described as 'largest Swedish candy store in the US' by creators and Palm Beach Post.",
            "Direct competitor to ScandyCandy in South Florida market.",
        ],
        "news": [
            "Dec 16, 2025: Palm Beach Post feature — 'Why are people so obsessed with the new Swedish candy shop in Boca Raton?'",
            "Instagram creator coverage: 'THE LARGEST SWEDISH CANDY STORE IN THE US' reel went viral.",
            "Planning new Florida locations and online store launch per Palm Beach Post.",
        ],
        "social": [
            "Instagram: @goyummyswedishcandy — active, growing.",
            "Significant TikTok/Instagram reel coverage from South Florida food creators.",
            "CEO Willie King interviewed by content creators.",
        ],
        "revenue": [
            "Not publicly disclosed. No third-party estimates available.",
            "Claims 400+ candy varieties — implies significant import volume.",
            "3 locations in South Florida (high-traffic retail areas).",
            "Pricing: ~$14-16/lb pick-and-mix (market standard).",
        ],
        "openings": [
            "Current: Boca Raton (flagship), Fort Lauderdale, Palm Beach Gardens.",
            "Two new Florida locations planned per Palm Beach Post (Dec 2025).",
            "Online store launching per press coverage.",
        ],
        "diligence": "Closest comp to ScandyCandy in South Florida. Multi-unit operator with 3 locations. Key question: founder background (Willie King — Swedish connection?), unit economics, expansion pace. Direct head-to-head with ScandyCandy.",
    },
    "Saturday Candy Co.": {
        "slug": "saturday-candy-co",
        "lede": "Founder-led Swedish candy retailer on Long Island, NY. Founded by Julia Brandt, a Swedish immigrant. Started online 2024, 3 brick-and-mortar locations by 2025-26.",
        "posture": "Target watch",
        "markets": "Long Island, NY (Stony Brook, Sayville, Westhampton Beach)",
        "confidence": "High",
        "site": "http://saturdaycandyco.org/",
        "ig": "https://www.instagram.com/saturdaycandyco",
        "founder": [
            "Founded by <strong>Julia Brandt</strong>, a local Setauket mom who moved from Sweden to the US in 2018.",
            "Founded the brand in July 2024 shortly after welcoming her first child.",
            "Solo founder — no co-founders identified.",
            "Swedish-born with authentic cultural connection to <em>lördagsgodis</em>.",
        ],
        "origin": [
            "Started as online shop from her Three Village home.",
            "Grew through community events across the Hamptons.",
            "First brick-and-mortar opened October 2025 in Stony Brook Village.",
            "Expanded to Sayville and Westhampton Beach within ~12 months.",
        ],
        "news": [
            "Oct 2025: Greater Long Island feature — 'Colorful new candy shop brings a taste of Sweden to Stony Brook Village.'",
            "TikTok: 'Long Island's newest Swedish Candy store is now open' — 4,674 likes, 114 comments.",
            "Rapid expansion: 3 locations in ~12 months from online launch.",
        ],
        "social": [
            "Instagram: @saturdaycandyco — active.",
            "TikTok: @saturdaycandyco — growing, featured on Hoboken Girl and other outlets.",
            "Strong local Long Island press and community engagement.",
        ],
        "revenue": [
            "Not publicly disclosed. No third-party estimates.",
            "3 locations in affluent Long Island communities.",
            "Stony Brook Village and Hamptons markets = premium foot traffic.",
            "Vegan/gluten-free options from Bubs brand + branded merchandise (tote bags, crewnecks, hats).",
        ],
        "openings": [
            "Current: Stony Brook (73 Main St), Sayville (12 Gillette Ave), Westhampton Beach (1 Moniebogue Lane).",
            "Open 7 days a week, 10am-6pm.",
            "No announced expansion beyond Long Island yet.",
        ],
        "diligence": "Impressive multi-unit growth for a single founder (3 locations in ~18 months). Swedish-born founder. Long Island is a distinct market from NYC — less competition. Key question: can the Long Island model port to other suburban markets?",
    },
    "Sweetish Candy": {
        "slug": "sweetish-candy",
        "lede": "Established Swedish candy retailer in Lancaster, PA. Founded 2019 by Tyler Graybeal (non-Swedish founder inspired by trip to Sweden). 2 stores + nationwide ecommerce + wholesale.",
        "posture": "Comp / benchmark",
        "markets": "Lancaster, PA + nationwide ecommerce",
        "confidence": "High",
        "site": "https://www.sweetishcandy.com/",
        "ig": "https://www.instagram.com/sweetishcandystore/",
        "founder": [
            "Founded by <strong>Tyler Graybeal</strong> — non-Swedish founder inspired by friends who studied in Lund, Sweden.",
            "Background: not in candy retail previously. Noticed vacant storefront in downtown Lancaster.",
            "Flew to Sweden to experience pick-and-mix culture firsthand before launching.",
            "Solo founder/owner.",
        ],
        "origin": [
            "Opened 2019 at 301 N Queen St, downtown Lancaster, PA.",
            "COVID pivot: launched online store in 2020 — proved critical for survival.",
            "2023: Launched Sweetish Wholesale, supplying other Scandinavian retailers.",
            "2024: TikTok surge — went from 30-50 orders/day to 10,000+ orders.",
        ],
        "news": [
            "NPR Marketplace 'My Economy' series (Oct 1, 2024) — documented TikTok surge.",
            "NBC Today Show (Mar 18, 2024) — named as destination for vegan Swedish candies.",
            "Food & Wine (Feb 26, 2024) — recommended for authentic 'Saturday candy.'",
            "YouTube: 'Behind the Scenes of a Candy Shop - Meet the Owner' feature.",
            "6-year anniversary interview with Tyler Graybeal (Apr 3, 2025).",
        ],
        "social": [
            "Instagram: <strong>12K followers</strong> (@sweetishcandystore) — 'Imported Scandinavian Sweets Lancaster, PA.'",
            "2,500+ posts. Active content strategy.",
            "Significant earned media (NPR, NBC, Food & Wine).",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Scale signal: 10,000+ orders in days during TikTok surge.",
            "Wholesale arm = additional revenue stream beyond DTC.",
            "2 physical locations + nationwide ecommerce + wholesale.",
            "200+ candy varieties.",
            "Trustpilot: 3.7/5 — online fulfillment was the weak spot during surge.",
        ],
        "openings": [
            "Queen St (downtown Lancaster): original flagship, open Tue-Sun.",
            "Granite Run (Sweetish North): opened 2024 to handle growing demand.",
            "No announced expansion beyond Lancaster yet.",
        ],
        "diligence": "Proof that non-Swedish founders can build a legitimate Swedish candy business. Wholesale arm is a differentiator. Key comp for ecommerce economics. Online fulfillment is the operational risk.",
    },
    "Sockerbit": {
        "slug": "sockerbit",
        "lede": "Pioneer US Swedish candy retailer. Founded 2010 in LA by Florence Baras and Stefan Ernberg. 1 active LA store + Pasadena coming soon. $1-5M revenue range.",
        "posture": "Comp / legacy benchmark",
        "markets": "Los Angeles, CA",
        "confidence": "High",
        "site": "https://sockerbit.com/",
        "ig": "https://www.instagram.com/sockerbitnyc/",
        "founder": [
            "Founded 2010 by <strong>Florence Baras</strong> and <strong>Stefan Ernberg</strong> — a couple.",
            "Met while working at a candy company in Europe.",
            "Swedish/European candy industry veterans.",
        ],
        "origin": [
            "First store opened 2010 in Los Angeles (7922 W 3rd St) — the original US Swedish candy store.",
            "'Sockerbit' = Swedish for 'sugar cube.'",
            "Expanded to NYC (Christopher St, Greenwich Village) — later closed.",
            "14+ years of operating history.",
        ],
        "news": [
            "KTLA feature: 'Exploring Swedish candy at L.A.'s Sockerbit.'",
            "Forbes: named one of best candy stores in the US and Canada.",
            "LAist: named one of best chocolate and candy shops in Los Angeles.",
            "Yelp: 346 reviews — strong local reputation.",
            "NYC Christopher St location closed — important market viability data point.",
        ],
        "social": [
            "Instagram: @sockerbitnyc — active.",
            "Positioning: 'curate the very best of authentic Swedish candy, handpicking iconic treats.'",
            "Yelp: 346 reviews (one of most-reviewed Swedish candy stores in US).",
        ],
        "revenue": [
            "ZoomInfo: <strong>$1M-$5M revenue</strong>, 10-19 employees.",
            "Single active retail location + ecommerce.",
            "14 years of operating history = proven sustainability.",
            "Pricing: premium LA market positioning.",
        ],
        "openings": [
            "Current: Los Angeles (7922 W 3rd St) — active.",
            "Coming soon: Pasadena (One Colorado, D21).",
            "NYC (89 Christopher St) — CLOSED.",
        ],
        "diligence": "The original US Swedish candy store (2010). 14+ years operating history. Smaller than BonBon but proven longevity. NYC location closed — important data point. Key question: why didn't they scale faster in 14 years?",
    },
    "Lil Sweet Treat": {
        "slug": "lil-sweet-treat",
        "lede": "Fastest-expanding candy retailer in the US. Founded Sept 2024 by Elly Ross (former big tech). 11 locations across 7 cities in <2 years. Multi-category global candy, not Swedish-only.",
        "posture": "Comp / scale benchmark",
        "markets": "NYC, Boston, Chicago, DC, Philadelphia, San Francisco, Los Angeles",
        "confidence": "High",
        "site": "https://lilsweettreat.com/",
        "ig": "https://www.instagram.com/ellybellyeats/",
        "founder": [
            "Founded September 2024 by <strong>Elly Ross</strong> (also known as Elly Belly).",
            "Former big tech employee. Left corporate to start candy business.",
            "Viral TikTok personality — millions of views as @ellybellyeats.",
            "Solo founder with growing corporate team.",
        ],
        "origin": [
            "Started as TikTok content creator (@ellybellyeats) reviewing candy.",
            "First physical location: East Village, NYC.",
            "Expanded to 11 locations across 7 cities in <2 years.",
            "Multi-category: global pick-and-mix candy, not Swedish-only.",
        ],
        "news": [
            "Retail Brew feature: 'How Lil Sweet Treat built a community of candy connoisseurs on TikTok.'",
            "Rockefeller Center feature: 'Meet Elly Ross, the Founder of Lil Sweet Treat.'",
            "TODAY Show: 'How this candy connoisseur left big tech and found sweet success.'",
            "Hoboken Girl: announced Hoboken location.",
            "TikTok: announced San Francisco grand opening June 6.",
        ],
        "social": [
            "TikTok: @ellybellyeats — millions of views, major viral following.",
            "Instagram: active corporate account + founder personal account.",
            "Rockefeller Center location = major brand partnership.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "11 locations across 7 major US cities in <2 years.",
            "Corporate team growing (taste testing new candies for expansion).",
            "Multi-category revenue (not just Swedish candy).",
        ],
        "openings": [
            "Current (11): East Village, West Village, Upper West Side, Rockefeller Center (NYC); Back Bay (Boston); West Loop (Chicago); Georgetown (DC); Walnut St (Philadelphia); Chestnut St (San Francisco); The Grove + Abbot Kinney (Venice/LA).",
            "Hoboken, NJ announced after public vote / Hoboken Girl and social snippets; exact address not surfaced yet.",
            "Aggressive multi-city expansion model.",
        ],
        "diligence": "Not a pure Swedish candy play — global pick-and-mix. But 11 locations in <2 years is the benchmark. Founded by a single young founder. Key question: unit economics and whether Swedish-only is a constraint or advantage vs. their broader approach.",
    },
    "Swedie Pop": {
        "slug": "swedie-pop",
        "lede": "Swedish candy retailer with 2 locations (Cerritos, CA + West Palm Beach, FL). Launched 2024 by 'two candy-obsessed moms.' Dual-coast presence.",
        "posture": "Comp",
        "markets": "Cerritos, CA + West Palm Beach, FL",
        "confidence": "Medium",
        "site": "https://www.swediepop.com/",
        "ig": None,
        "founder": [
            "Launched 2024 by 'two candy-obsessed moms' (names not publicly confirmed).",
            "'Straight outta Sweden & Scandinavia & ready to snack' (per website).",
            "West Palm Beach location positioning: 'from our family to yours.'",
        ],
        "origin": [
            "Launched 2024 in Long Beach (LB) area per itsswediepop.com.",
            "West Palm Beach location at 3700 S Dixie Hwy.",
            "Cerritos location at Los Cerritos Center mall.",
        ],
        "news": [
            "Website: itsswediepop.com — 'launched in 2024 in the LB by two candy obsessed moms.'",
            "swediepop.com — separate West Palm Beach operation.",
            "Possible two separate operators using similar brand name.",
        ],
        "social": [
            "Instagram presence for both locations.",
            "Limited press coverage compared to competitors.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "2 locations in very different markets (SoCal mall + South Florida).",
            "Limited scale signals.",
        ],
        "openings": [
            "Current: Cerritos (Los Cerritos Center mall), West Palm Beach.",
            "No announced expansion.",
        ],
        "diligence": "Interesting dual-coast model. Key question: is this one operator with 2 stores or 2 independent operators using same brand name? Two different websites (itsswediepop.com vs swediepop.com) suggests possible split.",
    },
    "Mums — The Swedish Candy Co.": {
        "slug": "mums-the-swedish-candy-co",
        "lede": "Swedish candy retailer + ecommerce in Northville, MI. Claims '#1 Rated Swedish Candy Brand' and '200,000+ Mums Candy Lovers.' Expanding to pop-ups.",
        "posture": "Target watch",
        "markets": "Northville, MI (metro Detroit) + ecommerce",
        "confidence": "Medium",
        "site": "https://www.mumscandy.com/",
        "ig": "https://www.instagram.com/mumscandy/",
        "founder": [
            "Founder not publicly identified by name in sources reviewed.",
            "BBB listing: Mums The Swedish Candy Co., 235 E Main St Unit 105b, Northville, MI.",
            "Claims '#1 Rated Swedish Candy Brand' — source of rating not verified.",
        ],
        "origin": [
            "Based in Northville, MI (metro Detroit area).",
            "Strong online/direct-to-consumer brand presence.",
            "Claims '200,000+ Mums Candy Lovers' — likely email/social following.",
        ],
        "news": [
            "Instagram reel (June 11, 2026): 'Made in Sweden. Made to break your taste scale.'",
            "Art in the Park Plymouth, MI 2026 — pop-up presence.",
            "Active social media marketing.",
        ],
        "social": [
            "Instagram: <strong>@mumscandy</strong> — claims '100% Swedish Candy #1 Rated Swedish Candy Brand.'",
            "'200,000+ Mums Candy Lovers' — scale claim, likely combined social/email.",
            "TikTok presence referenced on Instagram.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "'200,000+ candy lovers' claim suggests significant online customer base.",
            "Single brick-and-mortar + ecommerce + pop-ups.",
            "Midwest market = less competition than coastal cities.",
        ],
        "openings": [
            "Current: 235 E Main St Unit 105b, Northville, MI.",
            "Pop-up at Art in the Park, Plymouth MI (2026).",
            "No permanent second location announced.",
        ],
        "diligence": "Single store but strong online brand. '200,000+ candy lovers' claim is significant if real. Midwest market has less competition. Key question: retail vs. online revenue split.",
    },
    "Nantasket Sweets By Swedes": {
        "slug": "nantasket-sweets-by-swedes",
        "lede": "Swedish-born founder Maria Stolt's candy store. Opened Christmas Eve 2020 on Nantasket Beach, Hull, MA. Expanding to Boston's Charles Street. Women-owned.",
        "posture": "Target watch",
        "markets": "Hull, MA + Boston (Charles St, opening soon)",
        "confidence": "High",
        "site": "https://www.nantasketsweets.com/",
        "ig": "https://www.instagram.com/nantasketsweets/",
        "founder": [
            "Founded and owned by <strong>Maria Stolt</strong>, a Swedish woman who left Sweden 5 years ago.",
            "'The only Swedish woman owned Candy store on the east coast USA' (per website).",
            "Open since Christmas Eve 2020.",
            "Solo founder/owner.",
        ],
        "origin": [
            "Beach town location — Nantasket Beach in Hull, MA.",
            "Concept: Swedish candy + homemade fudge, caramels, and chocolates.",
            "Women-owned business.",
        ],
        "news": [
            "WCVB (Boston ABC): 'Swedish candy tempts taste buds by the beach in Hull, Mass.'",
            "Instagram: 'Opening at the intersection of Charles and Revere Street' — Boston expansion.",
            "Website: detailed founding story published.",
        ],
        "social": [
            "Instagram: <strong>@nantasketsweets</strong> — '165 Nantasket Ave HULL, 115 Charles Street Boston.'",
            "Women-owned business positioning.",
            "Active content with candy, fudge, and caramel photos.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Homemade fudge and caramels = higher-margin products alongside candy.",
            "Seasonal beach town location (Nantasket) + year-round Boston (Charles St).",
            "Ecommerce: nationwide shipping.",
        ],
        "openings": [
            "Current: 165 Nantasket Ave, Hull, MA.",
            "Opening soon: 115 Charles St, Boston, MA.",
            "Ecommerce shipping nationwide.",
        ],
        "diligence": "Authentic Swedish woman-owned operation with 5+ years history. Expanding from beach town to Boston. Key comp for second-location economics in New England. Differentiated by homemade products alongside Swedish candy.",
    },
    "Sodt": {
        "slug": "sodt",
        "lede": "Scandinavian candy shop in Portland, ME, founded by Nikoline Østergaard. Opened May 2025. Second location in Freeport, ME opening summer 2026.",
        "posture": "Target watch",
        "markets": "Portland, ME + Freeport, ME (opening summer 2026)",
        "confidence": "High",
        "site": "https://www.sodtme.com/",
        "ig": None,
        "founder": [
            "Co-owned by <strong>Nikoline Østergaard</strong> (Scandinavian name — likely Danish/Norwegian).",
            "Husband-and-wife or partner team (co-owner referenced).",
        ],
        "origin": [
            "Located at 119 Cumberland Ave, Portland (formerly Sticky Sweet space).",
            "'Sødt' = Danish/Norwegian for 'sweet.'",
            "Curated Scandinavian sweets (not just Swedish — broader Nordic).",
        ],
        "news": [
            "Portland Press Herald (May 6, 2026): 'Portland's Nordic candy store opening Freeport location this summer.'",
            "Portland Food Map: tracked store construction and opening.",
            "YouTube: 'Portland welcomes Sodt, a new Scandinavian-inspired candy shop.'",
            "Instagram: 'officially opening May 17th @ 12pm!'",
        ],
        "social": [
            "Instagram: active presence for @sodt (Portland).",
            "Strong local Portland press coverage.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "2 locations (Portland + Freeport) in small Maine market.",
            "Freeport = outlet shopping destination (LL Bean HQ) = tourist foot traffic.",
        ],
        "openings": [
            "Current: 119 Cumberland Ave, Portland, ME.",
            "Coming summer 2026: 58 Main St, Freeport, ME.",
        ],
        "diligence": "Authentic Scandinavian founder. Portland→Freeport expansion is logical retail corridor. Two-store model in small Maine market is a good template for tier-2 New England cities.",
    },
    "Madeleine's Candy Shop": {
        "slug": "madeleine-s-candy-shop",
        "lede": "Swedish candy shop in Boston's South End. Founded by Madeleine Brason, a former clinical researcher. Opened Feb 2025 to lines down the block.",
        "posture": "Comp",
        "markets": "Boston South End",
        "confidence": "High",
        "site": None,
        "ig": "https://www.instagram.com/madeleinescandyshop",
        "founder": [
            "Founded by <strong>Madeleine Brason</strong> — former clinical researcher.",
            "'Never planned to open a candy shop' — stumbled into it.",
            "Non-Swedish founder inspired by NYC candy trend.",
        ],
        "origin": [
            "Opened February 2025 at 47 Clarendon St, Boston South End.",
            "Opened on a cold, snowy day to a line down the block.",
            "'My candy shop is a little bit of everything' — not Swedish-only.",
        ],
        "news": [
            "Edible Boston (Nov 13, 2025): 'Edible Food Find: Madeleine's Candy Shop.'",
            "Daily Free Press (Apr 17, 2021): early coverage of concept.",
            "Berkeley Beacon: profile of opening.",
            "Boston.com (Nov 5, 2025): 'The Swedish candy craze has taken Boston by storm.'",
        ],
        "social": [
            "Instagram: <strong>@madeleinescandyshop</strong> — 'instantly famous' per Boston.com.",
            "Strong earned media from Boston press.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Single location in high-rent South End.",
            "Strong opening demand (lines down the block).",
        ],
        "openings": [
            "Current: 47 Clarendon St, Boston, MA 02116.",
            "Single location, no announced expansion.",
        ],
        "diligence": "Single-location, non-Swedish founder (former clinical researcher). Strong opening demand. Not Swedish-only. Key question: is this a template for non-Swedish founders or an outlier?",
    },
    "Swedish Moose Candy Co.": {
        "slug": "swedish-moose-candy-co",
        "lede": "Swedish candy chain in Utah. Multiple locations (American Fork, St. George, Provo). Founded by Simonsen and Mård-Castman. Expanding in Utah.",
        "posture": "Target watch / comp",
        "markets": "Utah (American Fork, St. George, Provo)",
        "confidence": "Medium-High",
        "site": "https://swedishmoose.co/",
        "ig": None,
        "founder": [
            "Founded by <strong>Simonsen</strong> and <strong>Mård-Castman</strong>.",
            "Swedish-connected founders (Scandinavian surnames).",
        ],
        "origin": [
            "Multiple Utah locations — American Fork, St. George, Provo.",
            "'Come experience a taste of Sweden at one of our Utah locations!'",
        ],
        "news": [
            "SLUG Mag: 'It's Always the Weekend at Swedish Moose Candy Co.' — profile of founders.",
            "Instagram: 'TELL YOUR KIDS' — grand opening coverage for American Fork.",
            "Explore Utah Valley Facebook: grand opening coverage in Provo.",
            "Two new stores in American Fork and St. George planned for spring (per SLUG Mag).",
        ],
        "social": [
            "Instagram: active with grand opening content and product photos.",
            "Strong Utah food blogger coverage (@wasatcheats).",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Multiple locations in Utah market.",
            "Online store at swedishmoose.co.",
        ],
        "openings": [
            "Current: American Fork, St. George, Provo (Utah).",
            "Multiple locations expanding within Utah.",
        ],
        "diligence": "Multi-unit operator in a unique market (Utah — Scandinavian heritage, family culture). Key comp for understanding non-coastal market dynamics. Multiple locations in a single metro is a different model than coastal city-hopping.",
    },
    "So Swede": {
        "slug": "so-swede",
        "lede": "Swedish candy shop in American Fork, UT. Co-founded by Olive Redd. Opened June 2025. Shopify ecommerce + single brick-and-mortar.",
        "posture": "Comp",
        "markets": "American Fork, UT",
        "confidence": "Medium",
        "site": "https://ohsoswede.com/",
        "ig": "https://www.instagram.com/ohsoswede",
        "founder": [
            "Co-founded by <strong>Olive Redd</strong> (per Deseret News).",
            "Shopify-based ecommerce at ohsoswede.com.",
        ],
        "origin": [
            "Opened June 2025 at 38 N Merchant St, American Fork, UT.",
            "'Colorful aesthetic, nostalgic energy and distinctly Scandinavian sweets.'",
        ],
        "news": [
            "Deseret News (Oct 28, 2025): 'Utah can't get enough of this Swedish candy store.'",
            "Lehi Free Press / AF Citizen: 'So Swede candy shop brings foreign flavors to AF.'",
            "Directly competes with Swedish Moose Candy Co. in American Fork.",
        ],
        "social": [
            "Instagram: @ohsoswede — 'Follow us on Instagram.'",
            "Deseret News feature with photos.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Single location + ecommerce.",
            "Carries Candy People, Bubs, and other Scandinavian brands.",
        ],
        "openings": [
            "Current: 38 N Merchant St, American Fork, UT.",
            "No announced expansion.",
        ],
        "diligence": "Competes directly with Swedish Moose in American Fork/Utah Valley. Key question: how does Utah support multiple Swedish candy operators in the same town?",
    },
    "Vännest": {
        "slug": "vannest",
        "lede": "Swedish candy store in NYC West Village. Grand opening March 28, 2026. Viral on social media with lines out the door.",
        "posture": "Comp / market saturation signal",
        "markets": "NYC West Village (Bleecker St)",
        "confidence": "Medium",
        "site": None,
        "ig": None,
        "founder": [
            "Founder identity not surfaced in public sources reviewed.",
            "Swedish-connected branding and concept.",
        ],
        "origin": [
            "253 Bleecker St, West Village — grand opening March 28, 2026.",
            "Located on same block as Candy King (306 Bleecker).",
        ],
        "news": [
            "Instagram: 'THE GRAND OPENING! VÄNNEST SWEDISH CANDY STORE' — viral coverage.",
            "'The most popular candy shop in NYC for a reason' — creator content.",
            "'The viral Swedish candy store everyone's talking about just opened in the West Village.'",
            "Yelp: listed as top Swedish candy in NYC.",
        ],
        "social": [
            "Instagram: strong viral content with multiple creators covering opening.",
            "TikTok: creator hauls and reviews.",
            "Lines out the door on opening day.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Single location, newly opened.",
            "West Village = high-rent, high-traffic retail.",
        ],
        "openings": [
            "Current: 253 Bleecker St, New York, NY.",
            "Single location, newly opened March 2026.",
        ],
        "diligence": "New entrant in already crowded West Village Swedish candy corridor. Candy King at 306 Bleecker, Vännest at 253 Bleecker. Key signal: this block is becoming the epicenter of Swedish candy competition.",
    },
    "Kändi": {
        "slug": "kandi",
        "lede": "Swedish candy retailer in Los Angeles with 3 locations (Studio City, Santa Monica, Century City coming soon). Premium positioning.",
        "posture": "Comp",
        "markets": "Los Angeles, CA (Studio City, Santa Monica, Century City)",
        "confidence": "Medium",
        "site": None,
        "ig": None,
        "founder": [
            "Founder identity not surfaced in public sources reviewed.",
        ],
        "origin": [
            "Studio City: 12188 Ventura Blvd (Yelp: 67 reviews, top Swedish candy in LA).",
            "Santa Monica: 1230 Montana Ave Ste 103.",
            "Century City: Westfield Century City (coming soon).",
        ],
        "news": [
            "Yelp: #1 Swedish candy near Los Angeles.",
            "TikTok: 'The best Swedish candy in LA! Kändi, 12188 Ventura Blvd, Studio City.'",
            "SACC Florida networking event featured Kändi products.",
        ],
        "social": [
            "TikTok: creator coverage from LA food influencers.",
            "Instagram: presence referenced in TikTok content.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "3 locations in prime LA retail areas.",
            "Direct competitor to Sockerbit in LA market.",
        ],
        "openings": [
            "Current: Studio City (Ventura Blvd), Santa Monica (Montana Ave).",
            "Coming soon: Century City (Westfield mall).",
        ],
        "diligence": "Multi-unit LA operator with 3 locations. Direct competitor to Sockerbit. Key question: founder background and Swedish connection.",
    },
    "Goodis": {
        "slug": "goodis",
        "lede": "Ecommerce-only Swedish candy brand based in NJ. Co-founded by Nemrud Kurt with Swedish family connections. Launched late 2024. 313+ products. Expanding to Europe.",
        "posture": "Comp / ecommerce benchmark",
        "markets": "Online (Carlstadt, NJ) + expanding to Europe",
        "confidence": "Medium",
        "site": "https://goodis.us/",
        "ig": "https://www.instagram.com/goodis.us/",
        "founder": [
            "Co-founded by <strong>Nemrud Kurt</strong> (Bergen County, NJ entrepreneur).",
            "Family connections in Sweden.",
            "Featured on Swedish national TV (TV4) for US Swedish candy expansion.",
        ],
        "origin": [
            "Launched late 2024 as ecommerce-only operation.",
            "Based in Carlstadt, NJ (Bergen County).",
            "313+ products — largest Swedish candy catalog found.",
        ],
        "news": [
            "NJBiz: 'New Jersey-based confectioner aims to capitalize on Swedish candy craze.'",
            "Snack & Bakery Wholesale: 'Goodis expands candy brand to Europe.'",
            "Instagram: 'Goodis goes primetime — featured in Swedish national TV (TV4).'",
            "SwedishCrave: 'Goodis launched last fall... one of the largest Swedish candy e-commerce stores in the US.'",
        ],
        "social": [
            "Instagram: @goodis.us — active.",
            "Swedish national TV feature (TV4).",
            "SwedishCrave detailed review.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "313+ product catalog.",
            "Ecommerce-only — no physical stores.",
            "International expansion to Europe announced.",
        ],
        "openings": [
            "No physical locations — ecommerce only.",
            "Expanding to European markets.",
        ],
        "diligence": "Pure ecommerce play — no physical stores. 313+ products is largest catalog. International expansion is notable. Key comp for online-only economics vs. brick-and-mortar.",
    },
    "Candy King (Cloetta)": {
        "slug": "candy-king-cloetta",
        "lede": "Corporate-owned Swedish candy giant's first US flagship. CandyKing founded Stockholm 1984, owned by Cloetta (Stockholm Stock Exchange). NYC flagship opened Dec 6, 2025.",
        "posture": "Comp / exclude (corporate)",
        "markets": "NYC West Village (Bleecker St)",
        "confidence": "High",
        "site": None,
        "ig": "https://www.instagram.com/candyking_nyc",
        "founder": [
            "Founded in Stockholm, 1984 — Europe's leading pick-and-mix candy retailer.",
            "Owned by <strong>Cloetta</strong>, a Swedish public company listed on Stockholm Stock Exchange.",
            "Hundreds of European locations.",
            "Corporate-owned — not a founder-led startup.",
        ],
        "origin": [
            "40+ year history in European candy retail.",
            "First US location: 306 Bleecker St, West Village, NYC.",
            "Opened December 6, 2025.",
        ],
        "news": [
            "Time Out: 'This super popular Swedish candy brand is opening its first US store in NYC.'",
            "Snack Food & Wholesale Bakery (Mar 2026): 'Candy Profile' industry feature.",
            "SwedishCrave: detailed review of NYC flagship.",
            "27-foot-wide candy wall — approximately 200+ varieties.",
            "Exclusive art installations by AJ Lavilla and Michela Muserra.",
        ],
        "social": [
            "Instagram: @candyking_nyc.",
            "TikTok: @candyking_nyc.",
            "Tripadvisor: 5.0/5 rating.",
        ],
        "revenue": [
            "Parent company Cloetta is publicly traded — US store economics not broken out.",
            "27-foot candy wall = 200+ varieties.",
            "Premium pricing: $15-25/lb depending on mix.",
        ],
        "openings": [
            "Current: 306 Bleecker St, NYC West Village.",
            "US flagship only — no additional US locations announced.",
        ],
        "diligence": "Major corporate entrant with deep resources. Not an acquisition target. Key signal: Cloetta's investment validates the US market but increases competitive pressure on independents.",
    },
    "All Aboard Candy": {
        "slug": "all-aboard-candy",
        "lede": "Swedish candy shop in Philadelphia's Rittenhouse Square. Co-founded by childhood besties Emily Grossman and Alyssa Bonventure. Opened June 2025.",
        "posture": "Comp",
        "markets": "Philadelphia, PA (Rittenhouse Square)",
        "confidence": "Medium",
        "site": None,
        "ig": "https://www.instagram.com/allaboardcandy/",
        "founder": [
            "Co-founded by <strong>Emily Grossman</strong> and <strong>Alyssa Bonventure</strong> — childhood besties.",
            "Non-Swedish founders.",
            "Social-media-first launch model.",
        ],
        "origin": [
            "Opened brick-and-mortar June 2025 at 233 S 20th St, Rittenhouse Square.",
            "Built social media following before opening physical store.",
            "Swedish candy wall is a key feature alongside other candy types.",
        ],
        "news": [
            "Grid Philly (Feb 2026): 'Fueled by social media, entrepreneurs open a sweet brick-and-mortar.'",
            "PhillyMag (Jun 2025): 'All Aboard Candy: A Sweet New Shop Lands in Rittenhouse Square.'",
            "6ABC: 'All Aboard Candy is Rittenhouse Square's newest Candy Store.'",
        ],
        "social": [
            "Instagram: @allaboardcandy — 'officially open in Rittenhouse Square.'",
            "Strong social media presence built before brick-and-mortar.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Single location in Rittenhouse Square (high-rent).",
            "Swedish candy wall + other candy types.",
        ],
        "openings": [
            "Current: 233 S 20th St, Philadelphia, PA.",
            "Single location.",
        ],
        "diligence": "Social-media-first launch model. Non-Swedish founders. Philadelphia is an untapped market. Key question: foot traffic sustainability in Rittenhouse rent environment.",
    },
    "Big Top Candy Shop": {
        "slug": "big-top-candy-shop",
        "lede": "Retro candy shop on South Congress in Austin, TX. Opened 2007 by owner Brandon Hodge. Not Swedish-only — nostalgic/retro candy store.",
        "posture": "Comp / exclude (not Swedish-pure)",
        "markets": "Austin, TX (South Congress)",
        "confidence": "High",
        "site": None,
        "ig": None,
        "founder": [
            "Owned by <strong>Brandon Hodge</strong>.",
            "18+ years operating on South Congress.",
        ],
        "origin": [
            "Opened 2007 at 1706 S Congress Ave.",
            "'KEEP AUSTIN THE WAY IT WAS' — retro/nostalgic concept.",
            "Carries Moomin Swedish candy as one product line.",
        ],
        "news": [
            "KXAN Austin: Halloween feature with owner Brandon Hodge.",
            "Instagram: 'One of America's oldest family-owned candy shops.'",
            "Carries retro sodas, old-fashioned candy, and Swedish candy.",
        ],
        "social": [
            "Instagram: active presence.",
            "Austin institution — strong local reputation.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "18+ years of operating history.",
            "Retro/nostalgic candy + Swedish candy as product line.",
        ],
        "openings": [
            "Current: 1706 S Congress Ave, Austin, TX.",
            "Single location.",
        ],
        "diligence": "Not a Swedish candy concept — retro/nostalgic candy store. Included as geographic comp only. Swedish candy is a product line, not the core concept.",
    },
    "BouNom Emporium": {
        "slug": "bounom-emporium",
        "lede": "Swedish candy shop in Avon, CT. Owned by Khamla (also owner of BouNom Bakery nearby). 'Only shop dedicated to Swedish candy in Connecticut.'",
        "posture": "Comp",
        "markets": "Avon, CT",
        "confidence": "Medium",
        "site": None,
        "ig": "https://www.instagram.com/bounom_emporium/",
        "founder": [
            "Owned by <strong>Khamla</strong> — also owns BouNom Bakery across the street.",
            "Cross-ownership with established bakery business.",
        ],
        "origin": [
            "Located at 136 Simsbury Rd #15, Avon, CT.",
            "Gilded age candy shop aesthetic.",
            "'No Passport Needed' — Swedish candy tagline.",
        ],
        "news": [
            "Instagram: viral content — 'Swedish candy is taking over the internet, so we came to BouNom Emporium.'",
            "'Did you know BouNom Emporium is the only shop dedicated to Swedish candy in Connecticut?'",
            "Yelp reviews reference BouNom Bakery connection.",
        ],
        "social": [
            "Instagram: @bounom_emporium — active.",
            "Viral Instagram reel coverage.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Dual-concept model (bakery + candy shop).",
            "Only dedicated Swedish candy shop in CT.",
        ],
        "openings": [
            "Current: 136 Simsbury Rd #15, Avon, CT.",
            "Hours: Tue 11:30-5, Thu-Fri 11:30-5, Sat 9:30-5, Sun 9:30-3.",
        ],
        "diligence": "Only dedicated Swedish candy shop in Connecticut. Cross-ownership with bakery is interesting synergy model. Key question: is the bakery a better business, and is this a dual-concept play?",
    },
    "Confetti Blossom": {
        "slug": "confetti-blossom",
        "lede": "Swedish candy shop in Minneapolis skyway system (LaSalle Plaza). New entrant. Pop-up and event presence.",
        "posture": "Comp",
        "markets": "Minneapolis, MN (skyway level)",
        "confidence": "Low-Medium",
        "site": None,
        "ig": None,
        "founder": [
            "Founder identity not surfaced in public sources reviewed.",
        ],
        "origin": [
            "Located at 800 LaSalle Ave, skyway level, Minneapolis.",
            "Suite 222, LaSalle Plaza.",
            "Pop-up and event presence (Uptown Holiday Wonderland Market).",
        ],
        "news": [
            "Yelp: listed as top Swedish candy in Minneapolis.",
            "Instagram: 'Join us in welcoming Confetti Blossom to their new home in LaSalle Plaza.'",
            "Holiday market pop-ups.",
        ],
        "social": [
            "Instagram: limited public presence.",
            "Event-based marketing (holiday markets).",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Skyway-level retail (office worker traffic).",
            "Pop-up revenue from events.",
        ],
        "openings": [
            "Current: LaSalle Plaza, skyway level, Minneapolis, MN.",
        ],
        "diligence": "Very little public information. Skyway location is unusual (office worker traffic). Key question: sustainable retail model or pop-up experiment?",
    },
    "Nikki's Candy": {
        "slug": "nikki-s-candy",
        "lede": "Swedish candy store in Reno, NV. Founded by Nikki. Grand opening Oct 28, 2025. First Swedish candy store in Nevada.",
        "posture": "Comp",
        "markets": "Reno, NV",
        "confidence": "Medium",
        "site": None,
        "ig": "https://www.instagram.com/nikkiscandyreno",
        "founder": [
            "Founded by <strong>Nikki</strong> — personal-story-driven founding.",
            "'The heart behind Nikki's Candy, a business inspired by a...' (Instagram).",
        ],
        "origin": [
            "5025 S McCarran Blvd, Smithridge Shopping Center, Reno, NV.",
            "Grand opening October 28, 2025.",
            "First Swedish candy store in Nevada.",
        ],
        "news": [
            "ThisisReno (Nov 2, 2025): 'Nikki's Candy: A New Swedish Candy Store in South Reno.'",
            "Instagram: 'Nikki's Candy, a Swedish candy store, opened its doors on Oct. 28.'",
        ],
        "social": [
            "Instagram: @nikkiscandyreno — active.",
            "'At Nikki's Candy, our dream customer is… everyone. Kids, parents...'",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "First-mover in Nevada market.",
            "Single location.",
        ],
        "openings": [
            "Current: 5025 S McCarran Blvd, Reno, NV.",
        ],
        "diligence": "First-mover in Reno. Personal-story-driven founding. Key question: can Reno support a Swedish candy store, and is this a replicable tier-3 market?",
    },
    "Nectar Candy Co.": {
        "slug": "nectar-candy-co",
        "lede": "Swedish candy cart/pop-up operator in Pittsburgh, PA. Mobile candy cart model — not fixed brick-and-mortar.",
        "posture": "Comp / format alternative",
        "markets": "Pittsburgh, PA (mobile/pop-up)",
        "confidence": "Low-Medium",
        "site": None,
        "ig": None,
        "founder": [
            "Founder identity not surfaced in public sources reviewed.",
            "'Every sweet thing starts small. Ours starts on wheels!'",
        ],
        "origin": [
            "Mobile candy cart — pop-up locations across Pittsburgh.",
            "No fixed brick-and-mortar location.",
            "SWEDISH CANDY CART in PITTSBURGH — 'need my nectar' branding.",
        ],
        "news": [
            "Instagram: multiple reels covering cart appearances.",
            "'Check out the new candy traveling cart! @nectar_candyco'",
        ],
        "social": [
            "Instagram: @nectar_candyco — active with pop-up content.",
            "Products: Sour Red Twists, Strawnana, Fizzy Pops, Spicy Mango Chews.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Mobile/cart model = lower overhead.",
            "Pop-up event revenue.",
        ],
        "openings": [
            "No fixed location — mobile cart model.",
            "Pop-up appearances across Pittsburgh.",
        ],
        "diligence": "Cart/pop-up model is a lower-capital entry format. Key question: economics of mobile candy cart vs. fixed retail.",
    },
    "Swedish Candy Culture": {
        "slug": "swedish-candy-culture",
        "lede": "Swedish candy retailer in Fort Worth, TX. Co-owned by Crimson Nathanson. 200+ varieties. Also operates a candy truck for events.",
        "posture": "Comp",
        "markets": "Fort Worth, TX (DFW metro)",
        "confidence": "Medium",
        "site": None,
        "ig": "https://www.instagram.com/swedishcandyculture",
        "founder": [
            "Co-owned by <strong>Crimson Nathanson</strong>.",
            "Also referenced intern/hiring posts — growing team.",
        ],
        "origin": [
            "3613 West Vickery Blvd, Fort Worth, TX.",
            "200+ varieties of imported candy.",
            "Also operates Swedish candy truck for events.",
        ],
        "news": [
            "Instagram: 'Swedish Candy Culture will open mid-to-late June at 3613 West Vickery Blvd.'",
            "'Dallas' First Candy Truck' — event and catering services.",
            "SACC Florida networking event reference.",
        ],
        "social": [
            "Instagram: @swedishcandyculture — active.",
            "TikTok: @swedishcandyculture.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Store + candy truck = dual-revenue model.",
            "DFW market entry.",
        ],
        "openings": [
            "Current: 3613 West Vickery Blvd, Fort Worth, TX.",
            "Candy truck for events.",
        ],
        "diligence": "DFW market entry. Store + truck is a dual-revenue model. Key question: is DFW a viable market and what's the store-vs-truck revenue split?",
    },
    "Sugar Moose Candy": {
        "slug": "sugar-moose-candy",
        "lede": "Swedish candy store in Kaysville, UT, with second location in Salt Lake City (9th & 9th). Part of the Utah Swedish candy cluster.",
        "posture": "Comp",
        "markets": "Utah (Kaysville + Salt Lake City)",
        "confidence": "Medium",
        "site": None,
        "ig": None,
        "founder": [
            "Founder identity not surfaced in public sources reviewed.",
        ],
        "origin": [
            "Original location: Main Street, Kaysville, UT.",
            "Second location: 9th and 9th, Salt Lake City — now open.",
            "'Did you know there is a Swedish candy store on Main Street in Kaysville?'",
        ],
        "news": [
            "Instagram (@wasatcheats): 'Big news for the Moose! Sugar Moose...' coverage.",
            "'SLC IS NOW OPEN! Sugar Moose's second location is officially...'",
            "Part of Utah Swedish candy cluster with Swedish Moose and So Swede.",
        ],
        "social": [
            "Instagram: covered by @wasatcheats and local food bloggers.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "2 locations in Utah.",
        ],
        "openings": [
            "Current: Kaysville (Main St) + Salt Lake City (9th & 9th).",
        ],
        "diligence": "Third Swedish candy brand in Utah market. Two locations. Key question: what drives Utah market support for 3+ Swedish candy operators?",
    },
    "The Sweetish Fish": {
        "slug": "the-sweetish-fish",
        "lede": "Swedish candy concept founded by Cape Cod natives Savanna Vaughn and Cara Crupi-Dulmaine. Started as candy truck in Sandwich, MA (June 2025). Now at Chestnut Hill + Seaport pop-ups.",
        "posture": "Comp",
        "markets": "Cape Cod, MA + Chestnut Hill, MA + Boston Seaport",
        "confidence": "Medium",
        "site": None,
        "ig": None,
        "founder": [
            "Founded by <strong>Savanna Vaughn</strong> and <strong>Cara Crupi-Dulmaine</strong> — Cape Cod natives.",
            "Non-Swedish founders inspired by NYC candy trend.",
            "'We saw it take off online and we were like, we need to do this.'",
        ],
        "origin": [
            "Candy truck on Route 6A in Sandwich, MA — opened June 7, 2025.",
            "Expanded to The Street Chestnut Hill (mall).",
            "Seaport pop-up at The Current.",
        ],
        "news": [
            "Cape News: 'Swedish Candy Makes Debut In Sandwich' — founding story.",
            "WBZ-TV: 'The Sweetish Fish is Cape Cod's newest candy business.'",
            "Boston.com: 'The Swedish candy craze has taken Boston by storm' — featured founders.",
            "Instagram: 'Meet The Sweetish Fish, now open at The Street.'",
        ],
        "social": [
            "Instagram: active with truck and pop-up content.",
            "Boston.com feature alongside Madeleine's and Lil Sweet Treat.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Truck + mall location + pop-ups = multi-format model.",
            "'A whole-family experience' positioning.",
        ],
        "openings": [
            "Current: Route 6A Sandwich, MA (truck) + The Street Chestnut Hill.",
            "Pop-up: Seaport (The Current).",
        ],
        "diligence": "Truck-to-brick-and-mortar pipeline is capital-efficient entry. Non-Swedish founders. Cape Cod origin with Boston expansion. Key question: truck vs. mall kiosk unit economics.",
    },
    "Swedish Candy Land": {
        "slug": "swedish-candy-land",
        "lede": "Online-only Swedish candy retailer based in Ulricehamn, Sweden. Ships worldwide. Founded by Daniel Johansson.",
        "posture": "Comp / exclude (Swedish-based)",
        "markets": "Online (Ulricehamn, Sweden) — ships to US",
        "confidence": "Medium",
        "site": "https://www.swedishcandyland.com/",
        "ig": None,
        "founder": [
            "Founded by <strong>Daniel Johansson</strong>.",
            "Based in Ulricehamn, Sweden.",
        ],
        "origin": [
            "Online-only retailer — no physical stores.",
            "Ships worldwide including to US.",
            "Blog and content marketing focused.",
        ],
        "news": [
            "Parade: 'Daniel Johansson, owner of Swedish Candy Land, a Swedish candy shop.'",
            "Barchart: 'Bubs Candy is Now Available with Fast Worldwide Shipping At Swedish Candy Land.'",
        ],
        "social": [
            "Limited social media presence identified.",
            "Content/blog marketing approach.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Ecommerce-only, worldwide shipping.",
            "Bubs candy availability promoted.",
        ],
        "openings": [
            "No physical locations — online only.",
        ],
        "diligence": "Swedish-based ecommerce shipping to US. Not a US retail acquisition target. Could be a supplier relationship. Key question: import/duty fees and fulfillment reliability.",
    },
    "To The Moon": {
        "slug": "to-the-moon",
        "lede": "Candy shop in Wilton Manors/Fort Lauderdale, FL. Carries Swedish candy alongside other types. Named after The Honeymooners. Not Swedish-only.",
        "posture": "Comp / exclude (not Swedish-pure)",
        "markets": "Wilton Manors/Fort Lauderdale, FL",
        "confidence": "Medium",
        "site": None,
        "ig": None,
        "founder": [
            "Owner 'Dan' referenced in Instagram content.",
            "Named after The Honeymooners TV show.",
        ],
        "origin": [
            "2205 Wilton Dr, Fort Lauderdale, FL (Wilton Manors area).",
            "General candy retailer — Swedish candy + Dubai chocolate bars + other candy.",
            "287 Yelp reviews suggest good traffic.",
        ],
        "news": [
            "Yelp: 287 reviews — listed among top Swedish candy near Hallandale Beach.",
            "TikTok: 'Explore the best Swedish candy and Dubai chocolate bar at To The Moon.'",
        ],
        "social": [
            "Some social media presence.",
            "TikTok coverage from South Florida creators.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "General candy retailer — Swedish candy is one category.",
            "287 Yelp reviews.",
        ],
        "openings": [
            "Current: 2205 Wilton Dr, Fort Lauderdale, FL.",
        ],
        "diligence": "General candy retailer, not a Swedish candy concept. Included for geographic comp in the Fort Lauderdale market where Go Yummy also operates.",
    },
    "Trolley Car Sweets & Treats": {
        "slug": "trolley-car-sweets-and-treats",
        "lede": "Scandinavian candy shop in Richmond, VA (Fan District, Strawberry Street). New entrant. Taking over former Idle Hands space.",
        "posture": "Comp",
        "markets": "Richmond, VA (Fan District)",
        "confidence": "Low-Medium",
        "site": None,
        "ig": None,
        "founder": [
            "Founder identity not surfaced in public sources reviewed.",
        ],
        "origin": [
            "407 Strawberry St, Richmond, VA (Fan District).",
            "Taking over former Idle Hands space.",
            "Scandinavian candy concept.",
        ],
        "news": [
            "Richmond Times-Dispatch: 'New candy shop headed to the Fan District.'",
            "Instagram: 'a Scandinavian candy shop... could open on Strawberry Street.'",
        ],
        "social": [
            "Instagram: @trolleycarsweetsandtreats — limited public presence.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Single location, newly opened.",
        ],
        "openings": [
            "Current: 407 Strawberry St, Richmond, VA.",
        ],
        "diligence": "First-mover in Richmond. Very little public information. Key question: is Richmond a viable Swedish candy market?",
    },
    "Yummi Joy": {
        "slug": "yummi-joy",
        "lede": "Austin candy store — spinoff of Toy Joy. Owned by Dorshelle Meyer. Carries Swedish candy alongside other types. Not Swedish-only.",
        "posture": "Comp / exclude (not Swedish-pure)",
        "markets": "Austin, TX (N Lamar Blvd)",
        "confidence": "Medium",
        "site": None,
        "ig": None,
        "founder": [
            "Owned by <strong>Dorshelle Meyer</strong> (also runs Toy Joy and Akiba Texas).",
            "Part of Austin Toy Joy ecosystem.",
        ],
        "origin": [
            "Spinoff of Toy Joy — iconic Austin toy store.",
            "N Lamar Blvd, Austin, TX.",
            "Carries Swedish candy, European candy, vegan ice cream (Sweet Ritual), housemade fudge, truffles.",
        ],
        "news": [
            "LinkedIn: Dorshelle Meyer — 'A spin off of our popular Toy Joy brand, Yummi Joy keeps AUSTIN sweet!'",
            "Yelp: 4.3 stars, 83 reviews.",
            "TikTok: Winnie Harlow coverage — 'Part 2 to Toy Joy — come with me to Yummi Joy! Swedish candy...'",
        ],
        "social": [
            "Instagram: connected to Toy Joy ecosystem.",
            "TikTok: creator coverage including Winnie Harlow.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Part of established Toy Joy retail ecosystem.",
            "Multiple revenue streams: candy, ice cream, fudge, truffles, espresso.",
        ],
        "openings": [
            "Current: N Lamar Blvd, Austin, TX.",
        ],
        "diligence": "Part of established Austin retailer ecosystem. Swedish candy is one product line. Key comp for understanding how existing candy retailers incorporate Swedish candy vs. dedicated concepts.",
    },
    "Hej Hej": {
        "slug": "hej-hej",
        "lede": "Swedish hot dog and candy pop-up in San Francisco (Cortland Ave). Founded by Steven B. Expanded from hot dogs to Swedish candy.",
        "posture": "Comp / format alternative",
        "markets": "San Francisco, CA (Cortland Ave)",
        "confidence": "Medium",
        "site": None,
        "ig": None,
        "founder": [
            "Founded by <strong>Steven B.</strong> — also runs Swedish hot dog pop-up.",
            "LinkedIn: Amelia Eudailey connected to 'Chef Hej Hej' (Jan 2026-Present).",
        ],
        "origin": [
            "Started as Swedish hot dog pop-up in SF.",
            "Expanded to candy store on Cortland Ave.",
            "'SF's cult Swedish hot dog pop-up is now a candy store.'",
        ],
        "news": [
            "SF Standard: feature coverage.",
            "Hoodline: 'Hej Hej, SF's cult Swedish hot dog pop-up, is now a candy store on Cortland Ave.'",
            "Instagram: 'Time to find a permanent home for Hej Hej!'",
        ],
        "social": [
            "Instagram: active with hot dog + candy content.",
            "TikTok: 'When I tell you a Swedish hot dog will change your life.'",
            "The Poor Traveler podcast: discount code for Hej Hej merch/candy.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Dual-concept: Swedish hot dogs + candy.",
            "Pop-up model transitioning to permanent location.",
        ],
        "openings": [
            "Current: Cortland Ave, San Francisco, CA.",
            "Searching for permanent location per Instagram.",
        ],
        "diligence": "Dual-concept (hot dogs + candy) is unique. Key question: is candy supplement to food or standalone business? Different value proposition.",
    },
    "Lilla Swedish Candy": {
        "slug": "lilla-swedish-candy",
        "lede": "Husband-and-wife team Nic Jansson and Holly Berrigan from Whately, MA. Founded online 2025. Opening in Thornes Marketplace, Northampton, MA July 2026.",
        "posture": "Comp / early-stage comp",
        "markets": "Northampton, MA (Thornes Marketplace, opening July 2026)",
        "confidence": "Medium",
        "site": "https://lillacandy.co",
        "ig": None,
        "founder": [
            "Founded by husband-and-wife team <strong>Nic Jansson</strong> and <strong>Holly Berrigan</strong>.",
            "Whately, MA residents.",
            "Third business enterprise — experienced operators.",
        ],
        "origin": [
            "Founded 2025 online at lillacandy.co.",
            "TikTok: @lillacandy.",
            "Opening brick-and-mortar in Thornes Marketplace, Northampton, MA.",
        ],
        "news": [
            "MassLive: 'Thornes Marketplace lands Lilla Swedish Candy shop.'",
            "WWLP: 'Whately couple to bring Scandinavian sweets to Northampton.'",
            "Opening expected July 2026.",
        ],
        "social": [
            "TikTok: @lillacandy — online presence.",
            "Instagram: building audience.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Online-first, transitioning to brick-and-mortar.",
            "Thornes Marketplace = established indie retail destination.",
        ],
        "openings": [
            "Coming July 2026: Thornes Marketplace, Lower Level 1, Northampton, MA.",
        ],
        "diligence": "Online-to-brick-and-mortar pipeline. Thornes Marketplace is well-known indie retail destination. Experienced operators (third business). Key comp for small-market New England viability.",
    },
    "Millie's Swedish Candy": {
        "slug": "millie-s-swedish-candy",
        "lede": "Swedish candy company opening in College Park, Orlando, FL (June 13, 2026). Previously operated as pop-up at holiday events.",
        "posture": "Comp",
        "markets": "Orlando, FL (College Park)",
        "confidence": "Low-Medium",
        "site": None,
        "ig": None,
        "founder": [
            "Founder identity not surfaced in public sources reviewed.",
        ],
        "origin": [
            "Previously operated as pop-up (Dora Mae Jewelry during Jingle Eve).",
            "Opening brick-and-mortar at 2529 Edgewater Dr, Orlando, FL.",
            "Opening June 13, 2026.",
        ],
        "news": [
            "Instagram: 'Millie's Swedish Candy Company opens this Saturday, June 13th.'",
            "Bungalower: 'Millie's Swedish Candy Pops Up at Dora Mae Jewelry During Jingle Eve.'",
        ],
        "social": [
            "Instagram: limited public presence.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Pop-up to brick-and-mortar pipeline.",
        ],
        "openings": [
            "Current: 2529 Edgewater Dr, Orlando, FL (opening June 13, 2026).",
        ],
        "diligence": "Pop-up-to-store model in Orlando. Very little public information. Key question: founder background and Orlando market viability.",
    },
    "Sukker Baby": {
        "slug": "sukker-baby",
        "lede": "Scandinavian candy brand. Retail presence at The Edit in Toronto. Ecommerce + retail. Canadian-based.",
        "posture": "Comp / exclude (Canadian-based)",
        "markets": "Toronto, Canada + online",
        "confidence": "Low",
        "site": None,
        "ig": "https://www.instagram.com/sukkerbaby.to/",
        "founder": [
            "Founder identity not surfaced in public sources reviewed.",
        ],
        "origin": [
            "Canadian operation — Toronto-based.",
            "Serious Eats referenced alongside Sockerbit as 'Scandinavian, not just Swedish.'",
            "Retail at The Edit in Toronto.",
        ],
        "news": [
            "Serious Eats: mentioned in Swedish candy trend article.",
            "Eater: 'Sockerbit and Sukker Baby describe themselves as Scandinavian, not just Swedish.'",
        ],
        "social": [
            "Instagram: @sukkerbaby.to — Toronto-based.",
        ],
        "revenue": [
            "Not publicly disclosed.",
            "Canadian operation — different market dynamics.",
        ],
        "openings": [
            "Current: The Edit, Toronto, Canada.",
        ],
        "diligence": "Canadian operation. Not a US acquisition target. Included as comp for broader North American market. Key question: US expansion plans?",
    },
    "Sötsak": {
        "slug": "sotsak",
        "lede": "Swedish candy store opening in Highland Village, Houston, TX. 'Sötsak' means 'sweet thing' in Swedish. New entrant in Texas market.",
        "posture": "Comp / watch",
        "markets": "Houston, TX (Highland Village, opening soon)",
        "confidence": "Low",
        "site": None,
        "ig": None,
        "founder": [
            "Founder identity not surfaced in public sources reviewed.",
        ],
        "origin": [
            "Opening in Highland Village, Houston, TX.",
            "'Sötsak' = Swedish for 'sweet thing/sweet treat.'",
            "Pre-opening stage.",
        ],
        "news": [
            "Instagram: 'Discover the candy world of SÖTSAK. The Swedish Candy Store.'",
            "Limited pre-opening coverage.",
        ],
        "social": [
            "Instagram: early-stage presence.",
        ],
        "revenue": [
            "Not publicly disclosed — pre-opening.",
        ],
        "openings": [
            "Opening soon: Highland Village, Houston, TX.",
        ],
        "diligence": "Pre-opening. Houston is a large, diverse market with no established Swedish candy presence. Highland Village is premium retail. Key question: who's behind this and go-to-market strategy?",
    },
    "The Pirate Candy Shop": {
        "slug": "the-pirate-candy-shop",
        "lede": "Not surfaced in public sources reviewed. May be a local candy shop with minimal online presence.",
        "posture": "Unknown",
        "markets": "Unknown",
        "confidence": "Low",
        "site": None,
        "ig": None,
        "founder": ["Founder identity not surfaced in public sources reviewed."],
        "origin": ["Not surfaced in public sources reviewed."],
        "news": ["No press coverage found in searches."],
        "social": ["No public social media presence identified."],
        "revenue": ["Not available."],
        "openings": ["No verified location information."],
        "diligence": "Could not find public information on this brand. May need direct research or removal from the universe if unverified.",
    },
    "Karameller": {
        "slug": "karameller",
        "lede": "Not surfaced in public sources reviewed. May be a local candy shop with minimal online presence.",
        "posture": "Unknown",
        "markets": "Unknown",
        "confidence": "Low",
        "site": None,
        "ig": None,
        "founder": ["Founder identity not surfaced in public sources reviewed."],
        "origin": ["Not surfaced in public sources reviewed."],
        "news": ["No press coverage found in searches."],
        "social": ["No public social media presence identified."],
        "revenue": ["Not available."],
        "openings": ["No verified location information."],
        "diligence": "Could not find public information on this brand. May need direct research or removal from the universe if unverified.",
    },
    "Coney's Candies": {
        "slug": "coney-s-candies",
        "lede": "Opening-announced Waconia, Minnesota candy shop combining Swedish candy, dirty soda, ice cream, and cotton candy. Not Swedish-pure, but relevant as a new small-market Swedish-candy-forward entrant.",
        "posture": "Watch / local opening proof",
        "markets": "Waconia, MN",
        "confidence": "Medium",
        "site": "https://coneyscandies.com/",
        "ig": "https://www.instagram.com/coneyscandies/",
        "founder": [
            "MSP Business Journal reports <strong>Crystal Jensen</strong> is opening Coney's Candies.",
            "Founder/owner background beyond the opening coverage was not deeply surfaced in this sweep.",
        ],
        "origin": [
            "Official site says Coney's is opening in Waconia in summer 2026.",
            "Concept mixes Swedish candy with dirty soda, ice cream, and the founder's cotton candy brand.",
            "The shop is positioned as an old-fashioned Main Street candy/soda-shop format rather than a pure Swedish candy store.",
        ],
        "news": [
            "MSP Business Journal reported the shop is opening at 136 Main St W in Waconia in July 2026.",
            "Official site says 'Opening in Waconia Summer 2026' and highlights Swedish candy, dirty soda, and ice cream.",
        ],
        "social": [
            "Instagram: @coneyscandies; public snippet shows opening-summer-2026 positioning.",
            "Exact follower count should be treated as drifting and was not used as a hard diligence fact.",
        ],
        "revenue": [
            "No revenue data surfaced.",
            "Revenue model is likely multi-category: Swedish candy + ice cream + dirty soda + cotton candy.",
            "Useful as a small-market, broader-sweets comp rather than a pure Swedish-candy acquisition target.",
        ],
        "openings": [
            "Opening announced: 136 Main St W, Waconia, MN; summer / July 2026.",
        ],
        "diligence": "Keep as a map/universe comp, not a target. The signal is geographic diffusion into Minnesota small-market Main Street retail and a broader sweets model that may be more durable than Swedish-only.",
    },
    "Swedish Crave": {
        "slug": "swedish-crave",
        "lede": "Swedish candy review/affiliate site (swedishcrave.com) that publishes detailed store reviews. Not a candy retailer.",
        "posture": "Exclude (media/content site)",
        "markets": "Online",
        "confidence": "Medium",
        "site": "https://www.swedishcrave.com/",
        "ig": None,
        "founder": ["Not a retail operation — content/review site."],
        "origin": ["Publishes detailed reviews of Swedish candy stores across the US."],
        "news": ["Comprehensive store review series covering BonBon, ScandyCandy, Sweetish, CandyKing, Goodis, and others."],
        "social": ["Website-based content."],
        "revenue": ["Not a retail operation — likely affiliate/ad revenue model."],
        "openings": ["No physical locations."],
        "diligence": "Not a retail operation. Content/review site. Should be excluded from retail comp analysis but is a valuable intelligence source on the competitive landscape.",
    },
}


def esc(s):
    return html_mod.escape(str(s), quote=False)


def make_link(label, url):
    return f'<a href="{url}" target="_blank" rel="noopener">{esc(label)}</a>'


def gm(query):
    return f"https://www.google.com/maps/search/?api=1&query={urlquote(query, safe='')}"


def make_panel(title, items):
    lis = "".join(f"<li>{item}</li>" for item in items)
    return f'<div class="panel"><h3>{esc(title)}</h3><ul>{lis}</ul></div>'


def make_unit_table(units):
    rows_html = ""
    for u in units:
        loc = esc(u.get("location", ""))
        addr = esc(u.get("address", ""))
        rows_html += f"<tr><td>{loc}</td><td>{addr}</td></tr>"
    return (
        f'<table><thead><tr><th>Location</th><th>Address</th></tr></thead>'
        f"<tbody>{rows_html}</tbody></table>"
    )


def load_units():
    map_path = os.path.join(BASE_DIR, "swedish-candy-map.html")
    with open(map_path) as f:
        html = f.read()
    m = re.search(r"const TABLE_ROWS = (\[.*?\]);", html, re.DOTALL)
    if not m:
        raise ValueError("Could not find TABLE_ROWS in map")
    rows = json.loads(m.group(1))
    by_brand = defaultdict(list)
    for r in rows:
        by_brand[r["brand"]].append(r)
    return by_brand


def main():
    by_brand = load_units()

    sections = [
        ("founder", "Founder / Ownership"),
        ("origin", "Origin / Background"),
        ("news", "News / Buzz"),
        ("social", "Social Accounts / Followers"),
        ("revenue", "Revenue / Scale Signals"),
        ("openings", "Openings / Pipeline"),
    ]

    generated = 0
    skipped = []

    for brand_name, data in BRANDS.items():
        slug = data["slug"]
        units_raw = by_brand.get(brand_name, [])
        if not units_raw:
            # Try partial match
            for bk in by_brand:
                if bk.lower() == brand_name.lower():
                    units_raw = by_brand[bk]
                    break

        units = [
            {"location": u.get("location", ""), "address": u.get("address", "")}
            for u in units_raw
        ]

        row_count = len(units)

        # Build links
        links_parts = []
        if data.get("site"):
            links_parts.append(make_link("Site", data["site"]))
        if data.get("ig"):
            links_parts.append(make_link("IG", data["ig"]))
        for u in units:
            addr = u.get("address", "")
            if addr:
                links_parts.append(make_link(u.get("location", "Map"), gm(f"{addr} {brand_name}")))
        links_html = "".join(links_parts)

        # Build panels
        panels = []
        for key, title in sections:
            items = data.get(key, [])
            if items:
                panels.append(make_panel(title, items))

        panels_html = "".join(panels)

        # Unit table
        unit_html = make_unit_table(units) if units else "<p>No mapped units.</p>"

        # Diligence note
        diligence = data.get("diligence", "")

        page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(brand_name)} | Swedish Candy Comp</title><meta name="description" content="Structured Swedish candy comp profile for {esc(brand_name)}."><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet"><style>
:root{{--paper:#f4ead8;--paper2:#eadcc4;--ink:#252018;--muted:#766b5e;--line:rgba(62,49,32,.16);--blue:#315e72;--clay:#b86f4d;--sage:#6f80662;--gold:#b78b38;--card:rgba(255,251,241,.76)}}
*{{box-sizing:border-box}}body{{margin:0;color:var(--ink);font-family:"Space Grotesk",ui-sans-serif,system-ui,sans-serif;line-height:1.5;background:linear-gradient(180deg,var(--paper),var(--paper2));min-height:100dvh}}.shell{{max-width:1180px;margin:auto;padding:26px 24px 72px}}nav{{display:flex;justify-content:space-between;gap:16px;align-items:center;margin:0 0 36px;padding:10px;border:1px solid var(--line);border-radius:999px;background:rgba(255,251,241,.72)}}nav a{{color:var(--ink);text-decoration:none;font-size:13px;padding:8px 11px;border-radius:999px}}h1{{font-family:"Fraunces",Georgia,serif;font-size:clamp(2.4rem,5vw,4.6rem);line-height:.96;margin:12px 0 14px}}h2{{font-family:"Fraunces",Georgia,serif;font-size:1.8rem;line-height:1;margin:34px 0 12px}}h3{{margin:0 0 8px;font-size:1rem}}.kicker{{display:inline-flex;border:1px solid rgba(49,94,114,.18);background:rgba(255,251,241,.66);border-radius:999px;padding:8px 12px;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--blue);font-weight:700}}.lede{{max-width:880px;color:var(--muted);font-size:1.12rem}}.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:24px 0}}.card,.panel{{border:1px solid var(--line);border-radius:16px;background:var(--card);padding:16px}}.card b{{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:var(--blue);margin-bottom:6px}}.card strong{{font-size:1.16rem}}.sections{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:18px}}.panel ul{{margin:0;padding-left:18px}}.panel li{{margin:0 0 7px}}.note{{border-left:4px solid var(--clay);padding:15px 18px;background:rgba(184,111,77,.09);border-radius:14px;color:var(--muted)}}table{{width:100%;border-collapse:collapse;background:rgba(255,251,241,.45);border:1px solid var(--line);border-radius:16px;overflow:hidden}}th,td{{padding:11px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;font-size:13px}}th{{font-size:10px;text-transform:uppercase;letter-spacing:.14em;color:var(--blue);background:rgba(255,251,241,.6)}}td:first-child{{font-weight:600}}tr:last-child td{{border-bottom:none}}.links{{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0}}.links a{{display:inline-block;padding:6px 14px;border:1px solid var(--line);border-radius:999px;font-size:12px;color:var(--blue);text-decoration:none;background:rgba(255,251,241,.6)}}.links a:hover{{background:rgba(49,94,114,.08)}}
</style></head><body><main class="shell"><nav><b>Dan's Business Path</b><div><a href="../swedish-candy-map.html">Swedish Candy Map</a><a href="../emerging-multi-unit-pipeline.html">Pipeline</a></div></nav><span class="kicker">Swedish candy comp profile</span><h1>{esc(brand_name)}</h1><p class="lede">{esc(data["lede"])}</p><div class="grid"><div class="card"><b>Posture</b><strong>{esc(data["posture"])}</strong></div><div class="card"><b>Rows</b><strong>{row_count}</strong></div><div class="card"><b>Markets</b><strong>{esc(data["markets"])}</strong></div><div class="card"><b>Confidence</b><strong>{esc(data["confidence"])}</strong></div></div><div class="links">{links_html}</div><section class="sections">{panels_html}</section><h2>Mapped Unit Records</h2>{unit_html}"""

        if diligence:
            page += f'<div class="note" style="margin-top:24px">{esc(diligence)}</div>'

        page += "</main></body></html>"

        out_path = os.path.join(OUT_DIR, f"{slug}.html")
        with open(out_path, "w") as f:
            f.write(page)
        generated += 1
        print(f"  ✓ {brand_name} ({row_count} units)")

    print(f"\nGenerated {generated} comp profile pages.")
    if skipped:
        print(f"Skipped: {skipped}")


if __name__ == "__main__":
    main()
