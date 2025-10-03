# 🌐 World Food Wiki

> A structured, open-source knowledge base of global dishes, ingredients, and cooking techniques — built for easy search, collaboration, and cultural exchange.

<p align="center">
  <img src="https://img.shields.io/badge/license-CC%20BY--SA%204.0-lightgrey" />
  <img src="https://img.shields.io/badge/status-beta-yellow" />
  <img src="https://img.shields.io/badge/contribute-welcome-brightgreen" />
</p>

---

## 🔍 What Is This

World Food Wiki is an attempt to unify **history + culinary practice** in one place:

- Describe each dish’s **origin, evolution, cultural context**  
- Provide **ingredients and cooking method(s)**  
- Organize knowledge in a structured, searchable way  
- Leverage metadata and indexing (in `data/`) to enable richer explorations  

It’s designed not just as a “cookbook,” but as a **food knowledge graph** with narrative depth.

---

## 📁 Repository Structure

Here’s a map of the major directories and their roles:

| Directory / File | Purpose |
|------------------|---------|
| `foods/` | Contains dish entries as individual Markdown files, following the style guide |
| `ingredients/` | Articles about raw materials, their history, use, etc. |
| `techniques/` | Cooking techniques (e.g. fermentation, roasting) explained |
| `glossary/` | Terminology and definitions important to the project |
| `data/` | Metadata, indexes, controlled vocabularies (e.g. `catalog.json`, `tags.yml`) |
| `docs/` | Project-level documentation: style guide, citation guide, taxonomy, etc. |
| `scripts/` | Tools for building indices, validating frontmatter, linking checks |
| `LICENSE` | Project license (CC BY‑SA 4.0) |

---

## 📖 How to Use / Explore

### A. Browsing

- The **foods folder** is your human-facing entry point. Browse by continent / country or filename.  
- Use `ingredients/` or `techniques/` to dive into background knowledge.

### B. Search & Filtering

- The `data/catalog.json` file is a machine-readable catalog of all dish entries.  
- Use metadata fields (regions, periods, techniques, ingredients) to filter or build custom queries (e.g. via `jq`, Python).  
- Controlled vocabulary in `data/tags.yml` ensures consistency in those fields.

### C. Local Tools

Before making or updating entries, run these checks:

```bash
python3 scripts/lint_frontmatter.py     # Validate metadata schema
python3 scripts/check_links.py          # Verify internal & external links
python3 scripts/build_index.py          # Regenerate catalog.json
```

---

## 📄 Entry Format

Each dish or topic is stored as a **single Markdown file** (not folder), located under `foods/` (or `ingredients/`, `techniques/`).  
The file should follow the **style guide** and include:

1. YAML frontmatter (title, aliases, regions, periods, techniques, categories, ingredients, origin_summary, license)  
2. Sections in order:

   - Introduction  
   - Place of Origin  
   - Time of Emergence  
   - Origins  
   - Historical Development  
   - Ingredients  
   - Cooking Method  
   - **References** (optional)  
   - **Citations** (optional)

Images, if any, go into a companion `gallery/` folder or hosting path, with attribution and license.

---

## 🛠️ Contributing

We’d love your help in building this knowledge base. Suggested workflow:

1. Fork and clone the repo  
2. Copy the template / follow `docs/style_guide.md` & `docs/citation_guide.md`  
3. Create or update a dish file (e.g. `foods/Asia/China/MapoTofu.md`)  
4. Run the validation and indexing scripts  
5. Submit a Pull Request and reference your source material  

Be well-cited when possible. If no references are available, honest acknowledgment is fine (you may omit references section).

See `docs/CONTRIBUTING.md` (or you can add one) for deeper guidelines.

---

## 🚧 Roadmap

Some planned enhancements:

- Web interface / static site generation (leveraging `data/catalog.json`)  
- Search UI with faceted filters (by region, technique, period)  
- Multilingual support & translation of entries  
- More robust validation, typo-catching, and link integrity  
- Seed more entries across underrepresented cuisines

---

## 📜 License & Attribution

This project is licensed under **Creative Commons Attribution‑ShareAlike 4.0 (CC BY‑SA 4.0)**.  
When using or adapting content, please provide proper attribution and share under the same or compatible license.

---

## 🤝 Acknowledgments

- Inspired by the structural clarity of **HowToCook** and other community-driven food history projects  
- Thanks to contributors who bring depth, local knowledge, and passion into each dish’s story  
