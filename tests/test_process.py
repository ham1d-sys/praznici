import pytest

from process import process_fetched_holidays


def test_process_fetched_holidays_():
    processed = process_fetched_holidays({"response": {"holidays": []}})
    assert processed is None

    with pytest.raises(KeyError, match=r"Malformed response JSON."):
        process_fetched_holidays({"text": ["foo"]})
        raise KeyError("Malformed response JSON.")
