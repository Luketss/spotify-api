import os
from dotenv import load_dotenv
import requests
import base64
import json

load_dotenv()
TOKEN = os.getenv('TOKEN')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def converting_code64():
    string = CLIENT_ID + ':' + CLIENT_SECRET
    string_bytes = string.encode('utf-8')
    base64_bytes = str(base64.b64encode(string_bytes), 'utf-8')
    return base64_bytes

def get_token():
    url = 'https://accounts.spotify.com/api/token'

    headers = {
        'Authorization' : 'Basic ' + converting_code64(),
        'Content-Type' : 'application/x-www-form-urlencoded'
    }

    payload = {
        'grant_type' : 'client_credentials'
    }

    r = requests.post(url, headers=headers, data=payload)
    json_result = json.loads(r.content)
    token = json_result['access_token']
    return token

TOKEN = get_token()

class Spotify:
    token = TOKEN

    def __init__(self, token):
        self.token = token

    def get_id_track(self, track):
        route = 'https://api.spotify.com/v1/search'
        query = f"?q={track}&type=track&limit=1"  
        url = route + query
        r = requests.get(url=url, headers= {'Authorization': 'Bearer  ' + Spotify.token})
        json_result = json.loads(r.content)
        track_id  = json_result['tracks']['items'][0]['id']
        return track_id

    def get_search_track(self, id):
        route = f'https://api.spotify.com/v1/tracks/{id}'
        url = route
        r = requests.get(url=url, headers= {'Authorization': 'Bearer  ' + Spotify.token})
        json_result = json.loads(r.content)
        track = json_result
        return track

spotify = Spotify(TOKEN)
track_id = spotify.get_id_track('downwithme')
print(spotify.get_search_track(track_id))


