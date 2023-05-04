from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

def downloadVideos(urls):

    for i, video_url in enumerate(urls):
        # Define the YouTube video URL

        # Download the YouTube video using pytube
        youtube = YouTube(video_url)
        video = youtube.streams.get_highest_resolution().download()

        # Convert the downloaded video to MP4 format using moviepy
        clip = VideoFileClip(video)
        mp4_file = f'./videos/video_{i}.mp4'
        clip.write_videofile(mp4_file)

        # Clean up the downloaded file
        clip.reader.close()
        clip.audio.reader.close_proc()
    # clean up mp4 files
    os.system("rm *.mp4")
