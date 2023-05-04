import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

from constants import YOUTUBE_API_KEY

# Set up the API key and build the YouTube API client
DEVELOPER_KEY = YOUTUBE_API_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)


def getVideo(tracks):
    output = []
    videoList = []
    for id in tracks:
        # Define the search query
        query = id + ' ' + tracks[id]

        # Call the search.list method to retrieve search results
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=1
        ).execute()

        # Extract the video IDs from the search results
        video_ids = []
        for search_result in search_response.get('items', []):
            video_ids.append(search_result['id']['videoId'])

        # Call the videos.list method to get the URLs of the videos
        videos_response = youtube.videos().list(
            id=','.join(video_ids),
            part='id,snippet',
            maxResults=1
        ).execute()

        # Print the title and URL of each video in the search results
        video_result = videos_response.get('items', [])[0]
        video_url = f'https://www.youtube.com/watch?v={video_result["id"]}'
        # for video_result in videos_response.get('items', []):
        #     video_url = f'https://www.youtube.com/watch?v={video_result["id"]}'
        #     print(f'{video_result["snippet"]["title"]}: {video_url}')

        out = f'{id}, {tracks[id]}, {video_result["snippet"]["title"]}, {video_url}\n'
        output.append(out)
        videoList.append(video_url)

    # f = open('videoList.csv','w')
    # for vURL in videoList:
    #     f.write(f'{vURL}\n') #Give your csv text here.
    # ## Python will convert \n to os.linesep
    # f.close()
    # TODO: return a dictionary of name: url
    print(videoList)
    return videoList
    # NAME ARTIST VIDEONAME URL 