# Initial Setup

This guide walks you through setting up the Job Search Assistant for the first time.

## Prerequisites

Before running setup, you should have:

- A resume file (PDF, DOC, or plain text) - optional but recommended
- An idea of what job titles you're targeting
- A folder where you want to store your job search data

## Running Setup

Start by running the setup command:

```
/setup
```

## Step 1: Resume Analysis

The assistant will ask for your resume:

```
Let's start with a quick profile. Please provide your resume:
- Enter a file path (e.g., ~/Documents/resume.pdf)
- Or paste your resume content
- Or type 'skip' to enter details manually
```

**Tip**: Providing a resume is the fastest way to get started. The assistant extracts your skills, experience, and background automatically.

### What Gets Extracted

From your resume, the assistant identifies:

| Information | Used For |
|-------------|----------|
| Skills | Job matching, gap analysis |
| Experience years | Seniority matching |
| Job titles | Career path planning |
| Education | Profile completeness |
| Projects | Skill evidence |

## Step 2: Skill Review

After analyzing your resume, you'll see extracted skills with confidence scores:

```
Technical Skills:
- Python: 3 (Expert - 7 years, lead projects)
- AWS: 2 (Proficient - 3 years)
- React: 2 (Proficient - 2 roles)
- Kubernetes: 1 (Familiar - recent projects)

Would you like to adjust any scores?
```

### Confidence Scoring

| Score | Level | What It Means |
|-------|-------|---------------|
| 3 | Expert | You can teach this, solve complex problems, make architectural decisions |
| 2 | Proficient | You're comfortable using this daily, can complete most tasks independently |
| 1 | Familiar | You've used it but would need references, still learning |

Take time to adjust scores for accuracy - they affect job matching.

## Step 3: Career Goals

You'll be asked about your target roles:

```
What job titles are you targeting?
What industries interest you most?
What's your salary expectation range?
```

Be specific about job titles for better matching results.

## Step 4: Workspace Location

Choose where to store your job search data:

```
Where would you like to store your job search data?

a) Here in [current directory] (Recommended)
b) In ~/.job-search/
c) Let me specify a custom path
```

**Recommendation**: Use a dedicated folder like `~/job-search` to keep everything organized.

## What Gets Created

After setup, your workspace includes:

```
your-workspace/
├── .job-search-config.json    # Configuration
├── index.json                  # Research index
├── docs/                       # Documentation
├── self/                       # Your profile
│   └── user.json              # Profile data
├── companies/                  # Company research
├── jobs/                       # Job tracking
│   ├── interested/
│   ├── applied/
│   ├── interviewed/
│   ├── offered/
│   └── rejected/
└── career/                     # Career planning
```

## Setup Complete

When setup finishes, you'll see a summary:

```
Your job search workspace is ready!

Profile Summary:
- Name: John Smith
- Current Title: Senior Software Engineer
- Skills Mapped: 15
- Profile Type: Quick

Suggested Next Steps:
1. Run /personal-analysis to complete your full profile
2. Try /find-job-postings Staff Software Engineer
3. Run /docs to browse documentation
```

## Next Steps

After setup, you can:

### Enhance Your Profile (Optional)

```
/personal-analysis
```

This provides a more detailed profile analysis with additional context.

### Start Searching

```
/find-job-postings [your target role]
```

Begin discovering job opportunities that match your profile.

### Research Companies

```
/find-company [company name]
```

Deep-dive into specific companies you're interested in.

### Browse Documentation

```
/docs
```

Opens a web-based documentation browser with your research.

## Troubleshooting

### Resume Not Parsing

If your resume doesn't parse correctly:

1. Try a different format (PDF often works best)
2. Paste the text content directly
3. Use 'skip' and enter information manually

### Workspace Already Exists

If you've run setup before:

```
/setup
```

You'll be offered options to:
- Continue with existing setup
- Create a new workspace
- Reset and start fresh

## Related

- [Quick Start Guide](quick-start.md) - Complete workflow walkthrough
- [Profile Setup](profile-setup.md) - Detailed profile configuration
- [Commands Reference](../commands/setup.md) - Full command documentation
