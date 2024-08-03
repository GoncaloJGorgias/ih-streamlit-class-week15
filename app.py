import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from my_pages import (
    page_Home as home,
    page_California_Dataset as page1,
    page_Location_Information as page2,
    page_Weather_Information as page3
)

# Side bar element:
st.sidebar.title(" Navigation bar")


page = st.sidebar.selectbox(
    "Select a page",
    [
        "🏠 Home",
        "🏡 California Housing Prices",
        "🌍 Location Information",
        "☀️ Weather Information",
    ]
)

if page == "🏠 Home":
    # the first home refers to the name of the file and the last home refers
    # to the name of the function that is inside the file
    home.home()
elif page == "🏡 California Housing Prices":
    page1.page1()
elif page == "🌍 Location Information":
    page2.page2()
else:
    page3.page3()
