import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_tracks(url):
    """Scrapes all tracks from an NTS episode."""
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        tracks = soup.find_all("div", class_="track__detail")

        # Process and store the extracted data
        extracted_tracks = {}
        for ix, t in enumerate(tracks):
            extracted_tracks[ix] = {
                "artist": t.find("span", class_="track__artist").text,
                "title": t.find("span", class_="track__title").text,
            }

        return extracted_tracks
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

def scrape_episodes(url):
    """Scrapes all urls to individual episodes from an NTS show."""
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        episodes = soup.find_all("div", class_="nts-grid-v2-item__content")

        # Process and store the extracted data
        extracted_episodes = {}
        for ix, e in enumerate(episodes):
            extracted_episodes[ix] = {
                "title": e.find("div", class_="nts-grid-v2-item__header__title").text,
                "url": urljoin(url, e.find("a", class_="nts-grid-v2-item__header nts-app")['href']),
            }

        return extracted_episodes
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None
