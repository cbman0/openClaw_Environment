# OpenClaw Environment

Documentation and tools for the OpenClaw agent system.

## Quick Links

| Section | Description |
|---------|-------------|
| [Agent Overview](docs/agent-system-overview.md) | How the agent team works |
| [Agent Roles](agents/AGENTS.md) | Detailed role definitions |
| [clawdCombo Status](docs/clawdcombo_status.md) | Current project status |
| [Diagrams](diagrams/) | Architecture and workflow diagrams |
| [Tools](tools/) | Utility scripts |
| [Reports](reports/) | Dated status reports |

---

## Directory Structure

```
openClaw_Environment/
├── README.md                    # This file
├── agents/
│   └── AGENTS.md               # Agent role definitions
├── docs/
│   ├── agent-system-overview.md # How the team works
│   └── clawdcombo_status.md   # Project status
├── diagrams/
│   ├── orchestra_flow.mmd
│   ├── orchestra_flow_with_runners.mmd
│   ├── tmp_diagram.mmd
│   └── agent_workflow_updated.mmd
├── tools/
│   └── ssh_push.py             # SSH auto-fix push wrapper
└── reports/
    └── 05MAR2026/              # March 2026 status reports
```

---

## Usage

### SSH Push Tool
Auto-fixes SSH auth errors before pushing:
```bash
python3 tools/ssh_push.py ~/Desktop/gitStuff/openClaw_Environment
```

### Diagrams
Open `.mmd` files in Mermaid Live Editor or VS Code with Mermaid extension:
- https://mermaid.live/
- VS Code: `Markdown Preview Mermaid Support` extension

---

## Related Repos

- [clawdCombo](git@github.com:cbMan0/clawdCombo.git) - DeFi strategy executor

---

*Last Updated: March 5, 2026*
