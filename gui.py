import streamlit as st
import requests

API_URL = "http://localhost:8000/shorten"

title = st.title("URL-Shortener")

long_url = st.text_input("enter url")
button = st.button("Shorten url")

if button:
    if long_url:
        try:
            response = requests.post(API_URL, json={"url": long_url})
            if response.ok:
                result = response.json()
                st.success("Shortening successfull")
                st.write(result["short_url"])
        
            else:
                st.error("Failed to shorten URL")
        except requests.exceptions.RequestException:
            st.error("Backend is offline")  

    else:
        st.error("Error")

        
