# /find-position

Map career paths based on your skills and goals.

## Usage

```
/find-position [role/title]
```

## Examples

```
/find-position
/find-position staff software engineer
/find-position engineering manager
/find-position platform engineer
```

## Description

Analyzes your current position and maps potential career paths, including promotions, lateral moves, and specializations.

## What It Does

1. **Assesses your current level** - Based on title and experience
2. **Researches target roles** - Requirements and market data
3. **Maps career paths** - Vertical and lateral options
4. **Identifies gaps** - Skills and experience needed
5. **Creates action plans** - How to reach each target

## Career Paths Analyzed

### Vertical (Promotions)
- Next level in your current track
- Requirements and timeline
- Key gaps to address

### Lateral (Same-Level Pivots)
- Adjacent roles you could transition to
- Skill overlap and new skills needed
- Rationale for the move

### Specializations
- Depth options in your domain
- Resources for deeper expertise
- Career value of specializing

## Output

Updates `career/career-tree.json` with:
- Current position assessment
- Readiness scores for each path
- Gap analysis
- Recommended actions

## Example Output

```
## Your Career Position

**Current:** Senior Software Engineer (Backend)
**Experience:** 7 years
**Level Fit:** Strong (85/100)

### Promotion Paths

#### Staff Software Engineer
Readiness: 65/100 | Timeline: 12-18 months

Key Gaps:
- System design leadership
- Cross-team influence

Actions:
- Lead a major architectural initiative
- Mentor 2-3 engineers regularly

#### Engineering Manager
Readiness: 45/100 | Timeline: 18-24 months

Key Gaps:
- People management experience

Actions:
- Request tech lead role
- Participate in hiring
```

## Tips

- Run without arguments for full career analysis
- Specify a role to focus on that specific path
- Use insights to guide skill development
- Revisit quarterly to track progress
