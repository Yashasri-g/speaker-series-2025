import os
import streamlit as st
from azure.ai.inference import ChatCompletionsClient as AzureChatClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from openai import OpenAI

# ----------------------------------------
# Setup Streamlit Page
# ----------------------------------------
st.set_page_config(page_title="AI Playground", page_icon="🤖", layout="centered")

st.title("🤖 AI Playground with GitHub Marketplace Models")
st.write("Experiment with Azure AI + OpenAI models in one place.")

# ----------------------------------------
# Available Models
# ----------------------------------------
AZURE_MODELS = {
    "OpenAI - GPT 4o mini (Azure)": "openai/gpt-4o-mini",
    "OpenAI - GPT 4o (Azure)": "openai/gpt-4o",
    "OpenAI - GPT o4 mini (Azure)": "openai/gpt-o4-mini",
    "Meta Llama 3.2 11B Vision Instruct": "meta-llama/Llama-3.2-11B-Vision-Instruct",
    "Microsoft Phi-3.5 MoE Instruct (128k)": "microsoft/phi-3.5-moe-instruct-128k"
}

OPENAI_MODELS = {
    "OpenAI - GPT 4o mini (SDK)": "gpt-4o-mini",
    "OpenAI - GPT 4o (SDK)": "gpt-4o",
    "OpenAI - GPT o4 mini (SDK)": "o4-mini"
}

ALL_MODELS = {**AZURE_MODELS, **OPENAI_MODELS}

# ----------------------------------------
# Authentication
# ----------------------------------------
github_token = os.getenv("GITHUB_TOKEN")
openai_key = os.getenv("OPENAI_API_KEY")

if not github_token and not openai_key:
    st.error("⚠️ Please set your GITHUB_TOKEN (for Azure models) or OPENAI_API_KEY (for OpenAI SDK).")
    st.stop()

azure_client = None
if github_token:
    azure_client = AzureChatClient(
        endpoint="https://models.github.ai/inference",
        credential=AzureKeyCredential(github_token),
    )

openai_client = None
if openai_key:
    openai_client = OpenAI(api_key=openai_key)

# ----------------------------------------
# Mode Selection
# ----------------------------------------
mode = st.radio(
    "Select a mode:",
    ["Custom Prompt", "Code Generator", "Translator", "Topic Explanation", "Research"],
    horizontal=True
)

model_name = st.selectbox("🔽 Choose a model:", list(ALL_MODELS.keys()))
selected_model = ALL_MODELS[model_name]

# ----------------------------------------
# Mode Logic
# ----------------------------------------
user_prompt = ""

if mode == "Custom Prompt":
    st.subheader("💬 Enter any custom prompt")
    user_prompt = st.text_area("Your prompt here:")

elif mode == "Code Generator":
    st.subheader("💻 Generate Code")
    lang = st.selectbox("Choose programming language:", ["Python", "Java", "C++", "JavaScript"])
    desc = st.text_area("Describe the code you want:")
    if desc:
        user_prompt = f"Write a {lang} code for the following requirement:\n{desc}"

elif mode == "Translator":
    st.subheader("🌐 Translator")
    text = st.text_area("Enter text to translate:")
    target_lang = st.selectbox("Translate to:", ["English", "Hindi", "Telugu", "French", "German"])
    if text:
        user_prompt = f"Translate this into {target_lang}: {text}"

elif mode == "Topic Explanation":
    st.subheader("📘 Explain a Topic")
    topic = st.text_input("Enter a topic:")
    level = st.selectbox("Explain for:", ["Beginner", "Intermediate", "Expert"])
    if topic:
        user_prompt = f"Explain {topic} to a {level.lower()} level learner."

elif mode == "Research":
    st.subheader("🔍 Research Assistant")
    query = st.text_area("Enter your research query:")
    if query:
        user_prompt = f"Provide a detailed research-style response with citations if possible on: {query}"

# ----------------------------------------
# Run Model
# ----------------------------------------
if st.button("▶ Run Model") and user_prompt.strip():
    with st.spinner("Generating response..."):
        response_text = ""

        if model_name in AZURE_MODELS and azure_client:
            response = azure_client.complete(
                messages=[
                    SystemMessage("You are a helpful AI assistant."),
                    UserMessage(user_prompt),
                ],
                model=selected_model,
                temperature=1,
                max_tokens=1024,
                top_p=1
            )
            response_text = response.choices[0].message.content

        elif model_name in OPENAI_MODELS and openai_client:
            response = openai_client.chat.completions.create(
                model=selected_model,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=1,
                max_tokens=1024,
                top_p=1
            )
            response_text = response.choices[0].message.content

        else:
            st.error("⚠️ No valid client configured for this model.")
            st.stop()

        st.success("✅ Response generated!")
        st.markdown("### 📝 Model Response")
        st.write(response_text)
