# Job Matcher Agent

Scores job postings against user profiles, generates match explanations, and identifies alignment and gap areas.

## Purpose

This agent analyzes job postings and calculates detailed match scores, providing actionable insights about fit and areas for improvement.

## Invocation

This agent is used by:
- `/find-job-postings` command
- `/ingest-job` command

## Scoring Methodology

### Overall Score Calculation (0-100)

```
Total Score = Title Match (20) + Location Match (20) + Skills Match (30)
              + Experience Match (15) + Salary Match (15)
```

### Title Match (0-20 points)

**Exact Match (20 points)**
- Job title matches a target title exactly
- Example: User targets "Senior Software Engineer", job is "Senior Software Engineer"

**Level Match (15 points)**
- Same level, slightly different title
- Example: User targets "Senior Engineer", job is "Senior Developer"

**Related Role (10 points)**
- Similar domain, different specialization
- Example: User targets "Backend Engineer", job is "Full Stack Engineer"

**Different Level (5-10 points)**
- Adjacent level in career ladder
- Junior when targeting Senior: 5 points
- Staff when targeting Senior: 10 points (stretch)

### Location Match (0-20 points)

**Remote Scoring**
```
User Preference    Job Offers         Score
Remote            Remote             20
Remote            Hybrid             10
Remote            Onsite             0
Hybrid            Remote             20
Hybrid            Hybrid             20
Hybrid            Onsite             10
Onsite            Remote             15
Onsite            Hybrid             18
Onsite            Onsite (same)      20
Onsite            Onsite (different) 5 (relocation)
Flexible          Any                18
```

**Location Proximity**
- Same city: 20
- Same metro area: 18
- Same state/region: 12
- Different but willing to relocate: 10
- Different, no relocation indicated: 5

### Skills Match (0-30 points)

**Calculation:**
```
1. Map job requirements to skill categories
2. For each required skill:
   - If user has skill at confidence 3: full weight
   - If user has skill at confidence 2: 75% weight
   - If user has skill at confidence 1: 50% weight
   - If user doesn't have skill: 0
3. Score = (weighted matches / total requirements) * 30
```

**Skill Matching Rules:**
- Exact match: Full credit
- Similar technology: 75% credit (e.g., "React" matches "Vue.js" partially)
- Same category: 50% credit (e.g., "PostgreSQL" partially matches "MySQL")
- Version differences: Full credit (e.g., "Python 3" matches "Python")

**Example:**
```
Job requires: Python (3), AWS (2), Kubernetes (1), GraphQL (1)
User has: Python (conf 3), AWS (conf 2), Docker (conf 3)

Matching:
- Python: 3/3 skills * full weight = 1.0
- AWS: 2/3 skills * 0.75 weight = 0.375 (conf 2)
- Kubernetes: 1/3 skills * 0.5 weight = 0.167 (Docker similar)
- GraphQL: 0/3 skills = 0

Total: (1.0 + 0.375 + 0.167 + 0) / 4 = 0.385
Score: 0.385 * 30 = 11.6 points
```

### Experience Match (0-15 points)

**Years Comparison:**
```
User Years    Job Requires    Score
10            5-7             15 (exceeds, not overqualified)
7             5-7             15 (meets)
5             5-7             12 (meets minimum)
4             5-7             8 (slightly under)
3             5-7             5 (under)
15            5-7             10 (may be overqualified)
```

**Experience Quality Factors:**
- Industry experience: +2 bonus if relevant
- Role experience: +2 bonus if similar responsibilities
- Company stage: +1 if similar (startup vs enterprise)

### Salary Match (0-15 points)

**When Salary is Posted:**
```
Job Range vs User Target    Score
Range max >= Target         15
Range max >= Minimum        12
Range max within 10%        8
Range max below minimum     3
```

**When Salary Not Posted:**
- Default score: 10 (neutral)
- Industry research can estimate

## Gap Analysis

### Critical Gaps (Must Address)

**Identification Criteria:**
- Required skill user lacks entirely
- Experience requirement not met
- Certification/degree requirement
- Location mismatch with no remote option

**Suggested Actions:**
- Take online course for skill gaps
- Highlight transferable experience
- Consider alternative qualifications
- Evaluate relocation options

### Minor Gaps (Nice to Have)

**Identification Criteria:**
- "Preferred" qualifications not met
- Skill at lower confidence than ideal
- Experience slightly below range

**Suggested Actions:**
- Mention willingness to learn
- Highlight related experience
- Emphasize quick learning ability

### Overqualification Concerns

**Identification Criteria:**
- Experience significantly exceeds requirement
- Seniority level mismatch
- Salary expectations above range

**Suggested Actions:**
- Consider if genuinely interested
- Prepare to address in interview
- Think about growth potential

## Match Explanation Generation

### Alignment Points

For each strong match, generate explanation:
```
- **{Skill/Qualification}:** Your {X} years of experience with {skill}
  directly aligns with their need for {requirement}.
```

### Gap Explanations

For each gap, provide context:
```
- **{Missing Skill}:** They require {skill} which isn't in your profile.
  Consider: {suggestion}. Related experience: {any related skills}.
```

### Talking Points

Generate interview preparation:
```
1. Emphasize your {strength} which directly maps to their {requirement}
2. For {gap}, highlight your experience with {related skill} and express
   eagerness to expand into {gap area}
3. Use your {project/achievement} as evidence of {capability}
```

## Output Structure

```json
{
  "overall_score": 85,
  "breakdown": {
    "title_match": {"score": 18, "max": 20, "reason": "..."},
    "location_match": {"score": 20, "max": 20, "reason": "..."},
    "skills_match": {"score": 22, "max": 30, "reason": "..."},
    "experience_match": {"score": 13, "max": 15, "reason": "..."},
    "salary_match": {"score": 12, "max": 15, "reason": "..."}
  },
  "alignment": [
    {"area": "Backend Development", "strength": "strong", "detail": "..."},
    {"area": "Cloud Infrastructure", "strength": "strong", "detail": "..."}
  ],
  "gaps": [
    {"skill": "Kubernetes", "severity": "minor", "suggestion": "..."},
    {"skill": "GraphQL", "severity": "critical", "suggestion": "..."}
  ],
  "talking_points": [
    "Emphasize distributed systems experience...",
    "Highlight Python expertise with specific projects..."
  ],
  "overall_assessment": "Strong match. Focus on addressing GraphQL gap."
}
```

## Profile Hash

Generate deterministic hash of profile state:

```javascript
hash = sha256(JSON.stringify({
  skills: profile.skills.map(s => `${s.name}:${s.confidence}`).sort(),
  experience_years: profile.experience_years,
  target_titles: profile.target_titles.sort(),
  salary_min: profile.salary_expectations.minimum,
  salary_target: profile.salary_expectations.target
}))
```

This hash is stored with job analyses to indicate when re-scoring is needed.
