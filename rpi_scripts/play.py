import os
import subprocess

# set the path to the directory containing the videos
video_dir = './videos'

# get a list of all the video files in the directory
videos = [f for f in os.listdir(video_dir) if os.path.isfile(os.path.join(video_dir, f)) and f.endswith('.mp4')]

# loop through the videos and play each one
for video in videos:
    # construct the full path to the video file
    video_path = os.path.join(video_dir, video)
    
    # use the subprocess module to play the video with the default media player
    subprocess.call(['start', '', video_path], shell=True)