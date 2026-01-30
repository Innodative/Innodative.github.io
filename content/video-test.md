Title: Video Embedding Test
Date: 2026-01-30
Category: Thoughts
Tags: test
Slug: video-test
Status: hidden
Summary: Testing video embedding with responsive design

{% newthought "This is a test post" %} to demonstrate video embedding with proper responsive design for both desktop and mobile viewing.

## Standard Video (Main Column)

Here's a video in the main text column:

<figure>
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
<iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
src="https://www.youtube.com/embed/dQw4w9WgXcQ"
frameborder="0" allowfullscreen></iframe>
</div>
<figcaption>A standard video embedded in the main column</figcaption>
</figure>

This works well for supplementary videos that don't need to dominate the page.

## Full-Width Video (Spans Main + Margin)

Here's a video that spans both the main text and margin area:

<figure class="fullwidth">
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
<iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
src="https://www.youtube.com/embed/dQw4w9WgXcQ" 
frameborder="0" allowfullscreen></iframe>
</div>
<figcaption>A full-width video that spans the entire content area</figcaption>
</figure>

This is better for key videos you want to emphasize.{% marginnote "mn-fullwidth" "On mobile, both styles collapse to full-width automatically thanks to responsive design." %}

## Testing Complete

Both embedding styles are responsive and will work on mobile devices. The `padding-bottom: 56.25%` maintains the 16:9 aspect ratio across all screen sizes.
