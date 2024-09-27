import logging
import requests
from bs4 import BeautifulSoup

# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum log level
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='web_scraper.log',
    filemode='w'  # Overwrite the log file each time (use 'a' to append)
)

logger = logging.getLogger()

def fetch_page(url):
    try:
        logger.info(f"Fetching URL: {url}")
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logger.info(f"Successfully fetched URL: {url}")
        return response.text
    except requests.exceptions.Timeout:
        logger.error(f"Request timed out for URL: {url}")
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e} for URL: {url}")
    except requests.exceptions.RequestException as e:
        logger.exception(f"Failed to fetch URL: {url}. Exception: {e}")

def parse_page(html_content):
    try:
        logger.debug("Parsing HTML content")
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.title.string
        logger.info(f"Page title: {title}")
        # Let's assume we're scraping all article headings from a news website
        headings = soup.find_all('h2')
        if not headings:
            logger.warning("No headings found on the page")
        return [heading.get_text() for heading in headings]
    except Exception as e:
        logger.exception("Error occurred during parsing: %s", e)

def main():
    url = "https://example.com/news"
    logger.info("Starting web scraper")

    page_content = fetch_page(url)
    if page_content:
        headings = parse_page(page_content)
        if headings:
            logger.info(f"Found {len(headings)} headings on the page")
            for heading in headings:
                logger.debug(f"Article Heading: {heading}")
        else:
            logger.warning("No headings were extracted")
    else:
        logger.error("Failed to retrieve the page content")

    logger.info("Web scraper finished")

if __name__ == "__main__":
    main()
