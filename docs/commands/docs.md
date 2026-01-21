# Documentation Command

Browse plugin documentation and navigate your saved research in a web browser.

## Usage

```
/job-search:docs
/job-search:docs --port 8080
/job-search:docs --stop
/job-search:docs --build
```

## What It Does

The `/job-search:docs` command launches a web-based documentation server that lets you:

- **Browse documentation** for all commands and workflows
- **Navigate your research** (companies, jobs, career data)
- **Search everything** with full-text search
- **View a dashboard** of your job search progress

## Options

| Option | Description |
|--------|-------------|
| (none) | Start server on port 8000, open browser |
| `--port PORT` | Use a custom port |
| `--stop` | Stop the running server |
| `--build` | Build static site for offline use |

## What You'll See

### Documentation Sections

- **Getting Started** - Installation, setup, quick start
- **Commands** - Detailed reference for all commands
- **Workflows** - Step-by-step guides
- **Data Structures** - File format specifications

### My Research

- **Dashboard** - Overview of your job search progress
- **Companies** - All researched companies with scores
- **Jobs** - Application pipeline by status
- **Career** - Skill assessment and career paths

### Search

The built-in search finds content across all documentation and your research files.

## Example

```
User: /job-search:docs

Assistant: Starting documentation server...

✓ Workspace found
✓ Updated index
✓ MkDocs server started

Documentation available at: http://localhost:8000
Opening browser...
```

## Server Features

### Auto-Reload

The server watches for file changes. When you:

- Research a new company with `/job-search:find-company`
- Save a job with `/job-search:ingest-job`
- Update your profile

The documentation automatically updates.

### Research Dashboard

The dashboard shows:

- Profile summary and strength score
- Application pipeline counts
- Recent activity
- Skill gaps at a glance

## Building for Offline Use

To create a static site:

```
/job-search:docs --build
```

This generates a `site/` directory you can:

- Open directly in a browser
- Host on any web server
- Deploy to GitHub Pages

## Requirements

- MkDocs (`pip install mkdocs`)
- MkDocs Material theme (`pip install mkdocs-material`)
- Workspace initialized via `/job-search:setup`

If MkDocs is not installed, the command provides installation instructions.

## Tips

\!\!\! tip "Keep It Running"
    Leave the docs server running while you work. It auto-updates as you add research.

\!\!\! tip "Use Search"
    The search bar finds content across all docs and your research files.

## Related Commands

- [Setup](setup.md) - Initialize your workspace
- [Find Company](find-company.md) - Research companies
- [Find Job Postings](find-job-postings.md) - Search for jobs
