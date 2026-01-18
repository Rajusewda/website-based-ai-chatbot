from bs4 import BeautifulSoup


def clean_html(soup: BeautifulSoup) -> str:
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    lines = [line.strip() for line in text.splitlines()]
    cleaned = " ".join(line for line in lines if line)

    return cleaned