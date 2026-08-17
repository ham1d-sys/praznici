"""
Generate report of 🇧🇬 Holidays for current year using the Calendarific API.
Calendarific documentation: https://calendarific.com/api-documentation.
"""

__version__ = "1.0.5"

import datetime as dt
import logging
import os

from dotenv import load_dotenv
from requests.exceptions import RequestException, HTTPError

from fetch import fetch_holidays
from process import process_fetched_holidays
from write import write_holidays_to_report

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(pathname)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")
ENDPOINT_URL = "https://calendarific.com/api/v2/holidays"
PARAMS = {"api_key": API_KEY, "country": "BG", "year": dt.datetime.now().year}
DOCUMENTATION = "https://calendarific.com/api-documentation"


def main():
    if not API_KEY:
        logging.warning("Please add your API key to the `.env` file, following the format shown in `.env.example`.")
        return

    # Fetch
    try:
        logger.info("Starting...")
        response = fetch_holidays(ENDPOINT_URL, PARAMS)
    except HTTPError as e:
        status_code = e.response.status_code
        response = e.response.json()
        if status_code == 401:
            logging.warning(
                f"Error: Missing or invalid api credentials. Ensure you have the API key from your Calendarific dashboard configured in `params`")
        elif status_code == 429:
            logger.warning(f"Error: API limits reached")
        elif status_code == 503:
            logger.warning(f"Error: {response.get('meta').get('error_details')}")
        else:
            logger.warning(
                f"Unknown error occurred.\nDetails: {e}.\nPlease refer to  {DOCUMENTATION} for more information.")
        return
    except RequestException as e:
        logger.warning(f"Error: {e}")
        return

    # Process
    try:
        processed = process_fetched_holidays(response)
        if not processed:
            logger.info(
                f"It seems no holidays matched your parameters. Try tweaking it to match the docs: {DOCUMENTATION}")
            return
    except KeyError as e:
        logger.warning(
            f"Error: {e}. Try making sure the right ENDPOINT_URL is https://calendarific.com/api/v2/holidays.")
        return

    # Write
    fieldnames = ["Name", "Description", "ISO", "Primary type", "Additional type(s)"]
    write_holidays_to_report(PARAMS, fieldnames, processed)


if __name__ == "__main__":
    main()
