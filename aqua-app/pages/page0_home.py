import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# center title
st.title("Welcome to the Chile Aquaculture Project")

# insert html map from /Users/victholl/Documents/aquaculture_chile/vict_playground/concession_eda.html
@st.cache_data(show_spinner="Loading map...")
def load_html_map():
    with open('media/concession_eda_production_bubble_map2.html', 'r') as file:
        html_map = file.read()
    return html_map

# make map bigger height and width
st.components.v1.html(load_html_map(), width="100%", height=900)
