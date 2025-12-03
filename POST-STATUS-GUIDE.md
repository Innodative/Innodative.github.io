# Post Status Control Guide

## How to Hide/Show Posts

Pelican has built-in support for controlling post visibility using the `Status:` metadata field.

### Status Options

Add this to your post's metadata (at the top of the markdown file):

**Published (default)**
```markdown
Title: My Post Title
Date: 2024-12-03
Tags: research, ai
Topic: thoughts

(No Status field needed - posts are published by default)
```

**Hidden**
```markdown
Title: My Draft Post
Date: 2024-12-03
Tags: research, ai
Topic: thoughts
Status: hidden

Post content here...
```

Posts marked as `hidden` are:
- NOT included in the main output
- NOT listed in indexes, archives, or feeds
- NOT visible on the live site
- Still viewable in your source files

**Draft**
```markdown
Title: Work in Progress
Date: 2024-12-03
Tags: research, ai
Topic: thoughts
Status: draft

Post content here...
```

Posts marked as `draft` are:
- Similar to hidden
- Treated the same way by Pelican
- Useful for distinguishing "not ready" from "intentionally hidden"

### Quick Workflow

1. **Hide a post**: Add `Status: hidden` to the metadata
2. **Publish a post**: Remove the `Status:` line (or change to `Status: published`)
3. **Work on drafts**: Keep `Status: draft` until ready

### Example: Hiding an Old Post

Original post:
```markdown
Title: Old Thoughts on X
Date: 2023-01-15
Tags: blockchain
Topic: thoughts

Content here...
```

To hide it:
```markdown
Title: Old Thoughts on X
Date: 2023-01-15
Tags: blockchain
Topic: thoughts
Status: hidden

Content here...
```

That's it! Rebuild the site and the post won't appear.

### Notes

- Status applies to both blog posts and pages
- Hidden posts are completely excluded from output
- No need to delete files - just toggle Status
- Easy to publish later by removing the Status line
