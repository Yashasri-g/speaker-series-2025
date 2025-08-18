import streamlit as st
import os
from openai import OpenAI
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

# ----------------------------
# Model Configurations
# ----------------------------
MODEL_CONFIG = {
    # --- OpenAI Inference SDK ---
    "openai/gpt-4o-mini": {
        "sdk": "openai",
        "token_key": "GITHUB_TOKEN_4O_MINI",
    },
    "openai/gpt-4o": {
        "sdk": "openai",
        "token_key": "GITHUB_TOKEN_4O",
    },
    "openai/o4-mini": {
        "sdk": "openai",
        "token_key": "GITHUB_TOKEN_O4_MINI",
    },

    # --- Azure AI Inference SDK ---
    "openai/gpt-4o-mini (Azure)": {
        "sdk": "azure",
        "token_key": "GITHUB_TOKEN_AZURE_4O_MINI",
        "real_model": "openai/gpt-4o-mini",
    },
    "openai/gpt-4o (Azure)": {
        "sdk": "azure",
        "token_key": "GITHUB_TOKEN_AZURE_4O",
        "real_model": "openai/gpt-4o",
    },
    "openai/o4-mini (Azure)": {
        "sdk": "azure",
        "token_key": "GITHUB_TOKEN_AZURE_O4_MINI",
        "real_model": "openai/o4-mini",
    },
    "meta/Llama-3.2-11B-Vision-Instruct": {
        "sdk": "azure",
        "token_key": "GITHUB_TOKEN_LLAMA",
    },
    "microsoft/Phi-3.5-MoE-instruct": {
        "sdk": "azure",
        "token_key": "GITHUB_TOKEN_PHI",
    },
}

# ----------------------------
# Default Use Cases
# ----------------------------
USE_CASES = {
    "Topic Explanation": "Explain quantum computing in simple terms for a beginner.",
    "Translation": "Translate the following English text into French:\n\n'Technology connects people across the world.'",
    "Code Generation / Debugging": "Write a Python function to check if a number is prime. Also, fix this buggy code:\n\n```python\nfor i in range(5)\n    print(i)\n```",
    "Business Idea Generation": "Suggest 3 innovative AI-based business ideas in the field of healthcare.",
}

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Multi-Model Playground", layout="wide")
st.title("🤖 Multi-Model Playground")
st.write("Run prompts on multiple GitHub-hosted AI models (OpenAI + Azure).")

model_choice = st.selectbox("Choose a model", list(MODEL_CONFIG.keys()))

use_case_choice = st.selectbox("Choose a use case", ["Custom Prompt"] + list(USE_CASES.keys()))
if use_case_choice == "Custom Prompt":
    prompt = st.text_area("Enter your custom prompt here:", "Explain the basics of machine learning.")
else:
    prompt = USE_CASES[use_case_choice]
    st.info(f"🔎 Using pre-defined use case: **{use_case_choice}**")

if st.button("Run"):
    config = MODEL_CONFIG[model_choice]
    token_key = config["token_key"]

    if token_key not in st.secrets:
        st.error(f"⚠️ Missing secret: `{token_key}`. Please add it in Streamlit → Settings → Secrets.")
    else:
        token = st.secrets[token_key]

        try:
            # --- OpenAI SDK ---
            if config["sdk"] == "openai":
                client = OpenAI(
                    base_url="https://models.github.ai/inference",
                    api_key=token,
                )
                response = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model=model_choice,
                    temperature=1,
                    max_tokens=1024,
                    top_p=1,
                )
                st.subheader("✅ Response")
                st.write(response.choices[0].message.content)

            # --- Azure SDK ---
            elif config["sdk"] == "azure":
                real_model = config.get("real_model", model_choice)
                client = ChatCompletionsClient(
                    endpoint="https://models.github.ai/inference",
                    credential=AzureKeyCredential(token),
                )
                response = client.complete(
                    messages=[UserMessage(prompt)],
                    model=real_model,
                    temperature=1,
                    max_tokens=1024,
                    top_p=1,
                )
                st.subheader("✅ Response")
                st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"❌ Error running {model_choice}: {str(e)}")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Built with Streamlit · Supports OpenAI + Azure AI models via GitHub Inference API")
