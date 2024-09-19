"""Used Car Sales Technical Assessment Tests"""

import tempfile
import pandas as pd
import pytest
from sales_ratio import import_csv, sales_ratio, set_top_10, print_top_10

# pylint: disable=line-too-long, missing-final-newline, line-too-long, trailing-whitespace, redefined-outer-name


@pytest.fixture
def sample_data() -> pd.DataFrame:
    """
    Create a sample DataFrame for testing

    Returns:
        pd.DataFrame: Sample data dataframe
    """
    # Create a sample DataFrame
    data = {
        "Make": ["Toyota", "Honda", "Ford", "Chevrolet"],
        "Sale Price": [10000, 15000, 12000, 18000],
        "Top Speed": [120, 130, 110, 140],
        "is_new_car": [False, False, True, False],
    }
    # Return the DataFrame
    return pd.DataFrame(data)


def test_import_csv() -> None:
    """
    Test the import_csv function
    """
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("column1,column2\n1,2\n3,4")
        temp_csv_path = f.name
    # import the csv file
    df = import_csv(temp_csv_path)
    # Check the output
    assert isinstance(df, pd.DataFrame)
    # Check the shape of the dataframe
    assert df.shape == (2, 2)
    # Check the column names
    assert list(df.columns) == ["column1", "column2"]


def test_sales_ratio(sample_data: pd.DataFrame) -> None:
    """
    Test the sales_ratio function

    Args:
        sample_data (pd.DataFrame): Sample data dataframe
    """
    # Calculate the sales ratio
    df = sales_ratio(sample_data)
    # Check the output
    assert "Ratio" in df.columns
    # Check the data type
    assert df["Ratio"].dtype == float
    # Check the values
    assert df["Ratio"].tolist() == [
        pytest.approx(83.333, rel=1e-2),
        pytest.approx(115.385, rel=1e-2),
        pytest.approx(109.091, rel=1e-2),
        pytest.approx(128.571, rel=1e-2),
    ]


def test_set_top_10(sample_data: pd.DataFrame) -> None:
    """
    Test the set_top_10 function

    Args:
        sample_data (pd.DataFrame): Sample data dataframe
    """
    # Calculate the sales ratio
    sales_df = sales_ratio(sample_data)
    # Get the top 10
    top_10 = set_top_10(sales_df)
    # Check the output
    assert top_10.shape == (3, 3)
    # Checl the values
    assert top_10["Sale Price"].tolist() == [18000, 15000, 10000]
    assert top_10["Top Speed"].tolist() == [140, 130, 120]
    assert top_10["Ratio"].tolist() == [
        pytest.approx(128.571),
        pytest.approx(115.385),
        pytest.approx(83.333),
    ]


def test_print_top_10(capsys, sample_data: pd.DataFrame) -> None:
    """
    Test the print_top_10 function

    Args:
        capsys (): Pytest fixture that captures stdout and stderr
        sample_data (pd.DataFrame): Sample data dataframe
    """
    # Calculate the sales ratio
    sales_df = sales_ratio(sample_data)
    # Get the top 10
    top_10 = set_top_10(sales_df)
    # Print the top 10
    print_top_10(top_10.head(10))
    # Capture the output
    captured = capsys.readouterr()
    # Check the output
    assert "Top 10 Cars by Price to Speed Ratio:" in captured.out
    assert "Sale Price     Top Speed      Ratio          " in captured.out
    assert "$18000.00      140            128.571        " in captured.out
    assert "$15000.00      130            115.385        " in captured.out
    assert "$10000.00      120            83.333         " in captured.out
