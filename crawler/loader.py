import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def load_website(url: str, max_pages: int = 5) -> list[dict]:
    visited = set()
    pages = []
    base_domain = urlparse(url).netloc

    queue = [url]

    while queue and len(pages) < max_pages:
        current_url = queue.pop(0)

        if current_url in visited:
            continue

        try:
            response = requests.get(
                current_url,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0"}
            )
        except requests.RequestException:
            continue

        if response.status_code != 200:
            continue

        if "text/html" not in response.headers.get("Content-Type", ""):
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title else ""

        pages.append({
            "url": current_url,
            "title": title,
            "html": soup
        })

        visited.add(current_url)

        for link in soup.find_all("a", href=True):
            next_url = urljoin(current_url, link["href"])
            parsed = urlparse(next_url)

            if parsed.netloc == base_domain and next_url not in visited:
                queue.append(next_url)

    return pages