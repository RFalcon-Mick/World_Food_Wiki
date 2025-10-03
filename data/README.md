# 📂 data/ Directory

The `data/` directory contains **structured metadata and indexes** that support search, validation, and consistency across the World Food Wiki.  
It acts as the **database layer** of this project.

---

## Purpose
- Provide a **machine-readable index** (`catalog.json`) for advanced search and external tools.  
- Store **controlled vocabularies** (`tags.yml`) to enforce consistent terminology.  
- Maintain **alias mappings** (`aliases.yml`) for multilingual dish names and spelling variations.  
- Serve as a foundation for **validation scripts** and **future web frontends**.  

---

## Files

### 1. `catalog.json`
- **Generated automatically** by `scripts/build_index.py`.  
- Aggregates all dish metadata from Frontmatter across the repository.  
- Example entry:
  ```json
  {
    "title": "Pizza",
    "aliases": ["Pizza", "ピッツァ", "Pitsa", "披萨"],
    "regions": ["Europe", "Italy", "Naples"],
    "periods": ["18th Century", "19th Century"],
    "techniques": ["Fermentation", "Baking"],
    "ingredients": ["Wheat Flour", "Yeast", "Tomato", "Cheese", "Olive Oil"],
    "path": "foods/Europe/Italy/Pizza.md"
  }
  ```

---

### 2. `tags.yml`
- Defines **controlled vocabulary** for metadata fields (regions, periods, techniques, categories, etc.).  
- Ensures consistency (e.g., always use `Fermentation`, not `Ferment` or `发酵`).  
- Example:
  ```yaml
  regions:
    - Europe
    - Asia
    - Middle East
    - Latin America
    - Africa
  techniques:
    - Fermentation
    - Baking
    - Steaming
    - Frying
    - Roasting
  periods:
    - Ancient
    - Medieval
    - 18th Century
    - 19th Century
    - Modern
  ```

---

### 3. `aliases.yml`
- Maps **dish names to alternative names** (translations, romanizations, local terms).  
- Prevents duplicate entries and improves search.  
- Example:
  ```yaml
  Pizza:
    - ピッツァ
    - Pitsa
    - 披萨
  Lanzhou Beef Noodles:
    - 兰州牛肉面
    - Lanzhou Lamian
  ```

---

## Optional / Future Files
- **`validation_schema.yml`** → Defines Frontmatter field requirements and types for linting scripts.  
- **`statistics.json`** → Auto-generated statistics (e.g., number of dishes per region).  
- **`search_index.json`** → Pre-built index for a static search interface.  

---

## Workflow
1. Contributors add or update dish files.  
2. Run scripts in `scripts/`:
   ```bash
   python3 scripts/lint_frontmatter.py
   python3 scripts/build_index.py
   ```
3. The scripts will validate fields, update `catalog.json`, and ensure terms match `tags.yml`.  

---

## Summary
- `catalog.json` → Machine index (auto-generated).  
- `tags.yml` → Controlled vocabulary.  
- `aliases.yml` → Name/translation mapping.  
- Additional files may be added for validation and search.  

This directory ensures that **the project is not only a wiki, but also a structured dataset** that can be searched, analyzed, and reused.
