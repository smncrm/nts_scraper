import requests
from bs4 import BeautifulSoup


def scrape_tracks(url):
    """Scrapes all tracks from an NTS show webpage"""
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
