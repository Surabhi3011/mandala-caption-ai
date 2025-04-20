# Mandala Caption Generator (Streamlit)
# Generates poetic captions based on a short description or mood

import streamlit as st
import openai

# --- CONFIGURATION ---
openai.api_key = st.secrets.get("OPENAI_API_KEY", "sk-...")  # Replace or use secrets.toml

# --- UI SETUP ---
st.set_page_config(page_title="Mandala Caption Generator", layout="centered")
st.title("🌀 Mandala Caption Generator")
st.write("Describe your mandala, and get a poetic caption to match the vibe.")

# --- INPUTS ---
description = st.text_area("Describe your mandala or mood:",
                           placeholder="E.g., Floral mandala in soft blue and gold. Theme: balance and inner peace.")
style = st.selectbox("Select caption style:", ["Poetic", "Reflective", "Minimalist", "Free Verse", "Haiku"])
generate = st.button("✨ Generate Caption")

# --- OPENAI PROMPTING ---
def generate_caption(desc, tone):
    prompt = f"""
You are an artistic caption generator for visual mandalas. 
Based on the following description, generate a short {tone.lower()} caption (1–2 lines) that reflects the emotional or symbolic tone of the artwork.

Description: {desc}
Caption:
"""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60,
        temperature=0.8
    )
    return response.choices[0].text.strip()

# --- OUTPUT ---
if generate:
    if description.strip() == "":
        st.warning("Please enter a description of your mandala.")
    else:
        with st.spinner("Generating caption..."):
            caption = generate_caption(description, style)
            st.success("Here’s your caption:")
            st.markdown(f"> _{caption}_")

# --- FOOTER ---
st.markdown("---")
st.caption("Built by Surabhi Gupta — inspired by art, powered by language.")
