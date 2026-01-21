# /update-job-status

Move a job through the application pipeline and track your progress.

## Usage

```
/update-job-status [job-file] [status]
/update-job-status [company] [status]
```

## Examples

```
/update-job-status stripe-senior-engineer applied
/update-job-status "Stripe - Senior Engineer" interviewed
/update-job-status jobs/interested/vercel-staff-engineer.md offered
/update-job-status vercel rejected
```

## Description

This command updates the status of a saved job posting and moves it to the appropriate directory in the application pipeline.

## Status Values

| Status | Directory | Description |
|--------|-----------|-------------|
| `interested` | `jobs/interested/` | Initial save, considering applying |
| `applied` | `jobs/applied/` | Application submitted |
| `interviewed` | `jobs/interviewed/` | In interview process |
| `offered` | `jobs/offered/` | Received an offer |
| `rejected` | `jobs/rejected/` | Declined or rejected |

## Workflow

### 1. Find the Job File

**If full path provided:**
- Read the file directly

**If partial name provided:**
- Search `jobs/*/` directories
- Match by filename or title
- If multiple matches, ask user to clarify

### 2. Validate Status Transition

Typical flow:
```
interested → applied → interviewed → offered
                ↓           ↓           ↓
             rejected   rejected    rejected
```

Warn (but allow) unusual transitions:
- `interested` → `interviewed` (skipped applied?)
- `applied` → `offered` (no interview recorded)
- Any status → `interested` (moving backwards)

### 3. Update the Job File

**Update Status Field:**
```markdown
- **Status:** {new_status}
```

**Add to Status History:**
```markdown
- **Status History:**
  - YYYY-MM-DD: Changed to {new_status} - {note}
```

### 4. Prompt for Notes

Ask user for relevant context based on new status:

**applied:**
- Application date
- Application method (website, referral, email)
- Contact person (if known)
- Materials submitted (resume version, cover letter)

**interviewed:**
- Interview date(s)
- Interview format (phone, video, onsite)
- Interviewers (names, titles)
- Topics discussed
- How it went
- Next steps mentioned

**offered:**
- Offer details (salary, equity, benefits)
- Start date proposed
- Deadline to respond
- Negotiation notes

**rejected:**
- Rejection source (company, self-withdrawal)
- Reason (if provided)
- Stage reached
- Lessons learned

### 5. Move the File

Move file from current directory to new status directory:
- `jobs/interested/` → `jobs/applied/`
- `jobs/applied/` → `jobs/interviewed/`
- etc.

### 6. Update Related Files

**If status is "offered" or "rejected":**
- Update company file with note if exists
- Consider impact on similar job searches

### 7. Confirm and Summarize

Display:
- Job title and company
- Previous status → New status
- Notes added
- New file location
- Suggested next actions

## File Updates

### Status History Format

```markdown
## Application
- **Deadline:** {date}
- **Link:** {url}
- **Status:** interviewed
- **Status History:**
  - 2024-01-20: Saved from job search
  - 2024-01-22: Applied via company website. Submitted tailored resume v2.
  - 2024-01-28: Phone screen scheduled for Feb 1
  - 2024-02-01: Phone screen completed. Moving to technical round.
  - 2024-02-05: Technical interview. Discussed system design and coding.
```

### Notes Section Updates

```markdown
## Notes

### Application Notes
- Submitted resume version: tailored-stripe-senior-engineer.md
- Cover letter: Emphasized distributed systems experience
- Referral: None

### Interview Notes
#### Phone Screen (Feb 1)
- Interviewer: Jane Smith (Recruiter)
- Discussed: Background, role expectations, timeline
- Went well, moved to next round

#### Technical Interview (Feb 5)
- Interviewers: John Doe (Staff Eng), Alice Chen (Manager)
- Topics: System design (rate limiter), coding (graph traversal)
- Felt good about system design, coding was challenging
- They mentioned decision by Feb 12

### Offer Notes
- Base: $185,000
- Equity: 50,000 options over 4 years
- Sign-on: $20,000
- Start date: March 1
- Response deadline: Feb 15
```

## Tools Used

- **Glob**: Find job files matching search
- **Read**: Load current job file
- **Edit**: Update status and history
- **Bash**: Move file to new directory
- **AskUserQuestion**: Gather notes and context

## Pipeline Summary Command

When no arguments provided, show pipeline summary:

```
## Application Pipeline Status

### Interested (3)
- Stripe - Senior Engineer (92/100) - saved 5 days ago
- Vercel - Staff Engineer (87/100) - saved 3 days ago
- Linear - Backend Engineer (85/100) - saved 1 day ago

### Applied (2)
- Anthropic - Software Engineer (90/100) - applied 7 days ago
- OpenAI - Backend Engineer (88/100) - applied 4 days ago

### Interviewed (1)
- Notion - Senior Engineer (89/100) - phone screen completed

### Offered (0)
No offers yet.

### Rejected (1)
- Apple - SRE (75/100) - rejected after phone screen
```

## Error Handling

- If job file not found, list available jobs
- If invalid status, show valid options
- If move fails, report error but keep original file
- Always preserve original content on any error
