# THESIS - Lunarety v2 Documentation

This directory contains documentation assets for the Lunarety v2 thesis project.

## Directory Structure

```
THESIS/
├── erd/                      # Entity Relationship Diagrams
│   └── data_model.mmd        # Mermaid source file
├── images/                   # Static images for documentation
├── presentation_assets/      # GIFs and videos for presentations
├── count_loc.py              # Lines of Code counter script
├── thesis.md                 # Thesis markdown source
├── thesis extended.md        # Thesis markdown source with extended content
└── thesis.docx               # Thesis Word document
```

---

## Scripts

### Count Lines of Code

The `count_loc.py` script counts lines of code across the `lunarety-v2` and `lunarety-v2-website` projects, excluding auto-generated files and dependencies.

#### Usage

```bash
# Navigate to the THESIS directory
cd THESIS

# Run the script
python count_loc.py
```

#### What it excludes:

- **Directories:** `node_modules`, `.next`, `.git`, `.vscode`, `.idea`, `dist`, `build`, `coverage`, `.pnpm-store`, `media`, `public`, `.cursor`, `generated`, `swagger`
- **Files:** `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `payload-types.ts`, `next-env.d.ts`, `tsconfig.tsbuildinfo`, `.DS_Store`, `Api.ts`

#### Supported extensions:

`.ts`, `.tsx`, `.js`, `.jsx`, `.css`, `.scss`, `.py`, `.html`, `.json`

---

## Generate ERD PNG from Mermaid

The ERD diagram source is located at `erd/data_model.mmd`. To generate a PNG image, use the Mermaid CLI tool.

### Installation

```bash
# Install mermaid-cli globally
npm install -g @mermaid-js/mermaid-cli
```

### Generate PNG

```bash
# Navigate to the THESIS directory
cd THESIS

# Generate PNG from the .mmd file
mmdc -i erd/data_model.mmd -o images/data_model_erd.png -b transparent -t dark

# Or with a white background
mmdc -i erd/data_model.mmd -o images/data_model_erd.png -b white

# Or with custom width for better readability
mmdc -i erd/data_model.mmd -o images/data_model_erd.png -w 2000 -b white
```

### CLI Options

| Option | Description                                     |
| ------ | ----------------------------------------------- |
| `-i`   | Input file (`.mmd` or `.md`)                    |
| `-o`   | Output file (`.png`, `.svg`, `.pdf`)            |
| `-b`   | Background color (`transparent`, `white`, etc.) |
| `-t`   | Theme (`default`, `dark`, `forest`, `neutral`)  |
| `-w`   | Width in pixels                                 |
| `-H`   | Height in pixels                                |

### Alternative: Using Docker

If you prefer not to install globally:

```bash
docker run --rm -v "$(pwd):/data" minlag/mermaid-cli \
  -i /data/erd/data_model.mmd \
  -o /data/images/data_model_erd.png \
  -b white
```

### Alternative: Online Tools

You can also use online tools to convert Mermaid to PNG:

- [Mermaid Live Editor](https://mermaid.live/) - Paste the `.mmd` content and export
- [Kroki](https://kroki.io/) - API-based diagram generation

---

## Generate DOCX from Markdown

Use [Pandoc](https://pandoc.org/) to convert the thesis markdown to a Word document.

### Installation

```bash
# macOS (Homebrew)
brew install pandoc

# Ubuntu/Debian
sudo apt install pandoc

# Windows (Chocolatey)
choco install pandoc
```

### Generate DOCX

```bash
# Navigate to the THESIS directory
cd THESIS

# Basic conversion
pandoc "thesis extended.md" -o "thesis extended.docx"

# With table of contents
pandoc "thesis extended.md" -o "thesis extended.docx" --toc

# With custom reference document (for styling)
pandoc "thesis extended.md" -o "thesis extended.docx" --toc --reference-doc=reference.docx

# Full command with common options
pandoc "thesis extended.md" \
  -o "thesis extended.docx" \
  --toc \
  --toc-depth=3 \
  --standalone \
  --resource-path=. \
  --extract-media=media_output
```

### Pandoc Options

| Option            | Description                          |
| ----------------- | ------------------------------------ |
| `-o`              | Output file                          |
| `--toc`           | Generate table of contents           |
| `--toc-depth=N`   | TOC depth (default: 3)               |
| `--standalone`    | Produce standalone document          |
| `--reference-doc` | Use custom Word template for styling |
| `--resource-path` | Path to search for images            |
| `--extract-media` | Extract media files to directory     |

### Using a Custom Template

For consistent styling, create a `reference.docx` template:

1. Generate a default reference: `pandoc -o reference.docx --print-default-data-file reference.docx`
2. Open `reference.docx` in Word and modify styles (headings, fonts, margins)
3. Save and use with `--reference-doc=reference.docx`

---

## Quick Reference

```bash
# Count lines of code
python count_loc.py

# Generate ERD diagram
mmdc -i erd/data_model.mmd -o erd/data_model_erd.png -w 2000 -b white

# Generate DOCX from thesis
pandoc "thesis extended.md" -o "thesis extended.docx" --toc --toc-depth=3
```
