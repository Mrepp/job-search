# Job Search Assistant

A comprehensive Claude Code plugin to assist users in finding their ideal job through intelligent research, analysis, and career planning.

## Features

- **Personal Analysis**: Build and maintain your professional profile
- **Company Research**: Deep-dive into companies matching your criteria
- **Position Discovery**: Identify roles aligned with your skills and goals
- **Job Matching**: Find and score job postings against your profile
- **Career Planning**: Map progression paths and identify skill gaps
- **Resume Tailoring**: Generate targeted resumes for specific positions

## Installation

### From Marketplace (Recommended)

Install directly from the marketplace:

```shell
# Add the marketplace (one-time)
/plugin marketplace add Mrepp/job-search

# Install the plugin
/plugin install job-search@mrepp-plugins
```

### Manual Installation

For development or if you prefer manual installation:

```bash
git clone https://github.com/Mrepp/job-search ~/.claude/plugins/job-search
```

## Commands

| Command | Description |
|---------|-------------|
| `/job-search:setup` | Initialize workspace and create quick profile from resume |
| `/job-search:docs` | Browse documentation and research in web browser |
| `/job-search:personal-analysis` | Build and maintain your user profile |
| `/job-search:find-company [criteria]` | Research companies by area, industry, culture |
| `/job-search:find-position [role]` | Identify career positions for your skills |
| `/job-search:find-job-postings [role] [location]` | Discover ranked job postings |
| `/job-search:ingest-job [url or paste]` | Add a job posting for analysis |
| `/job-search:update-job-status [job] [status]` | Move jobs through the application pipeline |
| `/job-search:skill-builder` | Map skills, identify gaps, create improvement plans |
| `/job-search:tailor-resume [job-file]` | Generate a tailored resume for a job |
| `/job-search:resume` | Manage and export resumes to PDF and other formats |

## Data Structure

The plugin stores all data in your working directory:

```
{working-directory}/
├── self/
│   ├── user.json              # Your profile
│   ├── resume/
│   │   ├── main-resume.md     # Primary resume
│   │   ├── tailored/          # Job-specific versions
│   │   └── exports/           # PDF/HTML/DOCX exports
│   ├── projects/              # Project descriptions
│   ├── education/             # Education history
│   ├── experience/            # Work experience
│   └── linkedin/              # LinkedIn profile
├── companies/
│   └── {company-name}.md      # Company research
├── jobs/
│   ├── interested/            # Initial saves
│   ├── applied/               # Submitted applications
│   ├── interviewed/           # In interview process
│   ├── offered/               # Received offers
│   └── rejected/              # Declined/rejected
└── career/
    ├── career-tree.json       # Career progression map
    └── skill-map.json         # Skill inventory
```

### Verify Installation

Restart Claude Code or start a new session. Run:

```shell
/job-search:setup
```

If the command is recognized, the plugin is installed correctly.

### Prerequisites

- [Claude Code CLI](https://github.com/anthropics/claude-code) installed and configured

## Getting Started

1. Run `/job-search:setup` to initialize your workspace and create your profile
2. Run `/job-search:docs` to browse documentation in your browser
3. Use `/job-search:find-company` or `/job-search:find-job-postings` to discover opportunities
4. Use `/job-search:ingest-job` to add specific postings you find
5. Track applications with `/job-search:update-job-status`
6. Build skills with `/job-search:skill-builder`

## Application Pipeline

Jobs move through these statuses:
- **interested** → Initial save
- **applied** → Application submitted
- **interviewed** → In interview process
- **offered** → Received offer
- **rejected** → Declined or rejected

## Skill Confidence Scoring

Skills are rated on a 1-3 scale:
- **1**: Basic familiarity
- **2**: Working proficiency
- **3**: Expert level

The system suggests scores based on your resume and experience; you can adjust them.
