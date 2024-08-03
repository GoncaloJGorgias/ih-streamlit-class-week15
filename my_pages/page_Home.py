import streamlit as st

# Home page
def home():
    """ Function that renders the main home page"""
    st.title(" Welcome to our first Streamlit APP!")

    st.write("""
            # Introduction:
            ### Streamlit is an open-source python package that allows us to create apps in a seamless form
            """)

if __name__ == '__main__':
    home()
