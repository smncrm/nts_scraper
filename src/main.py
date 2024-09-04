from scraper import scrape_episodes, scrape_tracks
from spotify_service import SpotifyService

# Usage example
show_url = "https://www.nts.live/shows/macca"
# episodes = scrape_episodes(show_url, dynamic_page=False)
episode_url = "https://www.nts.live/shows/macca/episodes/macca-10th-august-2024"
tracks = scrape_tracks(episode_url)

spotify_service = SpotifyService()

for track in tracks.values():
    res = spotify_service.search_track(track)
    print(f"NTS: {track}")
    if not res:
        print(f"SPF: NOTHING - NOTHING")
    else:
        print(f"SPF: {res['artist']} - {res['name']}")
