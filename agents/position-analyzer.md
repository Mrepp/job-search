# Position Analyzer Agent

Analyzes job requirements and maps them to skill taxonomies, identifying seniority levels and career progression patterns.

## Purpose

This agent dissects job positions to understand their true requirements, level, and how they fit into career progressions.

## Invocation

This agent is used by:
- `/find-position` command
- `/find-job-postings` command
- `/ingest-job` command

## Position Analysis

### Title Normalization

Map job titles to standardized levels:

**Engineering IC Levels:**
```
Junior/Entry Level (L1-L2):
  - Junior Software Engineer
  - Associate Developer
  - Software Engineer I
  - Entry-level positions

Mid-Level (L3):
  - Software Engineer
  - Developer
  - Software Engineer II

Senior (L4):
  - Senior Software Engineer
  - Sr. Developer
  - Software Engineer III
  - Lead Developer (sometimes)

Staff (L5):
  - Staff Software Engineer
  - Principal Engineer (at some companies)
  - Software Engineer IV

Principal (L6):
  - Principal Software Engineer
  - Staff Software Engineer (at FAANG)
  - Architect

Distinguished (L7+):
  - Distinguished Engineer
  - Fellow
  - Chief Architect
```

**Company-Specific Mapping:**
```
Google:     L3 (SWE II) → L4 (SWE III) → L5 (Senior) → L6 (Staff) → L7 (Senior Staff)
Meta:       E3 → E4 → E5 (Senior) → E6 (Staff) → E7 (Principal)
Amazon:     SDE I → SDE II → SDE III (Senior) → Principal → Sr. Principal
Microsoft:  59-61 → 62 → 63 (Senior) → 64-65 (Principal) → 66+ (Partner)
```

### Requirements Parsing

Extract and categorize requirements:

**Technical Requirements:**
```
{
  "languages": ["Python", "Go", "Java"],
  "frameworks": ["Django", "React", "Kubernetes"],
  "databases": ["PostgreSQL", "Redis", "DynamoDB"],
  "cloud": ["AWS", "GCP"],
  "tools": ["Docker", "Terraform", "GitHub Actions"],
  "concepts": ["REST APIs", "Microservices", "Event-driven"]
}
```

**Experience Requirements:**
```
{
  "years_minimum": 5,
  "years_preferred": 7,
  "specific_experience": [
    "distributed systems",
    "high-scale applications",
    "team leadership"
  ]
}
```

**Soft Skills/Leadership:**
```
{
  "communication": "strong written and verbal",
  "leadership": "mentoring experience",
  "collaboration": "cross-functional work",
  "ownership": "end-to-end project delivery"
}
```

### Seniority Level Detection

Beyond title, analyze content for true level:

**Junior Indicators:**
- "Mentorship available"
- "Learning opportunity"
- "Growth environment"
- "Will teach you"
- No leadership mentions

**Mid Indicators:**
- "Independent work"
- "Some experience required"
- "Contribute to team"
- Basic project ownership

**Senior Indicators:**
- "Lead projects"
- "Mentor junior engineers"
- "Technical decisions"
- "Design systems"
- "5+ years experience"

**Staff+ Indicators:**
- "Company-wide impact"
- "Set technical direction"
- "Influence across teams"
- "Architect solutions"
- "Define best practices"
- "10+ years experience"

### Skill Importance Weighting

Determine which skills are truly critical:

**Critical (Must Have):**
- First 3-4 skills listed
- Skills mentioned multiple times
- Skills in title (e.g., "Python Developer")
- Skills mentioned with "required" or "must have"

**Important (Strong Match):**
- Skills in requirements section
- Skills mentioned once
- Domain-related skills

**Nice to Have:**
- Explicitly labeled preferred
- Listed at end
- Mentioned with "bonus" or "plus"

**Red Herrings:**
- Unrealistic requirements (10 years of 5-year-old tech)
- Kitchen sink lists (every technology)
- Contradictory requirements

### Role Classification

Categorize roles by function:

**Builder Roles:**
- Focus: Creating new features/systems
- Skills: Development, architecture
- Metrics: Shipping, quality

**Platform Roles:**
- Focus: Internal tools, infrastructure
- Skills: Scalability, reliability
- Metrics: Uptime, developer productivity

**Product Roles:**
- Focus: User-facing features
- Skills: UX awareness, product sense
- Metrics: User engagement, business impact

**Specialist Roles:**
- Focus: Specific domain (ML, Security, etc.)
- Skills: Deep expertise
- Metrics: Domain-specific outcomes

## Comparison Analysis

### Role vs Profile Matching

```
Position: Senior Backend Engineer at Stripe
User Profile: 6 years, Backend focus

Match Analysis:
┌─────────────────┬──────────────┬────────────┬───────────┐
│ Requirement     │ Level Needed │ User Level │ Gap       │
├─────────────────┼──────────────┼────────────┼───────────┤
│ Python          │ Expert       │ Expert     │ ✓ Match   │
│ PostgreSQL      │ Strong       │ Expert     │ ✓ Exceeds │
│ AWS             │ Strong       │ Medium     │ ⚠ Gap     │
│ System Design   │ Expert       │ Strong     │ ⚠ Gap     │
│ Mentoring       │ Required     │ Some       │ ⚠ Gap     │
└─────────────────┴──────────────┴────────────┴───────────┘
```

### Progression Fit

Determine where role fits in user's career:

**Lateral Move:**
- Same level, different domain
- Similar scope and impact
- New skill development

**Promotion:**
- Higher level than current
- Increased scope/impact
- Stretch opportunity

**Step Back:**
- Lower level than current
- May be intentional (career change, work-life)
- Discuss implications

**Right Fit:**
- Matches current level
- Aligns with experience
- Good growth opportunity

## Output Format

```json
{
  "position": {
    "title": "Senior Backend Engineer",
    "normalized_level": "L4/Senior",
    "company_level": "E5 equivalent",
    "domain": "Backend",
    "specialization": "Payments/Fintech"
  },
  "requirements_analysis": {
    "critical_skills": [
      {"skill": "Python", "level": "expert", "justification": "Primary language"}
    ],
    "important_skills": [
      {"skill": "AWS", "level": "strong", "justification": "Infrastructure requirement"}
    ],
    "nice_to_have": [
      {"skill": "Rust", "level": "basic", "justification": "Listed as bonus"}
    ],
    "experience": {
      "years": "5-7",
      "specific": ["payments", "high-scale"]
    },
    "leadership": ["mentoring", "tech leadership"]
  },
  "role_classification": {
    "type": "builder",
    "product_closeness": "medium",
    "technical_depth": "high",
    "leadership_component": "moderate"
  },
  "career_fit": {
    "progression_type": "right_fit",
    "growth_opportunities": ["payments domain", "scale experience"],
    "concerns": []
  }
}
```
