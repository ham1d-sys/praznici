from process import process_fetched_holidays


def test_process_fetched_holidays():
    processed = process_fetched_holidays({"response": {"holidays": []}})
    assert processed is None
