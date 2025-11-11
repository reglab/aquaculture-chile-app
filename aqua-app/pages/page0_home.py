import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from pyprojroot import here


import os 
# print current directory
print('current directory:')
print(os.getcwd())  
st.write('current directory:')
st.write(os.getcwd())  



# # spinner until the entire page is loaded
# with st.spinner("Loading page..."):
#     # pause for 3 seconds
#     time.sleep(3)

# # @st.cache_data(show_spinner="Loading map...")
# def load_html_map():
#     # open /Users/victholl/Documents/aquaculture-chile-app/aqua-app/media/concession_eda_production_bubble_map2.html
#     with open('media/concession_eda_production_bubble_map2.html', 'r') as file:
#         html_map = file.read()
#     return html_map

# # title
# st.title("Welcome to the Chile Aquaculture Project")
# # display the html map
# st.components.v1.html(load_html_map(), width="100%", height=900)