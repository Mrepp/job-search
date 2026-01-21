# /resume

Manage and export resumes to PDF and other formats.

## Quick Start

```bash
# List all your resumes
/job-search:resume list

# Export your master resume to PDF
/job-search:resume export main

# Export a tailored resume (auto-creates if needed)
/job-search:resume export stripe-senior-engineer
```

## Usage

```
/job-search:resume list                              # List all available resumes
/job-search:resume export <target> [--format pdf]    # Export to PDF (default)
/job-search:resume status                            # Show portfolio status
```

## Subcommands

### list

Shows all available resumes in your portfolio.

```
/job-search:resume list
```

Output includes:
- Master resume location and last modified date
- All tailored resumes with company, title, alignment score, and date

### export

Exports a resume to PDF (default) or other formats.

```
/job-search:resume export <target> [--format pdf|html|docx]
```

**Target options:**
- `main` or `master` - Your master resume
- `{company}-{title}` - A tailored resume (e.g., `stripe-senior-engineer`)
- `jobs/interested/{job}.md` - Tailored resume for a specific job file

**Format options:**
- `pdf` (default) - Professional PDF via pandoc
- `html` - Standalone HTML file
- `docx` - Microsoft Word format

**Auto-creation:** If a tailored resume doesn't exist but the job file does, it will automatically be created using `/job-search:tailor-resume`.

### status

Shows comprehensive portfolio status including tool availability.

```
/job-search:resume status
```

## Examples

```bash
# Export master resume
/job-search:resume export main
/job-search:resume export master

# Export tailored resumes
/job-search:resume export stripe-senior-engineer
/job-search:resume export openai-research-engineer

# Export in different formats
/job-search:resume export main --format html
/job-search:resume export main --format docx

# Export for a specific job (auto-creates tailored version)
/job-search:resume export jobs/interested/anthropic-staff-engineer.md
```

## Requirements

### PDF Export

For PDF export, you need **pandoc** installed:

```bash
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt install pandoc

# Windows
choco install pandoc
```

For best quality, also install LaTeX:

```bash
# macOS
brew install --cask mactex-no-gui

# Ubuntu/Debian
sudo apt install texlive-xetex

# Windows
choco install miktex
```

**Alternative:** If you can't install LaTeX, install wkhtmltopdf:

```bash
# macOS
brew install wkhtmltopdf
```

## Output Locations

| Type | Location |
|------|----------|
| PDF exports | `self/resume/exports/{name}.pdf` |
| HTML exports | `self/resume/exports/{name}.html` |
| DOCX exports | `self/resume/exports/{name}.docx` |

## Tips

1. **Check tools first:** Run `/job-search:resume status` to verify pandoc is installed
2. **Keep master updated:** Your master resume should always be current
3. **Use tailored versions:** Always export job-specific tailored resumes for applications
4. **Review before sending:** Open the PDF to verify formatting looks correct

## Related Commands

- [`/job-search:tailor-resume`](tailor-resume.md) - Create tailored resume for a job posting
- [`/job-search:setup`](setup.md) - Initialize profile including master resume
- [`/job-search:ingest-job`](ingest-job.md) - Add job postings for tailored resumes
