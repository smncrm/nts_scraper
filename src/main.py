from scraper import scrape_episodes, scrape_tracks
from spotify_service import SpotifyService

# Usage example
show_url = "https://www.nts.live/shows/macca"
# episodes = scrape_episodes(show_url, dynamic_page=False)
episode_url = "https://www.nts.live/shows/macca/episodes/macca-10th-august-2024"
tracks = scrape_tracks(episode_url)

track_one = tracks[0]
print(track_one)

spotify_service = SpotifyService()

print(spotify_service.search_track(track_one))
