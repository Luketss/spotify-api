import os
from dotenv import load_dotenv
import requests
import json

from utils import converting_code64

load_dotenv()
TOKEN = os.getenv("TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


class Spotify:
    def __init__(self, client_id, client_secret):
        self.client_id = (client_id,)
        self.client_secret = client_secret
        self.token = self.get_token()

    def get_spotify_token(self) -> str:
        url = "https://accounts.spotify.com/api/token"

        headers = {
            "Authorization": f"Basic {converting_code64(self.client_id, self.client_secret)}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        payload = {"grant_type": "client_credentials"}

        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            json_result = response.json()
            token = json_result["access_token"]
            return token
        except requests.RequestException as e:
            print(f"Error getting Spotify token: {e}")
            return None

    def get_id_track(self, track):
        route = "https://api.spotify.com/v1/search"
        query = f"?q={track}&type=track&limit=1"
        url = route + query
        r = requests.get(url=url, headers={"Authorization": "Bearer  " + Spotify.token})
        json_result = json.loads(r.content)
        track_id = json_result["tracks"]["items"][0]["id"]
        return track_id

    def get_search_track(self, id):
        route = f"https://api.spotify.com/v1/tracks/{id}"
        url = route
        r = requests.get(url=url, headers={"Authorization": "Bearer  " + Spotify.token})
        json_result = json.loads(r.content)
        track = json_result
        return track


spotify = Spotify(CLIENT_ID, CLIENT_SECRET)
track_id = spotify.get_id_track("downwithme")
print(spotify.get_search_track(track_id))
