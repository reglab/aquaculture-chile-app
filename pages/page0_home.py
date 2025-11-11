import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from pathlib import Path


# # spinner until the entire page is loaded
# with st.spinner("Loading page..."):
#     # pause for 3 seconds
#     time.sleep(3)

@st.cache_data(show_spinner="Loading map...")
def load_html_map():
    # Use relative path that works both locally and on server
    file_path = Path(__file__).parent.parent / "media" / "concession_eda_production_bubble_map2.html"
    with file_path.open('r') as file:
        html_map = file.read()
    return html_map

# title
st.title("Welcome to the Chile Aquaculture Project")
# display the html map
st.components.v1.html(load_html_map(), width="100%", height=900)