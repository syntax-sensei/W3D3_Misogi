import streamlit as st
from recommendation_engine import recommend_agents

st.set_page_config(page_title="AI Coding Agent Recommender", layout="centered")

st.title("🤖 LLM-Powered Coding Agent Recommender")
st.write("Enter a coding task below, and get smart, LLM-backed recommendations!")

task = st.text_area("📝 Describe your coding task")

if st.button("Get Recommendations") and task.strip():
    with st.spinner("Thinking... 🤔"):
        recommendations = recommend_agents(task)
    st.subheader("🔍 Top Recommendations:")
    st.markdown(recommendations)
