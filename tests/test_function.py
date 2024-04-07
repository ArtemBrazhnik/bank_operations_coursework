import pytest
from src.function import loading_json, filter_list, date_format, sort_by_date, hide_num, format_sum
import os
from config import ROOT_DIR


test_path = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')
operations = [
    {"id": 1, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000000", "operationAmount": {"amount": "79931.03", "currency": {"name": "руб."}}},
    {"id": 2, "state": "CANCELED", "date": "2018-02-01T00:00:00.000000", "operationAmount": {"amount": "79931.03", "currency": {"name": "руб."}}},
    {"id": 3, "state": "EXECUTED", "date": "2018-03-01T00:00:00.000000", "operationAmount": {"amount": "79931.03", "currency": {"name": "руб."}}},
    {"id": 4, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000001", "operationAmount": {"amount": "79931.03", "currency": {"name": "руб."}}}
]

@pytest.fixture
def operations_fixture():
    return operations


def test_loading_json():
    assert loading_json(test_path) == []


def test_filter_list(operations_fixture):
    assert len(filter_list(operations_fixture)) == 3


def test_sort_by_date(operations_fixture):
    assert [i["id"] for i in sort_by_date(operations_fixture)] == [3, 2, 4, 1]


def test_date_format():
    assert date_format("2018-01-01T00:00:00.000000") == "01.01.2018"


def test_hide_num():
    assert hide_num('Счет 64686473678894779589') == 'Счет **9589'
    assert hide_num('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'


def test_format_sum():
    assert format_sum(operations[0]) == "79931.03 руб."
    assert format_sum(operations[1]) == "79931.03 руб."
    assert format_sum(operations[2]) == "79931.03 руб."
    assert format_sum(operations[3]) == "79931.03 руб."
