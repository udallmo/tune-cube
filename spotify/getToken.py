import json
import requests
import base64

from constants import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


def getToken():
    # Set up credentials
    client_id = SPOTIFY_CLIENT_ID
    client_secret = SPOTIFY_CLIENT_SECRET
    redirect_uri = 'http://localhost:8888/callback'
    scope = 'user-top-read user-read-recently-played'
    auth_url = 'https://accounts.spotify.com/authorize'
    token_url = 'https://accounts.spotify.com/api/token'

    # Construct the authorization URL
    auth_payload = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': redirect_uri,
        'scope': scope
    }

    # Construct the authorization URL
    auth_payload = {'client_id': client_id, 'response_type': 'code',
                    'redirect_uri': redirect_uri, 'scope': scope}
    output = auth_url + '?'
    for i, key in enumerate(auth_payload):
        print()
        if key == "redirect_uri":
            val = "http%3A%2F%2Flocalhost%3A8888%2Fcallback"
            output += f'{key}={val}'
        else:
            output += f'{key}={auth_payload[key]}'
        
        if i+1 != len(auth_payload.keys()):
            output += '&'
        
    # auth_response = requests.get(auth_url, params=auth_payload)
    print(output)

    # Retrieve the authorization code from the URL
    auth_code = input('Enter the authorization code from the URL: ')

    # Construct the request body for the access token
    token_payload = {'grant_type': 'authorization_code',
                     'code': auth_code, 'redirect_uri': redirect_uri}
    token_header = {'Authorization': 'Basic ' +
                    base64.b64encode((client_id + ':' + client_secret).encode()).decode()}
    token_response = requests.post(
        token_url, data=token_payload, headers=token_header)

    # Extract the access token from the response
    access_token = token_response.json()['access_token']
    print(access_token)
    return access_token
