# Agent skills

Skills in this repo live under `.agents/skills/`. Each skill is a folder the agent reads when a task matches it.

## What `SKILL.md` is

`SKILL.md` is the file that teaches the agent a specific job. It has two parts:

- **Frontmatter.** A short YAML block at the top. `name` is the skill's id. `description` says what the skill does and which requests should trigger it. The agent uses that description to decide whether to apply the skill.
- **Body.** The procedure. Steps, rules, and what "done" looks like. The agent follows this when the skill is in play.

A skill can also keep files beside `SKILL.md`: a template to copy, a script to run, or a longer reference. The agent opens those only when the procedure points to them.

## Web deck

[`.agents/skills/web-deck/SKILL.md`](.agents/skills/web-deck/SKILL.md) builds a website GUI from content you provide: a PowerPoint, an outline, or notes.

The result is one HTML file you open in a browser. Each source slide becomes one screen. **Next** walks the deck; on the last slide it returns to the start. Arrow keys work the same way, and a hash such as `#3` opens that slide directly.

The default look is a dark blue field with one amber accent on **Next**. If you name a background or an accent, those colors replace the defaults. Every slide includes an SVG that draws the point of that slide, using only claims that are in your source.

Ask for a web deck, HTML slides, or to turn a pptx or talk into a browser presentation, and the agent follows this skill. The deck is saved in a folder named from the title, next to the source file when you gave one.
