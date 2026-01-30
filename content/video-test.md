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

{% video "dQw4w9WgXcQ" "A standard video embedded in the main column" %}

This works well for supplementary videos that don't need to dominate the page.

## Full-Width Video (Spans Main + Margin)

Here's a video that spans both the main text and margin area:

{% fullwidthvideo "dQw4w9WgXcQ" "A full-width video that spans the entire content area" %}

This is better for key videos you want to emphasize.{% marginnote "mn-fullwidth" "On mobile, both styles collapse to full-width automatically thanks to responsive design." %}

## Testing Complete

Both embedding styles are responsive and will work on mobile devices. The video tags automatically create the proper 16:9 aspect ratio wrapper that works across all screen sizes.

Now you just use simple tags like `{% video "VIDEO_ID" "caption" %}` instead of the complex HTML!
