import os
from dotenv import load_dotenv
import streamlit as st
import requests

load_dotenv()

st.set_page_config(page_title="NFIRS AI Dashboard", layout="wide")

st.title("NFIRS AI Dashboard")
st.caption("Local environment demo")

st.write("Environment:", os.getenv("APP_ENV", "local"))
st.write("AI Provider:", os.getenv("AI_PROVIDER", "azure"))

st.divider()

try:
    r = requests.get("http://127.0.0.1:8000/health", timeout=3)
    st.subheader("API /health response")
    st.json(r.json())
except Exception as e:
    st.warning(f"FastAPI backend not reachable: {e}")
