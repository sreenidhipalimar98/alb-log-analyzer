# Kiro IDE Setup Guide — ALB Log Analyzer

This guide documents the Kiro IDE configuration for the ALB Log Analyzer workspace.

---

## Directory Structure

```
.kiro/
├── hooks/
│   ├── block-dangerous-commands.kiro.hook
│   └── block-sensitive-reads.kiro.hook
├── settings/
│   └── mcp.json
└── steering/
    ├── hook-handling-guide.md
    └── workspace-guide.md
```

---

## 1. MCP Server Configuration

**File:** `.kiro/settings/mcp.json`

Configures the GitHub MCP server for repo management (branches, PRs, issues).

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<your-github-pat>"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

Replace `<your-github-pat>` with a GitHub PAT that has `repo` scope.

---

## 2. Hooks

### Block Dangerous Shell Commands

Prevents execution of shell commands that should use IDE tools instead.

### Block Sensitive File Reads

Prevents reading sensitive files (credentials, keys, env files).

---

## 3. Steering Files

- **hook-handling-guide.md** — Teaches Kiro how to respond to hooks
- **workspace-guide.md** — Project context, tech stack, workflow

---

## 4. GitHub Context

| Item | Value |
|------|-------|
| Repository | `sreenidhipalimar98/alb-log-analyzer` |
| Default Branch | `main` |
| Development Branch | `develop` |
| Branch Strategy | Branch from `develop`, PRs to `develop` |

---

## 5. Quick Setup

```bash
mkdir -p .kiro/hooks .kiro/settings .kiro/steering
# Copy hook files, steering files
# Add your GitHub PAT to .kiro/settings/mcp.json
```
