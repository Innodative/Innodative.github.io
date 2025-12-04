# Pelican Tufte Academic Site

A clean, readable academic website built with [Pelican](https://getpelican.com/) using a custom theme inspired by [Tufte CSS](https://edwardtufte.github.io/tufte-css/).

## Features

- **Off-white/dark backgrounds** with comfortable text contrast (dark/light mode toggle)
- **Academic structure**: Research, Teaching, and Consulting as landing pages with subpages
- **Topic-based blog**: Thoughts and HowTos categories
- **Sidenotes and marginnotes** in the Tufte style
- **Responsive design** that gracefully adapts to mobile screens
- **EB Garamond typography** for classical elegance
- **GitHub Pages deployment** via GitHub Actions
- **Jekyll-style Tufte tags** for easy content creation

## Local Development

### Prerequisites

- Python 3.8+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

# Install dependencies
pip install pelican markdown

# Generate the site
pelican content

# Start the development server
pelican --listen
```

Visit `http://localhost:8000` to preview your site.

### Creating Content

**For static pages** (like research publications, course lists):
Add Markdown files to `content/pages/`:

```markdown
Title: My Page
Slug: my-page

Content here...
```

**For blog posts** (research notes, teaching reflections, thoughts):
Add Markdown files to `content/`:

```markdown
Title: My New Post
Date: 2024-01-15
Category: Thoughts
Summary: A brief description.

Your content here...
```

**Available blog categories:**
- `Thoughts` - Essays and reflections
- `HowTos` - Practical applications and case studies

Note: Research, Teaching, and Consulting are now static pages, not blog categories. To add blog posts about these topics, create posts that link from the respective landing pages.

Each category automatically gets its own page listing all articles in that topic.

For static pages (like About), add files to `content/pages/`:

```markdown
Title: About
Slug: about

Page content here...
```

### Tufte-Style Elements

This theme includes a plugin that provides Jekyll-style tags for Tufte elements, making it much easier to write content.

**Sidenotes** (numbered, appear in margin):
```
Some text{% sidenote "sn-unique-id" "This appears in the margin with a number." %} continues here.
```

**Marginnotes** (unnumbered, appear in margin with ⊕ toggle):
```
Some text{% marginnote "mn-unique-id" "This appears in the margin without a number." %} continues here.
```

**Newthought** (small caps opening phrase):
```
{% newthought "The opening phrase" %} of a new section in small caps.
```

**Epigraph** (styled quotation block):
```
{% epigraph "The quote text here." "Author Name" "Source Title" %}
```

**Main column image**:
```
{% maincolumn "assets/img/photo.jpg" "Caption for the image" %}
```

**Full-width image** (spans main content + margin):
```
{% fullwidth "images/wide-photo.jpg" "Caption for the full-width image" %}
```

**Margin figure** (image in margin):
```
{% marginfigure "mf-unique-id" "assets/img/small.jpg" "Caption in margin" %}
```

Note: Each sidenote, marginnote, and marginfigure needs a unique ID (like `sn-1`, `mn-example`, `mf-photo`) for the mobile toggle to work correctly.

### Mathematical Notation

MathJax is enabled for mathematical notation:

**Inline math:** `$E=mc^2$` or `\(E=mc^2\)`

**Display math:** 
```
$$
x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}
$$
```

**To show literal dollar signs without rendering math:**
- Use backticks for inline code: `` `$100` `` renders as `$100`
- Use backslash escape: `\$100` renders as \$100
- Math won't process inside code blocks or inline code

## Site Structure

The site is organized for academic use:

**Navigation:**
Research | Teaching | Consulting | Thoughts | HowTos | About | Colophon

**Static Pages:**
- `research.md` — Landing page with working papers and links to domains
- `research-astrophysics.md` — Astrophysics publications
- `research-data-science.md` — Data science publications
- `research-accounting.md` — Accounting publications
- `teaching.md` — Landing page with current courses
- `teaching-courses.md` — All courses taught
- `teaching-materials.md` — Course materials and resources
- `consulting.md` — Consulting services and approach
- `about.md` — Biographical information
- `colophon.md` — Site credits and tech stack

**Blog Posts:**
Regular articles with categories (Thoughts, HowTos)

## Dark Mode

The site includes an automatic dark/light mode toggle. Click the 🌙/☀️ button in the navigation. The preference is saved in your browser's localStorage.

To customize the color schemes, edit `themes/tufte/static/css/tufte.css`:

```css
:root, [data-theme="light"] {
    --bg-color: #fffff8;
    --text-color: #333333;
    /* ... more variables */
}

[data-theme="dark"] {
    --bg-color: #1a1a1a;
    --text-color: #e0e0e0;
    /* ... more variables */
}
```

## Deployment to GitHub Pages

### Option 1: GitHub Actions (Recommended)

1. Push this repository to GitHub
2. Go to **Settings → Pages**
3. Under "Build and deployment", select **GitHub Actions**
4. Update `SITEURL` in `publishconf.py` with your GitHub Pages URL:
   ```python
   SITEURL = 'https://yourusername.github.io/your-repo-name'
   ```
5. Push changes—the site will build and deploy automatically

### Option 2: Manual Deployment

```bash
# Generate production build
pelican content -s publishconf.py

# The output/ directory contains your static site
# Deploy it to any static hosting service
```

## Customization

### Site Settings

Edit `pelicanconf.py`:

```python
SITENAME = 'Your Site Title'
AUTHOR = 'Your Name'
SITESUBTITLE = 'Optional tagline'
```

### Blog Categories

To change blog category names, edit `pelicanconf.py`:

```python
TOPICS = [
    ('Thoughts', 'thoughts'),
    ('HowTos', 'use-cases'),
    ('Consulting', 'consulting'),
]
```

### Colors

Edit CSS variables in `themes/tufte/static/css/tufte.css` (see Dark Mode section above).

## Project Structure

```
├── content/
│   ├── pages/           # Static pages (about, contact)
│   ├── extra/           # Files copied as-is (.nojekyll)
│   └── *.md             # Blog posts
├── themes/
│   └── tufte/
│       ├── static/css/  # Tufte CSS
│       └── templates/   # Jinja2 templates
├── output/              # Generated site (gitignored)
├── pelicanconf.py       # Development config
├── publishconf.py       # Production config
└── .github/workflows/   # GitHub Actions
```

## License

Theme and configuration are provided under the MIT License. Content is yours.

