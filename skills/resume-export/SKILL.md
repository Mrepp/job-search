# Resume Export

Knowledge module for exporting resumes to professional formats (PDF, HTML, DOCX).

## PDF Generation Best Practices

### Tool Chain Recommendations

**Tier 1: Pandoc + LaTeX (Highest Quality)**
- Produces professional typeset PDFs
- Best font handling and typography
- Supports custom templates
- Installation: `brew install pandoc && brew install --cask mactex-no-gui`

**Tier 2: Pandoc + wkhtmltopdf (Good Quality, Simpler Setup)**
- HTML-based PDF generation
- CSS styling support
- No LaTeX dependency
- Installation: `brew install pandoc wkhtmltopdf`

**Tier 3: WeasyPrint (Python-based)**
- Pure Python solution
- CSS-based styling
- Good for programmatic generation
- Installation: `pip install weasyprint`

### Pandoc Command Reference

**Basic PDF (with LaTeX):**
```bash
pandoc input.md -o output.pdf --pdf-engine=xelatex
```

**PDF with formatting options:**
```bash
pandoc input.md -o output.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=0.75in \
  -V fontsize=11pt \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V documentclass=article
```

**PDF with custom font (requires xelatex):**
```bash
pandoc input.md -o output.pdf \
  --pdf-engine=xelatex \
  -V mainfont="Helvetica Neue" \
  -V geometry:margin=0.75in
```

**PDF via wkhtmltopdf:**
```bash
pandoc input.md -o output.pdf \
  --pdf-engine=wkhtmltopdf \
  -V margin-top=20mm \
  -V margin-bottom=20mm \
  -V margin-left=20mm \
  -V margin-right=20mm
```

**HTML export:**
```bash
pandoc input.md -o output.html --standalone --metadata title="Resume"
```

**DOCX export:**
```bash
pandoc input.md -o output.docx
```

## Resume Formatting Guidelines

### Markdown Structure for Best PDF Output

**Recommended Structure:**
```markdown
# Your Name

contact@email.com | (555) 123-4567 | City, State | linkedin.com/in/yourname

## Summary

Brief professional summary in 2-3 sentences...

## Experience

### Job Title
**Company Name** | City, State | Start Date - End Date

- Achievement with quantified impact
- Another achievement with metrics
- Technical accomplishment demonstrating skills

### Previous Role
**Previous Company** | City, State | Start Date - End Date

- Achievement bullet
- Another bullet

## Skills

### Technical Skills
Python, JavaScript, TypeScript, React, Node.js, PostgreSQL, AWS, Docker, Kubernetes

### Tools & Frameworks
Git, GitHub Actions, Terraform, DataDog, Grafana

## Education

### Degree Name
**University Name** | Graduation Year

## Projects (Optional)

### Project Name
Brief description with technologies used and impact
```

### Formatting Tips

**DO:**
- Use `#` for your name (h1), `##` for sections (h2), `###` for job titles (h3)
- Use `**bold**` for company names
- Use `-` for bullet points (consistent)
- Keep bullets concise (1-2 lines)
- Include quantified achievements where possible
- Use standard section names (Summary, Experience, Skills, Education)

**DON'T:**
- Use tables (render poorly in PDF)
- Include images or logos
- Use complex nested lists
- Use HTML tags in markdown
- Use colored text or custom styling (won't translate to PDF)

### Length Guidelines

| Career Level | Recommended Length |
|--------------|-------------------|
| Entry-level (0-3 years) | 1 page |
| Mid-level (3-7 years) | 1-2 pages |
| Senior (7+ years) | 2 pages max |
| Executive | 2 pages max |

### ATS Compatibility

For Applicant Tracking System compatibility:

1. **Use standard section headers**: "Experience", "Skills", "Education" (not creative alternatives)
2. **Avoid graphics/icons**: ATS can't parse visual elements
3. **Include keywords**: Match terminology from job descriptions
4. **Use standard fonts**: Helvetica, Arial, Times New Roman, Calibri
5. **Simple formatting**: Avoid columns, text boxes, headers/footers

## Export Format Selection

### When to Use PDF
- Final submission to job applications
- Sending to recruiters
- Printing for interviews
- Archival purposes

### When to Use HTML
- Online portfolio/website
- Email body (some clients)
- Quick preview
- Further customization with CSS

### When to Use DOCX
- When specifically requested
- For collaborative editing
- When recruiter needs to add cover sheet
- Legacy systems requiring Word format

## Troubleshooting

### "LaTeX not found" Error
```
Install LaTeX for best PDF quality:
  macOS:   brew install --cask mactex-no-gui
  Ubuntu:  sudo apt install texlive-xetex
  Windows: choco install miktex

Or use wkhtmltopdf as alternative:
  macOS:   brew install wkhtmltopdf
```

### "wkhtmltopdf not found" Error
```
Install wkhtmltopdf:
  macOS:   brew install wkhtmltopdf
  Ubuntu:  sudo apt install wkhtmltopdf
  Windows: choco install wkhtmltopdf
```

### PDF looks wrong
1. Check for complex markdown (tables, nested lists)
2. Simplify formatting
3. Try different PDF engine
4. Check font availability

### Unicode/Special Characters Issues
- Use `--pdf-engine=xelatex` (better Unicode support than pdflatex)
- Ensure system has required fonts installed
- Avoid unusual symbols in text

## Quality Checklist

Before exporting, verify:

- [ ] Contact information is current
- [ ] No typos or grammatical errors
- [ ] Dates are consistent format (Month Year or MM/YYYY)
- [ ] Company names and titles are accurate
- [ ] Skills section reflects current abilities
- [ ] Achievements are quantified where possible
- [ ] Content fits target length (1-2 pages)
- [ ] Section order emphasizes strengths
- [ ] No sensitive information included (SSN, full address, etc.)
