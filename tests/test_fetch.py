import responses

from run import ENDPOINT_URL, PARAMS
from fetch import fetch_holidays

@responses.activate
def test_fetch_holidays():
    responses.get(
        ENDPOINT_URL,
        status=500,
        json={"error_details": "Internal server error"}
    )
    responses.get(
        ENDPOINT_URL,
        status=422,
        json={"error_details": "Unknown error occurred."}
    )
    responses.get(
        ENDPOINT_URL,
        status=200,
        json={"holidays": ["New Year", "Christmas"]}
    )

    holidays = fetch_holidays(ENDPOINT_URL, PARAMS)
    assert holidays == {"holidays": ["New Year", "Christmas"]}



