import streamlit as st
import requests

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


if __name__ == '__main__':
    page2()
