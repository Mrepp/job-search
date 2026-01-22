# Skill Assessment

Knowledge module for evaluating and scoring professional skills using faceted skill trees.

## Skill Tree and Facets

Skills are not monolithic - they have **facets** (sub-skills) that capture depth in specific areas. For example, "Python" encompasses web development, data science, ML, and scripting - a user may be expert in some facets but basic in others.

### Facet Structure

Each skill is a tree with facets (sub-skills) that have independent confidence levels:

```json
{
  "name": "Python",
  "years": 5,
  "facets": {
    "web_development": { "confidence": 3, "components": ["Django", "FastAPI"] },
    "data_science": { "confidence": 2, "components": ["Pandas", "NumPy"] },
    "machine_learning": { "confidence": 1, "components": ["scikit-learn"] }
  },
  "computed_score": 78
}
```

### Facet Confidence Levels

Each facet uses a 0-3 scale:

- **Level 3 (Expert)**: 5+ years, can mentor others, deep understanding
- **Level 2 (Proficient)**: 2-5 years, works independently, knows best practices
- **Level 1 (Basic)**: <2 years, understands concepts, can complete basic tasks
- **Level 0 (None)**: No experience with this facet

### Facet Inference

Facets are **inferred from evidence** (low friction) rather than manually rated:

1. **Resume parsing** - Extract context around skill mentions
2. **Experience file mining** - Link technologies to facets
3. **Project analysis** - Infer depth from project descriptions

See `schemas/skill-taxonomy.schema.json` for predefined facets and keywords.

### Aggregation Rules

The `computed_score` (0-100) is derived from facets:

1. **Weighted average** by evidence count per facet
2. **Breadth bonus** - 3+ proficient facets adds +0.3 to base
3. **Depth bonus** - Expert in any facet ensures minimum base of 2.0
4. **Recency decay** - 10% penalty if unused for 2+ years

See `agents/skill-gap-analyzer.md` for the full algorithm.

## Skill Taxonomy

### Technical Skills

**Programming Languages**
- General purpose: Python, JavaScript, Java, C++, Go, Rust
- Scripting: Bash, PowerShell, Ruby, Perl
- Data: SQL, R, Julia
- Systems: C, Assembly
- Mobile: Swift, Kotlin, Dart
- Web: TypeScript, PHP

**Frameworks & Libraries**
- Frontend: React, Vue, Angular, Svelte
- Backend: Node.js, Django, Flask, Spring, Rails
- Mobile: React Native, Flutter, SwiftUI
- Data: Pandas, NumPy, TensorFlow, PyTorch

**Databases**
- Relational: PostgreSQL, MySQL, SQLite, Oracle
- NoSQL: MongoDB, Redis, DynamoDB, Cassandra
- Graph: Neo4j, Neptune
- Search: Elasticsearch, Solr

**Cloud & Infrastructure**
- Providers: AWS, GCP, Azure
- Containers: Docker, Kubernetes
- IaC: Terraform, CloudFormation, Pulumi
- CI/CD: GitHub Actions, Jenkins, CircleCI

**Tools & Practices**
- Version control: Git
- Methodologies: Agile, Scrum, Kanban
- Testing: Unit, Integration, E2E
- Monitoring: Prometheus, Grafana, Datadog

### Soft Skills

**Communication**
- Written communication
- Verbal presentation
- Technical writing
- Stakeholder management

**Leadership**
- Team management
- Mentoring
- Project management
- Decision making

**Problem Solving**
- Analytical thinking
- Debugging
- System design
- Root cause analysis

**Collaboration**
- Cross-functional work
- Remote collaboration
- Code review
- Pair programming

## Gap Prioritization Framework

### Priority Levels

**P0 - Critical Gaps**
- Required in >80% of target job postings
- Listed as "must have" or "required"
- Fundamental to the role
- Blocking factor for applications

**P1 - Important Gaps**
- Required in 50-80% of postings
- Listed as "preferred" or "nice to have"
- Significantly improves candidacy
- Differentiator in interviews

**P2 - Nice to Have**
- Required in 20-50% of postings
- Adjacent or complementary skill
- Shows breadth of knowledge
- Future-proofing

**P3 - Optional**
- Required in <20% of postings
- Specialized or niche
- Company-specific
- Can be learned on the job

### Effort Assessment

**Quick Wins (1-2 weeks)**
- Similar to existing skills
- Good documentation/tutorials
- Can build small project to demonstrate
- Online course available

**Medium Investment (1-3 months)**
- New paradigm or approach
- Requires practice projects
- Certification available
- Book or course recommended

**Long-term Development (3-12 months)**
- Fundamentally different skillset
- Requires real-world experience
- Mentorship helpful
- Major career pivot

## Learning Resource Recommendations

### By Skill Type

**Programming Languages**
- Official documentation
- "Learn X the Hard Way" books
- Exercism.io for practice
- LeetCode for algorithms

**Frameworks**
- Official tutorials
- Udemy/Coursera courses
- YouTube tutorials
- Build a project

**Cloud/Infrastructure**
- Cloud provider free tiers
- Official certifications
- A Cloud Guru / Linux Academy
- Hands-on labs

**System Design**
- "Designing Data-Intensive Applications"
- System Design Primer (GitHub)
- ByteByteGo newsletter
- Mock interviews

### Resource Quality Indicators

**High Quality:**
- Official documentation
- Well-reviewed courses (4.5+ stars)
- Recent publication (last 2 years)
- Hands-on projects included
- Active community

**Avoid:**
- Outdated materials (3+ years old)
- No practical exercises
- Poorly reviewed
- Incomplete coverage
- No community support
