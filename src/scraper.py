import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find and extract specific elements
        # Example: Extract all paragraph texts
        paragraphs = soup.find_all('p')
        
        # Process and store the extracted data
        extracted_data = []
        for p in paragraphs:
            extracted_data.append(p.text)
        
        return extracted_data
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None