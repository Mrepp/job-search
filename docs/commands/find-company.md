# /find-company

Research companies matching your criteria.

## Usage

```
/find-company [company-name or criteria]
```

## Examples

```
/find-company Stripe
/find-company Anthropic
/find-company "fintech companies in San Francisco"
/find-company "remote-friendly developer tools startups"
/find-company "enterprise software with good work-life balance"
```

## Description

Performs comprehensive company research including career page analysis, employee review aggregation, and personalized relevance scoring.

## What It Does

1. **Parses your criteria** - Company name or search terms
2. **Researches the company** - Career page, reviews, news
3. **Analyzes culture** - From Glassdoor, Reddit, Blind
4. **Calculates relevance** - Based on your profile
5. **Saves research** - To `companies/{company}.md`

## Research Includes

- **Company overview:** Industry, size, founding, funding
- **Culture analysis:** Values, work environment, growth
- **Employee sentiment:** Ratings, pros, cons
- **Tech stack:** Languages, tools, platforms
- **Benefits:** Compensation, perks
- **Red flags:** Any concerning patterns
- **Open positions:** Current relevant roles

## Relevance Scoring

Your profile is compared for fit (0-100):

| Category | Points | Based On |
|----------|--------|----------|
| Location | 25 | Remote availability, location match |
| Industry | 25 | Target industry alignment |
| Skills | 25 | Tech stack overlap |
| Culture | 25 | Review analysis, preferences |

## Output

Creates `companies/{company-name}.md` with:
- Full company analysis
- Relevance score and breakdown
- Links to open positions
- Research sources

## Tips

- Research companies before applying to their jobs
- Use specific criteria for discovery searches
- Check red flags section before applying
- Refresh research if over 3 months old
