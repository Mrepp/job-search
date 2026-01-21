# /find-company

Research companies based on your criteria including location, industry, size, and culture preferences.

## Usage

```
/find-company [company-name or criteria]
```

## Examples

```
/find-company Stripe
/find-company fintech companies in San Francisco
/find-company remote-friendly startups in developer tools
/find-company enterprise software companies with good work-life balance
```

## Description

This command performs deep research on companies to help you identify potential employers that align with your preferences and values.

## Workflow

### 1. Parse User Criteria

Extract search parameters from the user input:
- **Specific company name** - Direct lookup
- **Industry** - fintech, healthcare, developer tools, etc.
- **Location** - City, state, or "remote"
- **Size** - startup, mid-size, enterprise
- **Culture keywords** - work-life balance, fast-paced, collaborative

### 2. Load User Profile

Read `self/user.json` to get:
- Remote work preference
- Target industries
- Location preferences
- Current skills (for relevance matching)

### 3. Company Research

For each company found or specified:

**Career Page Analysis**
- WebSearch for "{company} careers" and "{company} jobs"
- WebFetch the career page
- Extract:
  - Open positions (especially matching user's target roles)
  - Company values and mission
  - Benefits and perks
  - Tech stack (if available)
  - Office locations

**Employee Reviews**
- WebSearch for "{company} Glassdoor reviews"
- WebSearch for "{company} employee reviews Reddit"
- WebSearch for "{company} Blind reviews" (for tech companies)
- Aggregate:
  - Overall rating
  - Pros mentioned frequently
  - Cons mentioned frequently
  - CEO approval
  - Recommendation rate

**Company Information**
- WebSearch for "{company} about" and "{company} wikipedia"
- Extract:
  - Industry
  - Founded date
  - Company size
  - Headquarters location
  - Funding/public status
  - Recent news

### 4. Calculate Relevance Score

Score 0-100 based on user profile match:

**Location Match (25 points)**
- Remote available + user prefers remote: 25
- Location matches user's location: 25
- Hybrid available: 15
- No match: 0

**Industry Match (25 points)**
- Matches target industry: 25
- Related industry: 15
- Any industry (user has no preference): 20

**Skills Match (25 points)**
- Company tech stack matches user skills: 0-25 based on overlap

**Culture Match (25 points)**
- Based on review analysis vs user preferences
- Work-life balance indicators
- Growth opportunities
- Compensation competitiveness

### 5. Save Company Profile

Create/update `companies/{company-name}.md`:

```markdown
# {Company Name}

## Overview
- **Industry:**
- **Size:**
- **Location(s):**
- **Founded:**
- **Status:** Private/Public

## Culture Analysis
[Analysis of company culture based on research]

## Employee Sentiment
- **Glassdoor Rating:** X/5
- **Would Recommend:** X%
- **CEO Approval:** X%
- **Key Positives:**
  - {positive points}
- **Key Concerns:**
  - {negative points}

## Tech Stack
- {technologies used}

## Relevance Score: X/100
**Breakdown:**
- Location Match: X/25
- Industry Match: X/25
- Skills Match: X/25
- Culture Match: X/25

**Reasoning:**
[Explanation of score]

## Open Positions
- [{Title}]({url}) - {location}
- ...

## Sources
- [Career Page]({url})
- [Glassdoor]({url})
- [LinkedIn]({url})

## Research Date
{ISO date}
```

### 6. Present Results

Display:
- Company overview
- Relevance score with reasoning
- Key pros and cons
- Matching open positions
- Offer to save or explore further

## Tools Used

- **WebSearch**: Find company pages, reviews, and information
- **WebFetch**: Retrieve detailed content from career pages and review sites
- **Read**: Load user profile
- **Write**: Save company research
- **Glob**: Check for existing company files

## Error Handling

- If no career page found, note limited information
- If reviews are sparse, indicate low confidence in culture analysis
- If company is very new/small, adjust expectations for available data
