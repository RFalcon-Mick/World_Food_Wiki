# ✍️ Style Guide · World Food Wiki

This document defines the **formatting and style rules** for all contributions to the project.  
Following these rules ensures that entries are **consistent, searchable, and reader-friendly**.

---

## 1. File Naming & Structure
- Each dish should be a **single Markdown file**:  
  `foods/<continent>/<country>/<dish>.md`
- Example:  
  `foods/europe/italy/pizza.md`

---

## 2. Frontmatter
Every dish file must start with a **YAML Frontmatter** block.  
This allows structured metadata for search and indexing.

**Required fields**:
```yaml
---
title: Pizza
aliases: [Pizza, ピッツァ, Pitsa]
regions: [Europe, Italy, Naples]
periods: [18th Century, 19th Century]
techniques: [Fermentation, Baking]
categories: [Staple, Street Food]
ingredients: [Wheat Flour, Yeast, Tomato, Cheese, Olive Oil]
origin_summary: >-
  One-sentence summary of origin and context.
license: CC BY-SA 4.0
---
```

**Rules**:
- Use **standardized vocabulary** from `data/tags.yml` (regions, periods, techniques).  
- `aliases` should include common translations, romanizations, or alternative spellings.  
- `origin_summary` should be 1–3 sentences maximum.  
- `license` defaults to `CC BY-SA 4.0` unless explicitly stated otherwise.

---

## 3. Section Order
Each dish Markdown file should follow this order:

1. **Dish Name (H1)**  
2. **Introduction** – Short description of the dish and its significance.  
3. **Place of Origin** – Country/region, with context.  
4. **Time of Emergence** – Year or approximate period.  
5. **Origins** – Cultural or historical roots.  
6. **Historical Development** – Chronological evolution of the dish.  
7. **Ingredients** – Bullet list of key ingredients.  
8. **Cooking Method** – Traditional method + major variations.  
9. **References** *(optional)*  
10. **Citations** *(optional)*  

---

## 4. Writing Style
- Use **concise, neutral, and informative** language.  
- Avoid personal opinions or unverifiable claims.  
- Prefer **chronological storytelling** for history.  
- When describing cooking methods, balance **technical accuracy** with **readability**.  
- If multiple styles/variations exist, use sub-sections or bullet points.

---

## 5. Formatting Rules
- Use **Markdown headings** (`#`, `##`, `###`) consistently.  
- Use **bullet lists** (`-`) for ingredients or timelines.  
- Use **inline code** (`` `like this` ``) only for commands or file paths.  
- Images (optional) must include **source + license** in captions.

---

## 6. References & Citations (Optional)
- **Not mandatory**. If you have reliable sources, add them. If not, leave the section out.  
- If added, references should follow the rules in [citation_guide.md](citation_guide.md).  
- Citations in text should use author + year, e.g., *(Helstosky, 2008)*.  

---

## 7. Do & Don’t Examples
✅ Do:
```markdown
## Time of Emergence
Pizza emerged in Naples during the late 18th century, becoming widely popular among the working-class population.

## Ingredients
- Wheat flour (Tipo 00)
- Yeast
- Tomato (San Marzano preferred)
- Mozzarella
- Olive oil
```

❌ Don’t:
```markdown
Pizza is super tasty and everyone loves it!  
It probably came from Italy, but who knows?  
Ingredients: flour, stuff, etc.
```

---

## 8. Summary
- Every dish must include **Frontmatter** + **core sections** (Intro, Origin, History, Ingredients, Method).  
- References, citations, and images are **optional but recommended**.  
- Consistency > perfection: keep it readable, verifiable, and respectful to food cultures.
