# Setting Up Your Profile

Your profile is the foundation for personalized job matching and career planning.

## Creating Your Profile

Run the personal analysis command:

```
/job-search:personal-analysis
```

## Information Collected

### Basic Information

The assistant will ask for:

- **Name** - Your full name
- **Email** - Contact email
- **Location** - City and state/country
- **Remote Preference** - remote, hybrid, onsite, or flexible

### Career Details

- **Current Title** - Your current job title
- **Experience Years** - Total years of professional experience
- **Target Titles** - Job titles you're pursuing
- **Target Industries** - Industries you're interested in

### Salary Expectations

- **Minimum** - The lowest salary you'd consider
- **Target** - Your ideal salary

### Skills

Skills are imported from your resume and rated on a 1-3 scale:

| Score | Level | Description |
|-------|-------|-------------|
| 1 | Basic | Familiar, used occasionally |
| 2 | Proficient | Regular use, work independently |
| 3 | Expert | Deep expertise, can teach others |

## Importing Your Resume

You can provide your resume in two ways:

### Option 1: File Path

```
Please provide the path to your resume: /Users/you/Documents/resume.pdf
```

### Option 2: Paste Content

```
Please paste your resume content:

[Paste your resume text here]
```

The assistant will parse your resume to extract:
- Work experience
- Education
- Skills and technologies
- Projects
- Achievements

## Profile Structure

Your profile is saved in `self/`:

```
self/
├── user.json              # Core profile data
├── resume/
│   ├── main-resume.md   # Your main resume
│   └── tailored/          # Job-specific versions
├── experience/
│   └── {company}-{title}.md
├── education/
│   └── {school}.md
├── projects/
│   └── {project-name}.md
└── linkedin/
    └── profile.md
```

## user.json Schema

```json
{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "location": "San Francisco, CA",
  "remote_preference": "remote",
  "experience_years": 7,
  "current_title": "Senior Software Engineer",
  "target_titles": ["Staff Engineer", "Principal Engineer"],
  "target_industries": ["Fintech", "Developer Tools"],
  "salary_expectations": {
    "minimum": 180000,
    "target": 220000
  },
  "skills": [
    {"name": "Python", "confidence": 3, "years": 5},
    {"name": "AWS", "confidence": 2, "years": 3},
    {"name": "Kubernetes", "confidence": 1, "years": 1}
  ],
  "profile_hash": "abc123...",
  "last_updated": "2024-01-20T10:00:00Z"
}
```

## Adjusting Skill Confidence

The assistant suggests confidence scores based on your resume, but you can adjust them:

```
Assistant: I've extracted these skills with suggested confidence levels:

Python - 3 (Expert) - 5 years, primary language
AWS - 2 (Proficient) - mentioned in 2 roles
Kubernetes - 1 (Basic) - mentioned once

Would you like to adjust any of these scores?

You: Adjust AWS to 3, I use it extensively
```

## Updating Your Profile

Run `/job-search:personal-analysis` again to:

- Update existing information
- Add new skills
- Adjust confidence levels
- Update target titles or salary expectations

The assistant will show your current profile and ask what you'd like to change.

## Profile Hash

A hash of your profile is generated and stored with job analyses. This helps you know if a job match score was calculated against your current profile or an older version.

## Tips for a Strong Profile

1. **Be accurate with confidence scores** - Don't inflate; interviewers will test you
2. **Include all relevant skills** - Even basics matter for matching
3. **Set realistic salary expectations** - Research market rates first
4. **Update regularly** - Keep your profile current as you grow
5. **Be specific about preferences** - Clear targets lead to better matches

## Next Steps

- [Find Companies](../commands/find-company.md) that match your profile
- [Search for Jobs](../commands/find-job-postings.md) with personalized scoring
- [Plan Your Career](../commands/find-position.md) based on your current position
