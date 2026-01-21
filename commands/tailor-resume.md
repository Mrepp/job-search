# /tailor-resume

Generate a tailored resume for a specific job posting.

## Usage

```
/tailor-resume [job-file]
/tailor-resume [company-title]
```

## Examples

```
/tailor-resume jobs/interested/stripe-senior-engineer.md
/tailor-resume stripe-senior-engineer
/tailor-resume "Stripe Senior Engineer"
```

## Description

This command creates a customized version of your resume optimized for a specific job posting, emphasizing relevant skills and experience while maintaining authenticity.

## Workflow

### 1. Load Source Materials

**Job Posting:**
- Read the specified job file
- Extract requirements (required/preferred)
- Note key skills and responsibilities
- Identify important keywords

**Master Resume:**
- Read `self/resume/main-resume.md`
- Parse existing content
- Identify all skills, experiences, projects

**Profile:**
- Read `self/user.json` for context
- Load experience files from `self/experience/`
- Load project files from `self/projects/`

### 2. Analyze Job-Resume Alignment

**Keyword Mapping:**
```
Job Keyword       Resume Mentions    Action
Python            5 mentions         Maintain
Kubernetes        0 mentions         Add if applicable
Leadership        2 mentions         Emphasize
Fintech           1 mention          Expand
```

**Experience Relevance:**
```
Experience                 Relevance   Tailor
Backend at CurrentCo       High        Lead with this
Intern at StartupX         Low         Minimize/remove
Project: Payment System    High        Expand details
```

### 3. Generate Tailored Content

**Summary/Objective:**
- Rewrite to address the specific role
- Incorporate key requirements
- Match their language and priorities

**Experience Section:**
- Reorder to put relevant experience first
- Expand bullet points for relevant work
- Add metrics that match their priorities
- Reduce space for less relevant roles

**Skills Section:**
- Reorder skills by relevance to job
- Use their exact terminology
- Group skills matching their categories

**Projects Section:**
- Highlight projects using required technologies
- Add projects that demonstrate needed skills
- Remove projects that aren't relevant

### 4. Optimization Checks

**Keyword Optimization:**
- Ensure key required skills appear
- Match their terminology exactly
- Include acronyms they use
- Avoid keyword stuffing

**ATS Compatibility:**
- Use standard section headers
- Avoid complex formatting
- Include skills in context
- Use text (not images/tables)

**Length Management:**
- Senior roles: 1-2 pages
- Junior roles: 1 page
- Prioritize relevant content

### 5. Generate Diff

Show what changed from master resume:

```diff
## Summary

- Experienced backend engineer with 7 years building scalable systems.
+ Senior Backend Engineer with 7 years building high-scale payment
+ systems and distributed architectures. Passionate about fintech
+ and financial infrastructure.

## Experience

### Backend Engineer at CurrentCo
- Built and maintained REST APIs serving 1M+ requests/day
+ Architected and maintained REST APIs serving 1M+ requests/day,
+ including payment processing endpoints handling $50M+ monthly volume

+ ### Key Achievement (NEW)
+ Led migration from monolith to microservices, reducing deployment
+ time by 80% and enabling team to ship features 3x faster
```

### 6. Save Tailored Resume

Save to `self/resume/tailored/{company}-{title}.md`:

```markdown
# {Your Name}

## Tailored for: {Job Title} at {Company}
Generated: {date}
Job File: {path to job file}
Master Resume Hash: {hash}

---

## Summary
{Tailored summary}

## Experience

### {Relevant Role 1}
**{Company}** | {Dates}
- {Tailored bullet 1}
- {Tailored bullet 2}
...

### {Relevant Role 2}
...

## Skills

### Core Technologies
{Reordered and emphasized skills}

### Additional Skills
{Supporting skills}

## Projects

### {Relevant Project 1}
{Description emphasizing job-relevant aspects}

## Education
{Standard education section}

---

## Tailoring Notes

### Changes from Master Resume:
- Summary rewritten for {target role}
- Emphasized {relevant experience}
- Reordered skills to highlight {relevant skills}
- Added detail to {project} showing {relevant work}
- Removed/minimized {irrelevant sections}

### Keywords Incorporated:
- {keyword 1} (required) - appears X times
- {keyword 2} (required) - appears X times
- {keyword 3} (preferred) - appears X times

### Alignment Score: X/100
```

### 7. Present Results

Display:
- Summary of changes made
- Before/after comparison for key sections
- Keyword coverage report
- Alignment score improvement
- File location for the tailored resume

## Tailoring Guidelines

### DO:
- Reorder existing content for relevance
- Expand on genuinely relevant experience
- Use their terminology where accurate
- Quantify achievements that matter to them
- Match their formatting preferences

### DON'T:
- Fabricate experience or skills
- Claim expertise you don't have
- Keyword stuff irrelevantly
- Copy their job description verbatim
- Remove important authentic content

### Emphasis Techniques

**Quantify Relevantly:**
```
Before: Built APIs
After: Built REST APIs processing $10M+ in daily transactions
(when applying to fintech)
```

**Match Context:**
```
Before: Implemented caching layer
After: Implemented Redis caching layer reducing latency by 60%
(when they require Redis experience)
```

**Use Their Words:**
```
Job says: "cross-functional collaboration"
Resume: "Led cross-functional collaboration between engineering,
         product, and design teams"
```

## Tools Used

- **Read**: Load job file, master resume, experience files
- **Write**: Save tailored resume
- **Glob**: Find related files

## Output Formats

The tailored resume is saved in markdown format. For PDF/Word export:
- Recommend using pandoc or similar tool
- Suggest online converters
- Note formatting may need adjustment
