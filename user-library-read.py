import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json

#Main Dashboard Information

#Prints Out Whole Response In A Nice Way
# print(json.dumps(current['items'], sort_keys=False, indent = 4))

SPOTIPY_CLIENT_ID = 'e28a6e30300349439d3a8383b8304ac2'
SPOTIPY_CLIENT_SECRET = 'd0ef0a7539dd4202bda55ed6b4f81497'
SPOTIPY_REDIRECT_URI = 'https://www.google.com'

NUMBER_OF_SONGS = 5

scope = 'user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI ))
current = sp.current_user_saved_albums(limit=NUMBER_OF_SONGS)



def get_most_recent_albums():
    acc = []
    for x in range(NUMBER_OF_SONGS):
        
        artist_name = current['items'][x]['album']['artists'][0]['name']
        album_name = current['items'][x]['album']['name']
        date_added = current['items'][x]['added_at']
        date_added = date_added[:-10]

        print(f'{x+1}: {album_name}, {artist_name}. Added on {date_added}')
        acc.append(f'{x+1}: {album_name}, {artist_name}. Added on{date_added}')

    return acc

get_most_recent_albums()





    