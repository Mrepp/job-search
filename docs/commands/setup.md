# Setup Command

Initialize your job search workspace and create your professional profile.

## Usage

```
/job-search:setup
```

## What It Does

The `/job-search:setup` command is your first step with the Job Search Assistant. It:

1. **Analyzes your resume** to extract skills and experience
2. **Creates your workspace** with organized directories
3. **Copies documentation** for easy reference
4. **Provides next steps** to get started

## Workflow

### 1. Resume Analysis

The command starts by asking for your resume:

```
Let's start with a quick profile. Please provide your resume:
- Enter a file path (e.g., ~/Documents/resume.pdf)
- Or paste your resume content
- Or type 'skip' to enter details manually
```

From your resume, it extracts:

- **Skills** with confidence scores (1-3)
- **Experience** years and history
- **Current title** and education
- **Projects** and achievements

### 2. Skill Scoring

Skills are scored on a 1-3 scale:

| Score | Level | Criteria |
|-------|-------|----------|
| 3 | Expert | 5+ years, lead/senior roles, certifications |
| 2 | Proficient | 2-5 years, used across multiple roles |
| 1 | Familiar | <2 years, side projects, coursework |

You can adjust these scores after review.

### 3. Career Goals

You'll be asked about:

- Target job titles
- Industries of interest
- Salary expectations

### 4. Workspace Location

Choose where to store your job search data:

| Option | Best For |
|--------|----------|
| Current directory | Dedicated job search folder |
| `~/.job-search/` | Keeping data separate from projects |
| Custom path | Specific organization needs |

## What Gets Created

After setup completes, your workspace includes:

```
your-workspace/
├── .job-search-config.json    # Configuration
├── index.json                  # Research index
├── INDEX.md                    # Quick reference
├── mkdocs.yml                  # For /job-search:docs command
├── docs/                       # Documentation copy
├── self/                       # Your profile
│   ├── user.json              # Profile data
│   ├── resume/                # Resume files
│   └── ...
├── companies/                  # Company research
├── jobs/                       # Job applications
│   ├── interested/
│   ├── applied/
│   ├── interviewed/
│   ├── offered/
│   └── rejected/
└── career/                     # Career planning
```

## After Setup

Once setup completes, you can:

1. **Enhance your profile** with `/job-search:personal-analysis`
2. **Search for jobs** with `/job-search:find-job-postings [role]`
3. **Research companies** with `/job-search:find-company [name]`
4. **Browse documentation** with `/job-search:docs`

## Tips

!!! tip "Have Your Resume Ready"
    The setup goes faster if you have your resume file available.

!!! tip "Review Skill Scores"
    Take time to adjust the automatically-assigned skill confidence scores for accuracy.

!!! tip "Choose a Dedicated Folder"
    Creating a dedicated folder for your job search keeps everything organized.

## Existing Setup

If you've already run `/job-search:setup`, running it again will:

1. Detect your existing configuration
2. Offer options to continue, create new, or reset

## Related Commands

- [Personal Analysis](personal-analysis.md) - Enhance your profile
- [Documentation](docs.md) - Browse docs and research
- [Find Job Postings](find-job-postings.md) - Search for jobs
