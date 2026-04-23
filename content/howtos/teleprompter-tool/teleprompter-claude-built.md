Title: My Teleprompter that Claude Built
Date: 2026-04-22
Modified: 2026-04-23
Draft: true
Category: HowTos
Tags: ai, tools, workflow, course-development
Slug: teleprompter-claude-built
Summary: A custom browser-based teleprompter built in a single chat. Why the economics of custom tools just changed.

I'm recording audio narration for a new blockchain course. The scripts live in Pages, complete with production callouts like [ON SCREEN: diagram of consensus mechanism] and [B-ROLL: server farm footage]. Reading them naturally while recording turned out to be harder than expected. Scrolling a document manually breaks pacing. Losing your place means starting over. {% sidenote "commercial-teleprompters" "Commercial teleprompter apps exist, most priced for broadcast studios rather than someone recording a few hours of course audio a week." %}

During a Claude conversation about the course, I mentioned the problem. Claude offered to build one.

A few iterations later, I had a single HTML file that did exactly what I needed.

## What it does

Paste a script from Pages, click one button, land in prompter mode. Production markup is stripped automatically, so [ON SCREEN], [VISUAL], [B-ROLL], and the table borders Pages sometimes injects disappear before the text hits the screen. The first line becomes the video title. A faint red guide line sits 38% from the top. That's where I read.

{% sidenote "keyboard-shortcuts" "Keyboard shortcuts: Space plays and pauses, up and down arrows adjust speed, Escape returns to the paste screen. Mouse wheel scrolls manually when paused." %}

Auto-scroll runs from 0.5x to 5x, adjustable live by slider or arrow key. Font steps from 28 to 56 pixels. Dark background, Georgia serif, generous line height. No dependencies, no install, no subscription. It runs in any browser, including on an iPad propped next to the mic.

## The iteration

The first version worked but treated the raw paste as narration, including all the production callouts. Version two stripped them. Version three caught the table borders. Keyboard shortcuts came next. The guide line started at the center and migrated up to 38% after testing it against an actual script.

Each change took a sentence to describe. The whole thing happened inside a single chat.

## The pattern

The teleprompter itself isn't the point. The pattern is.

Most professionals have small friction in their workflows. Tools that almost exist. Formats that don't quite fit. Annoyances absorbed so long ago you've stopped seeing them. The old answer was to live with them, search for an app, or ask IT.

The new answer is to describe what you want and get a working tool in minutes.

That shifts the economics. A custom tool used to be a project, which meant clearing a bar: worth a developer's time, worth a budget line, worth the wait. Most friction points never cleared that bar. They got absorbed.

When the tool takes a conversation to produce, the bar moves. Things that weren't worth building become worth building.

## Try it

The teleprompter is live at [/tools/teleprompter/](/tools/teleprompter/). Paste a script and see what happens. Save the page to use it offline for your own recording. There's nothing to connect to.

If you want to try this pattern yourself, pick one small friction point from your own week. Describe it to an AI. Iterate until it fits. Mine took a handful of rounds and no code on my part.

---

This article was developed with AI assistance for research, outlining, drafting, and editing. All ideas, experiences, and perspectives are my own.
