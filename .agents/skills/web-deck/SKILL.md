---
name: web-deck
description: Builds a self-contained HTML slide deck from a PowerPoint, outline, or notes the user provides, with one SVG per slide. Use when the user asks for a web deck, HTML slides, or to turn a pptx, PowerPoint, or talk into a browser presentation.
---

# Web deck

A deck is one HTML file a person walks with **Next**. The source decides the slides. Each slide carries one SVG of its point.

Write the file in a folder named from the title. Put it beside the source file when there is one; otherwise put it in the current project. It opens by double-click.

## 1. Name the job

Write one sentence: who is walking the deck, and what they came to follow.

The primary control is **Next**. On the last slide, Next reads **Start over**.

Done when that sentence exists before any color or layout choice.

## 2. Read the source

When more than one source is in reach, ask which one. Then take one branch.

**A .pptx.** Run `python3 scripts/extract_pptx.py <file.pptx>` from this skill folder. One source slide becomes one deck slide, in that order. `[image]` means the slide had a picture to redraw. Slide copy is the text on the slide. Speaker notes stay in the file.

**Text the user wrote.** An outline, notes, or a paste. One heading becomes one slide. A list with no headings becomes one slide per top-level item.

Done when every slide has a title and its support points, in source order, and a fact appears only when the source states it.

## 3. Set the system

Copy [template.html](template.html). That file is the chrome: field, type, Next, keyboard, and the hash (`#3` opens slide 3).

Tokens, used only at these sizes and weights:

- Field `#071426`, raised surface `#10243f`, line `#2a466c`, text `#e8eef7`, quiet text `#9aafc8`
- One accent `#e4a34b`, accent ink `#1c1408` on the Next button
- Sizes: title, lead, body, meta. Weights: 500 and 400. Space step: 8px

When the user names a field or an accent, replace those tokens, including the arrow marker fill, before writing slides. Quiet text stays readable on the field.

Done when the tokens are set and the template still has one Next button.

## 4. Write the slides

Duplicate the `section.slide` block once per source slide. The first heading is an `h1`. Later headings are `h2`. Give each heading an id `s1`, `s2`, … and `tabindex="-1"`.

Regions, in this order:

- **Primary** — the slide title.
- **Support** — the source points, then one SVG of the relationship those points claim.
- **Quiet** — the header (title, author, date) and the footer.

On a narrow width the support stacks under the title. Body copy stays within about 38ch. A heading states the slide's point in the source's words.

The SVG:

- `role="img"` and an `aria-label` that states what it shows
- Strokes in the text color, the line color, and the accent
- Labels sit inside the viewBox
- A picture in the source becomes a drawing of the structure it shows
- A chart with no data table becomes a drawing of the claim, captioned as an illustration of that claim

Keep technical names as the source spells them. Fix a typo only when it blocks reading.

Done when the file has one section per source slide, each with an SVG, and the script from the template is unchanged.

## 5. Check

Open the file. Use Next through every slide, then Start over. Also step with the right arrow and open `#2` directly.

Check a wide window and a window under 800px wide. In both, Next is on screen, body text is readable on the field, and each SVG's labels sit inside the drawing.

Done when both widths show the same slides in source order and a broken label or a missing claim is fixed and rechecked.

## Example

Source slide: "Zephyr-7B-beta needs about 13 GB, a quarter of a 70B model, and is used for reasoning and extraction."

Title: Zephyr-7B-beta. Support: those three claims. SVG: a short bar labeled 13 GB beside a bar about four times as wide labeled 70B. The figure states the memory claim the source gave.
