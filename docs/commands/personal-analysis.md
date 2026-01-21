# /personal-analysis

Build and maintain your professional profile.

## Usage

```
/personal-analysis
```

## Description

Creates or updates your user profile, which powers personalized job matching and career planning across all other commands.

## What It Does

### For New Users

1. Asks about your background and experience
2. Requests your resume (file or paste)
3. Parses resume to extract skills and experience
4. Helps set career goals and salary expectations
5. Suggests skill confidence scores for review
6. Creates profile structure in `self/`

### For Existing Users

1. Shows current profile summary
2. Asks what you'd like to update
3. Validates and saves changes

## Information Collected

- **Basic info:** Name, email, location
- **Preferences:** Remote work preference
- **Current role:** Title, years of experience
- **Goals:** Target titles, industries
- **Compensation:** Minimum and target salary
- **Skills:** Technical and soft skills with confidence levels

## Skill Confidence Scoring

Skills are rated 1-3:

| Score | Level | Description |
|-------|-------|-------------|
| 1 | Basic | Familiar, learning, occasional use |
| 2 | Proficient | Regular use, work independently |
| 3 | Expert | Deep expertise, teach others |

The system suggests scores based on your resume; you can adjust them.

## Output

Creates these files:

```
self/
├── user.json              # Core profile
├── resume/
│   └── main-resume.md   # Your resume
├── experience/            # Work history details
├── education/             # Education records
└── projects/              # Project descriptions
```

## Example Session

```
You: /personal-analysis