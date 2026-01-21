# /find-position

Identify career positions based on your skills and experience level, with career path mapping.

## Usage

```
/find-position [role/title]
```

## Examples

```
/find-position
/find-position senior software engineer
/find-position engineering manager
/find-position staff engineer
/find-position product manager
```

## Description

This command analyzes your profile and maps potential career paths, identifying roles you're qualified for now and progression paths for the future.

## Workflow

### 1. Load User Profile

Read `self/user.json` to get:
- Current title
- Years of experience
- Skills and confidence levels
- Target titles
- Industry preferences

### 2. Determine Current Level

Based on experience and title, identify:
- Current seniority tier (junior/mid/senior/staff/principal)
- Current domain (frontend, backend, fullstack, devops, etc.)
- Industry context

### 3. Research Career Paths

For the specified or target role:

**WebSearch for career information:**
- "{role} career path"
- "{role} career ladder"
- "{role} to {next level} progression"
- "{role} requirements {industry}"
- "{current title} to {target title} career change"

### 4. Build Career Tree

Create a structured career map:

**Current Position Assessment**
- How well user fits their current level
- Readiness for next level
- Alternative lateral moves

**Vertical Progression (Up)**
- Next level title
- Requirements to advance
- Typical timeline
- Skills needed
- Current gaps

**Lateral Moves (Sideways)**
- Adjacent roles at same level
- Required skill pivots
- Transferable skills
- Example paths

**Specialization Options**
- Deeper expertise paths
- Emerging specialties
- Certification opportunities

### 5. Gap Analysis

For each potential position:

**Skills Gap**
- Required skills not in profile
- Skills at lower confidence than needed
- New technologies to learn

**Experience Gap**
- Years of experience needed
- Type of experience needed (leadership, scale, domain)

**Credential Gap**
- Degrees or certifications helpful
- Portfolio/project needs

### 6. Save Career Tree

Create/update `career/career-tree.json`:

```json
{
  "generated_date": "ISO date",
  "profile_hash": "hash",
  "current_position": {
    "title": "Senior Software Engineer",
    "level": "senior",
    "domain": "backend",
    "years_at_level": 3,
    "readiness_score": 85
  },
  "vertical_paths": [
    {
      "target": "Staff Software Engineer",
      "readiness": 65,
      "timeline": "12-18 months",
      "key_gaps": ["system design leadership", "cross-team influence"],
      "suggested_actions": ["lead a major project", "mentor junior engineers"]
    },
    {
      "target": "Engineering Manager",
      "readiness": 50,
      "timeline": "18-24 months",
      "key_gaps": ["people management", "hiring experience"],
      "suggested_actions": ["request tech lead role", "participate in hiring"]
    }
  ],
  "lateral_paths": [
    {
      "target": "Platform Engineer",
      "readiness": 75,
      "timeline": "3-6 months",
      "overlap_skills": ["Python", "AWS", "system design"],
      "new_skills": ["Kubernetes", "Terraform"],
      "rationale": "Strong backend skills translate well"
    },
    {
      "target": "Solutions Architect",
      "readiness": 60,
      "timeline": "6-12 months",
      "overlap_skills": ["system design", "cloud", "communication"],
      "new_skills": ["pre-sales", "customer-facing"],
      "rationale": "Technical depth + client interaction"
    }
  ],
  "specializations": [
    {
      "specialty": "Distributed Systems",
      "current_skills": ["microservices", "message queues"],
      "growth_areas": ["consensus algorithms", "sharding"],
      "resources": ["DDIA book", "MIT 6.824"]
    }
  ]
}
```

### 7. Present Results

Display career map with:

**Current State Summary**
```
## Your Career Position

**Current:** Senior Software Engineer (Backend)
**Experience:** 7 years
**Level Fit:** Strong (85/100)
**Ready for Promotion:** Building toward Staff level
```

**Vertical Options**
```
### Promotion Paths

#### Staff Software Engineer
Readiness: ████████░░ 65%
Timeline: 12-18 months
Key Gaps:
- System design leadership
- Cross-team influence
Actions:
- Lead a major architectural initiative
- Mentor 2-3 engineers regularly
- Present at team/company tech talks
```

**Lateral Options**
```
### Lateral Moves

#### Platform Engineer
Readiness: ███████░░░ 75%
Timeline: 3-6 months
You Have: Python, AWS, system design
You Need: Kubernetes, Terraform
Why Consider: Leverages backend strength, high demand, often higher comp
```

**Skill Development**
```
### Recommended Focus Areas

1. **System Design Leadership** (for Staff path)
   - Lead RFC/design doc process
   - Resource: "Designing Data-Intensive Applications"

2. **Kubernetes** (for Platform path)
   - CKA certification path
   - Resource: KodeKloud courses
```

## Career Tree Visualization

```
                    Principal Engineer
                          ↑
                    Staff Engineer ←→ Engineering Manager
                          ↑                    ↑
    ┌─────────────────────┼─────────────────────┐
    │                     │                     │
Platform Engineer ←→ [YOU: Senior SWE] ←→ Tech Lead
    │                     │                     │
    └────→ SRE ←──────────┴──────────→ Solutions Architect
```

## Tools Used

- **WebSearch**: Research career paths and requirements
- **Read**: Load user profile
- **Write**: Save career tree
- **Glob**: Check for existing career data

## Error Handling

- If role is unfamiliar, research and clarify
- If no clear path, suggest exploration
- If profile is sparse, recommend /personal-analysis first
