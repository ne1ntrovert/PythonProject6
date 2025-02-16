import pytest
from datetime import datetime
from src.processing import filter_by_state, sort_by_date

test_data = [
    {"date": "2023-01-01T12:00:00", "state": "EXECUTED", "amount": 100},
    {"date": "2023-01-02T12:00:00", "state": "PENDING", "amount": 200},
    {"date": "2023-01-03T12:00:00", "state": "EXECUTED", "amount": 300},
    {"date": "2023-01-04T12:00:00", "state": "CANCELLED", "amount": 400},
]


def test_filter_by_state():
    executed = filter_by_state(test_data, "EXECUTED")
    assert len(executed) == 2
    assert all(item["state"] == "EXECUTED" for item in executed)

    pending = filter_by_state(test_data, "PENDING")
    assert len(pending) == 1
    assert pending[0]["state"] == "PENDING"

    cancelled = filter_by_state(test_data, "CANCELLED")
    assert len(cancelled) == 1
    assert cancelled[0]["state"] == "CANCELLED"

    unknown = filter_by_state(test_data, "UNKNOWN")
    assert len(unknown) == 0


def test_sort_by_date():
    sorted_data_desc = sort_by_date(test_data)
    assert sorted_data_desc[0]["date"] == "2023-01-04T12:00:00"
    assert sorted_data_desc[-1]["date"] == "2023-01-01T12:00:00"

    sorted_data_asc = sort_by_date(test_data, descending=False)
    assert sorted_data_asc[0]["date"] == "2023-01-01T12:00:00"
    assert sorted_data_asc[-1]["date"] == "2023-01-04T12:00:00"

    data_with_missing_date = [
        {"date": "2023-01-01T12:00:00", "state": "EXECUTED"},
        {"state": "PENDING"},
        {"date": "2023-01-03T12:00:00", "state": "EXECUTED"},
    ]

    sorted_with_missing_date = sort_by_date(data_with_missing_date)

    # Проверяем что первый элемент это запись с датой
    assert sorted_with_missing_date[0]["date"] == "2023-01-03T12:00:00"
    assert sorted_with_missing_date[-1]["state"] == "PENDING"
