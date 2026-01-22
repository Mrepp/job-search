# /skill-builder

Map your skills, identify gaps, and create personalized improvement plans.

## Usage

```
/skill-builder
/skill-builder [focus area]
/skill-builder deep-dive [skill]
```

## Examples

```
/skill-builder
/skill-builder system design
/skill-builder kubernetes
/skill-builder leadership skills
/skill-builder deep-dive python
```

## Description

This command analyzes your current skills against your career goals and saved job postings, creating a prioritized skill development plan with actionable resources.

## Workflow

### 1. Load Profile and Career Data

Gather:

- `self/user.json` - Current skill trees with facets
- `career/career-tree.json` - Target positions and gaps
- `career/skill-map.json` - Previous skill analysis (if exists)
- `jobs/interested/*.md` - Saved job requirements

### 2. Aggregate Skill Requirements

From saved jobs and target positions, build a requirements list:

```
Required Skill        Frequency    Priority    Your Score
Kubernetes            8/10 jobs    P0          22/100
System Design         9/10 jobs    P0          66/100
Python                10/10 jobs   P0          78/100
AWS                   7/10 jobs    P1          55/100
Leadership            5/10 jobs    P1          33/100
Terraform             4/10 jobs    P2          0/100
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

**By Category (with facet breakdown):**
```
Programming Languages:
  Python (78/100)
    ├─ web_development    ███████████████░ 3/3
    ├─ data_science       ██████████░░░░░░ 2/3
    └─ machine_learning   █████░░░░░░░░░░░ 1/3

  JavaScript (55/100)
    ├─ frontend           ███████████████░ 3/3
    └─ backend            █████░░░░░░░░░░░ 1/3

Infrastructure:
  Kubernetes (22/100) - Gap!
    ├─ deployment         █████░░░░░░░░░░░ 1/3
    ├─ networking         ░░░░░░░░░░░░░░░░ 0/3
    └─ operations         ░░░░░░░░░░░░░░░░ 0/3
```

**Facet Gap Overlay:**
```
Skill.Facet                  You    Target    Gap    Priority
Kubernetes.deployment        1      3         2      P0
Kubernetes.networking        0      2         2      P0
Python.machine_learning      1      3         2      P0
System Design.distributed    2      3         1      P1
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
      {
        "name": "Python",
        "computed_score": 78,
        "years": 5,
        "facets": {
          "web_development": { "display": "Web Development", "level": 3 },
          "data_science": { "display": "Data Science", "level": 2 },
          "machine_learning": { "display": "Machine Learning", "level": 1 }
        }
      }
    ],
    "infrastructure": [...],
    "databases": [...],
    "tools": [...],
    "soft_skills": [...]
  },
  "gaps": [
    {
      "skill": "Kubernetes",
      "facet": "deployment",
      "current_level": 1,
      "target_level": 3,
      "priority": "P0",
      "effort": "medium",
      "timeline": "2-3 months",
      "status": "not_started",
      "rationale": "Required by 80% of target jobs"
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

#### P0 - Critical Facet Gaps
1. **Kubernetes.deployment** - 1/3 → target 3/3
   Timeline: 2-3 months
   Top Resource: CKA Certification Path

2. **Python.machine_learning** - 1/3 → target 3/3
   Timeline: 3-4 months
   Top Resource: "Hands-On ML with Scikit-Learn"

#### P1 - Important Facet Gaps
3. **System Design.distributed** - 2/3 → target 3/3
   Timeline: Ongoing
   Top Resource: "Designing Data-Intensive Applications"

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

## Deep-Dive Mode

When invoked with `deep-dive [skill]`, provides detailed sub-skill (facet) analysis:

### Deep-Dive Usage

```
/skill-builder deep-dive python
/skill-builder deep-dive kubernetes
/skill-builder deep-dive aws
```

### Deep-Dive Workflow

1. **Load Skill Taxonomy**

   Check `schemas/skill-taxonomy.schema.json` for predefined facets.
   If skill not found, generate facets on-demand from context.

2. **Present Facet Assessment**

   Quick 5-question assessment for major facets:

   ```
   Let's map your Python expertise in detail.
   Rate each area 1-3 (or 'skip' if unsure):

   1. Web Development (Django, Flask, APIs): ___
   2. Data Science (Pandas, NumPy, analysis): ___
   3. Machine Learning (TensorFlow, PyTorch): ___
   4. Scripting & Automation (CLI, pipelines): ___
   5. DevOps & Tooling (pytest, packaging): ___
   ```

3. **Infer from Evidence**

   Before asking, check existing evidence:
   - Resume mentions
   - Experience files in `self/experience/`
   - Projects in `self/projects/`

   Pre-fill confidence levels from evidence, ask user to confirm/adjust.

4. **Generate Facet Map**

   ```
   Python Skill Tree
   ═══════════════════════════════════════

   Web Development        ███████████████░ 3/3 Expert
     └─ Django, Flask, FastAPI, REST APIs

   Data Science           ██████████░░░░░░ 2/3 Proficient
     └─ Pandas, NumPy, Jupyter

   Machine Learning       █████░░░░░░░░░░░ 1/3 Basic
     └─ scikit-learn

   Scripting/Automation   ███████████████░ 3/3 Expert
     └─ Click, asyncio, pipelines

   DevOps & Tooling       ██████████░░░░░░ 2/3 Proficient
     └─ pytest, poetry, mypy

   ═══════════════════════════════════════
   Computed Score: 78/100
   ```

5. **Identify Facet Gaps**

   Compare against job requirements that specify sub-skills:

   ```
   Facet Gap Analysis (vs. ML Engineer roles)
   ───────────────────────────────────────

   ⚠️  Machine Learning: You have 1, roles need 3
       This is your critical gap for ML positions.

   ⚠️  Data Science: You have 2, roles need 3
       Important gap - strengthen analysis skills.

   ✓  Web Development: Exceeds requirements
   ✓  Scripting: Meets requirements
   ```

6. **Generate Targeted Learning Path**

   Focus resources on weak facets:

   ```
   Priority: Strengthen Python ML Facet (1 → 3)

   Phase 1: Foundations (2-3 weeks)
   - Course: "Machine Learning A-Z" (Udemy)
   - Book: "Hands-On ML with Scikit-Learn"

   Phase 2: Deep Learning (4-6 weeks)
   - Course: "Deep Learning Specialization" (Coursera)
   - Framework: PyTorch or TensorFlow

   Phase 3: Project (3-4 weeks)
   - Build: ML-powered feature for existing project
   - Goal: Production-quality ML pipeline
   ```

7. **Update Profile**

   Save skill tree to user profile:

   ```json
   {
     "name": "Python",
     "years": 5,
     "facets": {
       "web_development": { "confidence": 3, "inferred": false },
       "data_science": { "confidence": 2, "inferred": false },
       "machine_learning": { "confidence": 1, "inferred": false }
     },
     "computed_score": 78
   }
   ```

### Project-Based Inference

Alternative to direct questions - ask about projects:

```
Tell me about a significant Python project you've worked on.
What did you build and what technologies did you use?
```

From the response, infer facet levels:

- "Built Django REST APIs" → web_development: 2-3
- "Data pipeline with Pandas" → data_science: 2
- "ML recommendation engine" → machine_learning: 2-3

## Progress Tracking

The skill map tracks:

- When skills were added
- Facet level changes over time
- Learning plan progress
- Completed resources and projects
- Evidence accumulated per facet
