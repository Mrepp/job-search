# /ingest-job

Add a job posting from a URL or pasted content for analysis and tracking.

## Usage

```
/ingest-job [url]
/ingest-job [paste job description]
```

## Examples

```
/ingest-job https://boards.greenhouse.io/company/jobs/12345
/ingest-job https://jobs.lever.co/company/abc123
/ingest-job

(Then paste the job description when prompted)
```

## Description

This command allows you to add specific job postings you've found to your tracking system. It analyzes the posting against your profile and saves it for application tracking.

## Workflow

### 1. Determine Input Type

**If URL provided:**
- Validate URL format
- WebFetch the job posting content
- Parse HTML/markdown content

**If no URL (or paste indicated):**
- Ask user to paste the job description
- Parse the pasted text content

### 2. Extract Job Information

Parse the content to extract:

**Basic Information**
- Job title
- Company name
- Location(s)
- Remote work policy
- Employment type (full-time, contract, etc.)
- Salary/compensation (if listed)
- Application deadline

**Requirements**
- Required qualifications
- Preferred qualifications
- Years of experience required
- Education requirements
- Specific skills/technologies

**Role Details**
- Key responsibilities
- Team information
- Reporting structure
- Day-to-day activities

**Company Info**
- Benefits mentioned
- Company description
- Culture indicators

### 3. Check for Company Research

Look in `/companies/` for existing research:
- If company exists: Load and reference
- If company doesn't exist: Offer to run `/find-company`

### 4. Load User Profile

Read `self/user.json` to get:
- Skills and confidence levels
- Experience years
- Target titles and industries
- Salary expectations
- Location preferences

### 5. Analyze Match

Calculate detailed match score (0-100):

**Title Analysis (20 points)**
- Compare to target titles
- Consider seniority level match
- Factor in role type alignment

**Location Analysis (20 points)**
- Check remote availability
- Compare to user location
- Consider relocation implications

**Skills Analysis (30 points)**
- Map required skills to user skills
- Calculate coverage percentage
- Weight by confidence levels
- Identify specific gaps

**Experience Analysis (15 points)**
- Compare years required to user's experience
- Consider relevant industry experience
- Check for overqualification concerns

**Salary Analysis (15 points)**
- Compare to user expectations
- Flag if below minimum
- Note if exceeds target

### 6. Generate Insights

**Alignment Points**
- Which requirements you strongly meet
- Experience that directly applies
- Skills that are exact matches

**Gap Analysis**
- Missing required skills
- Experience shortfalls
- Potential concerns
- Suggested mitigations

**Talking Points**
- Strengths to emphasize
- Experience to highlight
- Projects to mention

### 7. Save Job File

Create `jobs/interested/{company}-{title}.md`:

```markdown
# {Title} at {Company}

## Overview
- **Location:** {location}
- **Type:** {employment type}
- **Remote:** {remote policy}
- **Salary Range:** {range or "Not disclosed"}
- **Posted:** {date if available}
- **Source:** {URL or "Pasted content"}

## Profile Match Analysis
- **Match Score:** {X}/100
- **Profile Hash:** {hash}
- **Analysis Date:** {ISO date}

### Score Breakdown
| Category | Score | Details |
|----------|-------|---------|
| Title Match | X/20 | {details} |
| Location | X/20 | {details} |
| Skills | X/30 | {matched}/{total} |
| Experience | X/15 | {details} |
| Salary | X/15 | {details} |

### Alignment
{What makes you a good fit}

### Gaps
{Areas where you may fall short}

### Talking Points
{Key points to emphasize in application/interview}

## Requirements

### Required
- {requirement 1}
- {requirement 2}

### Preferred
- {preferred 1}
- {preferred 2}

## Responsibilities
- {responsibility 1}
- {responsibility 2}

## Company Context
{Reference to company research or brief company info}

## Application
- **Deadline:** {deadline or "Not specified"}
- **Link:** {URL}
- **Status:** interested
- **Status History:**
  - {date}: Ingested from {source}

## Notes
{Space for user notes, interview prep, follow-ups}
```

### 8. Present Summary

Display:
- Match score with breakdown
- Key alignment points
- Important gaps to address
- Recommended next steps
- Company research status

## Handling Different Sources

### Greenhouse (greenhouse.io)
- Clean job description format
- Usually includes salary bands
- Benefits often listed

### Lever (lever.co)
- Structured requirements
- Often has team descriptions
- Application tracking friendly

### LinkedIn Jobs
- May need to extract from complex page
- Company info integrated
- Often has salary estimates

### Company Career Pages
- Format varies widely
- May need more parsing effort
- Often most detailed

### Pasted Content
- User-formatted text
- May be incomplete
- Ask clarifying questions if needed

## Tools Used

- **WebFetch**: Retrieve job posting from URL
- **Read**: Load user profile and company research
- **Write**: Save job file
- **Glob**: Check for existing company research
- **AskUserQuestion**: Clarify missing information

## Error Handling

- If URL inaccessible, offer paste option
- If key fields missing, ask user to provide
- If company unknown, suggest researching
- If salary unclear, mark as "Not disclosed"
