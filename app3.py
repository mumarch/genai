# numpy version:1.26.4 is compatable with pandasai
# pip install numpy==1.26.4  pyyaml

import os
import pandas as pd
import streamlit as st # type: ignore
from pandasai import Agent
#from pandasai import LLM
#import numpy as np

#from pandasai.llm.local_llm import LocalLLM
from pandasai import SmartDataframe

#os.environ["PANDASAI_API_KEY"] = "$2a$10$fM2M9OzQKknKddp1YYRGKe/OpllKpux0yKRlZo8y2zTKBb0M/0U9a"
#API_KEY = "$2a$10$fM2M9OzQKknKddp1YYRGKe/OpllKpux0yKRlZo8y2zTKBb0M/0U9a"

# Securely store API key in environment variable (recommended)
PANDASAI_API_KEY = os.environ.get("PANDASAI_API_KEY")
if not PANDASAI_API_KEY:
    st.write("PANDASAI_API_KEY environment variable is not set")
    raise ValueError("PANDASAI_API_KEY environment variable is not set.")

st.title("Data Analysis using Prompts")

uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])

# reading the uploaded dataset
if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.write(data.head(2))

        agent = Agent(data)

        prompt = st.text_area("Enter your prompt")
    
        if st.button("Generate"):
            if prompt:
                with st.spinner("Generating response..."):
                    st.write(agent.chat(prompt))
    except Exception as e:
        st.error(f"Error processing file: {e}")
    
                





