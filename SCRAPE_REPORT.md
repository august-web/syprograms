# SYPrograms.org — Complete Scrape Report

> **Source**: https://syprograms.org/  
> **Scraped**: September 19, 2026  
> **Site builder**: mywebsitebuilder.com (template platform)  
> **Purpose**: Reference data for building an improved version of the site.

---

## 1. Site Overview

**Organization**: Southside Youth Programs (SYP)  
**Tagline / Mission**: After-school enrichment and youth development programs for the south side of Houston, TX.  
**Pages**: 5 (home, gallery, location, contact-us, blog)  
**CMS**: mywebsitebuilder.com (proprietary builder; HTML is ~200 KB per page of framework/script bloat)

---

## 2. Navigation (consistent across all pages)

| Label | URL |
|---|---|
| SYPrograms.org (logo / home) | `/` |
| Home | `/` |
| Gallery | `/gallery` |
| Location | `/location` |
| Contact us | `/contact-us` |
| Blog | `/blog` |
| Call (phone button) | `tel:281-536-8292` |

**Footer**: Sitemap link + "Follow us" label (no actual social media URLs found).

---

## 3. Color Palette & Typography

### Primary colors (extracted from CSS custom properties)
| Token | RGB | Hex | Usage |
|---|---|---|---|
| `--accent1` | `rgb(26, 72, 147)` | `#1A4893` | Primary brand blue |
| `--accent2` | `rgb(41, 180, 207)` | `#29B4CF` | Secondary cyan/teal |
| `--accent3` | `rgb(255, 255, 255)` | `#FFFFFF` | White surfaces |
| `--accent4` | `rgb(0, 0, 0)` | `#000000` | Black |
| `--background` | `rgb(33, 33, 33)` | `#212121` | Dark background |
| `--card` | `rgb(255, 255, 255)` | `#FFFFFF` | Card surface |
| `--text2-bg` | `rgb(104, 205, 225)` | `#68CDE1` | Light cyan |

**Dominant visual identity**: Navy blue (#1A4893) + cyan (#29B4CF) on dark backgrounds. Strong cyan accent in hero/cover sections.

### Fonts
- **Headings**: `Old Standard TT` (serif)
- **Body / UI**: `Rubik` (sans-serif)
- Icons: `FontAwesome` + `Material Icons`
- Google Fonts: `Old+Standard+TT:400,700|Rubik:400,700`

---

## 4. Page-by-Page Content

### 4.1 Home (`/`)

**Hero / Cover**
- Title: **"Welcome to SYPrograms.org"**
- Subtitle: *"Learn more about what we do"*
- CTA: `Read more` → links to `/contact-us`
- Hero background: stock photo of cheering teen at concert (Unsplash)

**Info Section** (below hero)
> Southside Youth Programs After-school 2025-26 starts **August 19th, 2025** on Monday through Thursday **4:00 PM - 6:00 PM**  
> For more information, contact Lynn at **281-536-8292**

---

### 4.2 Gallery (`/gallery`)

**Page header**
- Title: **"Gallery"**
- Subtitle: *"Our latest and best photos"*
- Description: *"We love to take pictures and show them to the world."*

**8 photo cards** (clockwise / alphabetical as labeled on site):

| # | Caption | File | Description |
|---|---|---|---|
| 1 | **Nameless Sound** | `gallery_33e8d626628d.jpg` | Girl playing a djembe-style hand drum |
| 2 | **Baylor SYP IMCO** | `gallery_90aa9663f831.jpg` | Group music class — keyboard, congas, xylophone, drum circle |
| 3 | **The Village People** | `gallery_26b945193908.jpg` | Big group photo in green-walled SYP center, kids holding stuffed animal |
| 4 | **Music Class** | `gallery_f2703c217b62.jpg` | Two girls playing an electronic keyboard together |
| 5 | **Learning Keyboard** | `gallery_6c094b50d13f.jpg` | Young man at keyboard with djembe + marimba in background |
| 6 | **Creativity** | `gallery_4c10f3564d08.jpg` *(also* `gallery_eee66a143f21.jpg`*)* | Smiling girl with magnetic tile construction on a colorful circular rug |
| 7 | **Pride** | `gallery_70cacef9c5c9.jpg` | Stock photo of diverse hands joined in a team huddle |
| 8 | **Culinay** | `gallery_fa027985888c.jpg` | Young person in white chef's hat + apron, "Nourishing Life" green shirt |

**Note**: At least two photos (`gallery_4c10f...` and `gallery_eee66a...`) appear to be the same subject shot twice, one rotated 90°. On the live site they are shown sideways — a clear UX bug to fix.

---

### 4.3 Location (`/location`)

**Address block**
- Address: **7210 Peerless St. suite B, Houston, TX, US**
- Phone: **[281-536-8292](tel:281-536-8292)**
- Email: **[southside917@aol.com](mailto:southside917@aol.com)**

**Featured program callout**: *Baylor College of Medicine — IMCO 2025-26*

> SYP and Baylor College of Medicine present **Inner-city Medical Career Opportunity 2025-26** sessions to begin **Saturday October 3, 2025, 9:00 AM** at Southside Youth Programs located at 7210 Peerless Street. This year's IMCO consist of 10 sessions the 1st Saturday in each month.  
>   
> This program introduces and encourages careers in medicine and health sciences. Medical lessons are taught by Physicians and residents from Baylor College of Medicine and included hands on and interactive labs. To sign up used the link below. Enrollment is limited so sign up today.  
>   
> For more information please contact **Oliver at 832-520-5031** or send an email to **oraysteven@gmail.com**.

**Sign-up form**: [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSeNA1TSsuKnWI9pUnRZrzAxtQZLDCa-uau0RCefvh8AmYQLhg/viewform?usp=dialog)

---

### 4.4 Contact Us (`/contact-us`)

**Page header**
- Title: **"Contact Southside Youth Programs"**
- Subtitle: *"Write something in this area."* (placeholder — never updated)

**Contact form fields** (8 fields, submission handled by site builder):
1. First name
2. Last name
3. Your email
4. Email subject
5. Your phone
6. Date field
7. Your address
8. Your message
- Consent checkbox: *"By checking this box and submitting your information, you are granting us permission to email you. You may unsubscribe at any time."*
- Submit button: **Send Message**

**Success state**: "Message Sent! Your message has been sent successfully, I hope to respond within 24 hours. You can also contact us through social media, links can be found below!"  
*(Note: no social media links are actually present — dead reference.)*

---

### 4.5 Blog (`/blog`)

**3 placeholder posts** — all titled **"Demo blog post"**, dated **1 Jan 2019**, excerpt *"This is a short demo introduction."* Each "Read more" links back to `/blog`. No actual blog content has been published.

---

## 5. Key Contact & Staff

| Role | Name | Phone | Email |
|---|---|---|---|
| Main / general | Lynn | 281-536-8292 | southside917@aol.com |
| IMCO (Baylor medical program) | Oliver | 832-520-5031 | oraysteven@gmail.com |

---

## 6. Programs Offered (deduced from site content)

1. **After-school program** — Mon–Thu, 4:00–6:00 PM (2025-26 session starts Aug 19, 2025)
2. **IMCO — Inner-city Medical Career Opportunity** (partner: Baylor College of Medicine) — 10 monthly Saturday sessions for high-schoolers exploring medicine/health careers
3. **Music classes** — keyboard, percussion, marimba (gallery evidence + photos from Nameless Sound collaboration)
4. **Arts / creativity programs** — visible in gallery (magnetic tiles, hands-on learning)
5. **Culinary program** ("Culinay" — youth cooking/healthy-eating initiative)

---

## 7. Local File Inventory

### Scraped HTML (raw)
- `/tmp/syprograms_home.html` — 179 KB
- `/tmp/syprograms_gallery.html` — 211 KB
- `/tmp/syprograms_location.html` — 203 KB
- `/tmp/syprograms_contact.html` — 210 KB
- `/tmp/syprograms_blog.html` — 205 KB

### Scraped assets (this workspace)
```
/Users/augustine/Documents/syprograms/scraped_assets/
├── site_content.json          # Full structured JSON of every page
├── parse_site.py              # The scraper script
└── images/                    # All 14 downloaded images
    ├── hero_youth_programs.jpg          (381 KB)  — Unsplash stock: teen at concert
    ├── contact_woman_programs.jpg       (175 KB)  — Unsplash stock: girl at lake
    ├── blog_img1.jpg                    ( 53 KB)  — Unsplash blog thumbnail
    ├── blog_img2.jpg                    ( 64 KB)  — Unsplash blog thumbnail
    ├── blog_img3.jpg                    ( 70 KB)  — Unsplash blog thumbnail
    ├── gallery_26b945193908.jpg         ( 13 MB)  — "The Village People" group photo
    ├── gallery_33e8d626628d.jpg         (  2 MB)  — Girl playing djembe
    ├── gallery_4c10f3564d08.jpg         (  3 MB)  — Girl with magnetic tiles (rotated)
    ├── gallery_6c094b50d13f.jpg         (  2 MB)  — Young man at keyboard + drums
    ├── gallery_70cacef9c5c9.jpg         (102 KB)  — "Pride" team-huddle stock photo
    ├── gallery_90aa9663f831.jpg         ( 13 MB)  — Baylor SYP IMCO music ensemble
    ├── gallery_eee66a143f21.jpg         ( 15 MB)  — Same girl with tiles (upright)
    ├── gallery_f2703c217b62.jpg         (  2 MB)  — Two girls on keyboard
    └── gallery_fa027985888c.jpg         (  2 MB)  — "Culinay" youth in chef outfit
```

> ⚠️ Gallery originals are huge (2–15 MB each). For a web build, **resize to ≤ 200 KB** with `sharp`/`ImageMagick` before use.

---

## 8. Content Gaps & Improvement Opportunities (for v2)

These are the things a redesign should fix:

1. **Placeholder text everywhere**: "Write something in this area.", `{{localize ...}}` template strings, generic Unsplash hero — makes the site feel unfinished.
2. **Blog has 3 dead demo posts** — either remove the section or build a real one.
3. **No social media links** in the footer or contact page, despite the success message promising them.
4. **No mission statement, history, or "About us" page** — the biggest content gap.
5. **No staff bios, donor info, or volunteer page** — typical nonprofit must-haves missing.
6. **Gallery images shown sideways** — a bug, not intentional.
7. **No event calendar / schedule** for recurring programs.
8. **No donation / "Get involved" CTA** — critical for a nonprofit.
9. **No SEO meta descriptions** (all empty `og:description=""`).
10. **8-field contact form** is overkill — 3-4 fields (name, email, phone, message) is standard.
11. **Program information scattered** — IMCO lives only on /location, after-school info only on home.
12. **Phone number duplicated** as a "Call" button in nav AND in body — fine, but could be a sticky mobile CTA.
13. **Heavy platform CSS** (~200 KB of inline framework) — a custom build would be 5-10× faster.

---

## 9. Source URLs (for reference)

- Sitemap index: `https://syprograms.org/sitemap.xml`
- Sitemap: `https://syprograms.org/sitemap-urlset.xml`
- Robots: `https://syprograms.org/robots.txt` (allows all, points to sitemap)
- Blog (external): `https://blog-viewer-api.mywebsitebuilder.com/...` (separate microservice, has no real posts)

---

*End of scrape report.*