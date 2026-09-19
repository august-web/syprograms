#!/usr/bin/env python3
"""Comprehensive scraper for syprograms.org - extracts all content from downloaded HTML files."""
import re
import json
import urllib.parse
from pathlib import Path
from html.parser import HTMLParser

PAGES = {
    "home": "/tmp/syprograms_home.html",
    "gallery": "/tmp/syprograms_gallery.html",
    "location": "/tmp/syprograms_location.html",
    "contact": "/tmp/syprograms_contact.html",
    "blog": "/tmp/syprograms_blog.html",
}

class ContentExtractor(HTMLParser):
    """Extract structured text content from HTML."""
    def __init__(self):
        super().__init__()
        self.result = []
        self.current_tag = None
        self.current_text = ""
        self.in_script = False
        self.in_style = False
        self.skip_tags = {"script", "style", "noscript"}

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag in self.skip_tags:
            if tag == "script":
                self.in_script = True
            elif tag == "style":
                self.in_style = True
            return

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "a", "span", "div", "button", "label"):
            self.current_tag = tag
            classes = attrs_dict.get("class", "")
            href = attrs_dict.get("href", "")
            if tag == "a" and href:
                self.result.append(f"[LINK] href={href}")

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.in_script = False
            self.in_style = False
            return
        if self.current_text.strip():
            text = self.current_text.strip()
            if text and not self.in_script and not self.in_style:
                if self.current_tag:
                    self.result.append(f"[{self.current_tag}] {text}")
                else:
                    self.result.append(text)
        self.current_text = ""
        self.current_tag = None

    def handle_data(self, data):
        if not self.in_script and not self.in_style:
            self.current_text += data

def extract_images(html):
    """Extract all image URLs (from data-src, src, background-image)."""
    images = set()
    # data-src attributes
    for m in re.finditer(r'data-src="([^"]*)"', html):
        url = m.group(1)
        if "url=" in url:
            encoded = url.split("url=")[1].split("&")[0] if "&" in url.split("url=")[1] else url.split("url=")[1]
            decoded = urllib.parse.unquote(encoded)
            images.add(decoded)
        elif url.startswith("http"):
            images.add(url)
    # background-image url()
    for m in re.finditer(r"background-image:\s*url\(['\"]?([^'\")\s]+)", html):
        url = m.group(1)
        if "url=" in url:
            encoded = url.split("url=")[1].split("&")[0] if "&" in url.split("url=")[1] else url.split("url=")[1]
            decoded = urllib.parse.unquote(encoded)
            images.add(decoded)
        elif url.startswith("http"):
            images.add(url)
    # regular img src
    for m in re.finditer(r'<img[^>]*src="([^"]*)"', html):
        url = m.group(1)
        if "url=" in url:
            encoded = url.split("url=")[1].split("&")[0] if "&" in url.split("url=")[1] else url.split("url=")[1]
            decoded = urllib.parse.unquote(encoded)
            images.add(decoded)
        elif url.startswith("http"):
            images.add(url)
    return images

def extract_links(html):
    """Extract all href links."""
    links = set()
    for m in re.finditer(r'href="([^"]*)"', html):
        links.add(m.group(1))
    return sorted(links)

def extract_meta(html):
    """Extract meta tags."""
    metas = {}
    for m in re.finditer(r'<meta[^>]*name="([^"]*)"[^>]*content="([^"]*)"', html):
        metas[m.group(1)] = m.group(2)
    for m in re.finditer(r'<meta[^>]*property="([^"]*)"[^>]*content="([^"]*)"', html):
        metas[m.group(1)] = m.group(2)
    return metas

def extract_css_vars(html):
    """Extract CSS custom properties (colors, fonts)."""
    vars_dict = {}
    for m in re.finditer(r'--kv-ee-([a-z0-9-]+):\s*([^;}{]+)', html):
        name = m.group(1)
        value = m.group(2).strip()
        if value and not value.startswith("var("):
            vars_dict[name] = value
    return vars_dict

def extract_fonts(html):
    """Extract font families."""
    fonts = set()
    for m in re.finditer(r"font-family:\s*([^;}{]+)", html):
        fonts.add(m.group(1).strip().strip("'\""))
    # Google fonts link
    for m in re.finditer(r'family=([^&"]+)', html):
        fonts.add(m.group(1).strip())
    return sorted(fonts)

# Process all pages
all_data = {}
for page_name, page_path in PAGES.items():
    with open(page_path) as f:
        html = f.read()

    # Extract text content
    extractor = ContentExtractor()
    try:
        extractor.feed(html)
    except Exception:
        pass
    text_content = [line for line in extractor.result if line.strip()]

    # Extract images, links, meta
    images = sorted(extract_images(html))
    links = extract_links(html)
    metas = extract_meta(html)
    css_vars = extract_css_vars(html)
    fonts = extract_fonts(html)

    all_data[page_name] = {
        "title": "",
        "text_content": text_content,
        "images": images,
        "links": links,
        "meta": metas,
        "css_variables": css_vars,
        "fonts": fonts,
    }

# Extract titles
for page_name, page_path in PAGES.items():
    with open(page_path) as f:
        html = f.read()
    m = re.search(r"<title[^>]*>([^<]*)</title>", html)
    if m:
        all_data[page_name]["title"] = m.group(1)

# Collect all unique images
all_images = set()
for page_data in all_data.values():
    all_images.update(page_data["images"])

# Save results
output = {
    "site_url": "https://syprograms.org/",
    "pages": all_data,
    "all_images": sorted(all_images),
}

with open("/Users/augustine/Documents/syprograms/scraped_assets/site_content.json", "w") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

# Print summary
print("=== SCRAPE SUMMARY ===")
print(f"Pages scraped: {len(all_data)}")
for name, data in all_data.items():
    print(f"\n--- {name.upper()} ---")
    print(f"  Title: {data['title']}")
    print(f"  Text blocks: {len(data['text_content'])}")
    print(f"  Images: {len(data['images'])}")
    print(f"  Links: {len(data['links'])}")
    print(f"  CSS vars: {len(data['css_variables'])}")
    print(f"  Fonts: {data['fonts'][:5]}")

print(f"\n=== ALL UNIQUE IMAGES ({len(all_images)}) ===")
for img in sorted(all_images):
    print(f"  {img}")

print(f"\n=== CSS COLOR VARIABLES ===")
for k, v in all_data["home"]["css_variables"].items():
    if any(c in v.lower() for c in ["#", "rgb", "rgba", "hsl"]):
        print(f"  --{k}: {v}")
