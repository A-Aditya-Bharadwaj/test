import streamlit as st

# Create the Streamlit app
st.title("Streamlit Web Browser")

# Input for the website URL
website_url = st.text_input("Enter a website URL:")

# Button to open the website
if st.button("Open Website"):
    if website_url.startswith("http://") or website_url.startswith("https://"):
        # Display the web browser component
        st.components.v1.iframe(website_url, width=800, height=600)
    else:
        st.warning("Please enter a valid URL starting with 'http://' or 'https://'.")
