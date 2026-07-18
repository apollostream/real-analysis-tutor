# Claude Code Plugins: Elite Technical Reference (Mid-2026)

**Last Updated**: July 2026 | **Knowledge Cutoff**: Haiku 4.5 | **Coverage**: Claude Code v2.1.154+

---

## 1. PLUGIN ANATOMY & DIRECTORY STRUCTURE

### 1.1 Plugin Root Layout

**Location**: Self-contained directory (named `<plugin-name>/`)

```
<plugin-name>/
├── .claude-plugin/
│   └── plugin.json                    # Manifest (optional if auto-discovery)
├── skills/                            # Recommended: nested skill structure
│   ├── code-reviewer/
│   │   ├── SKILL.md
│   │   ├── reference.md               # Progressive disclosure (optional)
│   │   └── scripts/                   # Supporting files
│   └── test-generator/
│       └── SKILL.md
├── commands/                          # Legacy: flat skill files (deprecated for new plugins)
│   ├── deploy.md
│   └── logs.md
├── agents/                            # Subagent definitions
│   ├── security-reviewer.md
│   └── performance-tester.md
├── hooks/
│   ├── hooks.json                     # Main hook config
│   └── scripts/
│       ├── prettier-format.sh
│       └── security-check.py
├── output-styles/                     # Custom output styles (NEW 2025+)
│   └── terse.md
├── themes/                            # Color themes (experimental)
│   └── dracula.json
├── monitors/                          # Background monitors (experimental)
│   └── monitors.json
├── bin/                               # Executables added to Bash tool PATH
│   ├── my-linter
│   └── my-formatter
├── .mcp.json                          # MCP server definitions
├── .lsp.json                          # LSP server configurations
├── settings.json                      # Default settings (only agent & subagentStatusLine)
├── package.json                       # Dependencies (optional)
├── README.md                          # Installation/usage docs
├── LICENSE                            # License file
├── CHANGELOG.md                       # Version history
└── CLAUDE.md                          # NOT loaded as context (use skills instead)
```

**Critical rules**:
- Only `plugin.json` goes inside `.claude-plugin/`
- All other directories MUST be at plugin root, not nested
- Auto-discovery: if `.claude-plugin/plugin.json` omitted, Claude Code scans default locations
- Single-skill shortcut: if plugin has `SKILL.md` at root + no `skills/` dir, it auto-loads as single skill

---

## 2. PLUGIN MANIFEST: plugin.json SCHEMA

**Location**: `.claude-plugin/plugin.json`

**Validation**: Run `claude plugin validate` before distribution

### 2.1 Full Schema (8 Fields Total)

```json
{
  "name": "my-enterprise-plugin",
  "version": "2.1.0",
  "description": "Specialized tooling for code review and deployment workflows",
  "author": {
    "name": "Your Name",
    "email": "you@example.com"
  },
  "homepage": "https://docs.example.com",
  "repository": "https://github.com/user/my-enterprise-plugin",
  "license": "MIT",
  "keywords": ["code-review", "deployment", "ci-cd"],
  "defaultEnabled": false,
  
  "skills": ["./skills/", "./extra-skills/"],
  "commands": ["./commands/deploy.md", "./commands/status.md"],
  "agents": ["./agents/"],
  "hooks": "./hooks/hooks.json",
  "mcpServers": "./my-mcp-config.json",
  "lspServers": "./.lsp.json",
  "outputStyles": "./output-styles/",
  
  "experimental.themes": "./themes/",
  "experimental.monitors": "./monitors.json",
  
  "userConfig": {
    "api_endpoint": {
      "type": "string",
      "title": "API Endpoint",
      "description": "Your team's deployment API",
      "required": true
    },
    "api_token": {
      "type": "string",
      "title": "API Token",
      "sensitive": true,
      "description": "Authentication token"
    }
  },
  
  "channels": [
    {
      "server": "slack",
      "userConfig": {
        "webhook_url": {
          "type": "string",
          "title": "Webhook URL",
          "sensitive": true
        }
      }
    }
  ],
  
  "dependencies": [
    { "name": "secrets-vault", "version": "~2.1.0" },
    { "name": "logging-sdk" }
  ]
}
```

### 2.2 Required Fields

| Field | Type | Purpose | Example |
|-------|------|---------|---------|
| `name` | string | Plugin identifier & skill namespace | `"my-plugin"` → `/my-plugin:skillname` |
| `description` | string | Shown in plugin manager | `"Enterprise code review suite"` |
| `version` *(optional)* | string | Semver for updates | `"2.1.0"` |
| `author` *(optional)* | object | Attribution | `{"name": "Team", "email": "..."}` |

### 2.3 Optional Metadata Fields

| Field | Type | Purpose |
|-------|------|---------|
| `homepage` | string | Documentation URL |
| `repository` | string | Source repo URL |
| `license` | string | License ID (MIT, Apache-2.0, etc.) |
| `keywords` | string[] | Discovery tags |
| `defaultEnabled` | boolean | Start disabled on install (v2.1.154+) |

### 2.4 Component Path Fields

**Path rules**:
- All paths relative to plugin root, start with `./`
- Multiple paths as arrays
- **Replaces default** (if set, default dir ignored): `commands`, `agents`, `outputStyles`, `experimental.themes`, `experimental.monitors`
- **Adds to default** (scans both): `skills`, `hooks`, `mcpServers`, `lspServers`

| Field | Type | Behavior | Example |
|-------|------|----------|---------|
| `skills` | string\|array | Adds to default `skills/` scan | `["./skills/", "./extra-skills/"]` |
| `commands` | string\|array | **Replaces** default `commands/` | `["./cmd1.md", "./cmd2.md"]` |
| `agents` | string\|array | **Replaces** default `agents/` | `"./custom-agents/"` |
| `hooks` | string\|array\|object | Inline or file path | `"./hooks/hooks.json"` or object |
| `mcpServers` | string\|array\|object | MCP config paths/inline | `"./.mcp.json"` |
| `lspServers` | string\|array\|object | LSP config paths/inline | `"./.lsp.json"` |
| `outputStyles` | string\|array | **Replaces** default | `"./output-styles/"` |

### 2.5 User Configuration Schema

Prompted on plugin enable, values available as `${user_config.KEY}` in YAML fields and `CLAUDE_PLUGIN_OPTION_<KEY>` env vars in subprocesses.

```json
{
  "userConfig": {
    "database_url": {
      "type": "string",
      "title": "Database URL",
      "description": "Connection string",
      "required": true
    },
    "max_workers": {
      "type": "number",
      "title": "Worker Pool Size",
      "min": 1,
      "max": 16,
      "default": 4
    },
    "enable_cache": {
      "type": "boolean",
      "title": "Enable Caching",
      "default": true
    },
    "file_path": {
      "type": "file",
      "title": "Config File",
      "description": "Path to config"
    },
    "tags": {
      "type": "string",
      "title": "Tags",
      "multiple": true,
      "description": "Comma-separated tags"
    }
  }
}
```

**Field types**: `string`, `number`, `boolean`, `directory`, `file`

**⚠️ Important**: Shell-form hook commands **reject** `${user_config.*}` substitution (injection risk). Use exec form with `args` or read from `CLAUDE_PLUGIN_OPTION_<KEY>` environment variable instead.

### 2.6 Plugin Dependencies

```json
{
  "dependencies": [
    { "name": "logging-sdk" },
    { "name": "auth-vault", "version": ">=1.0.0" },
    { "name": "formatter", "version": "~2.1.0" }
  ]
}
```

**Semver constraints**: `">=1.0.0"`, `"~2.1.0"` (≥2.1.0, <2.2.0), `"^1.2.3"` (≥1.2.3, <2.0.0)

---

## 3. SKILLS: SKILL.md SCHEMA & TRIGGERING

### 3.1 Skill File Structure

**Location**: `skills/<name>/SKILL.md` or flat `commands/<name>.md`

```markdown
---
name: code-reviewer
description: |
  Reviews code for best practices, performance, and security issues.
  Use when analyzing code quality, checking PRs, refactoring suggestions.
user-invocable: true
disable-model-invocation: false
allowed-tools: Read,Glob,Grep,WebSearch
model: claude-opus-4
effort: high
context: 15000
argument-hint: "[file path or glob pattern]"
---

# Code Review Skill

You are an expert code reviewer. When reviewing code:

1. **Best practices**: Style, naming, structure
2. **Performance**: Algorithmic efficiency, I/O patterns
3. **Security**: Injection risks, auth, crypto
4. **Testing**: Coverage, edge cases, mocks

Always cite specific lines and suggest concrete fixes.
```

### 3.2 SKILL.md Frontmatter Fields

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `name` | string | Directory name | Skill invocation name (if `SKILL.md` at root) |
| `description` | string | **Required** | Claude uses this to decide when to auto-invoke |
| `user-invocable` | boolean | `true` | Can user invoke with `/skill-name`? |
| `disable-model-invocation` | boolean | `false` | Only user can invoke (no auto-trigger by Claude) |
| `allowed-tools` | string | All tools | CSV: `Read,Write,Edit,Bash,Glob,Grep,WebSearch,WebFetch` |
| `model` | string | Session model | Override model for this skill |
| `effort` | string | `medium` | Guidance level: `low`, `medium`, `high` |
| `context` | number | Full available | Max tokens for skill context |
| `argument-hint` | string | None | Hint shown in `/help` (e.g., `"[filename]"`) |

**Best practices for descriptions**:
- Lead with action: "Analyzes X for Y" not "A skill that..."
- Specify trigger conditions: "Use when reviewing code, checking PRs, analyzing performance"
- Include relevant keywords for semantic matching
- Be specific about domain/tool dependencies

### 3.3 Progressive Disclosure: reference/ Files

For large skills, keep instructions minimal in `SKILL.md`, reference detailed docs:

```
skills/
└── complex-skill/
    ├── SKILL.md                       # ~100 lines: high-level overview
    ├── reference/
    │   ├── architecture.md
    │   ├── algorithms.md
    │   └── troubleshooting.md
    └── examples/
        ├── example1.sh
        └── example2.py
```

**SKILL.md body**:
```markdown
---
description: Complex ML pipeline orchestration
---

# ML Pipeline Skill

This skill orchestrates multi-stage ML training workflows.

For detailed architectural guidance, see [reference/architecture.md](./reference/architecture.md).
For algorithm selection, see [reference/algorithms.md](./reference/algorithms.md).
```

Claude learns to fetch referenced files on demand, avoiding loading all content upfront.

### 3.4 Argument Passing: $ARGUMENTS

In SKILL.md body, use `$ARGUMENTS` to capture user input:

```markdown
---
description: Process and format CSV files
argument-hint: "[filename or glob]"
---

# CSV Formatter

Process the file(s) specified in "$ARGUMENTS" with these transformations:
- Normalize headers
- Remove duplicate rows
- Sort by first column
```

Usage: `/plugin-name:formatter data/*.csv` → `$ARGUMENTS` = `"data/*.csv"`

### 3.5 Skills vs Commands: Directory Structure

| Layout | Trigger | Scope | Best For |
|--------|---------|-------|----------|
| `skills/<name>/SKILL.md` | `/plugin:name` | Namespaced | Multi-skill plugins, reusable components |
| `commands/<name>.md` | `/name` | Plugin namespace | Legacy, flat structure (deprecated for new) |
| Root `SKILL.md` (single) | `/plugin:name` | Namespace via frontmatter `name` | Single-skill plugins |

---

## 4. SUBAGENTS IN PLUGINS: agents/*.md

### 4.1 Subagent File Structure

**Location**: `agents/<name>.md`

```markdown
---
name: security-reviewer
description: |
  Specialist for security code review: vulnerability analysis, auth patterns,
  crypto practices, injection risks. Use when analyzing security posture.
model: claude-opus-4
tools: Read,Glob,Grep,WebSearch
temperature: 1.0
system-prompt-suffix: |
  When reviewing security:
  1. Threat modeling: STRIDE framework
  2. Check OWASP Top 10
  3. Recommend mitigations with CWE references
---

# Security Code Reviewer Subagent

You are a security specialist. When code is submitted for review:
- Identify vulnerabilities using threat modeling
- Suggest fixes with security best practices
- Reference CVEs and CWE IDs
- Rate severity and exploitability
```

### 4.2 Subagent Frontmatter Fields

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `name` | string | File name | Subagent identifier |
| `description` | string | **Required** | When Claude delegates to this subagent |
| `model` | string | Session model | Override for specialized reasoning |
| `tools` | string | All tools | CSV of permitted tools |
| `temperature` | number | 1.0 | Creativity setting (0–2) |
| `system-prompt-suffix` | string | None | Extra instructions appended to system prompt |
| `max-tokens` | number | Model limit | Token budget for subagent |

### 4.3 Subagent Use Cases

✅ **When to use subagents**:
- Task requires different tool set (e.g., security review with no file writes)
- Task needs specialized system prompt
- Need cost control (use cheaper model like Haiku)
- Preserve parent context (exploration in isolated window)

❌ **Anti-patterns**:
- Spawning subagent for trivial tasks (overhead > benefit)
- Unnecessary model switching (same model, minimal difference)
- Over-scoping tool restrictions (makes subagent less effective)

---

## 5. HOOKS IN PLUGINS: hooks/hooks.json

### 5.1 Hooks.json Schema

**Location**: `hooks/hooks.json` or inline in `plugin.json` under `hooks` field

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "install-deps.sh",
            "async": false
          }
        ]
      }
    ],
    
    "PreToolUse": [
      {
        "matcher": "Bash",
        "if": "Bash(rm -rf)",
        "hooks": [
          {
            "type": "command",
            "command": "check-safety.sh",
            "suppressOutput": false
          }
        ]
      },
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "node",
            "args": ["${CLAUDE_PLUGIN_ROOT}/lint.js", "${file_path}"]
          }
        ]
      }
    ],
    
    "PostToolUse": [
      {
        "matcher": "^Bash$",
        "hooks": [
          {
            "type": "mcp_tool",
            "server": "memory",
            "tool": "save_memory",
            "input": {
              "key": "last_bash_output",
              "value": "${stdout}"
            }
          }
        ]
      }
    ],
    
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Did the output look correct? Answer yes/no"
          }
        ]
      }
    ]
  }
}
```

### 5.2 Hook Events & Timing

| Event | When | Can Block? | Input Available |
|-------|------|-----------|------------------|
| `SessionStart` | Session begins/resumes | No | `session_id`, `cwd`, `model` |
| `SessionEnd` | Session terminates | No | Full transcript path |
| `UserPromptSubmit` | User submits prompt | Yes | `user_message`, `prompt_id` |
| `PreToolUse` | Before tool executes | Yes (block/modify) | `tool_name`, `tool_input` |
| `PostToolUse` | After tool succeeds | Yes (modify output) | `tool_name`, `stdout`, `exit_code` |
| `Stop` | Claude finishes response | Yes | Full turn context |
| `FileChanged` | File modified | No | `file_path`, `timestamp` |
| `StopFailure` | Claude stops with error | Yes | `error_message`, `tool_call` |

### 5.3 Hook Types

| Type | Input | Output | Use Case |
|------|-------|--------|----------|
| `command` | JSON on stdin | JSON on stdout | Shell scripts, Python, executables |
| `http` | POST JSON | Read response | External APIs, webhooks |
| `mcp_tool` | Tool-specific | Direct tool call | MCP server tools |
| `prompt` | Message to Claude | Yes/no decision | Approval gates, validation |
| `agent` | Context + prompt | Full tool execution | Complex validation with side effects |

### 5.4 Hook Matcher Patterns

```json
{
  "matcher": "Bash",                    // Exact match
  "matcher": "Edit|Write|Notebook",     // Multiple (| or ,)
  "matcher": "^Bash.*",                 // Regex (caret/dollar anchors work)
  "matcher": "mcp__memory__*",          // MCP tools (namespace pattern)
  "if": "Bash(rm -rf *)"                // Tool pattern + input condition
}
```

**Note**: `FileChanged` and `StopFailure` use narrower patterns (only exact matches, underscores, digits, letters, |).

### 5.5 Blocking & Exit Codes

**Shell hook exit codes**:
- `0`: Continue normally, parse JSON from stdout
- `2`: Block with error (stderr as error message to Claude)
- Other: Non-blocking error

**Blocking example** (PreToolUse):
```bash
#!/bin/bash
command=$(jq -r '.tool_input.command' < /dev/stdin)
if [[ "$command" == "rm -rf /"* ]]; then
  jq -n '{
    "continue": false,
    "hookSpecificOutput": {
      "permissionDecision": "deny",
      "permissionDecisionReason": "Destructive command blocked"
    }
  }'
  exit 2
fi
exit 0
```

### 5.6 Environment Variables in Hooks

Available in hook subprocess:
- `${CLAUDE_PLUGIN_ROOT}`: Plugin installation directory
- `${CLAUDE_PLUGIN_DATA}`: Persistent data dir (`~/.claude/plugins/data/{id}/`)
- `${CLAUDE_PROJECT_DIR}`: Project root

**Path substitution rules**:
- Shell form (default): Wrap in quotes: `"${CLAUDE_PLUGIN_ROOT}/script.sh"`
- Exec form (with `args`): No quoting needed, passed as single argument

---

## 6. SLASH COMMANDS: commands/*.md Format

**Legacy approach** (new plugins should use `skills/`). Flat Markdown files become `/command-name` shortcuts.

```markdown
---
description: Deploy to production
user-invocable: true
argument-hint: "[version]"
---

# Deploy Command

Deploy version $ARGUMENTS to production...
```

**Same frontmatter as skills**, same `$ARGUMENTS` support. Difference: no subdirectory nesting, no progressive disclosure via reference files.

---

## 7. PLUGIN INSTALLATION & VERSIONING

### 7.1 CLI Commands Summary

```bash
# Initialize new plugin at ~/.claude/skills/<name>/
claude plugin init my-plugin --with skills hooks mcp

# Install from marketplace
claude plugin install my-plugin@official-marketplace
claude plugin install my-plugin@official-marketplace --scope project

# Manage plugins
claude plugin list --json
claude plugin details my-plugin@marketplace
claude plugin enable/disable my-plugin
claude plugin update my-plugin

# Validate before distribution
claude plugin validate

# Tag release
claude plugin tag ./my-plugin --push

# Clean up dependencies
claude plugin prune --dry-run
```

### 7.2 Installation Scopes

| Scope | Location | Shared | Use Case |
|-------|----------|--------|----------|
| `user` | `~/.claude/settings.json` | Across all projects | Personal setup |
| `project` | `.claude/settings.json` | Team via git | Shared team workflows |
| `local` | `.claude/settings.local.json` | Not shared (gitignored) | Testing, temporary |
| `managed` | Admin-enforced | Enterprise policy | Org-wide enforcement |

### 7.3 Versioning Strategy

**Two approaches**:

1. **Explicit version** (stable releases):
   - Set `"version": "2.1.0"` in `plugin.json`
   - Users get updates only when you bump this field
   - **Must bump** for any distribution; commits alone don't trigger updates
   - Follow semver: MAJOR.MINOR.PATCH

2. **Commit-SHA version** (active development):
   - Omit `version` from `plugin.json` and marketplace entry
   - Every commit counts as new version
   - Users get updates on every push
   - Best for internal/team plugins

**⚠️ Warning**: If you set version, forgetting to bump it = no updates distributed.

### 7.4 Plugin Caching & File Resolution

Marketplace plugins cached in `~/.claude/plugins/cache/{plugin-id}/{version}/`
- Isolated from source repo
- Orphaned versions cleaned after 7 days
- Path traversal blocked: `../shared-utils` fails post-installation
- Symlinks within plugin dir preserved; outside dir dereferenced/skipped (security)

---

## 8. MARKETPLACE DISTRIBUTION: marketplace.json

### 8.1 Marketplace.json Schema

**Location**: Repository root `.claude-plugin/marketplace.json`

```json
{
  "version": 1,
  "owner": "Your Organization",
  "email": "support@example.com",
  "plugins": [
    {
      "id": "my-plugin",
      "name": "Enterprise Plugin Suite",
      "description": "Advanced code review and deployment",
      "version": "2.1.0",
      "author": "Team Name",
      "homepage": "https://docs.example.com",
      "repository": "https://github.com/yourorg/my-plugin",
      "license": "MIT",
      "keywords": ["review", "deploy"],
      "defaultEnabled": false,
      
      "source": {
        "type": "github",
        "owner": "yourorg",
        "repo": "my-plugin",
        "path": ".",
        "ref": "main"
      }
    },
    {
      "id": "formatter-tool",
      "name": "Code Formatter",
      "description": "Multi-language formatter plugin",
      "version": "1.0.0",
      "source": {
        "type": "git-subdir",
        "url": "https://github.com/yourorg/tools.git",
        "path": "plugins/formatter",
        "ref": "v1.0.0"
      }
    }
  ],
  "renames": {
    "old-plugin-name": "new-plugin-name"
  }
}
```

### 8.2 Plugin Entry Fields

| Field | Required | Purpose |
|-------|----------|---------|
| `id` | Yes | Unique identifier (kebab-case) |
| `name` | Yes | Display name |
| `description` | Yes | Short description |
| `source` | Yes | Where to fetch plugin |
| `version` | No | Override plugin.json version |
| `author`, `homepage`, `repository`, `license` | No | Attribution & links |
| `keywords` | No | Discovery tags |
| `defaultEnabled` | No | Default state (overrides plugin.json) |

### 8.3 Source Types

```json
// GitHub repository root
{
  "type": "github",
  "owner": "yourorg",
  "repo": "plugin-name",
  "path": ".",
  "ref": "main"
}

// Git subdirectory (any git host)
{
  "type": "git-subdir",
  "url": "https://github.com/yourorg/monorepo.git",
  "path": "plugins/my-plugin",
  "ref": "v2.1.0"
}

// Direct git repository
{
  "type": "git",
  "url": "https://github.com/yourorg/my-plugin.git",
  "ref": "main"
}

// HTTP URL (raw .zip)
{
  "type": "url",
  "url": "https://releases.example.com/my-plugin@2.1.0.zip"
}

// Local path (testing only)
{
  "type": "local",
  "path": "../plugins/my-plugin"
}

// npm package
{
  "type": "npm",
  "package": "@yourorg/my-plugin",
  "version": "2.1.0"
}
```

### 8.4 Adding Marketplaces

```bash
# Add marketplace interactively
/plugin marketplace add anthropics/claude-plugins-official

# CLI equivalent
claude plugin marketplace add anthropics/claude-plugins-official

# Update/refresh catalog
/plugin marketplace update claude-plugins-official
claude plugin marketplace update claude-plugins-official
```

---

## 9. 2025-2026 NEW FEATURES

### 9.1 Output Styles in Plugins (2025+)

Plugins can ship custom output styles in `output-styles/` directory.

**File**: `output-styles/my-style.md`

```markdown
---
name: Terse
description: Concise responses, code-first
keep-coding-instructions: true
force-for-plugin: false
---

When responding:
1. Lead with code, not explanation
2. Omit ceremony; use shorthand
3. Suggest improvements in comments
```

**Frontmatter**:
- `name`: Style identifier
- `description`: Shown in `/config` picker
- `keep-coding-instructions`: Preserve Claude Code's default coding rules (true/false)
- `force-for-plugin`: Auto-apply when plugin enabled, override user's outputStyle (true/false)

### 9.2 Background Monitors (Experimental, 2025+)

**Location**: `monitors/monitors.json`

```json
[
  {
    "name": "error-log",
    "command": "tail -F ./logs/error.log",
    "description": "Application error log stream",
    "when": "always"
  },
  {
    "name": "git-status",
    "command": "git status --porcelain --ignored",
    "description": "Uncommitted changes",
    "when": "file-changed"
  }
]
```

Each stdout line delivered to Claude as async notification. Use for watching logs, file changes, external services.

### 9.3 Statusline Configuration (2025+)

Plugins can customize statusline rendering via `settings.json`:

```json
{
  "subagentStatusLine": "custom",
  "statusLine": "${CLAUDE_PLUGIN_ROOT}/statusline.sh"
}
```

Custom statusline script receives JSON session data on stdin, outputs terminal string for persistent display.

### 9.4 LSP Server Integration (2024+, Refined 2025+)

**Location**: `.lsp.json`

```json
{
  "python": {
    "command": "python",
    "args": ["-m", "pylsp"],
    "extensionToLanguage": {
      ".py": "python"
    }
  },
  "typescript": {
    "command": "typescript-language-server",
    "args": ["--stdio"],
    "extensionToLanguage": {
      ".ts": "typescript",
      ".tsx": "typescript"
    }
  }
}
```

Provides real-time code intelligence (go-to-definition, find-references, diagnostics). Official Anthropic marketplace covers 11 languages as of July 2026.

### 9.5 Plugin-Scoped Settings (2025+)

Default plugin settings via `settings.json`:

```json
{
  "agent": "security-reviewer",
  "subagentStatusLine": "custom-statusline"
}
```

Only `agent` (names custom subagent) and `subagentStatusLine` (custom statusline) currently supported. Applied when plugin enabled.

### 9.6 User Configuration at Enable Time (2025+)

Plugins prompt for sensitive values at install:

```json
{
  "userConfig": {
    "api_key": {
      "type": "string",
      "title": "API Key",
      "sensitive": true,
      "description": "Service API key"
    }
  }
}
```

Sensitive values → macOS Keychain or `~/.claude/.credentials.json` (~2 KB limit). Non-sensitive values → `settings.json` under `pluginConfigs[<plugin-id>].options`.

### 9.7 Plugin Dependencies (2024+, Refined 2025+)

```json
{
  "dependencies": [
    { "name": "auth-sdk" },
    { "name": "logger", "version": "~1.2.0" }
  ]
}
```

Claude Code auto-installs required plugins; `/plugin uninstall --prune` removes unused dependencies.

---

## 10. HOOKS CONFIGURATION LOCATIONS & PRECEDENCE

| Location | Scope | Precedence |
|----------|-------|-----------|
| `~/.claude/settings.json` | User-wide (all projects) | Lowest |
| `.claude/settings.json` | Project-wide | Medium |
| `.claude/settings.local.json` | Project (gitignored) | High |
| Plugin `hooks/hooks.json` | When plugin enabled | Plugin-level |
| Skill/Agent frontmatter | Component active | Highest (specific) |

Multiple hooks from different levels **combine** (don't override).

---

## 11. BEST PRACTICES & ANTI-PATTERNS

### 11.1 Context Economy

✅ **Best practices**:
- Keep `CLAUDE.md` < 200 lines (SKILL.md loads on demand, CLAUDE.md always loaded)
- Use file references in CLAUDE.md instead of pasting code snippets
- Move situational knowledge to skills/agents (lazy-loaded)
- Use subagents to isolate large exploratory tasks

❌ **Anti-patterns**:
- Bloated `CLAUDE.md` with redundant linter rules
- Treating `CLAUDE.md` like documentation instead of working memory
- Pasting entire codebases into context
- Blocking Edit/Write tools mid-execution (breaks multi-step reasoning)

### 11.2 Skill Design

✅ **Best practices**:
- Descriptions precise & actionable ("Use when reviewing PRs for security")
- Set `disable-model-invocation: true` for skills with side effects (commit, deploy)
- Restrict `allowed-tools` to minimum needed
- Use progressive disclosure (reference/ files) for complex skills
- One skill = one responsibility

❌ **Anti-patterns**:
- Vague descriptions ("A utility skill")
- Skill bloat: 5 unrelated features in one skill
- Not restricting tool access (unnecessary permissions)
- Over-engineering helper functions without direction

### 11.3 Hook Performance

✅ **Best practices**:
- Keep `SessionStart` hooks < 1 second (runs every session)
- Use `if` condition to avoid unnecessary process spawns
- Prefer commands for simple logic, agents for complex validation
- Use `suppressOutput: true` for verbose tools

❌ **Anti-patterns**:
- Heavy computation in `SessionStart`
- Spawning hook for every tool call without filtering
- Synchronous blocking hooks on high-frequency events

### 11.4 Plugin Distribution

✅ **Best practices**:
- Document installation & configuration clearly in README
- Version explicitly (semver) for stable releases
- Changelog with every release
- Test plugin.json with `claude plugin validate`
- Supply example CLAUDE.md for plugin integration

❌ **Anti-patterns**:
- Forgetting to bump version (commits don't auto-trigger updates)
- No documentation of plugin options
- Symlinks outside plugin dir (broken post-cache)
- Hardcoding paths (use `${CLAUDE_PLUGIN_ROOT}` variables)

---

## 12. DEBUGGING TOOLS

### 12.1 Validation & Inspection

```bash
# Validate manifest, skills, hooks, agents
claude plugin validate

# List detailed component inventory & token cost
claude plugin details my-plugin@marketplace

# Debug plugin loading
claude --debug 2>&1 | grep -i plugin

# Inspect plugin structure
ls -la ~/.claude/plugins/cache/<plugin-id>/<version>/
```

### 12.2 Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| "No commands found" | Wrong directory structure | Move `commands/` to plugin root (not `.claude-plugin/`) |
| "Plugin not loading" | Invalid JSON in `plugin.json` | Run `claude plugin validate` |
| "Skill not appearing" | `SKILL.md` in wrong location | Use `skills/<name>/SKILL.md` or flat `commands/<name>.md` |
| "Hook not firing" | Script not executable | `chmod +x ./hooks/script.sh` |
| "MCP server fails" | Path not using variable | Replace absolute paths with `${CLAUDE_PLUGIN_ROOT}` |
| "Path errors post-install" | Relative paths used absolute | All paths must start with `./` |

---

## 13. EXAMPLE: COMPLETE ENTERPRISE PLUGIN

**Full working example** (code-review plugin):

```
enterprise-code-review/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── security-review/
│   │   ├── SKILL.md
│   │   ├── reference/
│   │   │   ├── owasp.md
│   │   │   └── cwe-mappings.md
│   │   └── scripts/
│   │       └── check-crypto.py
│   ├── performance-review/
│   │   └── SKILL.md
│   └── test-coverage/
│       └── SKILL.md
├── agents/
│   ├── security-specialist.md
│   ├── performance-expert.md
│   └── compliance-checker.md
├── hooks/
│   ├── hooks.json
│   └── scripts/
│       ├── pre-commit-check.sh
│       └── format-code.sh
├── output-styles/
│   └── detailed-review.md
├── .mcp.json
├── .lsp.json
├── settings.json
├── package.json
├── README.md
├── CHANGELOG.md
└── LICENSE
```

**plugin.json**:
```json
{
  "name": "enterprise-code-review",
  "version": "2.1.0",
  "description": "Security & performance code review suite",
  "author": {"name": "Security Team", "email": "security@company.com"},
  "keywords": ["security", "performance", "review"],
  "defaultEnabled": false,
  "skills": ["./skills/"],
  "agents": ["./agents/"],
  "hooks": "./hooks/hooks.json",
  "outputStyles": "./output-styles/",
  "userConfig": {
    "jira_token": {
      "type": "string",
      "title": "JIRA Token",
      "sensitive": true
    }
  }
}
```

---

## 14. OFFICIAL RESOURCES & CITATIONS

**Official Anthropic Documentation**:
- [Claude Code Plugins](https://code.claude.com/docs/en/plugins.md) — Main plugin guide
- [Plugins Reference](https://code.claude.com/docs/en/plugins-reference.md) — Complete technical schema
- [Skills](https://code.claude.com/docs/en/skills.md) — Skill authoring
- [Hooks](https://code.claude.com/docs/en/hooks.md) — Hook lifecycle & events
- [Subagents](https://code.claude.com/docs/en/sub-agents.md) — Subagent configuration
- [Plugin Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces.md) — Distribution

**Official Examples**:
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) — Curated marketplace
- [example-plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/example-plugin) — Reference plugin

**Community Resources**:
- [awesome-claude-code-and-skills](https://github.com/GetBindu/awesome-claude-code-and-skills) — Curated list
- [Tons of Skills](https://tonsofskills.com/) — Marketplace aggregator (ccpi CLI)
- [Claude Code 2026 Best Practices](https://www.iwoszapar.com/p/claude-code-best-practices) — Design patterns

---

## 15. UNCERTAINTY & CHANGE NOTES

**⚠️ Items with limited documentation or rapid evolution (verify with current docs)**:

1. **Plugin-scoped memory/state** — Announced for 2025+ but details sparse; status unclear as of July 2026
2. **Themes (experimental)** — Under `experimental.themes`; schema may change
3. **Monitors (experimental)** — Early feature; full lifecycle not yet documented
4. **Channels** — MCP-based message injection; newly stabilized in 2025, limited examples
5. **Managed plugins** — Enterprise feature; scoped documentation
6. **Nested CLAUDE.md in plugins** — Official policy: not loaded; work around by using skills instead

**Known limitations**:
- Plugins cannot access user's other installed plugins directly
- Cross-plugin communication through MCP only
- Plugin execution isolated in cache; no sibling symlink access outside plugin boundary
- Subagents cannot spawn other subagents (flat delegation only)

---

**Document Status**: Complete reference for mid-2026 (v2.1.154+)  
**Last Verified**: July 2026  
**Confidence**: High for documented features; Medium for experimental features; Low for pre-release announcements

