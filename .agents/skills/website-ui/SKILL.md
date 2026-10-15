---
name: website-ui
description: Design and implement a website page so hierarchy, type, color, and spacing serve one job and match the existing site. Use when the user asks to design a page, restyle a website, or review website UI.
---

# Website UI

Commit to one page design and implement it in the project's UI. The page has one job. Hierarchy, type, color, and spacing express that job and stay recognizable as this site.

If the user wants several looks to compare before committing, use the prototype skill instead. This skill ships one design on the real page.

## Branch

- **Design** — the page is new, or the user wants it designed and built. Run the sequence.
- **Restyle** — the job and the information stay. Redo presentation, then implement and check.
- **Review** — walk the rendered page against the page rules. Implement every presentation failure. If a failure is the job or the information, name it and wait.

## Sequence

### 1. Name the job

Write one sentence: who the page is for, what they came to do, and the single primary action.

Done when that sentence exists before any visual decision.

### 2. Read the site

Read neighboring pages and the styling system (type, color, spacing, components).

Done when you can name what this page reuses. If the site has no system, define one before the page: one type family, one accent, one spacing step, four type sizes, two weights. Put it where the project already keeps styles.

### 3. Assign hierarchy

Give every region one role:

- **Primary** — the job and its action. One control.
- **Support** — what makes that action make sense.
- **Quiet** — navigation, meta, legal.

Emphasis comes from position, then scale, then weight, then color.

Done when each region has one role and only one control is primary.

Example. Job: "A visitor deciding whether to start a trial. Primary action: Start trial." Primary is the outcome headline and one Start trial button. Support is the proof directly under it. Quiet is the header and footer.

### 4. Implement

Build with the project's components, tokens, and file conventions. The page renders the hierarchy from step 3.

Done when the page uses the system named in step 2.

### 5. Check the rendered page

Open the page and use the primary action. Check a wide width and a narrow width.

Done when both widths show the same job, the primary action is visible without hunting, body text is readable against its background, and groups are separated by the spacing step.

## Page rules

**Type.** Use the site's scale. Body copy stays within a comfortable measure. A heading states the section's point.

**Color.** Neutrals build structure. The accent marks the primary action and carries meaning (status, selection). Body and interface text stay clearly darker or lighter than their background.

**Spacing.** One step. Tighter inside a group, looser between groups. Align to the same edges as sibling pages.

**Layout.** The job picks the structure. Reading is a column. Comparing repeated objects is a list or grid of those objects. A workspace is a stable frame and one changing region. A marketing page is one idea per band.

**Narrow width.** Regions stack in role order: primary, support, quiet. The primary action stays on screen or one obvious step away.
