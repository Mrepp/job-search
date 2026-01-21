# Company Researcher Agent

Autonomous agent for comprehensive company research, analyzing career pages, aggregating employee reviews, and producing detailed company profiles.

## Purpose

This agent performs multi-step web research to build a complete picture of a company, helping users make informed decisions about potential employers.

## Invocation

This agent is invoked by the `/job-search:find-company` command.

## Research Process

### Step 1: Initial Discovery

**For a specific company:**
1. WebSearch "{company name} official website"
2. WebSearch "{company name} careers"
3. Identify official domain and career page URL

**For criteria-based search:**
1. WebSearch "{criteria} companies hiring"
2. WebSearch "best {industry} companies {location}"
3. Build list of 5-10 candidate companies
4. Research each one

### Step 2: Career Page Analysis

WebFetch the career page and extract:

**Company Description**
- Mission statement
- Values
- Product/service overview

**Open Positions**
- Job titles
- Departments
- Locations (including remote options)
- Links to apply

**Benefits & Perks**
- Healthcare
- PTO policy
- Equity/stock
- Professional development
- Unique perks

**Tech Stack (if visible)**
- Programming languages
- Frameworks
- Cloud providers
- Tools

### Step 3: Employee Sentiment Analysis

**Glassdoor Research**
1. WebSearch "{company} Glassdoor reviews"
2. WebFetch Glassdoor page (if accessible)
3. Extract:
   - Overall rating (X/5)
   - CEO approval %
   - Recommend to friend %
   - Review count
   - Top pros (most mentioned)
   - Top cons (most mentioned)
   - Interview experience

**Reddit/Blind Research**
1. WebSearch "site:reddit.com {company} working at"
2. WebSearch "{company} Blind reviews"
3. Look for:
   - Candid employee experiences
   - Compensation discussions
   - Work-life balance comments
   - Management quality

**LinkedIn Analysis**
1. WebSearch "{company} LinkedIn company"
2. Note:
   - Employee count
   - Growth rate
   - Common job titles
   - Employee backgrounds

### Step 4: Company Background

**General Information**
1. WebSearch "{company} about founded"
2. WebSearch "{company} Wikipedia"
3. Extract:
   - Founded year
   - Founders
   - Headquarters
   - Funding history (if private)
   - Stock info (if public)
   - Employee count

**Recent News**
1. WebSearch "{company} news {current year}"
2. Look for:
   - Funding announcements
   - Product launches
   - Layoffs or hiring sprees
   - Leadership changes
   - Acquisitions

### Step 5: Red Flag Detection

Watch for these warning signs:

**High Turnover Indicators**
- Many recent job postings for same role
- Short average employee tenure
- Reviews mentioning constant hiring

**Culture Issues**
- Low Glassdoor rating (<3.0)
- Frequent mentions of:
  - Long hours / work-life balance
  - Poor management
  - Lack of career growth
  - Political environment

**Financial Concerns**
- Recent layoffs
- Struggling to raise funding
- Negative revenue news
- Key executives leaving

**Communication Style**
- Vague job descriptions
- Unrealistic requirements
- No salary transparency

### Step 6: Relevance Scoring

Calculate a 0-100 score based on user profile:

```
Location Match (0-25):
  - Perfect match: 25
  - Remote available + user prefers: 25
  - Hybrid when user wants hybrid: 20
  - Close proximity: 15
  - No match: 0

Industry Match (0-25):
  - Exact match: 25
  - Related industry: 15
  - User has no preference: 20
  - Mismatch: 5

Skills Match (0-25):
  - 80%+ tech stack overlap: 25
  - 50-80% overlap: 20
  - 30-50% overlap: 15
  - <30% overlap: 10

Culture Match (0-25):
  - High Glassdoor + good WLB: 25
  - Mixed signals: 15
  - Red flags present: 5
```

## Output Format

### Company Markdown File

```markdown
# {Company Name}

## Overview
- **Industry:** {industry}
- **Size:** {employee count}
- **Location(s):** {locations}
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
- ...

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
- [Crunchbase]({url}) (if applicable)

---
*Research conducted: {ISO date}*
*Profile hash: {user profile hash at time of research}*
```

## Error Handling

- If career page is blocked, note "Limited career page access"
- If Glassdoor has no reviews, note "Insufficient review data"
- If company is very new, adjust expectations and note data limitations
- Always indicate confidence level in analysis
