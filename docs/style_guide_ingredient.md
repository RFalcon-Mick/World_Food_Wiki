# Style Guide for Ingredient Entries

This document defines the **standard format** for ingredient entries in the World Food Wiki project.  
Following this structure ensures consistency across the repository, making entries easier to read, search, and validate.

---

## General Rules
1. Each ingredient is represented by **a single Markdown file**.
2. Each file **must include YAML Frontmatter** at the top with standardized metadata.
3. All text should be written in **clear, neutral, and factual language**.
4. **Headings must follow the order below** (some sections are optional, but recommended).
5. References and citations are **optional** for ingredient entries.

---

## File Naming
- Use the **English common name** in lowercase with underscores for spaces.  
  Example:  
  ```
  garlic.md
  soy_sauce.md
  black_pepper.md
  ```

---

## YAML Frontmatter Fields
Each ingredient entry should begin with YAML frontmatter:

```yaml
---
title: Garlic
aliases:
  - Allium sativum
  - 蒜
  - Ail
  - Ajo
regions:
  - Middle East
  - Asia
  - Mediterranean
periods:
  - Ancient
categories:
  - Ingredient
origin_summary: Cultivated in Central Asia and northeastern Iran; spread globally as a flavoring and medicinal herb.
license: CC BY-SA 4.0
---
```

### Required Fields
- **title**: Standard English name.  
- **categories**: Must include `Ingredient`.  
- **origin_summary**: One-sentence summary of historical/geographic origin.  
- **license**: License for the text.

### Optional but Recommended Fields
- **aliases**: Common synonyms, scientific names, or translations.  
- **regions**: Associated regions of origin or widespread use.  
- **periods**: Time periods of documented usage (e.g., Ancient, Medieval, Modern).

---

## Recommended Sections in the Body

### 1. Introduction
- A short description of the ingredient, its general role in food, and any notable features.

### 2. Place of Origin
- The geographic region where the ingredient was first domesticated, discovered, or widely used.

### 3. Time of Emergence
- Approximate date or historical period when the ingredient entered human use.

### 4. Origins
- Information about the early domestication or discovery process.

### 5. Historical Development
- Key stages in the global spread and historical uses of the ingredient.

### 6. Culinary Uses
- Typical ways the ingredient is used in cooking.  
- Mention both **traditional uses** and **modern adaptations**.

### 7. Cultural Significance (Optional)
- Ritual, symbolic, or folkloric meanings associated with the ingredient.  

### 8. Nutritional Information (Optional)
- Key nutrients, beneficial compounds, or health effects.

---

## Sections to Omit
- **References** and **Citations** are **optional** in ingredient entries.  
  If included, follow the general style guide.

---

## Example Structure

```markdown
---
title: Garlic
aliases:
  - Allium sativum
  - 蒜
regions:
  - Asia
  - Middle East
categories:
  - Ingredient
origin_summary: Cultivated in Central Asia and northeastern Iran; spread globally as a flavoring and medicinal herb.
license: CC BY-SA 4.0
---

# Garlic

## Introduction
...

## Place of Origin
...

## Time of Emergence
...

## Origins
...

## Historical Development
...

## Culinary Uses
...

## Cultural Significance
...

## Nutritional Information
...
```

---

## Summary
Ingredient entries should:
- Start with YAML Frontmatter including **title**, **categories**, **origin_summary**, and **license**.  
- Follow a **consistent section order** for readability.  
- Avoid redundant references unless necessary.  
- Emphasize **origin, history, uses, and cultural context** over cooking instructions.
