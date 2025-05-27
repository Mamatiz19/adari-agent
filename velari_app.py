import streamlit as st

st.title("Velari Form")

market = st.text_input("Target Market")
language = st.text_input("Language")
tone = st.text_input("Tone")
brand_style = st.text_input("Brand Style")
avoid = st.text_input("Avoid")
past_success = st.text_input("Past Success")
campaign_message = st.text_area("Base Message")
product = st.text_input("Product")
group_age = st.selectbox("Age Target", ["Children", "Teenagers", "Adults", "Old Adults"])

if st.button("Generate Prompt"):
    st.markdown("### Output")
    st.code(f"""Target Market: {market}
Language: {language}
Tone: {tone}
Brand Style: {brand_style}
Avoid: {avoid}
Past Success: {past_success}
Base Message: {campaign_message}
Product: {product}
Age Target: {group_age}""")
