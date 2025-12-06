# Pamoja IB CS HL Vault Root

## Overview and Purpose
This vault organizes my IB Computer Science HL coursework (via Pamoja). It provides:
- A week-by-week index of lesson notes (Markdown-first for Obsidian/Notion export)
- Quick links to each week’s overview and lesson pages
- A place to capture revision notes, exam prep, and IA planning

Repository structure (key paths):
- `weeks/weekN/` → per‑week overview (N.0.md)
- `weeks/markdown/weekN/` → lesson notes (N.1.md, N.2.md, …)
- `weeks/.html/weekN/` → original lesson HTML (hidden folder)

---
## How to Work With This Vault (AI Prompting Context)
Use the following prompts and conventions so AI can help me study efficiently and aim for a 7:

### Converting content
- “Convert `weeks/.html/weekX/X.Y.html` into Notion‑ready Markdown. Preserve headings (H1/H2/H3), tables, lists. Replace iframes with plain URLs.”
- “Fix image/video embeds to standard Markdown; use plain YouTube links.”

### Studying & revision
- “Summarize `weeks/markdown/weekX/X.Y.md` into key points and exam‑style Q&A.”
- “Create flashcards (Q on front, concise A) from `X.Y.md`—limit to ≤ 20 high‑yield cards.”
- “Generate a mini‑quiz (5–10 questions: MCQ + short answers) from `X.Y.md`, with answers.”

### Linking & navigation
- “Update `root.md` link tree to include week N lessons that were added today.”
- “Create a ‘Further Reading’ section in `N.0.md` with 3 reputable links.”

### IB focus (HL, Pamoja)
- “Map `X.Y.md` content to IB CS Guide topics (HL), noting overlaps with Paper 1/2/3.”
- “Draft IA planning bullets: client need → success criteria → justification of techniques → testing plan.”

### House rules for edits
- Keep Markdown clean; avoid HTML unless necessary.
- Do not move files—use existing structure (`weeks/weekN` and `weeks/markdown/weekN`).
- When creating new notes, prefer `N.Z.md` naming (e.g., `6.5.md`).
- For Obsidian, keep attachments in `/attachments` and use relative links.

---