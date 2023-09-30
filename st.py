import streamlit as st
import os
from pytube import YouTube

video_url = st.text_input("Enter the YouTube video URL:")
if st.button("Download Video"):
    st.text("Downloading...")
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path='downloads')  # Save the video to a 'downloads' folder
    st.text("Download complete!")

# Get the current directory
current_directory = os.getcwd()

# List all files in the current directory
files = os.listdir(current_directory)

# Filter out directories and display only files
files = [file for file in files if os.path.isfile(os.path.join(current_directory, file))]

# Display the list of files in Streamlit
st.title("List of Files in Current Directory")
if not files:
    st.write("No files found in the current directory.")
else:
    for file in files:
        st.write(file)

if st.button("Play Video"):
    path = st.text_input("path:")
    st.video(path)  # Replace with the actual video filename
