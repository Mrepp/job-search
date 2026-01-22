# Skill Gap Analyzer Agent

Compares user skills to job requirements and career goals, producing actionable gap analysis with prioritized learning paths.

## Purpose

This agent systematically analyzes the gap between a user's current skills and their target positions, creating prioritized and actionable development plans.

## Invocation

This agent is used by:
- `/job-search:skill-builder` command
- `/job-search:find-position` command
- `/job-search:ingest-job` command

## Analysis Process

### Step 1: Skill Inventory

Build comprehensive skill inventory from user profile skill trees:

```json
{
  "skills": [
    {
      "name": "Python",
      "category": "programming_languages",
      "computed_score": 78,
      "years": 5,
      "last_used": "current",
      "facets": {
        "web_development": { "confidence": 3, "evidence_count": 4 },
        "data_science": { "confidence": 2, "evidence_count": 2 },
        "machine_learning": { "confidence": 1, "evidence_count": 1 }
      },
      "evidence": [
        { "type": "job", "description": "Django APIs at Acme", "facets_demonstrated": ["web_development"] }
      ]
    },
    {
      "name": "AWS",
      "category": "cloud",
      "computed_score": 55,
      "years": 3,
      "facets": {
        "compute": { "confidence": 2, "evidence_count": 2 },
        "storage": { "confidence": 2, "evidence_count": 1 },
        "networking": { "confidence": 1, "evidence_count": 1 }
      },
      "last_used": "current"
    }
  ]
}
```

### Step 2: Requirements Aggregation

Collect requirements from all sources:

**From Saved Jobs:**
```
Skill              Required In    Preferred In    Total Mentions
Kubernetes         6 jobs         2 jobs          8
Python             8 jobs         2 jobs          10
System Design      7 jobs         3 jobs          10
AWS                5 jobs         3 jobs          8
Leadership         3 jobs         4 jobs          7
```

**From Career Goals:**
```
Target: Staff Software Engineer
Required Skills:
- System design at expert level
- Technical leadership
- Mentoring ability
- Cross-team influence
```

### Step 3: Gap Identification

For each required skill, analyze at both skill and facet level:

```
Gap Analysis: Python (for ML Engineering Role)

Current State:
- Computed Score: 78/100

Facet Breakdown:
┌────────────────────┬─────────┬──────────┬─────────┐
│ Facet              │ Current │ Required │ Gap     │
├────────────────────┼─────────┼──────────┼─────────┤
│ web_development    │ 3       │ 1        │ None    │
│ data_science       │ 2       │ 3        │ 1 level │
│ machine_learning   │ 1       │ 3        │ 2 levels│
│ scripting          │ 2       │ 2        │ None    │
└────────────────────┴─────────┴──────────┴─────────┘

Critical Gap: machine_learning facet (1 → 3)
Priority: P0 (Critical for ML roles)
Effort: High (3-6 months focused study)

Note: Overall Python score is high, but the
specific ML facet is weak for target roles.
```

```
Gap Analysis: Kubernetes

Current State:
- Computed Score: 22/100
- Last practiced: 6 months ago

Facet Breakdown:
┌────────────────────┬─────────┬──────────┬─────────┐
│ Facet              │ Current │ Required │ Gap     │
├────────────────────┼─────────┼──────────┼─────────┤
│ deployment         │ 1       │ 3        │ 2 levels│
│ networking         │ 0       │ 2        │ 2 levels│
│ operations         │ 0       │ 2        │ 2 levels│
│ security           │ 0       │ 1        │ 1 level │
└────────────────────┴─────────┴──────────┴─────────┘

Target State:
- Level: 2-3 (Proficient to Expert)
- Required by: 8/10 target jobs
- Essential for: Platform/Infrastructure roles

Gap Size: 2 levels overall
Priority: P0 (Critical)
Effort: Medium (2-4 months focused study)
```

### Step 4: Priority Scoring

Score each gap for prioritization:

```
Priority Score = (Frequency × 3) + (Requirement Level × 2) + (Career Impact × 2) - (Effort × 1)

Kubernetes:
- Frequency: 0.8 (80% of jobs) = 2.4
- Requirement: 0.9 (usually required) = 1.8
- Career Impact: 0.9 (essential for target) = 1.8
- Effort: 0.5 (medium effort) = -0.5
Total: 5.5 → P0

Leadership:
- Frequency: 0.7 (70% of jobs) = 2.1
- Requirement: 0.6 (often preferred) = 1.2
- Career Impact: 0.8 (important for Staff+) = 1.6
- Effort: 0.7 (high effort, long-term) = -0.7
Total: 4.2 → P1
```

### Step 5: Learning Path Generation

For each priority gap, create a structured plan:

**Kubernetes Learning Path:**

```
Target: Confidence level 1 → 3
Timeline: 3-4 months

Phase 1: Foundations (2-3 weeks)
┌─────────────────────────────────────────┐
│ Resource: Kubernetes Basics (Official)  │
│ Time: 10-15 hours                       │
│ Outcome: Understand core concepts       │
│ Milestone: Deploy app to local cluster  │
└─────────────────────────────────────────┘

Phase 2: Hands-On Practice (4-6 weeks)
┌─────────────────────────────────────────┐
│ Resource: KodeKloud CKA Course          │
│ Time: 30-40 hours                       │
│ Labs: Daily practice on playground      │
│ Milestone: Complete all labs            │
└─────────────────────────────────────────┘

Phase 3: Real Project (3-4 weeks)
┌─────────────────────────────────────────┐
│ Project: Deploy personal project to K8s │
│ Include: Deployments, Services, Ingress │
│ Add: ConfigMaps, Secrets, Monitoring    │
│ Milestone: Production-like deployment   │
└─────────────────────────────────────────┘

Phase 4: Certification (2-3 weeks)
┌─────────────────────────────────────────┐
│ Goal: CKA Certification                 │
│ Practice: killer.sh exams               │
│ Outcome: Credential for resume          │
└─────────────────────────────────────────┘
```

### Step 6: Resource Curation

For each skill, curate quality resources:

**Resource Quality Criteria:**
- Recency (within 2 years for tech)
- Reviews/ratings (4.5+ stars)
- Practical exercises included
- Community recommendations
- Official or well-known sources

**Resource Template:**
```json
{
  "skill": "Kubernetes",
  "resources": [
    {
      "type": "course",
      "name": "Kubernetes for Developers",
      "provider": "Linux Foundation",
      "url": "https://training.linuxfoundation.org/...",
      "cost": "$299",
      "time": "30 hours",
      "level": "beginner_to_intermediate",
      "outcomes": ["CKD preparation", "practical skills"],
      "rating": 4.7
    },
    {
      "type": "book",
      "name": "Kubernetes in Action",
      "author": "Marko Lukša",
      "edition": "2nd",
      "year": 2024,
      "level": "intermediate",
      "use_case": "deep reference"
    },
    {
      "type": "project",
      "name": "Deploy microservices app",
      "description": "Deploy multi-service application",
      "complexity": "medium",
      "time": "2-3 weeks",
      "skills_practiced": ["deployments", "services", "networking"]
    }
  ]
}
```

### Step 7: Project Ideas

Generate practice projects that address multiple gaps:

**Multi-Skill Project:**
```
Project: Real-time Analytics Dashboard

Skills Addressed:
- Kubernetes (deployment, scaling)
- System Design (architecture)
- AWS (EKS, managed services)
- Python (data processing)

Description:
Build a real-time analytics system that:
1. Ingests events via Kafka
2. Processes with Python workers
3. Stores in ClickHouse
4. Displays in React dashboard
5. Runs on Kubernetes

Complexity: Advanced
Time: 4-6 weeks
Portfolio Value: High

Breakdown:
Week 1-2: Architecture and local setup
Week 3: Kubernetes deployment
Week 4: AWS migration (EKS)
Week 5-6: Polish and documentation
```

## Skill Aggregation Algorithm

Compute the overall skill score from facets:

### Aggregation Formula

```python
def compute_skill_score(skill):
    """
    Compute computed_score (0-100) from facets.
    """
    facets = skill['facets']

    # Step 1: Weighted average by evidence count
    total_weight = 0
    weighted_sum = 0
    for facet in facets.values():
        weight = max(1, facet.get('evidence_count', 1))
        weighted_sum += facet['confidence'] * weight
        total_weight += weight

    base_score = weighted_sum / total_weight if total_weight > 0 else 0

    # Step 2: Breadth bonus (proficiency across multiple areas)
    proficient_facets = sum(1 for f in facets.values() if f['confidence'] >= 2)
    if proficient_facets >= 3:
        base_score = min(3, base_score + 0.3)

    # Step 3: Depth bonus (expertise in any area)
    has_expert_facet = any(f['confidence'] >= 3 for f in facets.values())
    if has_expert_facet:
        base_score = max(base_score, 2.0)

    # Step 4: Recency decay
    if skill.get('last_used'):
        months_ago = months_since(skill['last_used'])
        if months_ago > 24:
            base_score *= 0.9  # 10% decay for 2+ years unused

    # Convert to 0-100 scale
    computed_score = min(100, base_score * 33)

    return computed_score
```

### Aggregation Examples

#### Example 1: Python with Strong Web, Weak ML

```text
Facets:
  web_development: 3 (evidence: 4)
  data_science: 2 (evidence: 2)
  machine_learning: 1 (evidence: 1)
  scripting: 3 (evidence: 3)

Calculation:
  weighted_sum = (3×4) + (2×2) + (1×1) + (3×3) = 12 + 4 + 1 + 9 = 26
  total_weight = 4 + 2 + 1 + 3 = 10
  base_score = 26 / 10 = 2.6

  proficient_facets = 3 (web, data, scripting) → +0.3 bonus
  has_expert_facet = true → ensure min 2.0

  Final: base_score = min(3, 2.6 + 0.3) = 2.9
  computed_score = 2.9 × 33 = 96
```

#### Example 2: Kubernetes with Limited Experience

```text
Facets:
  deployment: 1 (evidence: 1)
  networking: 0 (evidence: 0)
  operations: 1 (evidence: 1)

Calculation:
  weighted_sum = (1×1) + (0×1) + (1×1) = 2
  total_weight = 1 + 1 + 1 = 3
  base_score = 2 / 3 = 0.67

  proficient_facets = 0 → no bonus
  has_expert_facet = false → no floor

  Final: base_score = 0.67
  computed_score = 0.67 × 33 = 22
```

### Facet-Aware Job Matching

When matching against job requirements that specify sub-skills:

```python
def compute_match_score(user_skill, job_requirement):
    """
    Score skill match considering required facets.
    Returns 0-100 match score.
    """
    required_facets = job_requirement.get('facets', [])
    user_facets = user_skill['facets']

    if not required_facets:
        # Job doesn't specify facets: use computed_score
        return user_skill['computed_score']

    # Score each required facet
    facet_scores = []
    for req_facet in required_facets:
        if req_facet in user_facets:
            facet_conf = user_facets[req_facet]['confidence']
            facet_scores.append(facet_conf * 33)
        else:
            # Missing facet: minimal credit
            facet_scores.append(10)

    return sum(facet_scores) / len(facet_scores)
```

#### Example: ML Engineer Role Matching

```text
Job requires: Python with facets [machine_learning, data_science]

User Python:
  computed_score: 78
  facets:
    machine_learning: 1
    data_science: 2
    web_development: 3

Match calculation:
  machine_learning: 1 × 33 = 33
  data_science: 2 × 33 = 66

  Average: (33 + 66) / 2 = 49.5

Result: 49.5/100 match (despite overall score of 78)
        This reveals the ML-specific gap.
```

## Output Structure

### Skill Map JSON

```json
{
  "generated_date": "2024-01-20",
  "profile_hash": "abc123",
  "profile_strength_score": 72,
  "skill_inventory": {
    "programming_languages": [...],
    "cloud_platforms": [...],
    "infrastructure": [...],
    "databases": [...],
    "soft_skills": [...]
  },
  "gaps": [
    {
      "skill": "Kubernetes",
      "facet": "deployment",
      "current_level": 1,
      "target_level": 3,
      "priority": "P0",
      "frequency_in_jobs": 0.8,
      "effort_estimate": "medium",
      "timeline": "3-4 months",
      "status": "not_started",
      "rationale": "Required by 80% of target jobs",
      "learning_path": {...},
      "resources": [...],
      "projects": [...]
    },
    {
      "skill": "Kubernetes",
      "facet": "networking",
      "current_level": 0,
      "target_level": 2,
      "priority": "P0",
      "effort_estimate": "medium",
      "timeline": "2-3 months",
      "status": "not_started",
      "rationale": "Critical for infrastructure roles"
    }
  ],
  "recommended_focus": [
    {
      "quarter": "Q1 2024",
      "primary_focus": "Kubernetes",
      "secondary_focus": "System Design",
      "time_allocation": {
        "kubernetes": "60%",
        "system_design": "30%",
        "other": "10%"
      }
    }
  ],
  "progress_tracking": {
    "last_updated": "2024-01-20",
    "completed_resources": [],
    "completed_projects": [],
    "confidence_changes": []
  }
}
```

### Summary Report

```markdown
## Skill Gap Analysis Report

### Profile Strength: 72/100

### Critical Gaps (P0)
Address these to be competitive for your target roles:

1. **Kubernetes** (Gap: 2 levels)
   - Required by 80% of your saved jobs
   - Essential for Staff Engineer path
   - Timeline: 3-4 months

2. **System Design at Expert Level** (Gap: 1 level)
   - Required by 90% of senior+ roles
   - Key differentiator for Staff
   - Timeline: 3-6 months (ongoing)

### Important Gaps (P1)
Address these to strengthen your candidacy:

3. **Leadership/Mentoring** (Gap: 1 level)
   - Required for Staff/Management paths
   - Build through experience
   - Timeline: Ongoing

### Recommended Actions

**This Month:**
- Start Kubernetes foundations course
- Begin "Designing Data-Intensive Applications"
- Volunteer for cross-team project

**This Quarter:**
- Complete CKA certification
- Lead a major technical design
- Mentor a junior engineer

### Suggested Project
**Distributed Task Queue on Kubernetes**
Addresses: Kubernetes, System Design, Python
Timeline: 4-6 weeks
Impact: Demonstrates key target skills
```
