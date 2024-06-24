import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://en.wikipedia.org/wiki/Wikipedia" 

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the HTML elements that contain the headlines
    # The class names and tags may vary, so you may need to inspect the webpage for the correct selectors
    headlines = soup.find_all('h3')

    # Extract and print the text of each headline
    # print(response.content)
    for idx, headline in enumerate(headlines):
        print(f"{idx + 1}. {headline.get_text(strip=True)}")
else:
    print("Failed to retrieve the webpage.")