Title: Tufte CSS Demo
Date: 2020-04-13
Modified: 2025-11-26
Category: Thoughts
Status: hidden
Summary: A demonstration of Tufte CSS styling elements adapted for Pelican, showing sidenotes, margin notes, figures, and typography features.

{% newthought "This page" %} demonstrates the features of the Tufte CSS styling system as implemented for Pelican. Edward Tufte's style is known for its extensive use of sidenotes, tight integration of graphics with text, and a typography derived from the work of Robert Bringhurst.{% sidenote "sn-tufte" "Edward Tufte, *The Visual Display of Quantitative Information* (Graphics Press, 1983)." %}

The Tufte-Pelican implementation transforms the original Tufte CSS into custom Pelican plugins, making it easy to create content using markdown combined with custom tags. This approach maintains the elegant typography and layout principles while working within the Pelican static site generator framework.

## Sidenotes and Margin Notes

One of the most distinctive features of Tufte's style is the extensive use of sidenotes.{% sidenote "sn-demo" "This is a sidenote. Notice how it appears in the margin rather than at the bottom of the page." %} In print, these are positioned in the right margin. On the web, they appear in the wide right-hand column that this design provides.

Sidenotes are numbered sequentially and connected to their reference points in the main text through superscript numbers. They're designed to be easily readable without requiring the reader to navigate away from the main text.

Margin notes are similar to sidenotes but lack the numbered reference. They're useful for side comments that aren't critical to the main narrative.{% marginnote "mn-demo" "This is a margin note. It appears in the margin just like a sidenote, but without a reference number in the text." %} Use them when you want to provide additional context without interrupting the flow of the main text.

## Typography and Text

The default font for this theme is ETBook, a typeface designed to be highly readable on screens while echoing the style of Bembo, which was used in Tufte's print books.{% sidenote "sn-font" "See [ET Book](https://github.com/edwardtufte/et-book) on GitHub." %}

{% newthought "Particular attention" %} should be paid to typography. The `newthought` tag creates small caps at the beginning of a section, as demonstrated at the start of this paragraph. This provides a visual cue without the heavy-handedness of a subheading.

Text can include the usual markdown emphasis: *italics* and **bold**. Links look like [this link to Edward Tufte's website](https://www.edwardtufte.com/). The default link style is understated, keeping with Tufte's minimalist aesthetic.

Block quotes are set off from the main text:

> The English language . . . becomes ugly and inaccurate because our thoughts are foolish, but the slovenliness of our language makes it easier for us to have foolish thoughts. 
> 
> -- George Orwell, "Politics and the English Language"

## Figures and Images

Tufte emphasizes tight integration of graphics and text. Figures can be placed in the main text column:

{% maincolumn "/images/demo-figure.png" "William Playfair's chart of exports and imports between Denmark & Norway and England (1700-1780), demonstrating early use of area charts to show trade balance over time." %}

Or they can be placed in the margin using marginfigure:

{% marginfigure "mf-demo" "/images/demo-marginfigure.png" "Albrecht Dürer's famous 1515 woodcut of a rhinoceros, created without the artist ever seeing the animal in person. From page 71 of Edward Tufte's *Visual Explanations*." %}

The most distinctive visual element in Tufte's work is perhaps the full-width figure, which spans both the main text and the margin. The paradigmatic example is Charles Joseph Minard's 1869 chart showing Napoleon's march to Moscow and back:

{% fullwidth "/images/napoleons-march-demo.png" "Charles Joseph Minard's 1869 flow map depicting Napoleon's disastrous 1812 Russian campaign. The width of the tan line shows the army's size (422,000 starting), with temperature and geography integrated. Edward Tufte called this 'probably the best statistical graphic ever drawn.'" %}

This famous graphic shows six types of data: geography, direction of movement, troop strength, temperature, time, and the catastrophic losses suffered during the retreat. It's considered one of the best statistical graphics ever created.

## Equations and Mathematics

Mathematical expressions can be included using standard LaTeX notation, rendered by MathJax.{% sidenote "sn-math" "MathJax support is included in this theme." %} Inline math looks like this: $E=mc^2$. Display equations get their own space:

$$
\frac{1}{(\sqrt{\phi \sqrt{5}}-\phi)} = 1 + \frac{e^{-2\pi}} {1 + \frac{e^{-4\pi}} {1 + \frac{e^{-6\pi}} {1 + \frac{e^{-8\pi}} {1 + \cdots}}}}
$$

The golden ratio $\phi = (1 + \sqrt{5})/2$ appears frequently in mathematics and nature. Its continued fraction representation demonstrates the self-similar structure that makes it such an important number.

Here's another example showing the Cauchy-Schwarz inequality:

$$
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
$$

## Code

Code blocks can be included for technical content. Inline code looks like `this`, while code blocks get syntax highlighting:

```python
def fibonacci(n):
    """Generate Fibonacci sequence up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

fibonacci(100)
```

The monospaced font is distinct from the body text, making code easy to identify at a glance.

## Lists

Tufte CSS styles lists to align with the overall typography. Unordered lists look like this:

- First item in the list
- Second item with some additional detail
- Third item to round things out

And ordered lists maintain the same spacing:

1. Primary point to consider
2. Secondary consideration
3. Tertiary aspect worth noting

Nested lists maintain proper indentation and spacing:

1. Main category
   - Subcategory A
   - Subcategory B
2. Second main category
   - Another subcategory
   - Yet another subcategory

## Tables

Tables in Tufte CSS maintain the minimal aesthetic with light rules separating elements:

| Item | Quantity | Price |
|------|----------|-------|
| Apples | 5 | $3.50 |
| Oranges | 3 | $2.75 |
| Bananas | 8 | $4.00 |
| Total | 16 | $10.25 |

The table styling emphasizes readability through spacing rather than heavy borders.

## Responsive Design

This design is fully responsive. On smaller screens:

- Sidenotes and margin notes convert to collapsible toggles marked with ⊕ symbols
- Full-width figures scale appropriately
- The layout gracefully degrades to a single column
- Touch-friendly controls make navigation easy

The mobile experience maintains the essential character of the design while adapting to the constraints of smaller screens.

## Implementation Notes

This Pelican theme uses custom tags that mirror the functionality of the original Jekyll liquid tags:

**Examples:**

<pre><code>&#123;% newthought "text" %&#125;</code></pre>

Small caps opener for beginning of sections.

<pre><code>&#123;% sidenote "id" "content" %&#125;</code></pre>

Numbered sidenotes that appear in the margin.

<pre><code>&#123;% marginnote "id" "content" %&#125;</code></pre>

Unnumbered margin notes with a ⊕ toggle.

<pre><code>&#123;% maincolumn "image" "caption" %&#125;</code></pre>

Regular figures in the main text column.

<pre><code>&#123;% marginfigure "id" "image" "caption" %&#125;</code></pre>

Margin figures (note: ID parameter comes first, then image path, then caption).

<pre><code>&#123;% fullwidth "image" "caption" %&#125;</code></pre>

Full-width figures spanning main text and margin areas.

These tags are processed by Python plugins in the Pelican build process, generating the appropriate HTML structure with CSS classes for styling.

## Conclusion

{% newthought "The Tufte aesthetic" %} emphasizes clarity, precision, and efficient use of space. By bringing these principles to the web through Pelican, we can create content that is both beautiful and functional. The integration of text, graphics, and marginal notes produces a reading experience that is closer to a well-designed book than a typical web page.

This approach isn't suitable for every type of website, but for long-form content, technical writing, and academic publishing, it offers a compelling alternative to conventional web design.{% sidenote "sn-final" "For more on Tufte's design principles, see his books *The Visual Display of Quantitative Information*, *Envisioning Information*, and *Beautiful Evidence*." %}
