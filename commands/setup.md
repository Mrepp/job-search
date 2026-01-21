# /setup

Initialize your job search workspace and create your professional profile.

## Usage

```
/job-search:setup
/job-search:setup --path /custom/path
/job-search:setup --existing
```

## Description

This command prepares your job search environment by:

1. Running a quick skill analysis based on your resume
2. Configuring your workspace location
3. Creating the directory structure and indexes
4. Copying documentation for offline reference
5. Providing an overview of available capabilities

Run this command first before using any other job search commands.

## Workflow

### Step 1: Check for Existing Setup

1. Check for `.job-search-config.json` in:
   - Current working directory
   - `~/.job-search/`
   - User's home directory

2. If found:
   - Load existing configuration
   - Ask if user wants to:
     a) Continue with existing setup
     b) Create new workspace (keep old)
     c) Reset and reconfigure

3. If not found:
   - Proceed with fresh setup

### Step 2: Quick Skill Analysis (Resume-Based)

1. Ask for resume file path or allow paste:
   ```
   "Let's start with a quick profile. Please provide your resume:
    - Enter a file path (e.g., ~/Documents/resume.pdf)
    - Or paste your resume content
    - Or type 'skip' to enter details manually"
   ```

2. If resume provided, parse it:
   - Use profile-builder agent methodology
   - Extract: skills, experience years, current title, education
   - Extract: work history entries, projects

3. Apply 1-3 confidence scoring (from SKILL.md methodology):
   - **Score 3**: 5+ years of experience, lead/senior/architect mentions, certifications
   - **Score 2**: 2-5 years, used across multiple roles
   - **Score 1**: <2 years, side projects, coursework

4. Present extracted skills for user review:
   ```
   "I found these skills in your resume:

   Technical Skills:
   - Python: 3 (Expert - 7 years, lead projects)
   - AWS: 2 (Proficient - 3 years)
   - React: 2 (Proficient - 2 roles)
   - Kubernetes: 1 (Familiar - recent projects)

   Would you like to adjust any of these scores? (yes/no)"
   ```

5. Ask for target job titles and career goals:
   ```
   "What job titles are you targeting?"
   "What industries interest you most?"
   "What's your salary expectation range?"
   ```

6. Create `self/user.json` with:
   - Extracted profile data
   - `quick_profile: true` flag (can enhance with /job-search:personal-analysis)

7. Fallback if no resume provided:
   - Ask: current title, years experience, top 5 skills
   - Apply conservative confidence scores (default: 2)

### Step 3: Workspace Location

Present options:
```
"Where would you like to store your job search data?"

a) Here in [current directory] (Recommended)
   Best for: dedicated job search folder

b) In ~/.job-search/
   Best for: keeping data separate from projects

c) Let me specify a custom path
   Best for: specific organization needs
```

Save choice to `.job-search-config.json`:
```json
{
  "workspace_path": "/chosen/path",
  "plugin_path": "/path/to/job-search/plugin",
  "created": "2024-01-20T10:30:00Z",
  "profile_type": "quick",
  "docs_copied": true
}
```

### Step 4: Create Directory Structure

Create the following directories:

```
{workspace}/
├── .job-search-config.json    # Workspace configuration
├── index.json                  # Master index file
├── INDEX.md                    # Human-readable overview
├── mkdocs.yml                  # For /job-search:docs command
├── docs/                       # Plugin documentation copy
│   ├── index.md
│   ├── getting-started/
│   ├── commands/
│   ├── workflows/
│   ├── data-structures/
│   └── research/               # Generated research views
│       ├── dashboard.md
│       ├── companies/
│       ├── jobs/
│       └── career/
├── self/
│   ├── user.json
│   ├── resume/
│   │   ├── main-resume.md
│   │   └── tailored/
│   ├── projects/
│   ├── education/
│   ├── experience/
│   └── linkedin/
├── companies/
├── jobs/
│   ├── interested/
│   ├── applied/
│   ├── interviewed/
│   ├── offered/
│   └── rejected/
└── career/
    ├── skill-map.json
    └── career-tree.json
```

### Step 5: Copy Documentation

1. Copy plugin `/docs` folder to workspace `docs/`
   - Preserve directory structure
   - Update relative links to work locally

2. Create `docs/research/` for generated research views

3. Generate `INDEX.md`:
   ```markdown
   # Job Search Workspace

   ## Quick Links
   - [Documentation](docs/index.md) - Browse all documentation
   - [My Profile](self/user.json) - Your professional profile
   - [Companies](companies/) - Researched companies
   - [Jobs](jobs/) - Job applications by status
   - [Career](career/) - Career planning data

   ## Commands
   Run `/job-search:docs` to browse documentation in your browser.

   ## Getting Started
   1. Run `/job-search:personal-analysis` to enhance your profile
   2. Run `/job-search:find-job-postings [role]` to discover jobs
   3. Run `/job-search:find-company [name]` to research companies
   ```

### Step 6: Create Indexes

Create `index.json`:
```json
{
  "version": "1.0",
  "created": "2024-01-20T10:30:00Z",
  "last_updated": "2024-01-20T10:30:00Z",
  "workspace_path": "/path/to/workspace",
  "profile_summary": {
    "name": "User Name",
    "current_title": "Senior Software Engineer",
    "skill_count": 15,
    "profile_type": "quick"
  },
  "categories": {
    "companies": {
      "count": 0,
      "items": []
    },
    "jobs": {
      "interested": {"count": 0, "items": []},
      "applied": {"count": 0, "items": []},
      "interviewed": {"count": 0, "items": []},
      "offered": {"count": 0, "items": []},
      "rejected": {"count": 0, "items": []}
    },
    "interviews": {
      "upcoming": [],
      "completed": []
    },
    "documents": {
      "resumes": [],
      "cover_letters": [],
      "other": []
    }
  }
}
```

### Step 7: Onboarding Summary

Display welcome message:

```
Your job search workspace is ready at: {workspace_path}

Profile Summary:
- Name: {name}
- Current Title: {title}
- Skills Mapped: {count}
- Profile Type: Quick (enhance with /job-search:personal-analysis)

Available Commands:

**Profile & Skills**
- /job-search:personal-analysis - Enhance your profile with detailed experience
- /job-search:skill-builder - Analyze skill gaps and create learning plans

**Research**
- /job-search:find-company [name] - Research companies
- /job-search:find-position [role] - Explore career paths
- /job-search:find-job-postings [query] - Discover matching jobs

**Applications**
- /job-search:ingest-job [url] - Save and analyze job postings
- /job-search:update-job-status [job] [status] - Track your applications
- /job-search:tailor-resume [job] - Create targeted resumes

**Navigation**
- /job-search:docs - Browse documentation and saved research in browser

Suggested Next Steps:
{context-aware suggestions}
```

Suggest based on profile completeness:
- If quick profile: "To get the most from this plugin, run `/job-search:personal-analysis` to complete your full profile."
- If has skills: "Ready to start? Try `/job-search:find-job-postings {target_title}` to discover opportunities."

## Directory Structure Created

```
{workspace}/
├── .job-search-config.json
├── index.json
├── INDEX.md
├── mkdocs.yml
├── docs/
├── self/
│   ├── user.json
│   ├── resume/
│   ├── projects/
│   ├── education/
│   ├── experience/
│   └── linkedin/
├── companies/
├── jobs/
│   ├── interested/
│   ├── applied/
│   ├── interviewed/
│   ├── offered/
│   └── rejected/
└── career/
```

## Configuration File

`.job-search-config.json` schema:

```json
{
  "workspace_path": "string (absolute path)",
  "plugin_path": "string (path to plugin)",
  "created": "string (ISO date)",
  "profile_type": "quick | full",
  "docs_copied": "boolean"
}
```

## Example Session

```
User: /job-search:setup

Assistant: Welcome\! Let me help you set up your job search workspace.

First, do you have a resume file I can analyze?
- Enter a file path (e.g., ~/Documents/resume.pdf)
- Or paste your resume content
- Or type "skip" to enter details manually

User: ~/Documents/my-resume.pdf

Assistant: Great\! Analyzing your resume...

I found these skills:

Technical Skills:
- Python: 3 (Expert - 8 years, senior/lead roles)
- AWS: 2 (Proficient - 4 years across 2 roles)
- React: 2 (Proficient - 3 years)
- PostgreSQL: 2 (Proficient - 5 years)
- Kubernetes: 1 (Familiar - 1 year, recent projects)

Soft Skills:
- Team Leadership: 3 (5+ years managing teams)
- Technical Writing: 2 (Documentation in multiple roles)

Would you like to adjust any scores? (yes/no)

User: no

Assistant: Perfect. What job titles are you targeting?

User: Staff Software Engineer, Principal Engineer

Assistant: What industries interest you?

User: Fintech, AI/ML, Developer Tools

Assistant: Where would you like to store your job search data?

a) Here in /Users/john/job-search (Recommended)
b) In ~/.job-search/
c) Custom path

User: a

Assistant: Setting up your workspace...

✓ Created directory structure
✓ Copied documentation
✓ Created profile (self/user.json)
✓ Initialized indexes

Your job search workspace is ready at: /Users/john/job-search

Profile Summary:
- Name: John Smith
- Current Title: Senior Software Engineer
- Skills Mapped: 7
- Profile Type: Quick (enhance with /job-search:personal-analysis)

Suggested Next Steps:
1. Run /job-search:personal-analysis to complete your full profile
2. Try /job-search:find-job-postings Staff Software Engineer to discover opportunities
3. Run /job-search:docs to browse documentation in your browser
```
