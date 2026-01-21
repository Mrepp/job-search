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

1. Clone or copy this plugin to your Claude Code plugins directory
2. The plugin will be automatically loaded when you start Claude Code

## Commands

| Command | Description |
|---------|-------------|
| `/personal-analysis` | Build and maintain your user profile |
| `/find-company [criteria]` | Research companies by area, industry, culture |
| `/find-position [role]` | Identify career positions for your skills |
| `/find-job-postings [role] [location]` | Discover ranked job postings |
| `/ingest-job [url or paste]` | Add a job posting for analysis |
| `/update-job-status [job] [status]` | Move jobs through the application pipeline |
| `/skill-builder` | Map skills, identify gaps, create improvement plans |
| `/tailor-resume [job-file]` | Generate a tailored resume for a job |

## Data Structure

The plugin stores all data in your working directory:

```
{working-directory}/
├── self/
│   ├── user.json              # Your profile
│   ├── resume/
│   │   ├── master-resume.md   # Primary resume
│   │   └── tailored/          # Job-specific versions
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

## Getting Started

1. Run `/personal-analysis` to create your profile
2. Use `/find-company` or `/find-job-postings` to discover opportunities
3. Use `/ingest-job` to add specific postings you find
4. Track applications with `/update-job-status`
5. Build skills with `/skill-builder`

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
