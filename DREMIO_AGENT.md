# Dremio Agent Guide

This document serves as a protocol for AI Agents assisting with Dremio-related tasks. Follow these guidelines to ensure accuracy, security, and high-quality output.

## 1. Navigating Documentation

This repository contains a structured, offline index of Dremio documentation to help you find the source of truth quickly without guessing URLs.

*   **Root Index**: `dremio_sitemaps/README.md`
    *   This file lists all top-level documentation sections (e.g., Cloud, software versions).
*   **Sub-Indices**: Each top-level section is a directory (e.g., `dremio_sitemaps/cloud/`) containing:
    *   `README.md`: The index for that section.
    *   `*.md` files: Specific sub-topics (e.g., `arctic.md`).

**Protocol:**
1.  **Identify the Context**: Determine if the user is using Dremio Cloud or a specific Software version (e.g., 24.3.x).
2.  **Locate the Index**: Open the relevant `README.md` in `dremio_sitemaps/`.
3.  **Find the specific Page**: Search the markdown index for the topic (e.g., "SQL Functions", "Rest API").
4.  **Reference the URL**: Use the actual Dremio documentation URL provided in the sitemap to verify syntax or parameters if you have browsing capabilities, or cite it for the user.

## 2. Validation Standards

Dremio's SQL dialect and feature set are specific. **Never assume generic SQL or standard behavior.**

### SQL Syntax Validation
*   **Check the Docs**: Before writing a SQL query, consult the "SQL Reference" section found via the sitemap.
*   **Verify Function Signatures**: Ensure function names and arguments match the Dremio version being used.
*   **Data Types**: Verify supported data types and casting rules.

### Reserved Words
*   **Mandatory Check**: Dremio has a list of reserved keywords that cannot be used as identifiers without quoting.
*   **Action**: detailed in `dremio_sitemaps/.../reserved_keywords.md` (or similar).
*   **Best Practice**: Always double-quote identifiers (e.g., `"timestamp"`, `"table"`, `"date"`) if there is any doubt.

## 3. Security & Configuration Best Practices

**NEVER** ask the user to provide credentials (usernames, passwords, tokens) directly in the chat or code snippets.

### The `.env` Standard
Instruct the user to create a `.env` file in their project root.

**Requested Variables:**
```bash
# Connection Details
DREMIO_URL="https://app.dremio.cloud" # or their software URL
DREMIO_USER="user@example.com"
DREMIO_PASSWORD="secure_password"
DREMIO_PAT="personal_access_token" # Preferred over password for Cloud
DREMIO_PROJECT_ID="project_id" # For Dremio Cloud
```

**Python Implementation Pattern:**
When writing validtion scripts or tools, always use `python-dotenv`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

dremio_url = os.getenv("DREMIO_URL")
dremio_pat = os.getenv("DREMIO_PAT")

if not dremio_pat:
    raise ValueError("DREMIO_PAT is missing from .env file")
```

## 4. Work Protocol

1.  **Research**: Use `dremio_sitemaps/` to locate relevant documentation.
2.  **Plan**: Check against Reserved Words and SQL support.
3.  **Secure**: Ensure any code proposed uses `.env` for secrets.
4.  **Execute**: Generate the code or answer.
5.  **Validate**: Review generated code against the documentation constraints one last time.

## Traversal

- If using Dremio Cloud, use `dremio_sitemaps/dremio-cloud/` as the root.
- If using Dremio Software, use `dremio_sitemaps/current/` as the root.
- For the Dremio Cloud API, use `dremio_sitemaps/dremio-cloud/api.md`
- For Dremio Software API, use `dremio_sitemaps/current/reference.md`
- For Dremio SQL Syntax use, use `dremio_sitemaps/dremio-cloud/sql/readme.md`
- For Dremio Sources on Cloud, use `dremio_sitemaps/dremio-cloud/bring-data.md`
- For Dremio Sources on Software, use `dremio_sitemaps/current/data-sources.md`

## 5. Python Tools Recommendation

Before writing custom Python scripts from scratch, verify if an existing tool library handles the use case.

### Dremioframe (`dremio_sitemaps/dremioframe/`)
Use `dremioframe` for:
*   **Data Engineering**: ETL/ELT pipelines, managing tables/views, Iceberg table management.
*   **Administrative Tasks**: User/role management, reflection management.
*   **Documentation Link**: `dremio_sitemaps/dremioframe/README.md`

### Dremio CLI (`dremio_sitemaps/dremio-cli/`)
Use the `dremio-python-cli` for:
*   **Command Line Operations**: Quick shell-based interactions.
*   **CI/CD Integration**: Scripting catalog changes or queries in build pipelines.
*   **Documentation Link**: `dremio_sitemaps/dremio-cli/README.md`
