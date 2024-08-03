import streamlit as st
import requests

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


if __name__ == '__main__':
    page3()