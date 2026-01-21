# Job Search Assistant

A comprehensive Claude Code plugin for intelligent job search, research, analysis, and career planning.

## Overview

The Job Search Assistant helps you navigate your job search with AI-powered tools for:

- **Profile Building** - Create and maintain a comprehensive professional profile
- **Company Research** - Deep-dive into companies matching your criteria
- **Job Discovery** - Find and rank job postings against your profile
- **Career Planning** - Map career paths and identify growth opportunities
- **Skill Development** - Analyze gaps and create learning plans
- **Application Tracking** - Manage your job application pipeline

## Quick Start

1. **Initialize your workspace**
   ```
   /job-search:setup
   ```
   This analyzes your resume, creates your profile, and sets up your workspace.

2. **Browse documentation**
   ```
   /job-search:docs
   ```
   Opens a web-based documentation browser with your research.

3. **Research companies**
   ```
   /job-search:find-company Stripe
   /job-search:find-company "fintech startups in SF"
   ```

4. **Discover jobs**
   ```
   /job-search:find-job-postings senior software engineer
   ```

5. **Track applications**
   ```
   /job-search:ingest-job https://example.com/job
   /job-search:update-job-status stripe-engineer applied
   ```

6. **Plan your career**
   ```
   /job-search:find-position staff engineer
   /job-search:skill-builder
   ```

## Commands

| Command | Description |
|---------|-------------|
| `/job-search:setup` | Initialize workspace and profile from resume |
| `/job-search:docs` | Browse documentation and research in browser |
| `/job-search:personal-analysis` | Build and maintain your profile |
| `/job-search:find-company` | Research companies |
| `/job-search:find-position` | Map career paths |
| `/job-search:find-job-postings` | Discover matching jobs |
| `/job-search:ingest-job` | Add job from URL or paste |
| `/job-search:update-job-status` | Track application progress |
| `/job-search:skill-builder` | Analyze skill gaps |
| `/job-search:tailor-resume` | Customize resume for a job |

## Data Storage

All data is stored in your working directory:

```
your-directory/
├── self/                 # Your profile and resume
├── companies/           # Company research
├── jobs/                # Job postings by status
│   ├── interested/
│   ├── applied/
│   ├── interviewed/
│   ├── offered/
│   └── rejected/
└── career/              # Career planning data
```

## Getting Help

- See [Installation](getting-started/installation.md) for setup instructions
- Run [/job-search:setup](getting-started/setup.md) to initialize your workspace
- Check [Quick Start](getting-started/quick-start.md) for a walkthrough
- Browse [Commands](commands/setup.md) for detailed documentation
