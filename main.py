import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

class Spotify:
    token = TOKEN
    def __init__(self, token):
        self.token = token
