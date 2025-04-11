import requests as rq
from bs4 import BeautifulSoup

# Get URL input from user
url = input("Enter Link: ").strip()
if not url.startswith("http"):
    url = "https://" + url

# Fetch page content
try:
    data = rq.get(url)
    data.raise_for_status()
    soup = BeautifulSoup(data.text, "html.parser")

    # Extract and save all links
    links = [link.get("href") for link in soup.find_all("a") if link.get("href")]

    with open("myLinks.txt", 'a', encoding='utf-8') as saved:
        for link in links:
            saved.write(link + '\n')

    print(f"✅ Extracted {len(links)} links and saved to 'myLinks.txt'.")

except Exception as e:
    print(f"❌ Error fetching the webpage: {e}")
