import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up authentication
scope = "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def get_user_playlists():
    playlists = sp.current_user_playlists()
    return {playlist["name"]: playlist["id"] for playlist in playlists["items"]}


def create_playlist():
    playlist_name = input("Enter the name of the playlist you want to add songs to: ")

    user_playlists = get_user_playlists()
    playlist_id = user_playlists.get(playlist_name)

    if playlist_id:
        print("Playlist existst already.")
    else:
        sp.user_playlist_create(user=sp.me()["id"], name=playlist_name)
        return


def search_track(track_name):
    results = sp.search(q=track_name, type="track", limit=1)
    sp.search()
    if results["tracks"]["items"]:
        return results["tracks"]["items"][0]["uri"]
    return None


create_playlist()
