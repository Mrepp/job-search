# /ingest-job

Add a job posting from URL or pasted content.

## Usage

```
/ingest-job [url]
/ingest-job
```

## Examples

```
/ingest-job https://boards.greenhouse.io/company/jobs/12345
/ingest-job https://jobs.lever.co/company/abc123
/ingest-job
(Then paste the job description)
```

## Description

Adds a specific job posting to your tracking system with full analysis and match scoring.

## What It Does

1. **Fetches the job** - From URL or pasted content
2. **Extracts structured data** - Title, requirements, etc.
3. **Checks company research** - Links or triggers research
4. **Scores against your profile** - Detailed match analysis
5. **Saves to tracking** - In `jobs/interested/`

## Information Extracted

- **Basic:** Title, company, location, salary
- **Requirements:** Required and preferred qualifications
- **Responsibilities:** Key duties
- **Benefits:** Listed perks
- **Application:** Deadline and link

## Match Analysis

Each job gets:
- **Match score** (0-100)
- **Score breakdown** by category
- **Alignment points** - Your strengths
- **Gap analysis** - Areas to address
- **Talking points** - For applications

## Output

Creates `jobs/interested/{company}-{title}.md` with:
- Full job details
- Match analysis
- Requirements breakdown
- Application tracking

## Supported Sources

- **Greenhouse** (greenhouse.io)
- **Lever** (lever.co)
- **LinkedIn Jobs**
- **Company career pages**
- **Pasted text** (any format)

## Tips

- Use URL when possible for complete data
- Paste content if URL doesn't work
- Review gap analysis before applying
- Use talking points in your cover letter
