import os
import streamlit as st
from openai import OpenAI
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# -----------------------------
# MODEL CONFIGURATION
# -----------------------------
MODEL_CONFIG = {
    # OpenAI models (via GitHub Models API)
    "GitHub - GPT-4o-mini": {
        "id": "openai/gpt-4o-mini",
        "provider": "github"
    },
    "GitHub - GPT-4o": {
        "id": "openai/gpt-4o",
        "provider": "github"
    },
    "GitHub - o1-mini": {
        "id": "openai/o1-mini",
        "provider": "github"
    },

    # Microsoft models (via GitHub Models API using Azure SDK)
    "Microsoft - Phi-3.5-MoE": {
        "id": "microsoft/phi-3.5-moe-instruct",
        "provider": "azure"
    },
    "Microsoft - Phi-3-mini": {
        "id": "microsoft/phi-3-mini-4k-instruct",
        "provider": "azure"
    }
}

# -----------------------------
# STREAMLIT APP CONFIG
# -----------------------------
st.set_page_config(page_title="Texora", layout="centered")
st.title("⚡ Texora - AI Playground")

st.markdown("Choose a model, set parameters, and run your prompt!")

# -----------------------------
# USER INPUT
# -----------------------------
task = st.radio("Select a task:", [
    "Code Generator", "Translator", "Topic Explanation", "Research", "Custom Prompt"
])

prompt = st.text_area("✍️ Enter your prompt:", height=150)

system_message = st.text_input("⚙️ System role (optional)", placeholder="e.g., You are a helpful assistant.")

temperature = st.slider("Temperature", 0.0, 2.0, 1.0, 0.1)
max_tokens = st.slider("Max tokens", 256, 4096, 1024, 128)
top_p = st.slider("Top-p", 0.0, 1.0, 1.0, 0.1)

model_choice = st.selectbox("Choose a model:", list(MODEL_CONFIG.keys()))

# -----------------------------
# RUN BUTTON
# -----------------------------
if st.button("Run"):
    if not prompt.strip():
        st.warning("⚠️ Please enter a prompt.")
    else:
        config = MODEL_CONFIG[model_choice]
        model_id = config["id"]
        provider = config["provider"]

        try:
            # -----------------------------
            # GitHub Models (OpenAI client)
            # -----------------------------
            if provider == "github":
                client = OpenAI(
                    base_url="https://models.github.ai/inference",
                    api_key=os.environ["GITHUB_TOKEN"]
                )

                messages = []
                if system_message:
                    messages.append({"role": "system", "content": system_message})
                messages.append({"role": "user", "content": prompt})

                response = client.chat.completions.create(
                    messages=messages,
                    model=model_id,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    top_p=top_p
                )
                output = response.choices[0].message.content

            # -----------------------------
            # Microsoft Models (Azure client)
            # -----------------------------
            elif provider == "azure":
                client = ChatCompletionsClient(
                    endpoint="https://models.github.ai/inference",
                    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"])
                )

                messages = []
                if system_message:
                    messages.append(SystemMessage(system_message))
                messages.append(UserMessage(prompt))

                response = client.complete(
                    messages=messages,
                    model=model_id,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    top_p=top_p
                )
                output = response.choices[0].message.content

            # -----------------------------
            # DISPLAY OUTPUT
            # -----------------------------
            st.success("✅ Response:")
            st.write(output)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
