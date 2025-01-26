import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/business"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

headlines = soup.find_all('a', href=True)

for headline in headlines:
    if 'articleshow' in headline['href']:  # Filtering URLs related to articles
        print("headline---",headline.get_text(strip=True))  # Print the headline text
        print("headlines link - ",headline['href'])

url_h1 = str(headline['href'])
print("url_h1 ---", url_h1)
response = requests.get(url_h1)
data = BeautifulSoup(response.content, 'html.parser')

links = data.find_all('a', href=True)

# Loop through each link and find all <span> elements inside it
for link in links:
    # Find all <span> tags within the <a> tag
    spans = link.find_all('span')
    
    # If there are any <span> elements, print them
    for span in spans:
        print("summary",span.get_text(strip=True))
