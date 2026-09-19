# Southside Youth Programs — syprograms.org

The official website for **Southside Youth Programs (SYP)**, a community-based
organization serving young people on the south side of Houston, Texas.

After-school care (Mon–Thu, 4–6 PM), the **IMCO** medical careers program run
with Baylor College of Medicine, music classes with Nameless Sound, arts and
creativity, and culinary workshops — all free for neighborhood youth.

## Tech stack

| Tool | Role |
|---|---|
| [Astro 7](https://astro.build) | Static site generator — zero framework JS shipped |
| [Tailwind CSS v4](https://tailwindcss.com) | Styling via the Vite plugin (`@theme` tokens, no config file) |
| [@fontsource](https://fontsource.org) | Self-hosted Old Standard TT (display) + Rubik (body) |
| [@astrojs/sitemap](https://docs.astro.build/en/guides/integrations-guide/sitemap/) | Auto-generated `sitemap-index.xml` |
| sharp (bundled with Astro) | Responsive image variants (WebP + JPG fallback) |

## Project structure

```
├── public/
│   ├── favicon.svg          # SYP chip: gold square, staggered S·Y·P letters
│   ├── og-image.jpg         # 1200×630 social share image
│   └── robots.txt
├── src/
│   ├── assets/              # Optimized photos (largest ≈ 650 KB)
│   │   ├── hero-group.jpg   # Group photo — home + about hero background
│   │   ├── after-school.jpg
│   │   └── gallery/         # 8 gallery photos
│   ├── components/
│   │   ├── Header.astro     # Fixed header, glass-on-scroll, animated mobile menu
│   │   ├── Footer.astro
│   │   ├── PageHeader.astro # Page hero — optional photo background
│   │   └── Logo.astro       # Reusable SYP mark
│   ├── data/
│   │   ├── site.ts          # Contact info, addresses, mailto helpers
│   │   ├── programs.ts      # The five programs
│   │   ├── gallery.ts       # Photo captions + alts
│   │   └── types.ts
│   ├── layouts/
│   │   └── Base.astro       # <head>, SEO, JSON-LD, view transitions, counters
│   ├── pages/               # File-based routes
│   │   ├── index.astro      # Home
│   │   ├── about.astro
│   │   ├── programs.astro   # Includes the IMCO sign-up panel
│   │   ├── gallery.astro    # Masonry grid + keyboard-navigable lightbox
│   │   ├── contact.astro    # mailto: form — no backend, nothing collected
│   │   └── 404.astro
│   └── styles/
│       └── global.css       # Brand tokens, utilities, keyframes
├── SCRAPE_REPORT.md          # Reference audit of the original site
└── scraped_assets/           # site_content.json + scraper script (reference)
```

## Brand

The identity comes from the SYP t-shirt: a gold chip with staggered letters.

| Token | Hex | Used for |
|---|---|---|
| Gold | `#E5C338` | Primary accent — CTAs, links, eyebrows |
| Brick red | `#D63F2E` | The **S** — accent details |
| Teal | `#66BFA3` | The **Y** — accent details |
| Ink navy | `#1E2235` | The **P** — dark surfaces, headings |

Tokens are named `cyan-*` (gold scale) and `navy-*` (ink scale) in
`src/styles/global.css` for historical reasons — the whole palette is remapped
there in one place.

## Commands

| Command | Action |
|---|---|
| `npm install` | Install dependencies |
| `npm run dev` | Local dev server at `localhost:4321` |
| `npm run build` | Production build to `./dist/` (~8 MB) |
| `npm run preview` | Preview the production build locally |

## Notes

- **No backend.** The contact form composes a `mailto:` to
  `southside917@aol.com`; no data is collected or stored.
- **Accessibility:** semantic landmarks, alt text throughout, focus styles,
  reduced-motion support, keyboard-navigable gallery lightbox.
- **IMCO sign-up** links to the official Google Form; questions go to Oliver
  (832-520-5031). General questions go to Lynn (281-536-8292).
- 7210 Peerless St, Suite B, Houston, TX 77021
