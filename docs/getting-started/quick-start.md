# Quick Start Guide

This guide walks you through a complete job search workflow using the plugin.

## Step 1: Create Your Profile

Start by setting up your professional profile:

```
/personal-analysis
```

The assistant will:
1. Ask about your background and experience
2. Request your resume (file path or paste)
3. Extract and organize your skills
4. Help set career goals and preferences

!!! tip "Have Your Resume Ready"
    Prepare your resume file or be ready to paste its contents for faster setup.

## Step 2: Research Companies

Once your profile is set up, research companies you're interested in:

```
/find-company Stripe
```

Or search by criteria:

```
/find-company "remote fintech companies with good work-life balance"
```

The assistant will:
- Research the company's career page
- Analyze employee reviews
- Calculate a relevance score based on your profile
- Save research to `companies/stripe.md`

## Step 3: Find Job Postings

Search for jobs matching your profile:

```
/find-job-postings senior software engineer remote
```

The assistant will:
- Search multiple job boards
- Score each posting against your profile
- Rank results by match quality
- Offer to save interesting positions

## Step 4: Save and Analyze Jobs

When you find a specific job posting, ingest it for detailed analysis:

```
/ingest-job https://boards.greenhouse.io/company/jobs/12345
```

Or paste the job description when prompted:

```
/ingest-job
```

The assistant will:
- Parse the job requirements
- Calculate a detailed match score
- Identify your strengths and gaps
- Save to `jobs/interested/`

## Step 5: Track Your Applications

As you apply to jobs, update their status:

```
/update-job-status stripe-engineer applied
```

Status options:
- `interested` → Initial save
- `applied` → Application submitted
- `interviewed` → In interview process
- `offered` → Received offer
- `rejected` → Declined or rejected

## Step 6: Plan Your Career

Map potential career paths:

```
/find-position staff software engineer
```

This shows:
- Your current career position
- Promotion paths with requirements
- Lateral move options
- Skills needed for each path

## Step 7: Build Your Skills

Create a personalized skill development plan:

```
/skill-builder
```

The assistant will:
- Aggregate requirements from saved jobs
- Identify skill gaps
- Prioritize what to learn
- Suggest resources and projects

## Step 8: Tailor Your Resume

When ready to apply, create a targeted resume:

```
/tailor-resume stripe-senior-engineer
```

This creates a customized resume emphasizing:
- Skills the job requires
- Relevant experience
- Matching keywords

## Example Workflow

Here's a typical job search session:

```
# Set up profile (first time only)
/personal-analysis

# Research a target company
/find-company Anthropic

# Search for matching jobs
/find-job-postings ML engineer San Francisco

# Save an interesting job
/ingest-job https://boards.greenhouse.io/anthropic/jobs/12345

# Check skill gaps
/skill-builder

# Prepare tailored resume
/tailor-resume anthropic-ml-engineer

# Submit application and track
/update-job-status anthropic-ml-engineer applied
```

## Next Steps

- [Profile Setup](profile-setup.md) - Detailed profile configuration
- [Complete Job Search Workflow](../workflows/complete-search.md) - Full workflow guide
- [Commands Reference](../commands/personal-analysis.md) - Detailed command docs
