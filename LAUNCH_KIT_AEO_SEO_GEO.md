# IncuBrix AEO, SEO & GEO 90-Day Visibility Launch Kit
**Document Version**: 1.0 (Production Release)  
**Target Launch Date**: Monday, November 23, 2026  
**Author / Lead**: Growth Engineering (Search & AI Answer Optimization)  
**Scope**: 90-Day Master Roadmap to Win Google Search, Answer Boxes (AEO), and Generative AI Assistants (GEO)  

---

## Executive Summary
This Launch Kit provides IncuBrix with an actionable, week-by-week 90-day execution roadmap to transform `incubrix.com` from unranked and uncited into the dominant brand that Google ranks, Answer Boxes quote, and AI assistants (ChatGPT, Gemini, Perplexity, Claude, Copilot) recommend when creators search for content repurposing solutions.

---

## 1. Core Visibility Goals & 90-Day Key Targets

| Metric | Baseline (Day 0) | Month 1 Target | Month 2 Target | Month 3 Target (Day 90) |
| :--- | :---: | :---: | :---: | :---: |
| **Google Top 10 Keyword Rankings** | 2 queries | 25 queries | 60 queries | **120+ queries** |
| **Featured Snippets & PAA Won** | 0 answer boxes | 6 answer boxes | 14 answer boxes | **25+ answer boxes** |
| **AI Assistant Mention Share (GEO)** | 0.0% | 15.0% | 28.0% | **45.0%+** |
| **Perplexity Direct Citation Inflow** | 0 referrals | 250 visits/mo | 750 visits/mo | **2,200 visits/mo** |
| **Monthly Organic Creator Sign-ups** | ~15 / mo | 120 / mo | 380 / mo | **850+ / mo** |

---

## 2. Technical Audit & Prioritized Implementation (Weeks 1–4)

### Week 1: Foundational Crawling & AI Gateway Fixes
- **Deploy `robots.txt` Permissions**: Add explicit `Allow: /` rules for `GPTBot`, `PerplexityBot`, `ClaudeBot`, and `Google-Extended`.
- **Deploy `/llms.txt`**: Standardized markdown specification defining IncuBrix core tools, pricing, and API capabilities for LLM crawlers.
- **Canonical & Redirect Hardening**: Eliminate 301 chained hops; enforce single canonical HTTPS non-www root.
- **Sitemap Refresh**: Submit XML Sitemap Index with updated `lastmod` timestamps to Google Search Console and Bing Webmaster Tools.

### Week 2: Structured Data (Schema.org) Deployment
- **`SoftwareApplication` Schema**: Inject complete JSON-LD on homepage with ratings (4.9/5), pricing ranges ($0-$199), and feature specifications.
- **`FAQPage` Schema**: Implement on `/pricing` and `/faq` addressing commercial licensing, free minutes, and refund terms.
- **`HowTo` Schema**: Implement on `/features/repurpose` detailing the 4-step video-to-shorts pipeline.
- **`Organization` Schema**: Establish Knowledge Graph linkages with `sameAs` attributes to Crunchbase, LinkedIn, and YouTube.

### Week 3: Core Web Vitals & Mobile Optimization
- **LCP Hero Compression**: Convert 2.4MB PNG hero images to responsive `.avif` and `.webp` with `fetchpriority="high"`, reducing mobile LCP from 3.8s to <1.2s.
- **Font Display Fix**: Add `font-display: swap` and preconnect links to eliminate Flash of Invisible Text (FOIT).
- **Mobile Tap Target Spacing**: Expand navigation buttons to minimum 48px touch bounding boxes.
- **Security Headers**: Configure HSTS, X-Content-Type-Options, and Content-Security-Policy on Cloudflare edge rules.

### Week 4: Internal Link Topology & Semantic Architecture
- **Orphan Page Elimination**: Connect `/features/scheduler` and feature sub-pages to site-wide navigation and footer.
- **Breadcrumb Hierarchy**: Add dynamic `BreadcrumbList` schema across all tutorial and educational guides.
- **Answer Target Styling**: Refactor introductory paragraphs on feature pages to answer primary questions directly within the first 60 words.

---

## 3. Content Publishing Calendar (Weeks 5–10)

| Week | Content Deliverable | Target Queries | Schema Deployed | Primary Distribution |
| :---: | :--- | :--- | :--- | :--- |
| **Week 5** | *P01: How to Repurpose YouTube Video to Shorts, Reels & TikTok* | Q001, Q004, Q012 | `HowTo` + VideoObject | Organic Search, Reddit /r/NewTubers |
| **Week 6** | *P02: Best AI Video Clipping Tools 2027: Descript vs Opus vs IncuBrix* | Q002, Q015, Q028 | `Table` + Product | Product Hunt, Medium, LinkedIn |
| **Week 7** | *P03: Turn a 60-Min Podcast into a Week of Content* | Q003, Q008, Q022 | `HowTo` + AudioObject | Podnews, Reddit /r/podcasting |
| **Week 8** | *P04: The Ultimate Guide to Kinetic Captions & Safe Zones* | Q005, Q018, Q035 | `TechArticle` | YouTube Shorts Community, TikTok |
| **Week 9** | *P06: Converting Video Interviews into LinkedIn Carousels* | Q009, Q031, Q055 | `HowTo` + Carousel | LinkedIn Articles, B2B Founders Club |
| **Week 10**| *P10: Comprehensive CreatorOps FAQ Hub (25 Q&As)* | Q020, Q065, Q099 | `FAQPage` | Google PAA Infiltration |

---

## 4. Citation Infiltration & Digital PR Execution (Weeks 7–12)

### High-Priority Citation Targets
1. **SaaS Directories & Category Grids (Weeks 7–8)**:
   - Claim vendor profiles on G2, Capterra, and Trustpilot.
   - Run an automated review collection campaign offering 100 free export minutes to active users who leave an honest G2 review (Target: 30 verified reviews).
2. **AI Tool Directories (Weeks 8–9)**:
   - Submit IncuBrix to Futurepedia, FutureTools, Ben's Bites, and The Rundown AI directory.
   - Provide direct tool descriptions citing unique multitrack audio capabilities.
3. **Editorial Roundups & Digital PR (Weeks 10–12)**:
   - Pitch Zapier, Buffer, and HubSpot blog editors to add IncuBrix to existing high-ranking articles (e.g. "Best AI Video Generators").
   - Offer updated 2027 benchmark data and custom infographics in exchange for attribution.

---

## 5. Tool Stack & Monthly Operating Budget

### Lean Audit Stack ($0/Month)
- **Technical Crawler**: Google Search Console + Screaming Frog SEO Spider (free tier 500 URLs) — **$0.00**
- **Structured Data Testing**: Google Rich Results Test & Schema.org Validator — **$0.00**
- **Performance Audit**: Google PageSpeed Insights & Chrome DevTools Lighthouse — **$0.00**
- **Automated Tracker Engine**: In-house Python visibility runner (`run_visibility_tracker.py`) — **$0.00**
- **Total Lean Budget**: **$0.00 / month**

### Production Scaling Stack ($99/Month)
- **Ahrefs Webmaster Tools**: Backlink and ranking tracker — **$0.00 (Free for verified owners)**
- **Cloudflare Pro Plan**: Edge image optimization (Polish/Mirage WebP conversion) & security headers — **$25.00 / mo**
- **Review Incentive Credits**: Free IncuBrix credits distributed to reviewers — **$0.00 (Zero marginal software cost)**
- **Content Distribution / Seed Ads**: Targeted boosts on top converting guides — **$74.00 / mo**
- **Total Production Budget**: **$99.00 / month**

---

## 6. RACI Team Ownership Matrix

| Activity | Growth Engineer | Full-Stack Dev | Content / Copywriter | Founder / CEO |
| :--- | :---: | :---: | :---: | :---: |
| **Robots.txt, llms.txt & Edge Redirects** | **A / R** | C | I | I |
| **JSON-LD Schema Deployment** | **A / R** | C | I | I |
| **Image Compression & Core Web Vitals** | C | **A / R** | I | I |
| **Writing 10 Publish-Ready Guides** | C | I | **A / R** | I |
| **Running Weekly Visibility Tracker** | **A / R** | I | I | I |
| **Citation Pitching & Directory Submission**| **A / R** | I | C | I |
| **Monthly Executive AEO/GEO Review** | **R** | I | I | **A** |

---

## 7. Risk Management & Algorithmic Volatility Protocol

1. **AI Model Hallucinations**: Monitor weekly raw answers in `visibility/raw_answers/`. If an LLM misstates pricing or features, submit correction feedback via model web interfaces and reinforce entity schema.
2. **Google Core Algorithm Updates**: Adhere strictly to Google's Helpful Content Guidelines. Avoid AI-spun filler; all 10 pages feature verified step-by-step methodologies and original benchmarking tables.
3. **Citation Decay**: Refresh third-party outreach quarterly to maintain fresh co-occurrence signals across LLM training checkpoints.
