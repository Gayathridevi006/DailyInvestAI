import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/business"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

headlines = soup.find_all('a', href=True)

for headline in headlines:
    if 'articleshow' in headline['href']:  # Filtering URLs related to articles
        print(headline.get_text(strip=True))  # Print the headline text
        print(headline['href'])