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

1. **Set up your profile**
   ```
   /personal-analysis
   ```

2. **Research companies**
   ```
   /find-company Stripe
   /find-company "fintech startups in SF"
   ```

3. **Discover jobs**
   ```
   /find-job-postings senior software engineer
   ```

4. **Track applications**
   ```
   /ingest-job https://example.com/job
   /update-job-status stripe-engineer applied
   ```

5. **Plan your career**
   ```
   /find-position staff engineer
   /skill-builder
   ```

## Commands

| Command | Description |
|---------|-------------|
| `/personal-analysis` | Build and maintain your profile |
| `/find-company` | Research companies |
| `/find-position` | Map career paths |
| `/find-job-postings` | Discover matching jobs |
| `/ingest-job` | Add job from URL or paste |
| `/update-job-status` | Track application progress |
| `/skill-builder` | Analyze skill gaps |
| `/tailor-resume` | Customize resume for a job |

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
- Check [Quick Start](getting-started/quick-start.md) for a walkthrough
- Browse [Commands](commands/personal-analysis.md) for detailed documentation
