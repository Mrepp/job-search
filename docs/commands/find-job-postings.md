# /find-job-postings

Discover and rank job postings matching your profile.

## Usage

```
/find-job-postings [role] [location]
```

## Examples

```
/find-job-postings
/find-job-postings senior software engineer
/find-job-postings "backend developer" remote
/find-job-postings "staff engineer" "San Francisco"
/find-job-postings "ML engineer" "New York"
```

## Description

Searches for job postings across multiple platforms and ranks them by how well they match your profile.

## What It Does

1. **Loads your profile** - Skills, experience, preferences
2. **Searches job boards** - Multiple sources
3. **Analyzes each posting** - Requirements extraction
4. **Scores against your profile** - 0-100 match score
5. **Presents ranked results** - Best matches first
6. **Offers to save** - To `jobs/interested/`

## Match Scoring

Each job is scored (0-100) on:

| Category | Points | What's Evaluated |
|----------|--------|------------------|
| Title Match | 20 | Alignment with target titles |
| Location | 20 | Remote/location preferences |
| Skills | 30 | Required skills you possess |
| Experience | 15 | Years and type match |
| Salary | 15 | Range vs your expectations |

## Results Display

```
## Job Search Results

### 1. Senior Backend Engineer at Stripe (92/100)
📍 Remote (US) | 💰 $180k-$220k | 🏢 Fintech
✅ Skills: 9/10 match | ✅ Experience: Exceeds
[View] [Save]

### 2. Staff Software Engineer at Vercel (87/100)
📍 SF (Hybrid) | 💰 $200k-$260k | 🏢 DevTools
✅ Skills: 8/10 match | ⚠️ Experience: Stretch
[View] [Save]
```

## Saving Jobs

When you save a job:
- Full analysis saved to `jobs/interested/`
- Company research triggered if not exists
- Profile hash recorded for staleness tracking

## Tips

- Run without arguments to use profile defaults
- Use quotes for multi-word terms
- Focus on jobs scoring 75+
- Save interesting ones for deeper analysis
