import logging
from typing import Dict, List

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
        for holiday in holidays:
            processed.append(
                {"Name": holiday["name"], "Description": holiday["description"], "ISO": holiday["date"]["iso"],
                 "Primary type": holiday["primary_type"], "Additional type(s)": ", ".join(
                    [t for t in holiday["type"] if t != holiday["primary_type"]])})
        logger.info("Processed fetched holidays.")
        return processed

    return None
