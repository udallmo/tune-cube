import requests

from getToken import getToken
from constants import TEST_TRACKS, TEST_VIDEOS
from getVideo import getVideo
from downloadVideo import downloadVideos
from sendtoS3 import sendToS3

def getTopTracks(token):
    headers = {'Authorization': 'Bearer ' + token}

    # Set up parameters for request
    time_range = 'short_term' # replace with the time range of your choice ('short_term', 'medium_term', or 'long_term')
    limit = 20 # replace with the number of tracks you want to retrieve

    # Send GET request to get top tracks
    # TODO: add an offset to get newer songs
    response = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=headers, params={'time_range': time_range, 'limit': limit})

    print(response)
    if response.status_code == 401:
        raise Exception("ERROR 401: needs a new token!!!")
        
    # Print the track names and artists

    tracks = dict()
    for track in response.json()['items']:
        tracks[track['name']] = track['artists'][0]['name']
        # print(f"{track['name']} by {track['artists'][0]['name']}")
    return tracks


if __name__ == '__main__':
    # token = getToken()
    token = "BQBRNsADyi1WOY5BVK17lLrHL4I50ksyeROpO-m9KcWDgZLtJEjS7TEHlnCWrklxvxfvUq3yU7hVUpovj3nE9HynNz3DLx-7N0J6nO9qzYunvYwJQCbjQK-sNOVJKZbptvMIfAVS8obqbk13fy4Fg_Bgzd9P1u-LzbSnFuwKM0bfDPsJLbpgpwL2"
    
    # tracks = getTopTracks(token)
    tracks = TEST_TRACKS

    # videoURLs = getVideo(tracks)
    videoURLs = TEST_VIDEOS

    #DONWLOAD VIDEOs from URL
    # downloadVideos(videoURLs)

    # TODO: send videos to AWS
    sendToS3()


