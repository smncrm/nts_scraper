import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up authentication
scope = "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def get_user_playlists():
    playlists = sp.current_user_playlists()
    return {playlist['name']: playlist['id'] for playlist in playlists['items']}

get_user_playlists()

