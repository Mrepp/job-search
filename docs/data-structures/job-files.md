# Job Files Data Structure

Documentation for job posting file format and pipeline organization.

## Overview

Job postings are stored as markdown files in `jobs/{status}/` directories, organized by application status.

## Directory Structure

```
jobs/
├── interested/           # Saved, not yet applied
│   ├── stripe-senior-engineer.md
│   └── anthropic-ml-engineer.md
├── applied/              # Application submitted
│   └── vercel-staff-engineer.md
├── interviewed/          # In interview process
│   └── linear-backend-engineer.md
├── offered/              # Received offer
│   └── notion-senior-engineer.md
└── rejected/             # Rejected or declined
    └── meta-swe.md
```

## File Naming Convention

```
{company}-{title-slug}.md
```

Examples:
- `stripe-senior-backend-engineer.md`
- `anthropic-ml-engineer.md`
- `linear-staff-engineer.md`

## File Template

```markdown
# {Title} at {Company}

## Overview
- **Location:** {location}
- **Type:** {Full-time/Contract/Part-time}
- **Remote:** {Yes/No/Hybrid}
- **Salary Range:** {range or "Not disclosed"}
- **Posted:** {date}
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
| Skills | X/30 | {matched}/{total} skills |
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
- **Deadline:** {date or "Not specified"}
- **Link:** {URL}
- **Status:** {current status}
- **Status History:**
  - {date}: {status change and notes}

## Notes
{User notes, interview prep, follow-ups}
```

## Section Details

### Overview Section

Basic job information:

| Field | Description |
|-------|-------------|
| Location | City, State or "Remote" |
| Type | Employment type |
| Remote | Remote work policy |
| Salary Range | Posted compensation or "Not disclosed" |
| Posted | When the job was posted |
| Source | Original URL or paste indicator |

### Profile Match Analysis

Personalized scoring against your profile:

**Match Score (0-100):**
Composite score from five categories:

| Category | Max Points | What It Measures |
|----------|------------|------------------|
| Title Match | 20 | How well title aligns with targets |
| Location | 20 | Location/remote preference match |
| Skills | 30 | Required skills you possess |
| Experience | 15 | Years and type of experience |
| Salary | 15 | Salary range vs expectations |

**Profile Hash:**
Hash of your profile at analysis time. If this doesn't match your current profile hash, the score may be stale.

### Alignment & Gaps

**Alignment:**
Your strengths for this position:
- Strong skill matches
- Relevant experience
- Culture fit indicators

**Gaps:**
Areas needing attention:
- Missing required skills
- Experience shortfalls
- Potential concerns

**Talking Points:**
Prepared points for applications/interviews:
- What to emphasize
- How to address gaps
- Relevant experiences to highlight

### Requirements

Extracted and categorized job requirements:

**Required:**
- Must-have qualifications
- Hard requirements
- Non-negotiable skills

**Preferred:**
- Nice-to-have qualifications
- Bonus skills
- Preferred experience

### Application Tracking

| Field | Description |
|-------|-------------|
| Deadline | Application deadline if specified |
| Link | Direct link to apply |
| Status | Current pipeline status |
| Status History | Chronological status changes with notes |

### Notes

Free-form section for:
- Interview preparation
- Follow-up reminders
- Contact information
- Personal observations

## Status Values

| Status | Directory | When to Use |
|--------|-----------|-------------|
| `interested` | `jobs/interested/` | Saved for consideration |
| `applied` | `jobs/applied/` | Application submitted |
| `interviewed` | `jobs/interviewed/` | In interview process |
| `offered` | `jobs/offered/` | Received an offer |
| `rejected` | `jobs/rejected/` | Rejected or withdrew |

## Status History Format

```markdown
- **Status History:**
  - 2024-01-15: Saved from job search
  - 2024-01-18: Applied via company website. Submitted tailored resume.
  - 2024-01-25: Recruiter screen scheduled for Jan 28
  - 2024-01-28: Recruiter screen completed. Moving to technical round.
  - 2024-02-03: Technical interview completed. System design + coding.
  - 2024-02-07: Offer received! $185k base + equity.
```

## Notes Section Examples

### Pre-Application Notes

```markdown
## Notes

### Application Strategy
- Emphasize payment systems experience
- Mention specific project: distributed transaction handler
- Use tailored resume: self/resume/tailored/stripe-senior-engineer.md

### Questions for Them
- Team size and structure?
- Tech stack modernization plans?
- On-call expectations?
```

### Interview Notes

```markdown
## Notes

### Recruiter Screen (Jan 28)
- Recruiter: Sarah Chen
- Discussed: Background, role expectations, timeline
- Went well, moved to next round
- Next: Technical interview week of Feb 3

### Technical Interview (Feb 3)
- Interviewers: John (Staff Eng), Lisa (Manager)
- System Design: Designed rate limiter - went well
- Coding: Graph problem - solved but took hints
- Red flag: Lisa seemed disengaged
- Decision expected by Feb 10
```

### Offer Notes

```markdown
## Notes

### Offer Details (Feb 7)
- Base: $185,000
- Equity: 50,000 options, 4-year vest, 1-year cliff
- Sign-on: $20,000
- Start date: March 1 flexible
- Response deadline: Feb 14

### Negotiation
- Asked for $200k base - countered at $190k ✓
- Additional 10k equity - approved ✓
- Remote work - confirmed ✓

### Comparison
- Higher base than Anthropic offer
- Less equity than Anthropic
- Better remote policy
```

## Example Complete File

```markdown
# Senior Backend Engineer at Stripe

## Overview
- **Location:** Remote (US)
- **Type:** Full-time
- **Remote:** Yes
- **Salary Range:** $180,000 - $220,000
- **Posted:** 2024-01-10
- **Source:** https://stripe.com/jobs/senior-backend-engineer

## Profile Match Analysis
- **Match Score:** 92/100
- **Profile Hash:** a1b2c3d4e5
- **Analysis Date:** 2024-01-15T14:30:00Z

### Score Breakdown
| Category | Score | Details |
|----------|-------|---------|
| Title Match | 20/20 | Exact match to target |
| Location | 20/20 | Remote matches preference |
| Skills | 27/30 | 9/10 required skills |
| Experience | 15/15 | Exceeds requirement |
| Salary | 10/15 | Range meets minimum |

### Alignment
- 5+ years Python experience matches requirement
- Distributed systems background from current role
- Payment processing experience from previous fintech
- Remote work experience

### Gaps
- Missing Go experience (preferred, not required)
- Haven't used their specific payment protocols
- Slight stretch on "expert-level" system design

### Talking Points
- Lead with distributed transaction system project
- Emphasize fintech domain knowledge
- Mention scale: handled 10M+ transactions/day
- Address Go gap: "quick learner, familiar with compiled languages"

## Requirements

### Required
- 5+ years backend development experience
- Strong Python or Ruby experience
- Experience with distributed systems
- Experience with relational databases
- Strong communication skills

### Preferred
- Go experience
- Payment processing experience
- Financial services industry background
- Experience with high-scale systems

## Responsibilities
- Design and build payment processing systems
- Improve reliability and performance of critical paths
- Mentor junior engineers
- Participate in on-call rotation
- Collaborate with product and design teams

## Company Context
See: companies/stripe.md

Stripe is a leading payment infrastructure company with strong
engineering culture and high bar for talent.

## Application
- **Deadline:** Rolling
- **Link:** https://stripe.com/jobs/senior-backend-engineer
- **Status:** offered
- **Status History:**
  - 2024-01-15: Saved from job search
  - 2024-01-17: Applied with tailored resume
  - 2024-01-22: Recruiter screen scheduled
  - 2024-01-25: Recruiter screen completed - moving forward
  - 2024-02-01: Technical phone screen
  - 2024-02-08: Virtual onsite (4 rounds)
  - 2024-02-15: Offer received!

## Notes

### Interview Prep
- Review system design: rate limiting, payment queues
- Practice coding: graph algorithms, dynamic programming
- Research: Stripe's recent products, API design philosophy

### Offer Details
- Base: $195,000
- Equity: 5,000 RSUs over 4 years
- Sign-on: $25,000
- Benefits: Great healthcare, learning budget
- Decision deadline: Feb 22
```

## File Lifecycle

1. **Created** via `/job-search:ingest-job` or `/job-search:find-job-postings`
2. **Analyzed** with match scoring and gap analysis
3. **Updated** via `/job-search:update-job-status` as you progress
4. **Moved** between directories as status changes
5. **Archived** in `rejected/` or used for offer comparison
