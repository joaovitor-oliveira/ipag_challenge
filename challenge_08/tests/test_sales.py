import pytest
from challenge_08.src.sales import Sales
import pandas as pd


MOCK_FILE_PATH = "challenge_08/files/mock.csv"
MOCK_FEATURES = [
    'Region', 'Country', 'Item Type', 'Sales Channel', 'Order Priority',
    'Order Date', 'Order ID', 'Ship Date', 'Units Sold', 'Unit Price',
    'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit'
]


@pytest.fixture
def sales():
    return Sales(MOCK_FILE_PATH)


def test_given_a_valid_path_when_call_load_file_then_sucess(sales):
    assert sales.load_file()


def test_given_an_invalid_path_when_call_load_file_then_file_not_found(capsys):
    Sales("file.csv")

    out, _ = capsys.readouterr()

    assert out in "Arquivo não encontrado. Caminho informado: file.csv\n"


def test_when_call_samples_then_return_a_sample_of_dataset(sales):
    sample = sales.sample()

    assert not sample.empty
    assert all(col in MOCK_FEATURES for col in sample.transpose().columns)


def test_when_call_get_units_sold_by_item_type(sales):
    expected_columns = ["Baby Food", "Cereal", "Office Supplies"]
    expected_values = ["9925", "2804", "1779"]
    expected_report = pd.Series(expected_values, index=expected_columns).to_string()

    report = sales.get_units_sold_by_item_type().to_string()

    assert expected_report in report


def test_when_call_get_total_revenue_by_item_type(sales):
    expected_columns = ["Baby Food", "Cereal", "Office Supplies"]
    expected_values = ["2533654.00", "576782.80", "1158502.59"]
    expected_report = pd.Series(expected_values, index=expected_columns).to_string()

    report = sales.get_total_revenue_by_item_type().to_string()

    assert expected_report in report


def test_when_call_get_total_cost_by_item_type(sales):
    expected_columns = ["Baby Food", "Cereal", "Office Supplies"]
    expected_values = ["1582243.50", "328376.44", "933903.84"]
    expected_report = pd.Series(expected_values, index=expected_columns).to_string()

    report = sales.get_total_cost_by_item_type().to_string()

    assert expected_report in report


def test_when_call_get_total_profit_by_item_type(sales):
    expected_columns = ["Baby Food", "Cereal", "Office Supplies"]
    expected_values = ["951410.50", "248406.36", "224598.75"]
    expected_report = pd.Series(expected_values, index=expected_columns).to_string()

    report = sales.get_total_profit_by_item_type().to_string()

    assert expected_report in report


def test_when_call_get_unit_solds_by_item_type_and_region(sales):
    expected_item_type = ["Baby Food", "Cereal", "Office Supplies"]
    expected_region = ["Australia and Oceania", "Central America and the Caribbean", "Europe"]
    expected_values = ["9925", "2804", "1779"]

    data = [expected_item_type, expected_region]

    index = pd.MultiIndex.from_arrays(data, names=('Item Type', 'Region'))

    expected_report = pd.Series(expected_values, index=index).to_string()

    report = sales.get_unit_solds_by_item_type_and_region().to_string()

    assert expected_report in report


def test_when_call_get_item_type_with_highest_revenue_by_country(sales):
    expected_country = ["Grenada", "Russia", "Tuvalu"]
    expected_item_type = ["Cereal", "Office Supplies", "Baby Food"]
    expected_values = ["576782.80", "1158502.59", "2533654.00"]

    data = [expected_country, expected_item_type]

    index = pd.MultiIndex.from_arrays(data, names=('Country', 'Item Type'))

    expected_report = pd.Series(expected_values, index=index).to_string()

    report = sales.get_item_type_with_highest_revenue_by_country().to_string()

    assert expected_report in report
