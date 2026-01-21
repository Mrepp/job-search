# Complete Job Search Workflow

A comprehensive guide to running a full job search using the plugin.

## Overview

This workflow covers the entire job search process from initial setup to offer negotiation.

## Phase 1: Foundation

### Set Up Your Profile

```
/personal-analysis
```

Ensure you have:
- [ ] Complete work history
- [ ] All relevant skills listed
- [ ] Accurate confidence scores
- [ ] Clear salary expectations
- [ ] Defined target titles and industries

### Define Your Criteria

Before searching, clarify:
- **Role type** - IC, management, or open to both?
- **Company stage** - Startup, growth, or enterprise?
- **Remote policy** - Must be remote, or flexible?
- **Industry preferences** - Specific industries or any?
- **Must-haves** - Non-negotiable requirements?

## Phase 2: Research

### Research Target Companies

Start with companies you're already interested in:

```
/find-company Stripe
/find-company Anthropic
/find-company Linear
```

Then discover new companies matching your criteria:

```
/find-company "remote-first developer tools startups"
/find-company "fintech companies with engineering blogs"
```

Review the generated company files in `companies/` and note:
- Relevance scores
- Culture analysis
- Red flags (if any)
- Open positions

### Build a Target List

Create a shortlist of 10-15 companies you're most interested in, ordered by:
1. Culture/values alignment
2. Role availability
3. Compensation potential
4. Growth opportunities

## Phase 3: Job Discovery

### Search for Positions

Search broadly first:

```
/find-job-postings senior software engineer remote
```

Then refine based on results:

```
/find-job-postings backend engineer fintech
/find-job-postings "staff engineer" "developer tools"
```

### Evaluate Match Scores

For each result, review:
- **Overall score** - Is it 80+? Good match.
- **Skills match** - Any critical gaps?
- **Experience match** - Right level?
- **Salary match** - Meets expectations?

### Save Interesting Positions

Save positions scoring 75+ to `jobs/interested/`:

```
# The command will offer to save positions
/find-job-postings

# Or ingest specific jobs you find
/ingest-job https://example.com/job
```

## Phase 4: Deep Analysis

### Analyze Your Top Choices

For your top 5-10 saved jobs, review:

1. **Read the full analysis** in `jobs/interested/`
2. **Check the company file** in `companies/`
3. **Identify specific gaps** to address
4. **Note talking points** for interviews

### Address Skill Gaps

Run the skill builder:

```
/skill-builder
```

For critical gaps (P0):
- Start learning immediately
- Don't wait to apply—start in parallel
- Be honest about current level in applications

For minor gaps (P1-P2):
- Mention willingness to learn
- Highlight related experience
- Plan to develop after landing a role

## Phase 5: Application

### Prepare Your Resume

For each job you're applying to:

```
/tailor-resume stripe-senior-engineer
```

Review the tailored resume:
- Does it emphasize relevant experience?
- Are key requirements addressed?
- Is the terminology matching?

### Submit Applications

Track your applications:

```
/update-job-status stripe-senior-engineer applied
```

Add notes about:
- Application date
- Application method
- Materials submitted
- Any referral or contact

### Manage Your Pipeline

Keep 10-20 applications active:
- Too few = high risk of dry spells
- Too many = can't prepare properly

Check your pipeline:

```
/update-job-status
```

This shows all jobs by status.

## Phase 6: Interview Process

### Track Interview Progress

As you progress:

```
/update-job-status stripe-senior-engineer interviewed
```

Add notes for each stage:
- Interviewers and their roles
- Topics discussed
- How it went
- Next steps mentioned

### Prepare Using Your Data

Before each interview, review:
- Company file for culture/product info
- Job file for requirements alignment
- Gap analysis for honest discussions
- Talking points for what to emphasize

### Handle Rejections

When rejected:

```
/update-job-status company-role rejected
```

Note:
- Stage reached
- Feedback received (if any)
- Lessons learned

## Phase 7: Offer and Decision

### Track Offers

When you receive an offer:

```
/update-job-status stripe-senior-engineer offered
```

Document:
- Base salary
- Equity/bonus
- Benefits
- Start date
- Response deadline

### Compare Offers

If you have multiple offers, compare:
- Total compensation
- Company culture fit
- Role and growth potential
- Work-life balance
- Location/remote flexibility

### Negotiation

Use your research:
- Industry salary data from skill analysis
- Company research on compensation
- Other offers as leverage (tactfully)

## Maintenance

### Keep Data Current

- Update profile as skills grow
- Add new companies you discover
- Archive old/irrelevant jobs
- Refresh company research quarterly

### Learn from the Process

After your search:
- What worked well?
- What would you do differently?
- Which skills proved most valuable?
- Which companies were best fits?

Use this to guide future career planning.

## Checklist

### Before Starting
- [ ] Resume updated and ready
- [ ] Clear on target roles
- [ ] Salary research completed
- [ ] Profile set up in tool

### During Search
- [ ] 10-15 target companies identified
- [ ] 10-20 active applications
- [ ] Daily/weekly job search routine
- [ ] Interview prep for each stage

### After Receiving Offer
- [ ] All offers documented
- [ ] Negotiation research done
- [ ] Decision criteria clear
- [ ] Response deadline tracked
