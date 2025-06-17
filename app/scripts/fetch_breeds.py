import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def fetch_cat_breeds():
    url = "https://vcahospitals.com/know-your-pet/cat-breeds"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.google.com/",
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
    except RequestException as e:
        print(f"Error fetching page: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Try multiple selectors
    breed_links = (
        soup.select("a[href*='/cat-breeds/']")
        or soup.select("ul.breed-list li a")
        or soup.select("div.content a")
    )

    breeds = [link.text.strip() for link in breed_links if link.text.strip()]
    return breeds


if __name__ == "__main__":
    breeds = fetch_cat_breeds()
    print("BREED_CHOICES = [")
    for b in breeds:
        value = b.lower().replace(" ", "_").replace("-", "_")
        print(f'    ("{value}", "{b}"),')
    print("]")
