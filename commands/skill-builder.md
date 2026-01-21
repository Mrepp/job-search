# /skill-builder

Map your skills, identify gaps, and create personalized improvement plans.

## Usage

```
/skill-builder
/skill-builder [focus area]
```

## Examples

```
/skill-builder
/skill-builder system design
/skill-builder kubernetes
/skill-builder leadership skills
```

## Description

This command analyzes your current skills against your career goals and saved job postings, creating a prioritized skill development plan with actionable resources.

## Workflow

### 1. Load Profile and Career Data

Gather:
- `self/user.json` - Current skills with confidence levels
- `career/career-tree.json` - Target positions and gaps
- `career/skill-map.json` - Previous skill analysis (if exists)
- `jobs/interested/*.md` - Saved job requirements

### 2. Aggregate Skill Requirements

From saved jobs and target positions, build a requirements list:

```
Required Skill        Frequency    Priority    Your Level
Kubernetes            8/10 jobs    P0          1 (Basic)
System Design         9/10 jobs    P0          2 (Proficient)
Python                10/10 jobs   P0          3 (Expert)
AWS                   7/10 jobs    P1          2 (Proficient)
Leadership            5/10 jobs    P1          1 (Basic)
Terraform             4/10 jobs    P2          0 (None)
```

### 3. Identify Gaps

Categorize gaps by priority:

**P0 - Critical Gaps:**
- Required by 80%+ of target jobs
- Listed as "must have"
- Essential for target level

**P1 - Important Gaps:**
- Required by 50-80% of target jobs
- Listed as "preferred"
- Important for advancement

**P2 - Nice to Have:**
- Required by 20-50% of target jobs
- Complementary skills
- Future-proofing

**P3 - Optional:**
- Required by <20% of jobs
- Specialized or niche
- Can learn on the job

### 4. Create Skill Map

Build comprehensive skill visualization:

**By Category:**
```
Programming Languages:
  ████████████████ Python (3/3) - Expert
  ████████████░░░░ JavaScript (2/3) - Proficient
  ████████░░░░░░░░ Go (1/3) - Basic
  ░░░░░░░░░░░░░░░░ Rust (0/3) - None

Infrastructure:
  ████████████░░░░ AWS (2/3) - Proficient
  ████████░░░░░░░░ Docker (1/3) - Basic
  ░░░░░░░░░░░░░░░░ Kubernetes (0/3) - Gap!
```

**Gap Overlay:**
```
Skill               You    Target    Gap    Priority
Kubernetes          0      2         2      P0
System Design       2      3         1      P0
Leadership          1      2         1      P1
Terraform           0      2         2      P2
```

### 5. Generate Learning Plans

For each prioritized gap:

**Assessment:**
- Current level
- Target level
- Effort estimate
- Timeline

**Resources:**
- Online courses
- Books
- Practice projects
- Certifications
- Communities

**Milestones:**
- Learning checkpoints
- Project goals
- Confidence level targets

### 6. Generate Project Ideas

For skill development through practice:

**Template:**
```
## Project: {Name}

**Target Skills:** {skills}
**Difficulty:** Beginner/Intermediate/Advanced
**Estimated Time:** {duration}

### Description
{What to build}

### Learning Objectives
- {objective 1}
- {objective 2}

### Suggested Approach
1. {step 1}
2. {step 2}

### Resources
- {resource 1}
- {resource 2}

### Success Criteria
- {criterion 1}
- {criterion 2}
```

### 7. Save Skill Map

Create/update `career/skill-map.json`:

```json
{
  "generated_date": "ISO date",
  "profile_hash": "hash",
  "skill_inventory": {
    "programming_languages": [
      {"name": "Python", "confidence": 3, "years": 5, "status": "current"},
      {"name": "JavaScript", "confidence": 2, "years": 3, "status": "current"}
    ],
    "infrastructure": [...],
    "databases": [...],
    "tools": [...],
    "soft_skills": [...]
  },
  "gaps": [
    {
      "skill": "Kubernetes",
      "current_level": 0,
      "target_level": 2,
      "priority": "P0",
      "effort": "medium",
      "timeline": "2-3 months",
      "status": "not_started"
    }
  ],
  "learning_plans": [
    {
      "skill": "Kubernetes",
      "resources": [...],
      "projects": [...],
      "milestones": [...],
      "started_date": null,
      "completed_date": null
    }
  ],
  "progress_history": [
    {
      "date": "ISO date",
      "updates": [...]
    }
  ]
}
```

### 8. Present Results

**Summary Dashboard:**
```
## Skill Development Dashboard

### Profile Strength: 72/100
Based on match against your target roles

### Priority Gaps

#### P0 - Critical (Address Now)
1. **Kubernetes** - 0/3 → target 2/3
   Timeline: 2-3 months
   Top Resource: CKA Certification Path

2. **System Design** - 2/3 → target 3/3
   Timeline: 3-4 months
   Top Resource: "Designing Data-Intensive Applications"

#### P1 - Important (Next Quarter)
3. **Leadership Skills** - 1/3 → target 2/3
   Timeline: Ongoing
   Top Resource: Seek tech lead opportunities

### Recommended Project
**Build a Distributed Task Queue**
Covers: Kubernetes, System Design, Python
Time: 4-6 weeks
```

## Tools Used

- **Read**: Load profile and job files
- **Write**: Save skill map
- **Glob**: Find saved jobs and career data
- **WebSearch**: Find learning resources
- **AskUserQuestion**: Clarify preferences

## Focus Areas

When a focus area is specified:

**/skill-builder kubernetes**
- Deep dive on Kubernetes specifically
- Comprehensive learning path
- Detailed resource list
- Multiple project ideas
- Certification guidance

**/skill-builder leadership**
- Focus on soft skills
- Book recommendations
- Mentorship suggestions
- Opportunities to seek

## Progress Tracking

The skill map tracks:
- When skills were added
- Confidence level changes over time
- Learning plan progress
- Completed resources and projects
