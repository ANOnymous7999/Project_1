import requests
from bs4 import BeautifulSoup
from .utils import print_info, extract_image_urls, extract_emails, extract_phones

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def scrape_page(url):
    print_info(f"Attempting to scrape additional data from: {url}")
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()

            data = {
                "emails": extract_emails(text),
                "phones": extract_phones(text),
                "images": extract_image_urls(response.text)
            }

            # Find all images in tags
            for img in soup.find_all('img'):
                src = img.get('src')
                if src and src.startswith('http'):
                    data['images'].append(src)

            data['images'] = list(set(data['images']))
            return data
    except Exception as e:
        # print_error(f"Failed to scrape {url}: {e}")
        pass
    return None
