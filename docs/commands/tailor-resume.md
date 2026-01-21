# /tailor-resume

Generate a customized resume for a specific job.

## Usage

```
/tailor-resume [job-file]
```

## Examples

```
/tailor-resume stripe-senior-engineer
/tailor-resume jobs/interested/anthropic-ml-engineer.md
/tailor-resume "Vercel Staff Engineer"
```

## Description

Creates a targeted version of your resume optimized for a specific job posting.

## What It Does

1. **Loads the job** - Requirements and keywords
2. **Loads your resume** - Master version
3. **Analyzes alignment** - What to emphasize
4. **Generates tailored version** - Customized content
5. **Shows the diff** - What changed
6. **Saves the result** - To `self/resume/tailored/`

## Tailoring Applied

**Summary/Objective:**
- Rewritten for the specific role
- Incorporates key requirements
- Matches their language

**Experience:**
- Reordered by relevance
- Expanded relevant details
- Added matching metrics

**Skills:**
- Reordered by job requirements
- Uses their exact terminology
- Grouped by their categories

**Projects:**
- Highlights relevant work
- Emphasizes matching technologies

## Output

Creates `self/resume/tailored/{company}-{title}.md`:

```markdown
# Jane Smith

## Tailored for: Senior Backend Engineer at Stripe

---

## Summary
{Customized summary targeting this role}

## Experience
{Reordered and emphasized for relevance}

## Skills
{Prioritized by job requirements}

---

## Tailoring Notes

### Changes Made:
- Summary rewritten for payments focus
- Emphasized fintech experience
- Reordered skills: Python, Go, PostgreSQL first

### Keywords Incorporated:
- distributed systems (required) - 4x
- payment processing (required) - 2x
- API design (preferred) - 3x
```

## Guidelines

**Does:**
- Reorder existing content
- Expand relevant experience
- Match terminology
- Quantify appropriately

**Doesn't:**
- Fabricate experience
- Claim skills you lack
- Keyword stuff
- Remove important content

## Tips

- Review the diff before submitting
- Keep tailored versions for reference
- Use talking points from job analysis
- Export to PDF for submission
