from scraper import scrape_website

# Usage example
url = "https://www.nts.live/shows/macca/episodes/macca-10th-august-2024"
result = scrape_website(url)

if result:
    for item in result:
        print(item)