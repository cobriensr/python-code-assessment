"""Used Car Sales Technical Assessment Tests"""

import tempfile
import pandas as pd
import pytest
from porsche_sales import (
    import_csv,
    filter_porsche,
    calculate_depreciation,
    aggregate_depreciation,
    print_results,
)

# pylint: disable=line-too-long, missing-final-newline, line-too-long, redefined-outer-name


@pytest.fixture
def sample_data() -> pd.DataFrame:
    """
    Create a sample DataFrame for testing

    Returns:
        pd.DataFrame: Sample data dataframe
    """
    # Create a sample DataFrame
    data = {
        "Make": ["Porsche", "BMW", "Porsche", "Toyota"],
        "Sale Price": [50000, 40000, 60000, 30000],
        "Annual Depreciation Rate": [0.1, 0.15, 0.12, 0.2],
        "MM/DD/YY Purchase Date": [
            "01/01/2020",
            "02/15/2020",
            "03/10/2020",
            "04/20/2020",
        ],
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


def test_filter_porsche(sample_data: pd.DataFrame) -> None:
    """
    Test the filter_porsche function
    """
    # Filter the sample data
    filtered_df = filter_porsche(sample_data)
    # Check the output
    assert filtered_df.shape == (2, 4)
    # Check the Make column
    assert (filtered_df["Make"] == "Porsche").all()


def test_calculate_depreciation() -> None:
    """
    Test the calculate_depreciation function
    """
    # Test the function
    assert calculate_depreciation(100000, 3, 0.15) == pytest.approx(61407.50, rel=1e-2)


def test_aggregate_depreciation(sample_data: pd.DataFrame) -> None:
    """
    Test the aggregate_depreciation function

    Args:
        sample_data (pd.DataFrame): Sample data
    """
    # Filter the sample data
    filtered_df = filter_porsche(sample_data)
    # Aggregate the depreciation
    agg_df = aggregate_depreciation(filtered_df)
    # Check the output
    assert agg_df.shape == (2, 4)
    # Check the columns
    assert "Original Purchase Date" in agg_df.columns
    assert "Depreciated Date" in agg_df.columns
    assert "Original Sale Price" in agg_df.columns
    assert "Depreciated Value" in agg_df.columns


def test_print_results(capsys):
    """
    Test the print_results function

    Args:
        capsys: Pytest fixture that captures stdout and stderr
    """
    # Create test data
    test_data = {
        "Original Purchase Date": ["2020-01-01", "2020-03-10"],
        "Depreciated Date": ["2023-01-01", "2023-03-10"],
        "Original Sale Price": [50000, 60000],
        "Depreciated Value": [35000, 42000],
    }
    # Create a DataFrame from test data
    test_df = pd.DataFrame(test_data)
    # Print the results
    print_results(test_df)
    # Capture the output
    captured = capsys.readouterr()
    # Check the output
    assert "Depreciated Values after 3 Years:" in captured.out
    assert "=======================================================" in captured.out
    assert "Depreciated Date          Depreciated Value" in captured.out
    assert "2023-01-01                $35000.00" in captured.out
    assert "2023-03-10                $42000.00" in captured.out
