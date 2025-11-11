import plotly.express as px
import streamlit as st



with open('media/disconnection_map.html', 'r') as file:
    html_map_1 = file.read()

# make map bigger height and width
st.components.v1.html(html_map_1, width="100%", height=1000)