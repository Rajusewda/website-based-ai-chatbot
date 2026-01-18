from urllib.parse import urlparse
import requests


class URLValidationError(Exception):
    pass


def is_valid_url(url: str) -> bool:
    if not url or not isinstance(url, str):
        return False

    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def check_website_access(url: str, timeout: int = 10) -> None:
    if not is_valid_url(url):
        raise URLValidationError("Invalid URL format")

    try:
        response = requests.get(
            url,
            timeout=timeout,
            headers={"User-Agent": "Mozilla/5.0"}
        )
    except requests.RequestException:
        raise URLValidationError("Website is unreachable")

    if response.status_code != 200:
        raise URLValidationError(f"Website returned status code {response.status_code}")

    content_type = response.headers.get("Content-Type", "")
    if "text/html" not in content_type.lower():
        raise URLValidationError("Only HTML pages are supported")

    if not response.text or not response.text.strip():
        raise URLValidationError("Website contains no readable content")