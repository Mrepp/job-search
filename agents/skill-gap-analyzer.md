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

Build comprehensive skill inventory from user profile:

```json
{
  "skills": [
    {
      "name": "Python",
      "category": "programming_languages",
      "confidence": 3,
      "years": 5,
      "evidence": ["primary language at current job", "multiple projects"],
      "last_used": "current"
    },
    {
      "name": "AWS",
      "category": "cloud",
      "confidence": 2,
      "years": 3,
      "evidence": ["EC2, S3, Lambda usage"],
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

For each required skill:

```
Gap Analysis: Kubernetes

Current State:
- Level: 1 (Basic)
- Evidence: Docker experience, read documentation
- Last practiced: 6 months ago

Target State:
- Level: 2-3 (Proficient to Expert)
- Required by: 8/10 target jobs
- Essential for: Platform/Infrastructure roles

Gap Size: 2 levels (1 → 3)
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
      "category": "infrastructure",
      "current_level": 1,
      "target_level": 3,
      "priority": "P0",
      "frequency_in_jobs": 0.8,
      "effort_estimate": "medium",
      "timeline": "3-4 months",
      "status": "not_started",
      "learning_path": {...},
      "resources": [...],
      "projects": [...]
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
