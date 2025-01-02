import pandas as pd
from homeproject.utils import find_hottest_month_and_city
import pytest


def test_find_hottest_month_and_city():
    data = {
        'dt': pd.to_datetime(['2020 - 01 - 01', '2020 - 02 - 01', '2020 - 03 - 01']),
        'City': ['City1', 'City2', 'City3'],
        'AverageTemperature': [20, 25, 30]
    }
    df = pd.DataFrame(data)
    month, city = find_hottest_month_and_city(df, 2020)
    assert month == 'March'
    assert city == 'City3'


def test_no_data_year():
    data = {
        'dt': pd.to_datetime(['2020 - 01 - 01', '2020 - 02 - 01', '2020 - 03 - 01']),
        'City': ['City1', 'City2', 'City3'],
        'AverageTemperature': [20, 25, 30]
    }
    df = pd.DataFrame(data)
    month, city = find_hottest_month_and_city(df, 2021)
    assert month is None
    assert city is None


def test_missing_columns():
    data = {
        'City': ['City1', 'City2', 'City3'],
        'AverageTemperature': [20, 25, 30]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        find_hottest_month_and_city(df, 2020)
