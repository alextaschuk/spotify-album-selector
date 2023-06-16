import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

client_id = ['CLIENT_ID']
client_secret = ['CLIEN_SECRET']

redirect_uri = 'http://google.com/'
scope = 'user-library-read'


def get_album_names(results):
    for item in results['items']:
        album = item['album']
        album_names.append(album['name'])


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                     client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
results = sp.current_user_saved_albums()

album_names = []

get_album_names(results)  # load album info

while results['next']:
    results = sp.next(results)
    get_album_names(results)

for x in range(3):
    random.shuffle(album_names)

list_index = random.randrange(len(album_names) - 1)
album_to_listen_to = album_names[list_index]

print(album_to_listen_to + ' was chosen.')
