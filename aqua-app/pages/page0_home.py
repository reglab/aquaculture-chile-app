import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from pyprojroot import here

# set root directory
root = here()

print('root directory:')
print(root)

# # spinner until the entire page is loaded
# with st.spinner("Loading page..."):
#     time.sleep(3)

# # @st.cache_data(show_spinner="Loading map...")
# # insert html map from /Users/victholl/Documents/aquaculture_chile/vict_playground/concession_eda.html
# def load_html_map():
#     with open(root / 'media' / 'concession_eda_production_bubble_map2.html', 'r') as file:
#         html_map = file.read()
#     return html_map
# st.title("Welcome to the Chile Aquaculture Project")
# st.components.v1.html(load_html_map(), width="100%", height=900)