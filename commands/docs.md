# /docs

Browse plugin documentation and navigate your saved research using a web-based interface.

## Usage

```
/job-search:docs
/job-search:docs --port 8080
/job-search:docs --stop
/job-search:docs --build
```

## Description

This command launches a web-based documentation server using MkDocs that allows you to:

1. Browse plugin documentation (commands, workflows, data structures)
2. Navigate your local research (companies, jobs, career data)
3. Search across all saved content
4. View a dashboard of your job search progress

The documentation is served at `http://localhost:8000` by default and opens automatically in your browser.

## Options

| Option | Description |
|--------|-------------|
| (none) | Start server on default port 8000, open browser |
| `--port PORT` | Use a custom port number |
| `--stop` | Stop the running documentation server |
| `--build` | Build a static site for offline viewing |

## Workflow

### Step 1: Check Prerequisites

1. Verify workspace exists (`.job-search-config.json` found)
   - If not found, prompt user to run `/job-search:setup` first

2. Check if MkDocs is available
   - If not installed, provide installation instructions

### Step 2: Update Research Index

Before starting the server, scan and update the workspace index:

1. Scan directories:
   - `companies/` - count and list company research files
   - `jobs/interested/`, `jobs/applied/`, etc. - count jobs by status
   - `career/` - check for skill-map.json and career-tree.json
   - `self/` - read profile summary from user.json

2. Update `index.json`:
   - Refresh counts and file listings
   - Update `last_updated` timestamp
   - Report any new or changed files since last update

### Step 3: Generate Dynamic Research Pages

Generate markdown files in `docs/research/` that provide navigation for user data:

**`docs/research/dashboard.md`**
```markdown
# Job Search Dashboard

## Profile Summary
- **Name**: {name}
- **Current Title**: {current_title}
- **Skills Mapped**: {skill_count}
- **Profile Strength**: {calculated_score}/100

## Application Pipeline

| Status | Count | Most Recent |
|--------|-------|-------------|
| Interested | {n} | {latest_job} |
| Applied | {n} | {latest_job} - {days} days ago |
| Interviewed | {n} | {latest_job} |
| Offered | {n} | - |
| Rejected | {n} | - |

## Companies Researched
{count} companies analyzed. [View all →](companies/index.md)

| Company | Relevance | Industry |
|---------|-----------|----------|
| {top companies by relevance} |

## Skill Gaps
**P0 (Critical)**: {list}
**P1 (Important)**: {list}

[View skill details →](career/skills.md)
```

**`docs/research/companies/index.md`**
```markdown
# Researched Companies

| Company | Relevance Score | Industry | Last Updated |
|---------|-----------------|----------|--------------|
| [Stripe](stripe.md) | 92/100 | Fintech | Jan 20, 2024 |
| [Anthropic](anthropic.md) | 90/100 | AI/ML | Jan 18, 2024 |
...

## Add New Company
Run `/job-search:find-company [name]` to research a new company.
```

**`docs/research/jobs/pipeline.md`**
```markdown
# Job Application Pipeline

## Interested ({count})
Jobs you're considering applying to.

| Job | Company | Match Score | Added |
|-----|---------|-------------|-------|
| [Senior Engineer](interested/stripe-senior.md) | Stripe | 92% | Jan 20 |
...

## Applied ({count})
Applications submitted and awaiting response.

| Job | Company | Match Score | Applied | Days |
|-----|---------|-------------|---------|------|
| [Software Engineer](applied/anthropic-swe.md) | Anthropic | 90% | Jan 13 | 7 |
...

## Interviewed ({count})
Currently in interview process.

## Offered ({count})
Received offers.

## Rejected ({count})
Declined or rejected applications.

## Update Status
Run `/job-search:update-job-status [job] [status]` to move jobs through the pipeline.
```

**`docs/research/career/skills.md`**
```markdown
# Skill Assessment

## Your Skills

### Technical Skills
| Skill | Confidence | Years | Evidence |
|-------|------------|-------|----------|
| Python | 3 (Expert) | 8 | Lead projects, certifications |
| AWS | 2 (Proficient) | 4 | Multiple roles |
...

### Soft Skills
| Skill | Confidence | Evidence |
|-------|------------|----------|
| Team Leadership | 3 (Expert) | 5+ years managing |
...

## Skill Gaps

### P0 - Critical (Required in >80% of target jobs)
- **Kubernetes**: 0 → Target: 2
  - Resources: [Official docs](https://kubernetes.io/docs/)
  - Estimated time: 2-3 months

### P1 - Important (Required in 50-80% of target jobs)
- **System Design**: 1 → Target: 3
  - Resources: "Designing Data-Intensive Applications"

## Build Skills
Run `/job-search:skill-builder [skill]` to create a learning plan.
```

### Step 4: Generate Workspace mkdocs.yml

Create/update `mkdocs.yml` in the workspace root with dynamic navigation:

```yaml
site_name: Job Search - {User Name}
docs_dir: docs

nav:
  - Home: index.md

  # Plugin Documentation
  - Getting Started:
    - Installation: getting-started/installation.md
    - Initial Setup: getting-started/setup.md
    - Quick Start: getting-started/quick-start.md
    - Profile Setup: getting-started/profile-setup.md
  - Commands:
    - Setup: commands/setup.md
    - Documentation: commands/docs.md
    - Personal Analysis: commands/personal-analysis.md
    - Find Company: commands/find-company.md
    - Find Position: commands/find-position.md
    - Find Job Postings: commands/find-job-postings.md
    - Ingest Job: commands/ingest-job.md
    - Update Job Status: commands/update-job-status.md
    - Skill Builder: commands/skill-builder.md
    - Tailor Resume: commands/tailor-resume.md
  - Workflows:
    - Complete Job Search: workflows/complete-search.md
    - Career Planning: workflows/career-planning.md
    - Skill Development: workflows/skill-development.md
  - Data Structures:
    - User Profile: data-structures/user-profile.md
    - Company Files: data-structures/company-files.md
    - Job Files: data-structures/job-files.md

  # User Research (dynamically generated)
  - My Research:
    - Dashboard: research/dashboard.md
    - Companies:
      - Overview: research/companies/index.md
      # Individual company files linked here
    - Jobs:
      - Pipeline: research/jobs/pipeline.md
      - Interested: research/jobs/interested.md
      - Applied: research/jobs/applied.md
      - Interviewed: research/jobs/interviewed.md
    - Career:
      - Skill Map: research/career/skills.md
      - Career Paths: research/career/paths.md

theme:
  name: material
  features:
    - navigation.sections
    - navigation.expand
    - search.suggest
    - content.code.copy
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - tables
  - toc:
      permalink: true

plugins:
  - search
```

### Step 5: Link Research Files

Create symlinks (Unix) or copies of research files into the docs structure:

```
docs/research/companies/stripe.md → ../../../companies/stripe.md
docs/research/companies/anthropic.md → ../../../companies/anthropic.md
docs/research/jobs/interested/*.md → ../../../jobs/interested/*.md
docs/research/jobs/applied/*.md → ../../../jobs/applied/*.md
```

This allows MkDocs to serve the actual research files within the documentation navigation.

### Step 6: Start MkDocs Server

```bash
cd {workspace}
mkdocs serve --dev-addr localhost:8000
```

Then open `http://localhost:8000` in the default browser.

### Step 7: Display Status

```
Documentation server started at: http://localhost:8000

Your workspace contains:
- 5 company research files
- 8 tracked jobs (3 interested, 2 applied, 1 interviewed)
- 15 mapped skills with 2 P0 gaps

The server will auto-reload when files change.
Run `/job-search:docs --stop` to stop the server.
```

## Navigation Structure

Once running, the documentation provides:

### Plugin Documentation
- **Getting Started**: Installation, setup, quick start guides
- **Commands**: Detailed reference for all 10 commands
- **Workflows**: Step-by-step guides for common tasks
- **Data Structures**: File format specifications

### My Research
- **Dashboard**: Overview of your job search progress
- **Companies**: All researched companies with relevance scores
- **Jobs**: Application pipeline with status tracking
- **Career**: Skill assessment and career path planning

### Search
MkDocs provides full-text search across all documentation and research files.

## Build Static Site

To build a static site for offline viewing or hosting:

```
/job-search:docs --build
```

This generates a `site/` directory that can be:
- Opened directly in a browser (`file://`)
- Hosted on any static web server
- Deployed to GitHub Pages

## Example Session

```
User: /job-search:docs

Assistant: Starting documentation server...

✓ Workspace found: /Users/john/job-search
✓ Updated index (2 new files since last access)
✓ Generated research pages
✓ MkDocs server started

Documentation available at: http://localhost:8000

Your workspace contains:
- 5 company research files
- 8 tracked jobs (3 interested, 2 applied, 1 interviewed, 2 rejected)
- 15 mapped skills with 2 P0 gaps

Opening browser...

The server will auto-reload when files change.
Run `/job-search:docs --stop` to stop the server.
```

## Stopping the Server

```
User: /job-search:docs --stop

Assistant: Documentation server stopped.
```

## Building Static Site

```
User: /job-search:docs --build

Assistant: Building static documentation site...

✓ Generated research pages
✓ Built site to /Users/john/job-search/site/

To view offline:
1. Open site/index.html in your browser
2. Or run: python -m http.server -d site 8000

To deploy:
- Copy the site/ directory to any static web host
- Or push to GitHub Pages
```

## Requirements

- MkDocs installed (`pip install mkdocs`)
- MkDocs Material theme (`pip install mkdocs-material`)
- Workspace initialized via `/job-search:setup`

If MkDocs is not installed, the command will provide installation instructions.
