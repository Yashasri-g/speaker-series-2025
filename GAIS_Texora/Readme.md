# Multi-Model Playground - ThinkSpace

A **Streamlit application** for interacting with multiple AI models hosted on GitHub’s inference endpoint. Supports both **OpenAI models** and **Azure-hosted inference models**.

This app provides predefined **use cases** (topic explanation, translation, code debugging, business idea generation) and supports custom prompts.

---

## Features

- Run prompts on **multiple GitHub-hosted AI models** (OpenAI and Azure)
- Predefined use cases for common and specialized scenarios
- Custom prompt functionality
- Secure token management via **Streamlit Secrets**
- Unified interface for OpenAI and Azure SDKs

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/multi-model-playground.git
cd multi-model-playground
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
streamlit
openai
azure-ai-inference
azure-core
```

### 3. Configure Secrets

A **GitHub Personal Access Token (PAT)** is required for authentication.

1. Visit [GitHub Personal Access Tokens](https://github.com/settings/tokens) to generate the necessary tokens.
2. Generate tokens with access to **GitHub Models**.
3. Add the tokens to **Streamlit Secrets Manager** (`.streamlit/secrets.toml`):

```toml
GITHUB_TOKEN_4O_MINI = "ghp_xxxxxxxxx..."
GITHUB_TOKEN_4O = "ghp_xxxxxxxxx..."
GITHUB_TOKEN_O4_MINI = "ghp_xxxxxxxxx..."

GITHUB_TOKEN_AZURE_4O_MINI = "ghp_xxxxxxxxx..."
GITHUB_TOKEN_AZURE_4O = "ghp_xxxxxxxxx..."
GITHUB_TOKEN_AZURE_O4_MINI = "ghp_xxxxxxxxx..."
GITHUB_TOKEN_LLAMA = "ghp_xxxxxxxxx..."
GITHUB_TOKEN_PHI = "ghp_xxxxxxxxx..."
```

---

## Running the Application

```bash
streamlit run app.py
```

---

## Supported Models

| Model                                | SDK    | Token Key                    |
| ------------------------------------- | ------ | ---------------------------- |
| openai/gpt-4o-mini                   | OpenAI | GITHUB_TOKEN_4O_MINI         |
| openai/gpt-4o                        | OpenAI | GITHUB_TOKEN_4O              |
| openai/o4-mini                       | OpenAI | GITHUB_TOKEN_O4_MINI         |
| openai/gpt-4o-mini (Azure)           | Azure  | GITHUB_TOKEN_AZURE_4O_MINI   |
| openai/gpt-4o (Azure)                | Azure  | GITHUB_TOKEN_AZURE_4O        |
| openai/o4-mini (Azure)               | Azure  | GITHUB_TOKEN_AZURE_O4_MINI   |
| meta/Llama-3.2-11B-Vision-Instruct   | Azure  | GITHUB_TOKEN_LLAMA           |
| microsoft/Phi-3.5-MoE-instruct       | Azure  | GITHUB_TOKEN_PHI             |

---

## Default Use Cases

- **Topic Explanation**: Simplify complex topics for broad understanding
- **Translation**: Translate text into various languages
- **Code Generation / Debugging**: Write or troubleshoot code snippets
- **Business Idea Generation**: Generate new business or startup ideas

---

## Security

- Tokens are **not hardcoded** in the source code
- Use **Streamlit Secrets Manager** or environment variables for sensitive information
- Do not commit `.streamlit/secrets.toml` or any file containing secrets to version control

---

## Example Usage

1. Select a model (e.g., `openai/gpt-4o-mini`)
2. Choose a use case (e.g., `Code Generation / Debugging`)
3. Optionally, enter a custom input such as: “Write a function to reverse a string in Python”
4. Click **Run** to receive an AI-generated response

---

## License

MIT License © 2025
