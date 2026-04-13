# Official Dremio CLI (`dremio-cli`)

> **⚠️ Dremio Cloud ONLY.** This CLI is officially maintained by Dremio and is designed exclusively for Dremio Cloud. It does NOT support Dremio Software (self-hosted / on-prem).

## 📦 Package Info

| | |
|---|---|
| **PyPI package** | [`dremio-cli`](https://pypi.org/project/dremio-cli/) |
| **Source code** | [github.com/dremio/cli](https://github.com/dremio/cli) |
| **Invoked as** | `dremio` |
| **Platform support** | Dremio Cloud only |
| **Requirements** | Python 3.11+ |

## 🚀 Installation

```bash
# Recommended — isolated install (no venv needed)
pipx install dremio-cli

# Or with uv (fast, also isolated)
uv tool install dremio-cli

# Or with pip (requires virtual environment on modern Python)
pip install dremio-cli

# Install from source
git clone https://github.com/dremio/cli.git
cd cli
uv tool install .
```

> **Note:** On macOS and modern Linux, `pip install` into the system Python is blocked (`externally-managed-environment` error). Use `pipx` or `uv tool install` instead — they automatically create isolated environments.

After install, verify:
```bash
dremio --help
```

## 🔐 Authentication

There are three ways to authenticate, in priority order:

### Option A: CLI Flags (highest priority)
```bash
dremio --token YOUR_PAT --project-id YOUR_PROJECT_ID query run "SELECT 1"

# For EU region
dremio --uri https://api.eu.dremio.cloud --token YOUR_PAT --project-id YOUR_PROJECT_ID query run "SELECT 1"
```

### Option B: Environment Variables
```bash
export DREMIO_TOKEN=dremio_pat_xxxxxxxxxxxxx
export DREMIO_PROJECT_ID=your-project-id
# export DREMIO_URI=https://api.eu.dremio.cloud  # optional, for EU region
```

### Option C: Config File (lowest priority)
```bash
mkdir -p ~/.config/dremioai
cat > ~/.config/dremioai/config.yaml << 'EOF'
pat: dremio_pat_xxxxxxxxxxxxx
project_id: your-project-id
# uri: https://api.dremio.cloud  # default; change for EU region
EOF
chmod 600 ~/.config/dremioai/config.yaml
```

**Where to find credentials:**
- **PAT**: Dremio Cloud → Account Settings → Personal Access Tokens → New Token
- **Project ID**: Dremio Cloud → Project Settings (the UUID in the URL also works)

## ✅ Verify Setup
```bash
dremio query run "SELECT 1 AS hello"
```
Expected output: `{"job_id": "...", "state": "COMPLETED", "rowCount": 1, "rows": [{"hello": "1"}]}`

## 📚 Command Reference

### Query Commands (`dremio query`)
```bash
dremio query run "SELECT * FROM my_table LIMIT 10"   # Execute SQL
dremio query status <job_id>                          # Check job status
dremio query cancel <job_id>                          # Cancel a running job
```

### Folder Commands (`dremio folder`)
```bash
dremio folder list                      # List folders
dremio folder get <path>                # Get folder details
dremio folder create --path <path>      # Create a folder
dremio folder delete <path>             # Delete a folder
dremio folder grants <path>             # List grants on a folder
```

### Schema Commands (`dremio schema`)
```bash
dremio schema describe <table>          # Describe a table schema
dremio schema lineage <table>           # Show column lineage
dremio schema sample <table>            # Sample rows from a table
```

### Wiki Commands (`dremio wiki`)
```bash
dremio wiki get <entity>                # Get wiki content
dremio wiki update <entity> --text "..." # Update wiki content
```

### Tag Commands (`dremio tag`)
```bash
dremio tag get <entity>                 # Get tags
dremio tag update <entity> --tags "a,b" # Update tags
```

### Reflection Commands (`dremio reflection`)
```bash
dremio reflection create                # Create a reflection
dremio reflection list                  # List reflections
dremio reflection get <id>              # Get reflection details
dremio reflection refresh <id>          # Refresh a reflection
dremio reflection delete <id>           # Delete a reflection
```

### Job Commands (`dremio job`)
```bash
dremio job list                         # List recent jobs
dremio job get <job_id>                 # Get job details
dremio job profile <job_id>             # Download job profile
```

### Engine Commands (`dremio engine`)
```bash
dremio engine list                      # List engines
dremio engine get <id>                  # Get engine details
dremio engine create                    # Create an engine
dremio engine update <id>               # Update an engine
dremio engine delete <id>               # Delete an engine
dremio engine enable <id>               # Enable an engine
dremio engine disable <id>              # Disable an engine
```

### User Commands (`dremio user`)
```bash
dremio user list                        # List users
dremio user get <id>                    # Get user details
dremio user create                      # Create a user
dremio user delete <id>                 # Delete a user
dremio user whoami                      # Show current user info
dremio user audit                       # Show audit log
```

### Role Commands (`dremio role`)
```bash
dremio role list                        # List roles
dremio role get <id>                    # Get role details
dremio role create                      # Create a role
dremio role update <id>                 # Update a role
```

## 🌐 Platform Support

| Feature | Dremio Cloud | Dremio Software |
|---|---|---|
| SQL Query Execution | ✅ | ❌ Not supported |
| Job Management | ✅ | ❌ Not supported |
| Schema / Lineage | ✅ | ❌ Not supported |
| Reflections | ✅ | ❌ Not supported |
| Folder Management | ✅ | ❌ Not supported |
| Tags & Wiki | ✅ | ❌ Not supported |
| Engine Management | ✅ | ❌ Not supported |
| User Management | ✅ | ❌ Not supported |

> For Dremio Software (self-hosted), use the **Community CLI** (`alt-dremio-cli`) instead. See `dremio_sitemaps/alt-dremio-cli/README.md`.

## 💡 Tips & Best Practices

1. Always use `pipx` or `uv tool install` to avoid venv management overhead.
2. Store credentials in `~/.config/dremioai/config.yaml` (chmod 600) rather than environment variables if working in shared environments.
3. Use `dremio --help` and `dremio <command> --help` to discover all subcommands and flags.

## 🔗 Additional Resources

- [Dremio Cloud API Reference](https://docs.dremio.com/cloud/reference/api/)
- [PyPI: dremio-cli](https://pypi.org/project/dremio-cli/)
- [GitHub: dremio/cli](https://github.com/dremio/cli)
