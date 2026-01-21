# Company Files Data Structure

Documentation for company research file format and organization.

## Overview

Company research is stored in `companies/{company-name}.md` as markdown files containing structured analysis.

## File Location

```
companies/
├── stripe.md
├── anthropic.md
├── linear.md
└── vercel.md
```

## File Template

```markdown
# {Company Name}

## Overview
- **Industry:** {industry}
- **Size:** {employee count}
- **Location(s):** {headquarters and offices}
- **Founded:** {year}
- **Status:** {Private/Public - Series X / NYSE: XXX}

## Company Description
{2-3 paragraph description of what the company does}

## Culture Analysis

### Values & Mission
{Company's stated values and how they manifest}

### Work Environment
{Analysis based on reviews and research}

### Growth Opportunities
{Career development, learning, promotion paths}

## Employee Sentiment

### Glassdoor Summary
- **Overall Rating:** {X}/5 ({count} reviews)
- **Would Recommend:** {X}%
- **CEO Approval:** {X}%

### Key Positives
- {positive 1}
- {positive 2}
- {positive 3}

### Key Concerns
- {concern 1}
- {concern 2}
- {concern 3}

### Interview Experience
{Summary of interview process from reviews}

## Tech Stack
{Languages, frameworks, cloud, tools used}

## Benefits & Perks
- {benefit 1}
- {benefit 2}
- {benefit 3}

## Red Flags
{Any concerning patterns identified, or "None identified"}

## Relevance Score: {X}/100

### Score Breakdown
| Category | Score | Reasoning |
|----------|-------|-----------|
| Location | X/25 | {reason} |
| Industry | X/25 | {reason} |
| Skills | X/25 | {reason} |
| Culture | X/25 | {reason} |

### Summary
{2-3 sentence summary of why this company is/isn't a good fit}

## Open Positions

| Title | Location | Type |
|-------|----------|------|
| [{title}]({url}) | {location} | {full-time/contract} |

## Sources
- [Career Page]({url})
- [Glassdoor]({url})
- [LinkedIn]({url})
- [Crunchbase]({url})

---
*Research conducted: {ISO date}*
*Profile hash: {user profile hash}*
```

## Section Details

### Overview Section

Basic company facts:

| Field | Description |
|-------|-------------|
| Industry | Primary industry (e.g., "Fintech", "Developer Tools") |
| Size | Employee count or range |
| Location(s) | HQ and major offices |
| Founded | Year established |
| Status | Funding stage or public ticker |

### Culture Analysis

Three subsections providing culture insights:

**Values & Mission:**
- Official stated values
- How they appear in practice
- Alignment with user preferences

**Work Environment:**
- Pace and pressure level
- Work-life balance indicators
- Remote work culture
- Team dynamics

**Growth Opportunities:**
- Internal mobility
- Learning and development
- Promotion velocity
- Leadership development

### Employee Sentiment

Aggregated from Glassdoor, Blind, Reddit:

| Metric | Description |
|--------|-------------|
| Overall Rating | Glassdoor star rating |
| Would Recommend | Percentage who'd recommend to friend |
| CEO Approval | Percentage approving of CEO |
| Key Positives | Most frequently mentioned pros |
| Key Concerns | Most frequently mentioned cons |

### Tech Stack

Technologies used by the company:

```markdown
## Tech Stack
**Languages:** Python, Go, TypeScript
**Frontend:** React, Next.js
**Backend:** GraphQL, REST APIs
**Databases:** PostgreSQL, Redis, DynamoDB
**Cloud:** AWS (EKS, Lambda, S3)
**Tools:** Terraform, GitHub Actions, Datadog
```

### Red Flags

Warning signs identified during research:

- High turnover indicators
- Recent layoffs
- Poor management reviews
- Financial concerns
- Culture issues

If none found: "None identified based on available data"

### Relevance Score

Personalized score (0-100) based on user profile:

**Location Match (25 points):**
- Remote available + user prefers remote: 25
- Location matches user's location: 25
- Hybrid available: 15
- No match: 0

**Industry Match (25 points):**
- Matches target industry: 25
- Related industry: 15
- Any (no preference): 20

**Skills Match (25 points):**
- High overlap with user skills: 25
- Moderate overlap: 15
- Low overlap: 10

**Culture Match (25 points):**
- High ratings + user preference alignment: 25
- Mixed signals: 15
- Red flags present: 5

### Open Positions

Table of relevant current openings:

| Column | Description |
|--------|-------------|
| Title | Job title with link to posting |
| Location | Where the job is based |
| Type | Full-time, contract, etc. |

### Sources

Links to research sources for verification.

### Metadata

Footer with:
- Research date
- Profile hash (for tracking staleness)

## Example File

```markdown
# Stripe

## Overview
- **Industry:** Fintech / Payments
- **Size:** ~8,000 employees
- **Location(s):** San Francisco, CA (HQ); Dublin, Singapore, Remote
- **Founded:** 2010
- **Status:** Private - Last valued at $50B

## Company Description
Stripe builds economic infrastructure for the internet. Businesses
of all sizes use Stripe's software and APIs to accept payments,
send payouts, and manage their businesses online.

The company is known for its developer-focused approach, with
industry-leading API documentation and developer experience.
Stripe has expanded beyond payments into fraud prevention,
business incorporation, and financial services.

## Culture Analysis

### Values & Mission
Stripe emphasizes "users first" and rigorous thinking. The culture
is intellectually driven with a focus on long-term impact over
short-term metrics.

### Work Environment
Known for high-quality talent and ambitious projects. Can be
intense but generally respects work-life balance. Strong writing
culture with emphasis on clear communication.

### Growth Opportunities
Good internal mobility. Known for investing in employee development.
Clear engineering levels with promotion opportunities.

## Employee Sentiment

### Glassdoor Summary
- **Overall Rating:** 4.2/5 (2,847 reviews)
- **Would Recommend:** 82%
- **CEO Approval:** 91%

### Key Positives
- Exceptional talent and smart colleagues
- Interesting technical challenges
- Strong compensation and benefits
- Remote-friendly culture

### Key Concerns
- Intense pace can lead to burnout
- Rapid growth creating growing pains
- Some teams more chaotic than others

### Interview Experience
Rigorous 5-6 round process. Heavy emphasis on coding and system
design. Take-home project for some roles. Generally positive
candidate experience with prompt communication.

## Tech Stack
**Languages:** Ruby, Go, Java, Python, TypeScript
**Databases:** MongoDB, Redis, PostgreSQL
**Cloud:** AWS
**Tools:** Kubernetes, Terraform, Custom internal tools

## Benefits & Perks
- Competitive base + equity
- Comprehensive health insurance
- $10K/year learning budget
- Remote work options
- Generous parental leave
- Home office setup stipend

## Red Flags
None identified based on available data.

## Relevance Score: 92/100

### Score Breakdown
| Category | Score | Reasoning |
|----------|-------|-----------|
| Location | 25/25 | Remote available, matches preference |
| Industry | 25/25 | Fintech matches target industry |
| Skills | 22/25 | Strong Python, Go overlap |
| Culture | 20/25 | High ratings, intense pace noted |

### Summary
Excellent match based on industry alignment, remote availability, and
tech stack overlap. High bar for hiring but strong career opportunity.

## Open Positions

| Title | Location | Type |
|-------|----------|------|
| [Senior Backend Engineer](https://stripe.com/jobs/123) | Remote | Full-time |
| [Staff Software Engineer](https://stripe.com/jobs/456) | SF/Remote | Full-time |
| [Platform Engineer](https://stripe.com/jobs/789) | Remote | Full-time |

## Sources
- [Career Page](https://stripe.com/jobs)
- [Glassdoor](https://glassdoor.com/stripe)
- [LinkedIn](https://linkedin.com/company/stripe)

---
*Research conducted: 2024-01-20T10:00:00Z*
*Profile hash: a1b2c3d4e5*
```

## Updating Company Files

Company research can become stale. Consider refreshing when:
- More than 3 months old
- Major company news (funding, layoffs)
- Before applying to their positions
- Before interviews

Run `/find-company {name}` to update existing research.
