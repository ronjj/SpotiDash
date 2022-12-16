import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json


#Prints Out Whole Response In A Nice Way
#print(json.dumps(current, sort_keys=False, indent = 4))


#Helper Functions to get information on the currently playing song

SPOTIPY_CLIENT_ID = 'e28a6e30300349439d3a8383b8304ac2'
SPOTIPY_CLIENT_SECRET = 'd0ef0a7539dd4202bda55ed6b4f81497'
SPOTIPY_REDIRECT_URI = 'https://www.google.com'

scope = 'user-read-currently-playing'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI ))

current = sp.currently_playing()


def is_playing():
    """Returns True if song is playing, False if a song is not currently playing"""
    result = current['is_playing']
    print(result)
    return result

def get_currently_playing():
    """Returns a string of the currently playing song"""
   
    artist_name = current['item']['album']['artists'][0]['name']
    song_title = current['item']['name']

    if artist_name == None:
        result = 'No song is playing'
        print(result)
    else:
        result = f'{song_title} by {artist_name} is playing'
        print(result)
    
    return result

def get_currently_playing_uri():
    link = current['item']['external_urls']['spotify']

    if link == None:
        print("nothing is playing")
    else:
        print(link)
        return link

get_currently_playing()
is_playing()





# spotipy_client_id = os.environ['SPOTIPY_CLIENT_ID']
# spotipy_secret = os.environ['SPOTIPY_CLIENT_SECRET']
# spotipy_redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']

# scope = "user-library-read"

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])