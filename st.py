import streamlit as st
from pytube import YouTube
import tempfile
import os

# Function to download a YouTube video
def download_video(video_url):
    try:
        # Create a temporary directory to save the video
        temp_dir = tempfile.mkdtemp()
       
        # Download the YouTube video
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        video_path = os.path.join(temp_dir, f"{yt.title}.mp4")
        stream.download(output_path=temp_dir)

        return video_path
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Streamlit app
st.title("YouTube Video Downloader and Player")

# User input for YouTube video URL
video_url = st.text_input("Enter the YouTube video URL:")

if st.button("Download Video"):
    if not video_url:
        st.warning("Please enter a YouTube video URL.")
    else:
        st.text("Downloading video...")
        video_path = download_video(video_url)
        st.text("Download complete!")

# Display the list of downloaded videos
downloaded_videos = [file for file in os.listdir(tempfile.gettempdir()) if file.endswith(".mp4")]

if downloaded_videos:
    selected_video = st.selectbox("Select a video to play:", downloaded_videos)

    if st.button("Play Selected Video"):
        video_path = os.path.join(tempfile.gettempdir(), selected_video)
        st.video(video_path)
else:
    st.info("No downloaded videos found.")
