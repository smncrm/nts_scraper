from scraper import scrape_episodes, scrape_tracks
from spotify_service import SpotifyService

# Usage example - Find the first track of each episode of the One Glove Breakfast Show and add them to a playlist.
show_url = "https://www.nts.live/shows/macca"
episodes = scrape_episodes(show_url, dynamic_page=True)

NTS_tracks = []
for episode in episodes.values():
    scraped = scrape_tracks(episode["url"])
    if scraped:
        NTS_tracks.append(scraped[0])
        print(f"Successfully added the first track of {episode['title']}.")
    else:
        print(f"Could not scrape episode {episode['title']} with URL {episode['url']}.")

spotify_service = SpotifyService()
playlist_id = spotify_service.create_playlist("First Tracks - One Glove Breakfast Show")

track_uris = []
for track in NTS_tracks:
    spotify_track = spotify_service.search_track(track)
    print(f"NTS: {track}")
    if not spotify_track:
        print(f"SPF: NOTHING - NOTHING")
    else:
        print(f"SPF: {spotify_track.artist} - {spotify_track.title}")
        track_uris.append(spotify_track.uri)

print(
    f"\nFound {len(track_uris)} of {len(NTS_tracks)} tracks. Adding them to the playlist now."
)

spotify_service.add_tracks_to_playlist(playlist_id=playlist_id, track_uris=track_uris)
