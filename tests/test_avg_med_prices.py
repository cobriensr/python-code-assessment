"""Used Car Sales Technical Assessment Tests"""
import os
import pandas as pd
import pytest
import pytest_cov
import pytest_html
import faker
from avg_med_prices import (
    add_zero_to_zipcode,
    calculate_price_differences,
    filter_by_zipcode,
    import_csv,
    print_results,
)

# pylint: disable=line-too-long, missing-final-newline, line-too-long

# used to generate fake data for parameterized tests
fake = faker.Faker()


@pytest.fixture
def car_sales_data() -> pd.DataFrame:
    """
    Load the car sales dataset from csv

    Returns:
        pd.DataFrame: The car sales dataset as a dataframe
    """
    # Adjust the path as necessary to locate your CSV file
    csv_path = os.path.join(os.path.dirname(__file__), "..", "car_sales_dataset.csv")
    return pd.read_csv(csv_path)
