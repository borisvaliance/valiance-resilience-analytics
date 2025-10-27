import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import subprocess
import sys
import time
import socket

def start_backend_if_needed(module_path="src.backend:app", host="127.0.0.1", port=8000):
    """Start uvicorn in background if nothing is listening on host:port."""
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((host, port))
        s.close()
        return
    except Exception:
        pass

    cmd = [
        sys.executable, "-m", "uvicorn",
        module_path,
        "--host", host,
        "--port", str(port),
        "--log-level", "warning"
    ]
    # Start background process; suppress output
    subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)  # give backend a moment to start

# call before creating UI so backend is available
start_backend_if_needed()

class ResilienceApp:
    def __init__(self):
        st.set_page_config(page_title="Resilience Analytics", layout="wide")
        self.data = None
        
    def run(self):
        st.title("Resilience Analytics Dashboard")
        
        # Sidebar for data upload
        with st.sidebar:
            uploaded_file = st.file_uploader("Upload CSV Data", type=["csv"])
            if uploaded_file is not None:
                self.data = pd.read_csv(uploaded_file)
                st.success("Data loaded successfully!")
        
        if self.data is not None:
            self.show_analysis()
    
    def show_analysis(self):
        st.header("Data Overview")
        st.dataframe(self.data.head())
        
        # Basic statistics
        st.header("Statistical Summary")
        st.write(self.data.describe())
        
        # Correlation heatmap
        st.header("Correlation Analysis")
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(self.data.corr(), annot=True, cmap='coolwarm')
        st.pyplot(fig)

if __name__ == "__main__":
    app = ResilienceApp()
    app.run()