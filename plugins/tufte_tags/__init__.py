"""
Tufte Tags Plugin for Pelican

Provides Jekyll-style tags for Tufte CSS elements:
    {% sidenote "id" "content" %}
    {% marginnote "id" "content" %}
    {% newthought "text" %}
    {% epigraph "quote" "author" "source" %}
    {% fullwidth "image" "caption" %}
    {% maincolumn "image" "caption" %}
    {% marginfigure "id" "image" "caption" %}

Supports:
    - Double or single quotes as delimiters
    - Escaped quotes inside content (\\" or \\')
    - Markdown inside parameters
    - HTML inside parameters
"""

import re
from markdown import markdown
from pelican import signals


def process_tufte_tags(content):
    """Process all Tufte tags in content."""
    if not content._content:
        return
    
    text = content._content
    
    # Process each tag type
    text = process_sidenotes(text)
    text = process_marginnotes(text)
    text = process_newthought(text)
    text = process_epigraph(text)
    text = process_fullwidth(text)
    text = process_maincolumn(text)
    text = process_marginfigure(text)
    
    content._content = text


def extract_quoted_string(text, start_pos):
    """
    Extract a quoted string starting at start_pos.
    Handles both single and double quotes, escaped quotes, and nested HTML.
    Returns (extracted_string, end_pos) or (None, -1) if no match.
    """
    # Skip whitespace
    pos = start_pos
    while pos < len(text) and text[pos] in ' \t\n':
        pos += 1
    
    if pos >= len(text):
        return None, -1
    
    quote_char = text[pos]
    if quote_char not in '"\'':
        return None, -1
    
    pos += 1  # Move past opening quote
    result = []
    depth = 0  # Track nesting depth for HTML attributes
    
    while pos < len(text):
        char = text[pos]
        
        # Check for escaped quote
        if char == '\\' and pos + 1 < len(text) and text[pos + 1] in '"\'':
            result.append(text[pos + 1])
            pos += 2
            continue
        
        # Track entering/exiting HTML tags to handle nested quotes
        if char == '<':
            depth += 1
        elif char == '>' and depth > 0:
            depth -= 1
        
        # Check for closing quote (but only if we're not inside an HTML tag)
        if char == quote_char and depth == 0:
            return ''.join(result), pos + 1
        
        result.append(char)
        pos += 1
    
    return None, -1  # No closing quote found


def parse_tag(text, tag_name, num_args):
    """
    Parse all instances of a tag with the given number of arguments.
    Returns list of (full_match, [args], start_pos, end_pos).
    """
    results = []
    pattern = r'{%\s*' + tag_name + r'\s+'
    
    for match in re.finditer(pattern, text):
        start = match.start()
        pos = match.end()
        args = []
        
        # Extract each argument
        for i in range(num_args):
            arg, pos = extract_quoted_string(text, pos)
            if arg is None:
                break
            args.append(arg)
        
        if len(args) != num_args:
            continue
        
        # Skip whitespace and find closing %}
        while pos < len(text) and text[pos] in ' \t\n':
            pos += 1
        
        if pos + 1 < len(text) and text[pos:pos+2] == '%}':
            end = pos + 2
            full_match = text[start:end]
            results.append((full_match, args, start, end))
    
    return results


def render_markdown(text):
    """Render Markdown in text, stripping the outer <p> tags."""
    if not text:
        return text
    rendered = markdown(text)
    # Strip outer <p></p> if present
    rendered = re.sub(r'^<p>(.*)</p>$', r'\1', rendered.strip(), flags=re.DOTALL)
    return rendered


def process_sidenotes(text):
    """
    Convert {% sidenote "id" "content" %} to proper HTML.
    Sidenotes are numbered margin notes.
    """
    matches = parse_tag(text, 'sidenote', 2)
    
    # Process in reverse order to preserve positions
    for full_match, args, start, end in reversed(matches):
        note_id = args[0]
        content = render_markdown(args[1])
        replacement = (
            f'<label for="{note_id}" class="margin-toggle sidenote-number"></label>'
            f'<input type="checkbox" id="{note_id}" class="margin-toggle"/>'
            f'<span class="sidenote">{content}</span>'
        )
        text = text[:start] + replacement + text[end:]
    
    return text


def process_marginnotes(text):
    """
    Convert {% marginnote "id" "content" %} to proper HTML.
    Marginnotes are unnumbered margin notes with a ⊕ toggle.
    """
    matches = parse_tag(text, 'marginnote', 2)
    
    for full_match, args, start, end in reversed(matches):
        note_id = args[0]
        content = render_markdown(args[1])
        replacement = (
            f'<label for="{note_id}" class="margin-toggle">⊕</label>'
            f'<input type="checkbox" id="{note_id}" class="margin-toggle"/>'
            f'<span class="marginnote">{content}</span>'
        )
        text = text[:start] + replacement + text[end:]
    
    return text


def process_newthought(text):
    """
    Convert {% newthought "text" %} to small caps span.
    Used for opening phrases of sections.
    """
    matches = parse_tag(text, 'newthought', 1)
    
    for full_match, args, start, end in reversed(matches):
        content = render_markdown(args[0])
        replacement = f'<span class="newthought">{content}</span>'
        text = text[:start] + replacement + text[end:]
    
    return text


def process_epigraph(text):
    """
    Convert {% epigraph "quote" "author" "source" %} to epigraph HTML.
    Also supports {% epigraph "quote" "author" %} without source.
    """
    # Try three-argument version first
    matches = parse_tag(text, 'epigraph', 3)
    
    for full_match, args, start, end in reversed(matches):
        quote = render_markdown(args[0])
        author = args[1]
        source = args[2]
        replacement = (
            f'<div class="epigraph"><blockquote>'
            f'<p>{quote}</p>'
            f'<footer>{author}, <cite>{source}</cite></footer>'
            f'</blockquote></div>'
        )
        text = text[:start] + replacement + text[end:]
    
    # Then two-argument version
    matches = parse_tag(text, 'epigraph', 2)
    
    for full_match, args, start, end in reversed(matches):
        quote = render_markdown(args[0])
        author = args[1]
        replacement = (
            f'<div class="epigraph"><blockquote>'
            f'<p>{quote}</p>'
            f'<footer>{author}</footer>'
            f'</blockquote></div>'
        )
        text = text[:start] + replacement + text[end:]
    
    return text


def process_fullwidth(text):
    """
    Convert {% fullwidth "image" "caption" %} to full-width figure.
    """
    matches = parse_tag(text, 'fullwidth', 2)
    
    for full_match, args, start, end in reversed(matches):
        image = args[0]
        caption = render_markdown(args[1])
        # Handle relative paths
        if not image.startswith(('http://', 'https://', '/')):
            image = '/' + image
        replacement = (
            f'<figure class="fullwidth">'
            f'<img src="{image}" alt="{caption}"/>'
            f'<figcaption>{caption}</figcaption>'
            f'</figure>'
        )
        text = text[:start] + replacement + text[end:]
    
    return text


def process_maincolumn(text):
    """
    Convert {% maincolumn "image" "caption" %} to main column figure.
    """
    matches = parse_tag(text, 'maincolumn', 2)
    
    for full_match, args, start, end in reversed(matches):
        image = args[0]
        caption = render_markdown(args[1])
        # Handle relative paths
        if not image.startswith(('http://', 'https://', '/')):
            image = '/' + image
        replacement = (
            f'<figure>'
            f'<img src="{image}" alt="{caption}"/>'
            f'<figcaption>{caption}</figcaption>'
            f'</figure>'
        )
        text = text[:start] + replacement + text[end:]
    
    return text


def process_marginfigure(text):
    """
    Convert {% marginfigure "id" "image" "caption" %} to margin figure.
    """
    matches = parse_tag(text, 'marginfigure', 3)
    
    for full_match, args, start, end in reversed(matches):
        fig_id = args[0]
        image = args[1]
        caption = render_markdown(args[2])
        # Handle relative paths
        if not image.startswith(('http://', 'https://', '/')):
            image = '/' + image
        replacement = (
            f'<label for="{fig_id}" class="margin-toggle">⊕</label>'
            f'<input type="checkbox" id="{fig_id}" class="margin-toggle"/>'
            f'<span class="marginnote">'
            f'<img src="{image}" alt="{caption}"/>'
            f'{caption}'
            f'</span>'
        )
        text = text[:start] + replacement + text[end:]
    
    return text


def register():
    """Register the plugin with Pelican."""
    signals.content_object_init.connect(process_tufte_tags)
