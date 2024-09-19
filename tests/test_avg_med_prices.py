"""Used Car Sales Technical Assessment Tests"""

import os
import tempfile
import pandas as pd
import pytest
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


def test_add_zero_to_zipcode() -> None:
    """
    Test the add_zero_to_zipcode function
    """
    test_df = pd.DataFrame({"zipcode": [123, 1234, 12345]})
    result_df = add_zero_to_zipcode(test_df)
    assert list(result_df["zipcode"]) == ["00123", "01234", "12345"]


def test_filter_by_zipcode() -> None:
    """
    Test the filter_by_zipcode function
    """
    test_df = pd.DataFrame({"zipcode": ["00123", "20123", "15123", "30123"]})
    result_df = filter_by_zipcode(test_df)
    assert list(result_df["zipcode"]) == ["00123", "15123"]
    assert result_df.index.tolist() == [0, 2]  # Check sorting


def test_calculate_price_differences() -> None:
    """
    Test the calculate_price_differences function
    """
    test_df = pd.DataFrame(
        {"Sale Price": [100, 200, 300], "Resell Price": [150, 180, 350]}
    )
    result = calculate_price_differences(test_df)
    assert result["Average Price Change"][0] == pytest.approx(26.67, rel=1e-2)
    assert result["Median Price Change"][0] == 50
    assert result["Average Absolute Price Change"][0] == pytest.approx(40, rel=1e-2)
    assert result["Median Absolute Price Change"][0] == 50


def test_print_results(capsys):
    """
    Test the print_results function

    Args:
        capsys (): Pytest fixture that captures stdout and stderr
    """
    test_results = {
        "Average Price Change": [100.5],
        "Median Price Change": [-50.25],
        "Average Absolute Price Change": [75.75],
        "Median Absolute Price Change": [60.0],
    }
    print_results(test_results)
    captured = capsys.readouterr()
    assert "Average:            $       100.50" in captured.out
    assert "Median:             $       -50.25" in captured.out
    assert "Average Absolute:   $        75.75" in captured.out
    assert "Median Absolute:    $        60.00" in captured.out
