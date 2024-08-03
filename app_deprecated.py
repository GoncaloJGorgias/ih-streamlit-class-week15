import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

## Goals:
    # Home page

    # Page 1:
        ## See the data
        # Plot a map
        # Interact with the data

    # Page 2:
        ## Connect to an API and fetch some specific data about that location (latitude, longitude)

    # Page 3:
        ## Somewhat connected to page 2 results and will be used to get weather information through a public API

# Load our data
@st.cache_data #streamlit python decorator that allows us to store the data and don't need to reload/ re-run every single time 
def load_data():
    """ function that loads and stores data"""
    
    cali = fetch_california_housing()
    data = pd.DataFrame(cali.data, columns = cali.feature_names)
    data['Median_House_Value'] = cali.target

    data.columns = [col_.lower() for col_ in data.columns]

    return data

data = load_data()



# Home page
def home():
    """ Function that renders the main home page"""
    st.title(" Welcome to our first Streamlit APP!")

    st.write("""
            # Introduction:
            ### Streamlit is an open-source python package that allows us to create apps in a seamless form
            """)

# Page 1 : DataFrame showcase and add interactivity with plots
def page1():
    """ Function that encapsulates page1 logic:
    - Displays dataframe
    - Displays map chart
    - Allows user interactivity
"""
    st.title(" California Housing Prices Dataset")
    st.write(" ## Dataframe showcase")
    st.dataframe(data)

    # Map plot:
    st.write(" ## Map plot of housing in California")
    st.map(data[['latitude', 'longitude']])

    # Scatter plot:
    x_axis = st.selectbox("Choose a variable for the x-axis", data.columns)
    y_axis = st.selectbox("Choose a variable for the y-axis", data.columns)

    plt.figure(figsize=(10,6))
    plt.scatter(data[x_axis], data[y_axis], alpha=0.5 )
    plt.title(f"Scatter plot of {x_axis} by {y_axis}:")
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(plt)


# Page 2: Connect to an API and retrieve information about that endpoint
def page2():
    """Connects to an endpoint API based on user inputs and retrieves information about it.
    """

    st.title( "Get location information:")
    st.write(" Enter your selected latitude and longitude:")

    lat = st.slider('Slide me for Latitude', min_value=-90, max_value=90)
    lon = st.slider('Slide me for Longitude', min_value=-180, max_value=180)

    if st.button("Get location"):
        # using API to get point information
        response = requests.get(f"http://api.geonames.org/findNearbyPlaceNameJSON?lat={lat}&lng={lon}&username=gorgias_demand_gen")

        if response.status_code == 200:
            location_info = response.json()
            if location_info["geonames"]:
                st.write("Location information:")
                # We are looping through the geonames key:values:
                for loc in location_info['geonames']:
                    st.write(f" Name of location: {loc['name']}")
                    st.write(f" Country of location: {loc['countryName']}")
                    st.write(f" Info: {location_info['geonames']}")

                    st.session_state.city_name = loc['name']

            else:
                st.write(" No location was retrieved.")

        else:
            st.write(" Failed to make API request")

# Page 3:
def page3():
    """ Connects to an API and retrieves weather report based on previous selected city
"""

    st.title(" Get weather information:")
    city = st.session_state.get("city_name", None)
    # Retrieve city name from previous function:

    api_key ='5a68dbd3fe6242678ac130253242505'

    if city:
        st.write( f"City: {city}:")
        url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
        response = requests.get(url)

        if response.status_code == 200:
            weather_info = response.json()
            st.write(f"Weather in {weather_info['location']['name']}, {weather_info['location']['country']}:")
            st.write(f"Temperature: {weather_info['current']['temp_c']}°C")
            st.write(f"Weather: {weather_info['current']['condition']['text']}")
            st.write(f"Humidity: {weather_info['current']['humidity']}%")
            st.write(f"Wind: {weather_info['current']['wind_kph']}")

        else:
            st.write("Failed to fetch weather report information")
    else:
        st.write(" So far you ahven't selected any location from Page 2. Go to page 2 and input lat and longitude.")

# Side bar element:
st.sidebar.title(" Navigation bar")
options = st.sidebar.radio("Select a page", ["Home", "Page 1", "Page 2", "Page 3"])

if options == "Home":
    home()
elif options == "Page 1":
    page1()
elif options == "Page 2":
    page2()
else:
    page3()
