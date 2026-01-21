# /resume

Manage and export resumes to PDF and other formats.

## Usage

```
/job-search:resume list
/job-search:resume export <target> [--format pdf|html|docx]
/job-search:resume status
```

## Examples

```
/job-search:resume list
/job-search:resume export main
/job-search:resume export master-resume
/job-search:resume export stripe-senior-engineer
/job-search:resume export jobs/interested/openai-research-engineer.md
/job-search:resume export main --format docx
```

## Description

This command manages your resume portfolio and exports resumes to professional PDF format. It can export your master resume or any tailored version, automatically creating tailored resumes on demand if they don't exist.

## Subcommands

### /job-search:resume list

Display all available resumes with metadata.

**Workflow:**
1. Check for master resume at `self/resume/main-resume.md`
2. Glob `self/resume/tailored/*.md` to find all tailored versions
3. For each tailored resume, extract metadata:
   - Target company and role
   - Generation date
   - Alignment score
4. Display formatted inventory table

**Output Format:**
```
Resume Portfolio:

Master Resume:
  Path: self/resume/main-resume.md
  Last modified: {date}

Tailored Resumes:
  Company           | Title             | Score  | Date       | Path
  ------------------|-------------------|--------|------------|---------------------------
  Stripe            | Senior Engineer   | 87/100 | 2024-01-19 | self/resume/tailored/stripe-senior-engineer.md
  OpenAI            | Research Engineer | 92/100 | 2024-01-18 | self/resume/tailored/openai-research-engineer.md

Total: 1 master + {N} tailored resumes
```

---

### /job-search:resume export <target>

Export a resume to PDF (or other format).

**Arguments:**
- `<target>` - Resume identifier (required):
  - `main` or `master` - Export master resume
  - `{company}-{title}` - Export specific tailored resume
  - `jobs/{status}/{job-file}.md` - Export tailored resume for this job
- `--format` - Output format (optional, default: `pdf`):
  - `pdf` - Professional PDF via pandoc
  - `html` - Standalone HTML file
  - `docx` - Microsoft Word format

**Target Resolution:**

| Input | Resolves To |
|-------|-------------|
| `main`, `master`, `master-resume` | `self/resume/main-resume.md` |
| `stripe-senior-engineer` | `self/resume/tailored/stripe-senior-engineer.md` |
| `Stripe Senior Engineer` | `self/resume/tailored/stripe-senior-engineer.md` |
| `jobs/interested/stripe-se.md` | Find/create tailored resume for this job |

**Workflow:**

#### Step 1: Parse Arguments
- Extract target identifier
- Extract format (default: pdf)
- Validate format is supported (pdf, html, docx)

#### Step 2: Resolve Target to File Path
```
If target is "main", "master", or "master-resume":
  → Use self/resume/main-resume.md

Else if target matches a file in self/resume/tailored/:
  → Use that file directly

Else if target is a job file path (jobs/*/...):
  → Extract company-title slug
  → Look for self/resume/tailored/{slug}.md

Else:
  → Normalize to slug format (lowercase, hyphenated)
  → Search self/resume/tailored/*{slug}*.md
```

#### Step 3: Check If Resume Exists
- If file exists → proceed to Step 5
- If missing → proceed to Step 4

#### Step 4: Auto-Create Missing Tailored Resume
When a tailored resume doesn't exist:

1. Search for corresponding job file:
   ```
   Glob: jobs/*/{target-slug}*.md
   Glob: jobs/*/...{normalized-target}...
   ```

2. If job file found:
   - Display: "Creating tailored resume for {company} - {title}..."
   - Execute `/job-search:tailor-resume {job-file}` workflow inline
   - Wait for completion
   - Continue to Step 5

3. If no job file found:
   - Error: "Cannot find job posting for '{target}'"
   - Suggest: "Use /job-search:resume list to see available resumes"
   - Suggest: "Use /job-search:ingest-job to add a new job posting first"

#### Step 5: Validate Resume Content
- Read the markdown file
- Check for required sections:
  - Summary/Objective
  - Experience
  - Skills
- Warn if missing critical content but proceed

#### Step 6: Check PDF Tools
- Run: `pandoc --version`
- If pandoc available:
  - Check for LaTeX: `xelatex --version` or `pdflatex --version`
  - If LaTeX available → use xelatex engine
  - Else check: `wkhtmltopdf --version`
  - If wkhtmltopdf available → use as fallback
- If pandoc not available:
  - Error with installation instructions (see Error Handling)

#### Step 7: Generate Output
- Create exports directory: `mkdir -p self/resume/exports`
- Execute conversion based on format:

**PDF with LaTeX (best quality):**
```bash
pandoc "{input_file}" \
  -o "self/resume/exports/{output_name}.pdf" \
  --pdf-engine=xelatex \
  -V geometry:margin=0.75in \
  -V fontsize=11pt \
  -V colorlinks=true \
  -V linkcolor=blue
```

**PDF with wkhtmltopdf (fallback):**
```bash
pandoc "{input_file}" \
  -o "self/resume/exports/{output_name}.pdf" \
  --pdf-engine=wkhtmltopdf \
  -V margin-top=0.75in \
  -V margin-bottom=0.75in \
  -V margin-left=0.75in \
  -V margin-right=0.75in
```

**HTML:**
```bash
pandoc "{input_file}" \
  -o "self/resume/exports/{output_name}.html" \
  --standalone \
  --metadata title="{name} - Resume"
```

**DOCX:**
```bash
pandoc "{input_file}" \
  -o "self/resume/exports/{output_name}.docx"
```

#### Step 8: Report Results
Display:
```
Resume exported successfully!

  Source: self/resume/tailored/stripe-senior-engineer.md
  Output: self/resume/exports/stripe-senior-engineer.pdf
  Format: PDF (via pandoc + xelatex)
  Size: 145 KB

The PDF is ready for submission.
```

---

### /job-search:resume status

Show comprehensive resume portfolio status and tool availability.

**Workflow:**
1. Check master resume existence and metadata
2. Count and summarize tailored resumes
3. Check export tool availability
4. List recent exports

**Output Format:**
```
Resume Portfolio Status

Master Resume: {checkmark or X} {Present/Missing}
  Path: self/resume/main-resume.md
  Last modified: {date}
  Word count: {count}
  Sections: Summary, Experience ({count}), Skills, Projects ({count}), Education

Tailored Resumes: {count} total
  - stripe-senior-engineer.md (Score: 87/100)
  - openai-research-engineer.md (Score: 92/100)
  - anthropic-staff-engineer.md (Score: 85/100)

Export Tools:
  pandoc:     {checkmark/X} {version or "Not installed"}
  xelatex:    {checkmark/X} {version or "Not installed"}
  wkhtmltopdf:{checkmark/X} {version or "Not installed"}

Recent Exports:
  Date       | Resume              | Format | Path
  -----------|---------------------|--------|----------------------------------
  2024-01-20 | master-resume       | PDF    | self/resume/exports/master-resume.pdf
  2024-01-19 | stripe-senior-eng   | PDF    | self/resume/exports/stripe-senior-engineer.pdf

Export capability: {Ready/Limited/Unavailable}
```

---

## Error Handling

### Pandoc Not Installed

```
Error: pandoc is not installed

To install pandoc:

  macOS:   brew install pandoc
  Ubuntu:  sudo apt install pandoc
  Windows: choco install pandoc

For best PDF quality, also install LaTeX:
  macOS:   brew install --cask mactex-no-gui
  Ubuntu:  sudo apt install texlive-xetex
  Windows: choco install miktex

Alternative: Install wkhtmltopdf for PDF without LaTeX:
  macOS:   brew install wkhtmltopdf
  Ubuntu:  sudo apt install wkhtmltopdf
```

### Master Resume Not Found

```
Error: Master resume not found at self/resume/main-resume.md

To create your master resume:
1. Run /job-search:setup to initialize your profile
2. Or manually create self/resume/main-resume.md

Your master resume should include:
- Contact information
- Summary/Objective
- Work experience
- Skills
- Education
```

### Job File Not Found (for auto-creation)

```
Error: Cannot create tailored resume - no job posting found for "{target}"

To resolve:
1. Use /job-search:ingest-job to add the job posting first
2. Or use /job-search:resume list to see available resumes
3. Or specify the exact path: /job-search:resume export self/resume/tailored/{exact-name}.md
```

---

## Tools Used

- **Read**: Load resume files and job postings
- **Write**: Save exported files
- **Glob**: Find tailored resumes and job files
- **Bash**: Execute pandoc for conversion, check tool versions

## Output Locations

| Type | Location |
|------|----------|
| Master resume | `self/resume/main-resume.md` |
| Tailored resumes | `self/resume/tailored/{company}-{title}.md` |
| PDF exports | `self/resume/exports/{name}.pdf` |
| HTML exports | `self/resume/exports/{name}.html` |
| DOCX exports | `self/resume/exports/{name}.docx` |

## Integration with Other Commands

- **`/job-search:tailor-resume`**: Called automatically when exporting a tailored resume that doesn't exist
- **`/job-search:ingest-job`**: Use this first to add job postings before creating tailored resumes
- **`/job-search:setup`**: Creates initial master resume

## Best Practices

### Before Exporting
- Ensure your master resume is up-to-date
- For tailored exports, verify the job posting is ingested
- Run `/job-search:resume status` to check tool availability

### PDF Quality Tips
- Install LaTeX (xelatex) for highest quality output
- Use standard markdown formatting (headers, lists, bold)
- Avoid complex tables or images
- Keep content concise - 1-2 pages recommended

### File Naming
- Exports use the same base name as source: `stripe-senior-engineer.md` → `stripe-senior-engineer.pdf`
- Existing exports are overwritten without warning
- Timestamp can be added manually if versions needed
