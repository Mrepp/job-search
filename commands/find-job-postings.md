# /find-job-postings

Discover and rank relevant job postings matching your profile.

## Usage

```
/find-job-postings [role] [location]
```

## Examples

```
/find-job-postings
/find-job-postings senior software engineer
/find-job-postings product manager San Francisco
/find-job-postings backend developer remote
/find-job-postings "staff engineer" "New York"
```

## Description

This command searches for job postings that match your profile and preferences, scoring and ranking them by relevance.

## Workflow

### 1. Load User Profile

Read `self/user.json` to get:
- Target job titles
- Location / remote preference
- Experience level
- Target industries
- Skills inventory
- Salary expectations

### 2. Build Search Queries

Construct searches based on:
- Role/title from arguments OR target_titles from profile
- Location from arguments OR user location + remote preference
- Experience level keywords (junior, senior, staff, etc.)

### 3. Search for Postings

Execute multiple WebSearches:
- "{role} jobs {location}"
- "{role} {industry} jobs"
- "remote {role} jobs"
- Site-specific: "site:linkedin.com/jobs {role}"
- Site-specific: "site:greenhouse.io {role}"
- Site-specific: "site:lever.co {role}"

### 4. Fetch and Analyze Top Results

For top 10-15 results:

1. **WebFetch the job posting**
2. **Extract structured data:**
   - Job title
   - Company name
   - Location
   - Remote policy
   - Salary range (if posted)
   - Required skills/qualifications
   - Preferred qualifications
   - Years of experience required
   - Responsibilities
   - Benefits mentioned
   - Application deadline
   - Application URL

### 5. Score Each Posting

Calculate match score (0-100):

**Title Match (20 points)**
- Exact match to target title: 20
- Similar level/type: 15
- Related but different: 10
- Significantly different: 5

**Location Match (20 points)**
- Remote + user prefers remote: 20
- Exact location match: 20
- Hybrid available: 15
- Relocation required: 5

**Skills Match (30 points)**
- Calculate overlap between required skills and user skills
- Weight by confidence level (skill conf 3 = full weight, 1 = partial)
- Score = (matched skills / required skills) * 30

**Experience Match (15 points)**
- User meets or exceeds requirement: 15
- Within 1-2 years: 10
- Significantly under: 5
- Significantly over: 10 (may be overqualified)

**Salary Match (15 points)**
- Posted range >= user target: 15
- Posted range >= user minimum: 10
- Below minimum but close: 5
- No salary posted: 10 (neutral)

### 6. Generate Profile Hash

Create a hash of the current profile state:
- Skills and confidence levels
- Experience years
- Target titles
- Salary expectations

This hash is stored with job files to indicate if the match score is current.

### 7. Present Results

Display ranked results:

```
## Job Search Results

Found 12 matching positions for "Senior Software Engineer"

### 1. Senior Backend Engineer at Stripe (92/100)
📍 Remote (US) | 💰 $180k-$220k | 🏢 Fintech
✅ Skills: 8/10 match | ✅ Experience: Meets requirement
[View Details] [Save to Interested]

### 2. Staff Software Engineer at Vercel (87/100)
📍 San Francisco, CA (Hybrid) | 💰 $200k-$260k | 🏢 Developer Tools
✅ Skills: 9/10 match | ⚠️ Experience: May be stretch
[View Details] [Save to Interested]

...
```

### 8. Save Selected Postings

When user selects postings to save:
- Create `jobs/interested/{company}-{title}.md`
- Include full analysis and profile hash
- Trigger company research if company not in `/companies/`

## Output Format

### Search Results Display

For each job, show:
- Match score and ranking
- Title, company, location
- Salary range (if available)
- Key match/gap highlights
- Quick actions (view, save)

### Saved Job File

```markdown
# {Title} at {Company}

## Overview
- **Location:** {location}
- **Type:** Full-time/Contract
- **Remote:** Yes/No/Hybrid
- **Salary Range:** {range}
- **Posted:** {date}
- **Source:** {url}

## Profile Match Analysis
- **Match Score:** {X}/100
- **Profile Hash:** {hash}
- **Analysis Date:** {ISO date}

### Score Breakdown
| Category | Score | Details |
|----------|-------|---------|
| Title Match | X/20 | {reason} |
| Location | X/20 | {reason} |
| Skills | X/30 | {matched}/{total} skills |
| Experience | X/15 | {reason} |
| Salary | X/15 | {reason} |

### Alignment
- {strength 1}
- {strength 2}
- ...

### Gaps
- {gap 1} - {suggested action}
- {gap 2} - {suggested action}
- ...

## Requirements
### Required
- {requirement}
- ...

### Preferred
- {preferred qualification}
- ...

## Responsibilities
- {responsibility}
- ...

## Benefits
- {benefit}
- ...

## Application
- **Deadline:** {date or "Rolling"}
- **Link:** {url}
- **Status:** interested
- **Status History:**
  - {date}: Saved from job search

## Notes
{Space for user notes}
```

## Tools Used

- **WebSearch**: Find job postings across platforms
- **WebFetch**: Retrieve full job descriptions
- **Read**: Load user profile
- **Write**: Save job files
- **Glob**: Check existing saved jobs

## Error Handling

- If a job posting URL fails, skip and note in results
- If salary not posted, indicate "Not disclosed"
- If company unknown, offer to research
- Handle rate limiting by spacing requests
