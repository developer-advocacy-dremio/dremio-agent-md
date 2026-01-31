# Dremio Agent Helper

This repository is designed to supercharge AI coding assistants (like Google Gemini, ChatGPT, Claude) when working with Dremio. It provides a structured, traversable map of the Dremio documentation and specific protocols to ensure accurate, secure, and valid SQL generation.

## 📂 Repository Structure

*   **`DREMIO_AGENT.md`**: The master protocol file. Point your agent here first. It defines how the agent should Validate SQL, handle security (using `.env`), and navigate the sitemaps.
*   **`dremio_sitemaps/`**: A hierarchical directory structure containing markdown indices of the official Dremio documentation. This allows an agent to "browse" the documentation structure without needing live internet access or guessing URLs.
    *   `dremio_sitemaps/cloud/`: Documentation for Dremio Cloud.
    *   `dremio_sitemaps/24_3_x/`: Documentation for Dremio Software v24.3.x.
    *   And more...

## 🚀 How to Use This Repo

To get the best results from your AI agent, you need to "prime" it with the context from this repository.

### Step 1: Clone or Open
Ensure your agent has access to this file system.

### Step 2: Prime the Agent
Copy and paste one of the following prompts into your chat to initialize the agent's context.

#### 🔰 Initialization Prompt (Start Here)
> "I am working on a Dremio project. Please read `DREMIO_AGENT.md` to understand the protocols for SQL validation, security, and documentation navigation. Use the indices in `dremio_sitemaps/` to verify any Dremio features or syntax before generating code. Confirm when you have read the agent guide."

#### 🔍 SQL Validation Prompt
> "I need you to write a query to [describe task]. Before you write the code, please look up the specific function signatures and 'Reserved Words' in the `dremio_sitemaps` directory to ensure compliance. Remember to use the `.env` protocol defined in `DREMIO_AGENT.md` for any connection parameters."

#### 🛠️ Troubleshooting Prompt
> "I am getting a syntax error in my Dremio query. Please use the `dremio_sitemaps` to find the correct documentation for [Feature Name] and cross-reference my code. Check specifically for deprecated syntax or reserved keyword conflicts."

## 💡 Best Practices for Users

1.  **Always Reference the Guide**: If the agent hallucinates a function, remind it: *"Check `DREMIO_AGENT.md` and the sitemaps for the correct syntax."*
2.  **Security First**: Never paste your actual passwords or PATs into the chat. The agent is trained via `DREMIO_AGENT.md` to ask for env vars.
3.  **Version Specificity**: If you are on software, direct the agent to `dremio_sitemaps/current/`. If on cloud, direct it to `dremio_sitemaps/dremio-cloud/`.
