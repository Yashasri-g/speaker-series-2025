import os
import streamlit as st
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage, SystemMessage
from azure.core.credentials import AzureKeyCredential
from openai import OpenAI

# -------------------------------
# Mapping models to secrets
# -------------------------------
MODEL_CONFIG = {
    "Azure GPT-4o Mini": {
        "id": "openai/gpt-4o-mini",
        "token": "AZURE_4O_MINI_TOKEN",
        "provider": "azure",
    },
    "Azure GPT-4o": {
        "id": "openai/gpt-4o",
        "token": "AZURE_4O_TOKEN",
        "provider": "azure",
    },
    "Azure o4-mini": {
        "id": "openai/o4-mini",
        "token": "AZURE_O4_MINI_TOKEN",
        "provider": "azure",
    },
    "Azure Llama-3.2-11B": {
        "id": "meta-llama/Llama-3.2-11B-Vision-Instruct",
        "token": "AZURE_LLAMA_TOKEN",
        "provider": "azure",
    },
    "Azure Phi-3.5-MoE": {
        "id": "microsoft/Phi-3.5-MoE-instruct",
        "token": "AZURE_PHI_TOKEN",
        "provider": "azure",
    },
    "OpenAI GPT-4o Mini": {
        "id": "gpt-4o-mini",
        "token": "OPENAI_4O_MINI_TOKEN",
        "provider": "openai",
    },
    "OpenAI GPT-4o": {
        "id": "gpt-4o",
        "token": "OPENAI_4O_TOKEN",
        "provider": "openai",
    },
    "OpenAI o4-mini": {
        "id": "o4-mini",
        "token": "OPENAI_O4_MINI_TOKEN",
        "provider": "openai",
    },
}

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="AI Workbench", page_icon="🤖", layout="wide")
st.title("🤖 AI Workbench")
st.markdown("Choose a model and task, then enter your prompt.")

# Model selector
model_choice = st.selectbox("Select Model", list(MODEL_CONFIG.keys()))

# Task selector
task = st.radio(
    "Choose a task",
    ["Code Generator", "Translator", "Topic Explanation", "Research Assistant", "Custom Prompt"],
)

# Input prompt
prompt = st.text_area("Enter your prompt", height=150)

if st.button("Run"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        config = MODEL_CONFIG[model_choice]
        model_id = config["id"]
        token = os.environ.get(config["token"])
        provider = config["provider"]

        if provider == "azure":
            client = ChatCompletionsClient(
                endpoint="https://models.github.ai/inference",
                credential=AzureKeyCredential(token),
            )
            response = client.complete(
                model=model_id,
                messages=[SystemMessage("You are a helpful assistant."), UserMessage(prompt)],
                temperature=1,
                max_tokens=512,
                top_p=1,
            )
            st.success(response.choices[0].message.content)

        elif provider == "openai":
            client = OpenAI(api_key=token, base_url="https://api.openai.com/v1")
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                temperature=1,
                max_tokens=512,
                top_p=1,
            )
            st.success(response.choices[0].message.content)
