# /skill-builder

Analyze skill gaps and create development plans.

## Usage

```
/skill-builder
/skill-builder [focus area]
```

## Examples

```
/skill-builder
/skill-builder kubernetes
/skill-builder "system design"
/skill-builder leadership
```

## Description

Analyzes your skills against career goals and saved jobs, creating prioritized learning plans.

## What It Does

1. **Loads your data** - Profile, jobs, career goals
2. **Aggregates requirements** - From all sources
3. **Identifies gaps** - Current vs needed skills
4. **Prioritizes development** - By impact and effort
5. **Creates learning plans** - Resources and projects
6. **Saves skill map** - To `career/skill-map.json`

## Gap Priority Levels

| Priority | Criteria | Action |
|----------|----------|--------|
| P0 | Required by 80%+ of jobs | Address immediately |
| P1 | Required by 50-80% | This quarter |
| P2 | Required by 20-50% | Nice to have |
| P3 | Less than 20% | Optional |

## Output

Shows a development dashboard:

```
## Skill Development Dashboard

### Profile Strength: 72/100

### P0 - Critical Gaps

1. **Kubernetes** (0 → 2)
   Timeline: 2-3 months
   Resource: CKA certification path

2. **System Design** (2 → 3)
   Timeline: 3-4 months
   Resource: DDIA book + mock interviews

### Recommended Project
**Distributed Task Queue**
Covers: Kubernetes, System Design, Python
Time: 4-6 weeks
```

## Focus Mode

Specify a skill for deep dive:

```
/skill-builder kubernetes
```

Returns:
- Detailed learning path
- Phased timeline
- Curated resources
- Multiple project ideas
- Certification guidance

## Resources Included

- **Courses:** Recommended online courses
- **Books:** Key reading material
- **Projects:** Hands-on practice ideas
- **Certifications:** Relevant credentials
- **Communities:** Groups to join

## Tips

- Run regularly to track progress
- Update profile as skills improve
- Focus on P0 gaps first
- Use projects to build multiple skills
