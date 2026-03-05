# Agent System Overview

## How the Agent Team Works

The OpenClaw environment uses a hierarchical agent system with specialized roles that collaborate to execute tasks efficiently.

## Core Architecture

### Main Agent
- The primary coordinator that receives user requests
- Delegates work to specialized sub-agents
- Maintains overall context and memory
- Handles final delivery to user

### Runner Agents (Persistent Layer)

The system runs with 8 persistent runner agents that manage their respective domains:

| Agent | Role | Responsibilities |
|-------|------|------------------|
| **cbMan0_Orchestrator** | Workflow manager | Task decomposition, sub-agent spawning, progress monitoring |
| **cbMan0_Architect** | Design authority | Architecture proposals, ADRs, technology choices |
| **cbMan0_Implementer** | Code generator | Production-ready code from specs |
| **cbMan0_Tester** | QA specialist | Unit/integration tests, test execution |
| **cbMan0_Reviewer** | Quality gate | Code review, security, style enforcement |
| **cbMan0_Toolsmith** | Tool builder | CLI utilities, scripts, automation |
| **cbMan0_Secretary** | Governance | File placement, audits, structure health |
| **cbMan0_TimeoutAdvisor** | Diagnostics | Timeout analysis, bottleneck identification |

### Communication Flow

1. **Task Ingestion** → Main agent receives request
2. **Decomposition** → Orchestrator breaks into sub-tasks
3. **Delegation** → Tasks assigned to appropriate agents
4. **Execution** → Workers perform the actual work
5. **Monitoring** → Progress tracked by Orchestrator
6. **Review** → Reviewer approves/rejects changes
7. **Delivery** → Final output to user

### Heartbeat System

The heartbeat monitors active work:
- Checks repository every ~1 minute
- Flags if >30 minutes without commits
- Sends progress updates to user
- Maintains accountability

### Memory & Continuity

- **MEMORY.md** - Long-term archive of decisions and context
- **memory/YYYY-MM-DD.md** - Daily working logs
- **IDENTITY.md** - Agent persona and preferences
- **SOUL.md** - Core personality and values

---

## Current Configuration

- **Runtime:** agent=main | host=DESKTOP-U8OGDN5
- **OS:** Linux 6.6.87.2-microsoft-standard-WSL2 (x64)
- **Model:** ollama/minimax-m2.5:cloud
- **Shell:** bash
- **Channel:** webchat (direct)

---

*Last Updated: March 5, 2026*
