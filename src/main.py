from scraper import scrape_episodes, scrape_tracks

# Usage example
show_url = "https://www.nts.live/shows/macca"
episodes = scrape_episodes(show_url, dynamic_page=True)
episode_url = "https://www.nts.live/shows/macca/episodes/macca-10th-august-2024"
tracks = scrape_tracks(episode_url)

print(episodes)