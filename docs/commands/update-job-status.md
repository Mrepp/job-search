# /update-job-status

Track job applications through the pipeline.

## Usage

```
/update-job-status [job-file] [status]
/update-job-status
```

## Examples

```
/update-job-status stripe-senior-engineer applied
/update-job-status "Stripe Senior Engineer" interviewed
/update-job-status vercel offered
/update-job-status anthropic rejected
/update-job-status
```

## Description

Moves jobs through your application pipeline and tracks progress with notes.

## Status Values

| Status | Description |
|--------|-------------|
| `interested` | Saved, considering applying |
| `applied` | Application submitted |
| `interviewed` | In interview process |
| `offered` | Received an offer |
| `rejected` | Rejected or withdrew |

## What It Does

1. **Finds the job file** - By name or path
2. **Updates status** - With timestamp
3. **Prompts for notes** - Context for this stage
4. **Moves the file** - To appropriate directory

## Notes Prompted

Depending on new status:

**applied:**
- Application date and method
- Materials submitted
- Contact person

**interviewed:**
- Interview date and format
- Interviewers
- Topics and how it went

**offered:**
- Offer details (salary, equity)
- Deadline to respond
- Negotiation notes

**rejected:**
- Stage reached
- Reason if known
- Lessons learned

## Pipeline View

Run without arguments to see pipeline summary:

```
## Application Pipeline

### Interested (3)
- Stripe - Senior Engineer (92/100) - 5 days
- Vercel - Staff Engineer (87/100) - 3 days

### Applied (2)
- Anthropic - ML Engineer (90/100) - 7 days

### Interviewed (1)
- Linear - Backend Engineer (85/100) - phone screen

### Offered (0)
No offers yet.

### Rejected (1)
- Meta - SWE (75/100) - after phone screen
```

## Tips

- Update status immediately after each stage
- Add detailed notes for interview prep
- Track deadlines for offers
- Review rejections for patterns
