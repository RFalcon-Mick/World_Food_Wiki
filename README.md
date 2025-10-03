# 🌍 World Food Wiki

> A collaborative encyclopedia of world food, emphasizing **history, migration, and cultural context**, while also providing **authentic recipes and cooking methods**.

---

## 📖 Vision
- Explore the **origins and evolution** of dishes from different cultures and time periods.  
- Present **well-documented recipes** alongside their historical narratives.  
- Provide a **structured, searchable knowledge base** for researchers, food lovers, and home cooks.  

---

## 📂 Repository Structure
```
world-food-wiki/
├─ foods/          # Dishes organized by Continent → Country → Dish
├─ ingredients/    # Ingredients and their histories
├─ techniques/     # Cooking techniques across cultures
├─ collections/    # Thematic collections (festivals, street food, etc.)
├─ timelines/      # Historical timelines of major ingredients/dishes
├─ glossary/       # Terminology and definitions
├─ docs/           # Style guide, taxonomy, citation rules
├─ data/           # Machine-readable index and controlled vocabulary
├─ scripts/        # Build tools and validation scripts
└─ README.md
```

---

## 🔍 How to Search

### A. GitHub Search
Use GitHub's built-in search with filters:
- Search by **dish name or alias**:  
  `repo:<your-repo> "Pizza" OR "披萨" path:/foods/`
- Search by **region**:  
  `repo:<your-repo> path:/foods/Europe/Italy/`
- Search by **technique** (from Frontmatter):  
  `repo:<your-repo> "techniques:Fermentation"`

### B. Structured Index
- `data/catalog.json`: Machine-readable index of all entries.  
- `data/tags.yml`: Controlled vocabulary for regions, periods, and techniques.  
- `docs/taxonomy.md`: Explanation of categories and tags.  

### C. Advanced Local Search
Build your own advanced queries:
```bash
python3 scripts/build_index.py
cat data/catalog.json | jq '.items[] | select(.regions[] | contains("Mediterranean"))'
```

---

## 📝 Entry Structure
Each dish folder contains:
```
foods/Continent/Country/Dish/
├─ README.md     # Overview (summary + history snapshot + recipe links)
├─ history.md    # Detailed historical timeline
├─ recipe.md     # One or more authentic recipes
├─ references.md # Citations and sources
├─ gallery/      # Images (with proper license)
```

Example: [`foods/europe/italy/pizza`](foods/Europe/Italy/Pizza)

---

## 📑 Frontmatter Standard
All entries start with a YAML block:
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
  Developed in Naples in the 18th–19th centuries, influenced by wheat culture,
  New World tomatoes, and high-temperature ovens.
license: CC BY-SA 4.0
---
```

---

## 🤝 Contributing
We welcome contributions! Please:
1. Follow the [style guide](docs/style-guide.md) and [citation rules](docs/citation-guide.md).  
2. Provide reliable **sources and references** in `references.md`.  
3. Run validation scripts before submitting:
   ```bash
   python3 scripts/lint_frontmatter.py
   python3 scripts/check_links.py
   python3 scripts/build_index.py
   ```
4. Submit a Pull Request with the appropriate template.  

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📚 License
- Text is licensed under **CC BY-SA 4.0**.  
- Images must be copyright-compliant (CC, public domain, or self-made).  

---



## 🙏 Acknowledgements 
- Thanks to all contributors documenting the intertwined history of food and humanity.
