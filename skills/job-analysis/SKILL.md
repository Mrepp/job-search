# Job Analysis

Knowledge module for parsing job descriptions, extracting requirements, and interpreting job postings.

## Job Description Parsing Patterns

### Title Normalization

**Seniority Levels**
```
Entry Level:
  - Junior, Associate, Entry-level
  - I, Level 1
  - New Grad, Recent Graduate

Mid Level:
  - (no prefix), II
  - Mid-level, Intermediate

Senior:
  - Senior, Sr., III
  - Lead (sometimes)

Staff/Principal:
  - Staff, Principal, IV
  - Distinguished
  - Architect

Management:
  - Manager, Engineering Manager
  - Director
  - VP, Head of
```

**Role Types**
```
Engineering:
  - Software Engineer, Developer, Programmer
  - Full Stack, Frontend, Backend
  - Platform, Infrastructure, Systems
  - DevOps, SRE, Cloud

Product:
  - Product Manager, PM
  - Product Owner
  - Technical Program Manager

Design:
  - UX Designer, UI Designer
  - Product Designer
  - Design Engineer

Data:
  - Data Scientist, Data Engineer
  - ML Engineer, AI Engineer
  - Analytics Engineer
```

### Requirements Extraction

**Required vs Preferred**

Look for these patterns:

**Required Indicators:**
- "Must have", "Required"
- "X+ years of experience with"
- "Strong background in"
- "Proficiency in"
- "Demonstrated experience"
- Listed first or under "Requirements"

**Preferred Indicators:**
- "Nice to have", "Preferred"
- "Bonus points for"
- "Experience with X is a plus"
- "Familiarity with"
- Listed under "Preferred" or at end

**Extracting Years of Experience:**
```
Pattern: "(\\d+)\\+?\\s*(years?|yrs?)"
Examples:
  - "5+ years" → min: 5, max: null
  - "3-5 years" → min: 3, max: 5
  - "at least 7 years" → min: 7, max: null
```

**Extracting Skills:**
```
Look for:
- Bullet points starting with technology names
- "Experience with X, Y, and Z"
- "Tech stack includes:"
- "You'll work with:"
- "Proficiency in X required"
```

### Company Size Indicators

**Startup Signals:**
- "Fast-paced environment"
- "Wear many hats"
- "Ground floor opportunity"
- "Equity compensation"
- Team size mentioned (< 50)

**Growth Company Signals:**
- "Series B/C/D funded"
- "Scaling rapidly"
- "Building out the team"
- "High growth"

**Enterprise Signals:**
- "Fortune 500"
- "Global presence"
- "Established processes"
- "Cross-functional collaboration"
- Formal job levels (E5, L6)

## Salary Range Estimation

### When Not Posted

**Research Methods:**
1. Check Levels.fyi for company
2. Search Glassdoor salary reports
3. Use Blind salary discussions
4. Reference similar role postings

**Estimation Factors:**
- Company stage and funding
- Location (adjust for COL)
- Seniority level
- Industry (fintech pays more than non-profit)
- Company reputation

### Salary Bands by Level (2024 US Tech)

**Entry Level (0-2 years)**
- Median: $80-100k
- Range: $70-130k
- FAANG/top-tier: $120-180k

**Mid Level (2-5 years)**
- Median: $120-150k
- Range: $100-180k
- FAANG/top-tier: $180-250k

**Senior (5-8 years)**
- Median: $160-200k
- Range: $140-250k
- FAANG/top-tier: $250-350k

**Staff+ (8+ years)**
- Median: $220-280k
- Range: $180-400k+
- FAANG/top-tier: $350-600k+

### Location Adjustments

```
San Francisco Bay Area: 1.0x (baseline)
New York City: 0.95x
Seattle: 0.95x
Los Angeles: 0.90x
Austin: 0.85x
Denver/Boulder: 0.85x
Chicago: 0.80x
Remote (US): 0.85x (varies)
```

## Remote Work Policy Interpretation

### Fully Remote

**Strong Indicators:**
- "100% remote"
- "Work from anywhere"
- "Distributed team"
- No office location listed
- "Remote-first"

**Verification:**
- Check if they have office
- Look for geographic restrictions
- Ask about timezone requirements

### Hybrid

**Common Patterns:**
- "Hybrid" or "Flexible"
- "X days in office"
- "Office available"
- Location listed + remote mentioned

**Questions to Clarify:**
- How many days in office?
- Is it enforced?
- What about fully remote exceptions?

### Remote-Tolerant (Not First)

**Warning Signs:**
- "Remote possible" but office emphasized
- Leadership is all in one location
- "Prefer local candidates"
- Meeting times assume one timezone

### Geographic Restrictions

**Common Restrictions:**
- "Remote (US only)"
- "Remote (specific states)"
- "Must be within X hours of EST"
- "Remote in US, UK, or Canada"

**Why Restrictions Exist:**
- Tax/legal complexity
- Timezone overlap needs
- Benefits administration
- Government contracts

## Red Flags in Job Postings

### Unrealistic Requirements

**Signs:**
- "10 years of Kubernetes experience" (impossible)
- Every technology stack listed
- Conflicting requirements
- Senior title, entry pay

**What It Means:**
- HR wrote without engineering input
- Listing is a wish list, not reality
- May be flexible in practice

### Vague Descriptions

**Signs:**
- No specific technologies mentioned
- Responsibilities are generic
- "Various projects"
- No team context

**What It Means:**
- Role is undefined
- May be assigned to whatever
- Less career growth clarity

### Culture Red Flags

**Warning Phrases:**
- "Work hard, play hard"
- "Family environment" (boundaries issues)
- "Startup mentality" (at large company)
- "Passionate about working nights/weekends"
- No work-life balance mention

### Process Red Flags

**Warning Signs:**
- Posted for 6+ months
- Multiple recruiter contacts
- Overly complex application
- Request for work samples before interview
- No response timeline

## Interview Process Signals

### Healthy Process

- Clear timeline communicated
- Reasonable number of rounds (3-5)
- Diverse interviewers
- Questions allowed throughout
- Prompt feedback

### Concerning Process

- 7+ interview rounds
- Long gaps without updates
- Same questions repeated
- No clear decision maker
- Pressure tactics
