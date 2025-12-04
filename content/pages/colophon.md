Title: Colophon
Slug: colophon

{% newthought "This website" %} is a collaboration between human and machine, built with modern tools while honoring classical typography principles.

## Design Philosophy

The visual design draws inspiration from [Tufte CSS](https://edwardtufte.github.io/tufte-css/), itself based on the work of Edward Tufte—statistician, artist, and pioneer of information design. Tufte's books on data visualization are masterworks of typography, demonstrating how thoughtful design enhances comprehension.

Key design principles:

**Generous margins** provide breathing room and space for sidenotes. On wide screens, supplementary information appears alongside the main text rather than interrupting the flow.{% marginnote "mn-sidenotes" "Sidenotes are Tufte's signature element. They keep related information visible without breaking reading rhythm." %}

**Classical typography** using EB Garamond for body text—a revival of Claude Garamond's sixteenth-century designs. Navigation and metadata use Source Sans Pro for clarity.

**Responsive design** that adapts gracefully to different screen sizes. On narrow screens, sidenotes become toggleable to preserve readability.

**Dark mode support** with carefully chosen color palettes for both light and dark themes. Toggle using the button in the navigation.

## Technical Stack

- **[Pelican](https://getpelican.com/)** — Static site generator written in Python
- **[Jinja2](https://jinja.palletsprojects.com/)** — Template engine for page layouts
- **Custom theme** — Built from scratch, inspired by Tufte CSS
- **Custom plugin** — Provides Jekyll-style tags for Tufte elements
- **[GitHub Pages](https://pages.github.com/)** — Hosting and deployment
- **[Markdown](https://daringfireball.net/projects/markdown/)** — Content authoring format

Static sites like this one require no database or server-side processing. They're fast, secure, and simple to maintain—just HTML, CSS, and JavaScript files served directly to browsers.

## Color Palette

**Light mode:**
- Background: `#fffff8` (off-white)
- Text: `#333333` (dark grey)
- Links: `#444444`
- Sidenotes: `#666666`

**Dark mode:**
- Background: `#1a1a1a` (near-black)
- Text: `#e0e0e0` (light grey)
- Links: `#b0b0b0`
- Sidenotes: `#aaaaaa`

## Typography

- **Body text**: [EB Garamond](https://fonts.google.com/specimen/EB+Garamond) at 1.3rem (approx. 20px)
- **Navigation**: [Source Sans Pro](https://fonts.google.com/specimen/Source+Sans+Pro)
- **Code**: SF Mono, Monaco, Inconsolata (system defaults)
- **Line height**: 1.65 for comfortable reading
- **Line length**: 600-900px for optimal readability

## Credits & Acknowledgments

**Design inspiration:**
- [Tufte CSS](https://edwardtufte.github.io/tufte-css/) by Dave Liepmann
- [tufte-jekyll](https://github.com/clayh53/tufte-jekyll) by Clay Harmon
- The books of Edward Tufte

**Development:**
This site was built in collaboration with Claude (Anthropic's AI assistant), who helped with:
- Custom Pelican theme development
- Plugin creation for Tufte-style tags
- Responsive layout implementation
- Dark mode integration
- Content structure and organization

The human provided direction, feedback, and iteration; Claude wrote code, solved technical problems, and offered design suggestions. The result demonstrates what's possible when humans and AI work together on creative technical projects.{% sidenote "sn-ai" "All content—research descriptions, teaching materials, biographical information—was written by the human. Claude handled the technical implementation." %}

## Source Code

The complete source for this site is available on [GitHub](https://github.com/Innodative/Innodative.github.io). Feel free to use it as a starting point for your own academic website.

## License

- **Theme and code**: MIT License
- **Content**: © Robert J Brunner (Innodative.com). All rights reserved.
- **Tufte CSS**: MIT License (original work by Dave Liepmann)

## Contact

Questions or suggestions about the site design? [Get in touch](/contact/).
