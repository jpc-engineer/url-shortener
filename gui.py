import streamlit as st
import requests

API_URL = "http://localhost:8000/shorten"
BASE_URL = "http://localhost:8000"

title = st.title("URL-Shortener")

long_url = st.text_input("enter url (Full link (https:// required)")
button = st.button("Shorten url")
st.divider()
code_to_del = st.text_input("Link to delete")

del_button = st.button("Delete Link")

if del_button:
    if code_to_del:
        try:
            response = requests.delete(f"{BASE_URL}/{code_to_del}")
            if response.ok:
                st.success("Deletion successful")
                st.write(f"{code_to_del} Deleted successfully")
            else:
                st.error("Failed to delete link")
        except requests.exceptions.RequestException:
            st.error("Backend is offline")

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

        
