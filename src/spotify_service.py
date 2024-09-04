from typing import List

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from Track import SpotifyTrack, Track


class SpotifyService:
    def __init__(self):
        scope = "playlist-modify-public playlist-modify-private"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    def get_user_playlists(self):
        playlists = self.sp.current_user_playlists()
        return {playlist["name"]: playlist["id"] for playlist in playlists["items"]}

    def create_playlist(self, playlist_name: str = None):
        if not playlist_name:
            playlist_name = input(
                "Enter the name of the playlist you want to add songs to: "
            )

        user_playlists = self.get_user_playlists()
        playlist_id = user_playlists.get(playlist_name)

        if playlist_id:
            print("Playlist existst already.")
            return playlist_id
        else:
            playlist = self.sp.user_playlist_create(
                user=self.sp.me()["id"], name=playlist_name
            )
            return playlist["id"]

    def search_track(self, track: Track):
        query = f"artist:{track.artist} track:{track.title}"
        results = self.sp.search(q=query, type="track", limit=1)
        if results["tracks"]["items"]:
            track = results["tracks"]["items"][0]
            return SpotifyTrack(
                artist=track["artists"][0]["name"],
                title=track["name"],
                uri=track["uri"],
            )
        else:
            return None

    def add_tracks_to_playlist(self, playlist_id, track_uris: List[str]):
        self.sp.playlist_add_items(playlist_id, track_uris)
