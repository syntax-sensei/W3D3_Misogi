import streamlit as st
from inference_calculator import calculate
import plotly.graph_objects as go

st.set_page_config(page_title="LLM Inference Calculator", layout="centered")

st.title("🤖 LLM Inference Cost & Performance Calculator")
st.write("Estimate latency, memory usage, and cost per request for large language models across various hardware types.")

# Sidebar Inputs
st.sidebar.header("🧠 Model & Inference Settings")
model_size = st.sidebar.number_input("Model Size (in B)", min_value=1.0, value=7.0, step=1.0)
tokens = st.sidebar.slider("Input Tokens", 1, 2048, 256)
batch_size = st.sidebar.slider("Batch Size", 1, 32, 1)
hardware_type = st.sidebar.selectbox("Hardware", ["cpu", "gpu", "a100", "tpu"])
deployment_mode = st.sidebar.selectbox("Deployment Mode", ["local", "api"])

# Run Calculator
if st.sidebar.button("🧮 Calculate"):
    result = calculate(model_size_b=model_size, tokens=tokens, batch_size=batch_size,
                       hardware_type=hardware_type, deployment_mode=deployment_mode)

    st.subheader("📊 Results")
    st.success("✅ Hardware Compatible" if result["Hardware Compatible"] else "❌ Not Compatible")

    st.metric("🕒 Latency (ms)", result["Latency (ms)"])
    st.metric("💾 Memory Usage (GB)", result["Memory Usage (GB)"])
    st.metric("💸 Cost per Request ($)", result["Cost per request ($)"])

    # Visualization
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=result["Latency (ms)"],
        title={"text": "Latency (ms)"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [0, 200]},
               'bar': {'color': "royalblue"},
               'steps': [
                   {'range': [0, 60], 'color': 'lightgreen'},
                   {'range': [60, 120], 'color': 'orange'},
                   {'range': [120, 200], 'color': 'red'}]}
    ))
    st.plotly_chart(fig)

    st.markdown("🧮 Tip: Lower model sizes and token counts reduce latency & cost.")
