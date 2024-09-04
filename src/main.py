from scraper import scrape_episodes, scrape_tracks
from spotify_service import SpotifyService

# Usage example
show_url = "https://www.nts.live/shows/macca"
# episodes = scrape_episodes(show_url, dynamic_page=False)
episode_url = "https://www.nts.live/shows/macca/episodes/macca-10th-august-2024"
tracks = scrape_tracks(episode_url)

spotify_service = SpotifyService()
playlist_id = spotify_service.create_playlist("test_single_episode")

track_uris = []
for track in tracks.values():
    spotify_track = spotify_service.search_track(track)
    print(f"NTS: {track}")
    if not spotify_track:
        print(f"SPF: NOTHING - NOTHING")
    else:
        print(f"SPF: {spotify_track.artist} - {spotify_track.title}")
        track_uris.append(spotify_track.uri)

print(
    f"\nFound {len(track_uris)} of {len(tracks)} tracks. Adding them to the playlist now."
)

spotify_service.add_tracks_to_playlist(playlist_id=playlist_id, track_uris=track_uris)
