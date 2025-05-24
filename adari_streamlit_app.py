
import streamlit as st
import openai

st.set_page_config(page_title="ADARI – Campaign Localization Agent", layout="centered")

st.title("🎯 ADARI: Multilingual Campaign Localization Agent")

st.markdown("This agent helps you translate and adapt marketing campaigns for different markets while respecting brand tone, language, and feedback.")

# --- Input form ---
with st.form("adari_form"):
    st.markdown("### 📩 Base Campaign Inputs")
    base_message = st.text_area("Campaign Message", placeholder="e.g. Celebrate summer with 30% off sunglasses!")
    market = st.text_input("Target Market", placeholder="e.g. Brazil")
    language = st.text_input("Language", placeholder="e.g. Portuguese")
    tone = st.text_input("Tone", placeholder="e.g. Friendly, energetic")

    st.markdown("### 🧠 Optional Brand Context")
    brand_style = st.text_input("Describe your brand style", placeholder="e.g. Modern and casual tone with youthful appeal")
    past_campaigns = st.text_area("What has worked in previous campaigns?", placeholder="e.g. Short CTAs and use of emojis resonate well")

    submitted = st.form_submit_button("Generate Localized Campaign")

if submitted:
    # Build prompt
    prompt = f"""You are ADARI, a multilingual marketing assistant agent.

Your task is to:
- Translate and culturally adapt the following campaign message.
- Adjust it to the market, language, and tone.
- Use any provided brand memory or campaign context to maintain consistency.

Target Market: {market}
Language: {language}
Tone: {tone}

Brand Style: {brand_style}
Previous Campaigns: {past_campaigns}

Base Message: {base_message}

Return:
1. Localized marketing message
2. Explanation of tone/wording
3. Suggested improvement
"""

    st.markdown("### 🧠 Generated Prompt")
    st.code(prompt)

    st.markdown("### ✅ Feedback")
    feedback = st.radio("Was this suggestion helpful?", ["👍 Yes", "👎 No"])
    comments = st.text_area("Optional feedback to improve ADARI")

    st.success("This interaction has been recorded. Use this prompt in OpenAI Playground or your backend.")
