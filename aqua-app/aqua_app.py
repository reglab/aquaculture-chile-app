import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium import plugins
import geopandas as gpd
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Chile Aquaculture Data",
    page_icon="🐟",
    layout="wide"
)

# make multipage streamlit app appear on sidebar not selectbox

pages = {
    "Data Exploration": [
        st.Page('pages/page0_home.py', title="Home"),
        st.Page('pages/page1_salmon_complaints.py', title="Salmon Concessions & Complaints"),
        st.Page('pages/page2_sensors.py', title="Sensors"),
        st.Page('pages/page3_production.py', title="Production"),
        st.Page('pages/page3b_production_movement.py', title="Ownership and Production Trends"),
        st.Page('pages/page4_environmental.py', title="Environmental Impacts")
        
    ],
    "External Datasets": [
        st.Page('pages/page5_other.py', title="Other Visualizations")
    ],
}

pg = st.navigation(pages)
pg.run()




# page = st.sidebar.selectbox("Select the Page to Explore", ["Home", "Concessions", "Sensors Exploration", "Production Exploration", "Complaints Exploration"])

# if page == "Home":
#     splash_page()
# elif page == "Concessions Exploration":
#     concessions_exploration_page()
# elif page == "Sensors Exploration":
#     sensors_exploration_page()
# elif page == "Production Exploration":
#     production_exploration_page()
# elif page == "Complaints Exploration":
# page = st.sidebar.selectbox("Select the Page to Explore", ["Home", "Concessions Exploration", "Sensors Exploration", "Production Exploration", "Complaints Exploration"])

# if page == "Home":
#     splash_page()
# elif page == "Concessions Exploration":
#     concessions_exploration_page()
# elif page == "Sensors Exploration":
#     st.write("This is the sensors exploration page")
# elif page == "Production Exploration":
#     st.write("This is the production exploration page")
# elif page == "Complaints Exploration":
#     st.write("This is the complaints exploration page")