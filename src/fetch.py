import logging
from typing import Dict

import flag
import requests
from requests.adapters import HTTPAdapter, Retry

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(pathname)s - %(message)s")
logger = logging.getLogger(__name__)


def fetch_holidays(endpoint: str, params: Dict) -> Dict | None:
    """
    Fetch holidays data.
    :param endpoint: API endpoint URL
    :param params: Parameters to incl. in header
    :return:
        Response in JSON format if status code is 200 or None otherwise.
    """
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 422])
    session.mount("https://", HTTPAdapter(max_retries=retries))

    response = session.get(endpoint, params=params)
    response.raise_for_status()

    if response.status_code == 200:
        logger.info(
            f"Response code: 200. Fetched {flag.flag(params['country'])} holidays {params['year']}.")
        return response.json()

    return None
