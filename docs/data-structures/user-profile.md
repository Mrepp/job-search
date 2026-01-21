# User Profile Data Structure

Documentation for the user profile schema and related files.

## Overview

Your profile is stored in `self/user.json` and contains all the information used for job matching, career planning, and skill analysis.

## user.json Schema

```json
{
  "name": "string",
  "email": "string",
  "location": "string",
  "remote_preference": "remote|hybrid|onsite|flexible",
  "experience_years": "number",
  "current_title": "string",
  "target_titles": ["string"],
  "target_industries": ["string"],
  "salary_expectations": {
    "minimum": "number",
    "target": "number"
  },
  "skills": [
    {
      "name": "string",
      "confidence": "1|2|3",
      "years": "number"
    }
  ],
  "profile_hash": "string",
  "last_updated": "ISO date string"
}
```

## Field Descriptions

### Basic Information

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Your full name |
| `email` | string | Contact email address |
| `location` | string | City, State/Country (e.g., "San Francisco, CA") |
| `remote_preference` | enum | Your work location preference |

### Remote Preference Values

| Value | Description |
|-------|-------------|
| `remote` | Fully remote only |
| `hybrid` | Mix of remote and office |
| `onsite` | Prefer working in office |
| `flexible` | Open to any arrangement |

### Career Information

| Field | Type | Description |
|-------|------|-------------|
| `experience_years` | number | Total professional experience |
| `current_title` | string | Your current job title |
| `target_titles` | array | Titles you're pursuing |
| `target_industries` | array | Industries you're interested in |

### Salary Expectations

```json
{
  "salary_expectations": {
    "minimum": 150000,
    "target": 180000
  }
}
```

| Field | Description |
|-------|-------------|
| `minimum` | Lowest acceptable base salary |
| `target` | Ideal base salary |

### Skills Array

```json
{
  "skills": [
    {"name": "Python", "confidence": 3, "years": 5},
    {"name": "AWS", "confidence": 2, "years": 3},
    {"name": "React", "confidence": 1, "years": 1}
  ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Skill name |
| `confidence` | 1-3 | Self-assessed proficiency level |
| `years` | number | Years of experience with skill |

### Confidence Scale

| Level | Name | Description |
|-------|------|-------------|
| 1 | Basic | Familiar, used occasionally, still learning |
| 2 | Proficient | Regular use, work independently, comfortable |
| 3 | Expert | Deep expertise, can teach others, go-to person |

### Tracking Fields

| Field | Description |
|-------|-------------|
| `profile_hash` | Hash of profile state for tracking staleness |
| `last_updated` | ISO 8601 timestamp of last update |

## Example user.json

```json
{
  "name": "Jane Smith",
  "email": "jane.smith@example.com",
  "location": "San Francisco, CA",
  "remote_preference": "remote",
  "experience_years": 7,
  "current_title": "Senior Software Engineer",
  "target_titles": [
    "Staff Software Engineer",
    "Principal Engineer"
  ],
  "target_industries": [
    "Fintech",
    "Developer Tools",
    "AI/ML"
  ],
  "salary_expectations": {
    "minimum": 180000,
    "target": 220000
  },
  "skills": [
    {"name": "Python", "confidence": 3, "years": 5},
    {"name": "TypeScript", "confidence": 2, "years": 3},
    {"name": "AWS", "confidence": 2, "years": 4},
    {"name": "PostgreSQL", "confidence": 3, "years": 5},
    {"name": "Docker", "confidence": 2, "years": 3},
    {"name": "Kubernetes", "confidence": 1, "years": 1},
    {"name": "System Design", "confidence": 2, "years": 4},
    {"name": "React", "confidence": 2, "years": 2}
  ],
  "profile_hash": "a1b2c3d4e5f6...",
  "last_updated": "2024-01-20T10:30:00Z"
}
```

## Related Files

### self/ Directory Structure

```
self/
├── user.json              # Core profile (this file)
├── resume/
│   ├── main-resume.md   # Primary resume
│   └── tailored/          # Job-specific resumes
│       └── {company}-{title}.md
├── experience/
│   └── {company}-{title}.md
├── education/
│   └── {institution}.md
├── projects/
│   └── {project-name}.md
└── linkedin/
    └── profile.md
```

### Experience File Format

`self/experience/{company}-{title}.md`:

```markdown
# {Title} at {Company}

**Duration:** {start date} - {end date}
**Location:** {location}

## Responsibilities
- {responsibility 1}
- {responsibility 2}

## Technologies
Python, AWS, PostgreSQL, Docker

## Achievements
- {achievement with metrics}
- {achievement with metrics}
```

### Education File Format

`self/education/{institution}.md`:

```markdown
# {Degree} from {Institution}

**Graduated:** {date}
**Field:** {major}
**GPA:** {gpa}

## Relevant Coursework
- {course 1}
- {course 2}

## Honors
- {honor/award}
```

### Project File Format

`self/projects/{project-name}.md`:

```markdown
# {Project Name}

## Description
{What the project does}

## Technologies
{Technologies used}

## My Role
{Your contribution}

## Outcomes
{Results and impact}

## Links
- [GitHub]({url})
- [Live Demo]({url})
```

## Profile Hash

The profile hash is a deterministic hash generated from:
- Skills and confidence levels
- Experience years
- Target titles
- Salary expectations

It's used to track whether job match scores are current or need recalculation.

### Hash Staleness

When viewing a job analysis:
- **Current hash matches**: Score is up-to-date
- **Hash mismatch**: Profile changed since scoring; consider re-analyzing

## Updating Your Profile

Use `/job-search:personal-analysis` to:
- Update any field
- Add or modify skills
- Adjust confidence levels
- Change career targets

The `last_updated` timestamp and `profile_hash` update automatically.
