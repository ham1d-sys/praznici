from typing import Dict, List

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(pathname)s - %(message)s")
logger = logging.getLogger(__name__)


def process_fetched_holidays(response: Dict) -> List[Dict] | None:
    """
    Process fetched holidays.
    :param response: HTTP response JSON.
    :return:
        List of dictionaries containing holidays or None if no holidays.
    """
    holidays = response["response"].get("holidays")

    if holidays:
        processed = []
        for i, holiday in enumerate(holidays, start=1):
            processed.append(
                {"Name": holiday["name"], "Description": holiday["description"], "ISO": holiday["date"]["iso"],
                 "Primary type": holiday["primary_type"], "Additional type(s)": ", ".join(
                    [t for t in holiday["type"] if t != holiday["primary_type"]])})
        logger.info("Processed fetched holidays.")
        return processed

    return None