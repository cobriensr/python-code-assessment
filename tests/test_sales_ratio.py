"""Used Car Sales Technical Assessment Tests"""

import tempfile
import pandas as pd
import pytest
import faker
from sales_ratio import import_csv, sales_ratio, set_top_10, print_top_10

# pylint: disable=line-too-long, missing-final-newline, line-too-long, trailing-whitespace, redefined-outer-name

# used to generate fake data for parameterized tests
fake = faker.Faker()

@pytest.fixture
def sample_data()-> pd.DataFrame:
    """
    Create a sample DataFrame for testing

    Returns:
        pd.DataFrame: Sample data dataframe
    """
    data = {
        'Make': ['Toyota', 'Honda', 'Ford', 'Chevrolet'],
        'Sale Price': [10000, 15000, 12000, 18000],
        'Top Speed': [120, 130, 110, 140],
        'is_new_car': [False, False, True, False]
    }
    return pd.DataFrame(data)

def test_import_csv() -> None:
    """
    Test the import_csv function
    """
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("column1,column2\n1,2\n3,4")
        temp_csv_path = f.name

    # Test the function
    df = import_csv(temp_csv_path)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["column1", "column2"]

def test_sales_ratio(sample_data: pd.DataFrame)-> None:
    """
    Test the sales_ratio function

    Args:
        sample_data (pd.DataFrame): Sample data dataframe
    """
    df = sales_ratio(sample_data)
    assert 'Ratio' in df.columns
    assert df['Ratio'].dtype == float
    assert df['Ratio'].tolist() == [pytest.approx(83.333, rel=1e-2), pytest.approx(115.385, rel=1e-2), 
                                    pytest.approx(109.091, rel=1e-2), pytest.approx(128.571, rel=1e-2)]

def test_set_top_10(sample_data: pd.DataFrame)-> None:
    """
    Test the set_top_10 function

    Args:
        sample_data (pd.DataFrame): Sample data dataframe
    """
    sales_df = sales_ratio(sample_data)
    top_10 = set_top_10(sales_df)
    assert top_10.shape == (3, 3)
    assert top_10['Sale Price'].tolist() == [18000, 15000, 10000]
    assert top_10['Top Speed'].tolist() == [140, 130, 120]
    assert top_10['Ratio'].tolist() == [pytest.approx(128.571), pytest.approx(115.385), pytest.approx(83.333)]

def test_print_top_10(capsys, sample_data: pd.DataFrame)-> None:
    """
    Test the print_top_10 function

    Args:
        capsys (): Pytest fixture that captures stdout and stderr
        sample_data (pd.DataFrame): Sample data dataframe
    """
    sales_df = sales_ratio(sample_data)
    top_10 = set_top_10(sales_df)
    print_top_10(top_10.head(10))
    captured = capsys.readouterr()
    assert "Top 10 Cars by Price to Speed Ratio:" in captured.out
    assert "Sale Price     Top Speed      Ratio          " in captured.out
    assert "$18000.00      140            128.571        " in captured.out
    assert "$15000.00      130            115.385        " in captured.out
    assert "$10000.00      120            83.333         " in captured.out