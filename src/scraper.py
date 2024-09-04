import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from Track import Track


def scrape_tracks(url):
    """Scrapes all tracks from an NTS episode."""
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        tracks = soup.find_all("div", class_="track__detail")

        # Process and store the extracted data
        extracted_tracks = {}
        for ix, t in enumerate(tracks):
            extracted_tracks[ix] = Track(
                artist=t.find("span", class_="track__artist").text,
                title=t.find("span", class_="track__title").text,
            )

        return extracted_tracks
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None


def scrape_episodes(url, dynamic_page=True, scroll_pause_time=2):
    """Scrapes all urls to individual episodes from an NTS show."""
    response = requests.get(url)

    if response.status_code == 200:
        if dynamic_page:
            driver = webdriver.Safari()
            driver.get(url)

            scroll_down(driver=driver, scroll_pause_time=scroll_pause_time)

            soup = BeautifulSoup(driver.page_source, "html.parser")
            driver.quit()
        else:
            soup = BeautifulSoup(response.text, "html.parser")

        episodes = soup.find_all("div", class_="nts-grid-v2-item__content")

        # Process and store the extracted data
        extracted_episodes = {}
        for ix, e in enumerate(episodes):
            extracted_episodes[ix] = {
                "title": e.find("div", class_="nts-grid-v2-item__header__title").text,
                "url": urljoin(
                    url, e.find("a", class_="nts-grid-v2-item__header nts-app")["href"]
                ),
            }

        return extracted_episodes
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None


def scroll_down(driver, scroll_pause_time):
    # Scroll down all the way
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script(f"window.scrollTo(0, {last_height+10});")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
