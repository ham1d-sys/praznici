"""
Generate report of 🇧🇬 Holidays for current year.
"""

__version__ = "0.1.0"

import csv
import logging
import os
from datetime import datetime as dt

import flag
import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter, Retry

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")


def main():
    if not API_KEY:
        logging.warning("Please add your API key to the `.env` file, following the format shown in `.env.example`.")
        return

    # Retry logic
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 600])
    session.mount("https://", HTTPAdapter(max_retries=retries))

    # Fetch
    logger.info("Starting...")
    params = {"api_key": API_KEY, "country": "BG", "year": dt.now().year, "type": "national"}
    endpoint_url = "https://calendarific.com/api/v2/holidays"
    response = session.get(endpoint_url, params=params)
    status = response.status_code
    if status == 401:
        logging.warning(
            f"Error: Code {status}. Missing or invalid api credentials. Ensure you have the API key from your Calendarific dashboard configured in `params`.")
        return
    elif status == 429:
        logger.warning(f"Error: Code {status}. Too many requests. API limits reached.")
        return
    elif status != 200:
        logger.warning(f"Error: Code {status}. Unknown error, refer to https://calendarific.com/api-documentation.")
        return
    else:
        logger.info(
            f"Response code: {status}. Fetched {flag.flag(params['country'])} {params['type']} holidays {params['year']}.")

    # Process
    response_json = response.json()
    holidays = response_json["response"].get("holidays")

    if not holidays:
        logger.info(
            "No holidays matches your parameters. Try changing the 'country', 'year' and/or 'type' args in `params`.")
        return

    processed = []
    for i, holiday in enumerate(holidays, start=1):
        processed.append({"Name": holiday["name"], "Description": holiday["description"], "ISO": holiday["date"]["iso"],
                          "Primary type": holiday["primary_type"], "Additional type(s)": ", ".join(
                [t for t in holiday["type"] if t != holiday["primary_type"]])})
    logger.info("Processed fetched holidays.")

    # Write
    fieldnames = ["Name", "Description", "ISO", "Primary type", "Additional type(s)"]
    filename = f"{params['country']}_{params['type']}_holidays_({params['year']})_report.csv"
    with open(filename, "w", encoding="UTF-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(processed)
    logger.info(f"Wrote report to `{filename}`.")


if __name__ == "__main__":
    main()
