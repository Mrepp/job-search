# Installation

## Prerequisites

- Claude Code CLI installed and configured
- A working directory for your job search data

## Installing the Plugin

### Option 1: Clone the Repository

```bash
# Navigate to your Claude Code plugins directory
cd ~/.claude/plugins/

# Clone the job-search plugin
git clone https://github.com/your-repo/job-search.git
```

### Option 2: Manual Installation

1. Download or copy the `job-search` folder
2. Place it in your Claude Code plugins directory (`~/.claude/plugins/`)
3. Restart Claude Code

## Directory Structure

After installation, your plugins directory should look like:

```
~/.claude/plugins/
└── job-search/
    ├── .claude-plugin/
    │   └── plugin.json
    ├── commands/
    ├── agents/
    ├── skills/
    └── README.md
```

## Verifying Installation

1. Start Claude Code
2. Run `/help` to see available commands
3. You should see the job-search commands listed:
   - `/personal-analysis`
   - `/find-company`
   - `/find-position`
   - `/find-job-postings`
   - `/ingest-job`
   - `/update-job-status`
   - `/skill-builder`
   - `/tailor-resume`

## Creating Your Workspace

Choose a directory to store your job search data:

```bash
mkdir ~/job-search-data
cd ~/job-search-data
```

This is where the plugin will create:
- Your profile (`self/`)
- Company research (`companies/`)
- Saved jobs (`jobs/`)
- Career planning data (`career/`)

## Next Steps

- [Quick Start Guide](quick-start.md) - Get started with your first job search
- [Profile Setup](profile-setup.md) - Create your professional profile
