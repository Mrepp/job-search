# /personal-analysis

Build and maintain your user profile with skills, experience, and career preferences.

## Usage

```
/personal-analysis
```

## Description

This command creates or updates your professional profile, which is used by all other job search commands to provide personalized recommendations and match scoring.

## Workflow

### For New Users

1. **Check for existing profile**
   - Look for `self/user.json` in the working directory
   - If not found, start the profile creation process

2. **Gather basic information**
   - Ask for name, email, location
   - Determine remote work preference (remote/hybrid/onsite/flexible)
   - Years of experience
   - Current job title

3. **Career goals**
   - Target job titles
   - Target industries
   - Salary expectations (minimum and target)

4. **Resume and experience import**
   - Ask user for resume file location OR paste resume content
   - Parse resume to extract:
     - Work experience entries
     - Education history
     - Skills and technologies
     - Projects and achievements

5. **LinkedIn profile (optional)**
   - Request LinkedIn profile export or URL
   - Extract additional context and endorsements

6. **Skill assessment**
   - Present extracted skills
   - Suggest confidence scores (1-3) based on:
     - Years mentioned
     - Frequency in resume
     - Role responsibilities
   - Allow user to adjust scores

7. **Save profile structure**
   - Create `self/user.json` with core data
   - Create `self/experience/` entries for each job
   - Create `self/education/` entries for each degree
   - Create `self/projects/` entries for notable projects
   - Save resume to `self/resume/master-resume.md`

### For Existing Users

1. Load current profile from `self/user.json`
2. Present current profile summary
3. Ask what the user wants to update:
   - Basic information
   - Career goals
   - Skills and confidence levels
   - Add new experience
   - Update resume

## Directory Structure Created

```
self/
├── user.json
├── resume/
│   ├── master-resume.md
│   └── tailored/
├── projects/
│   └── {project-name}.md
├── education/
│   └── {institution}.md
├── experience/
│   └── {company}-{title}.md
└── linkedin/
    └── profile.md
```

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
    {"name": "string", "confidence": 1-3, "years": "number"}
  ],
  "profile_hash": "string",
  "last_updated": "ISO date"
}
```

## Example Session

```
User: /personal-analysis