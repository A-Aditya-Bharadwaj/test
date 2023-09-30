import streamlit as st
from googleapiclient.discovery import build

# Set your API key
API_KEY = "AIzaSyCahbpYK90MAmocUXpvi4BictBUjryJZo4"
CX = "009a9cd036ce642b7"

# Create a function to perform the Google search
def google_search(query, num_results=10):
    service = build("customsearch", "v1", developerKey=API_KEY)
    results = service.cse().list(q=query, cx=CX, num=num_results).execute()
    return results.get("items", [])

# Create the Streamlit app
st.title("Google Search App")

# Input for the search query
query = st.text_input("Enter your search query:")

if st.button("Search"):
    st.text("Searching...")

    # Perform the search
    results = google_search(query)

    # Display search results
    if results:
        for result in results:
            st.write(f"Title: {result['title']}")
            st.write(f"Link: {result['link']}")
            st.write(f"Snippet: {result['snippet']}")
            st.write("----")
    else:
        st.warning("No results found.")