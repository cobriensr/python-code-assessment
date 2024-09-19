"""Used Car Sales Technical Assessment"""

import pandas as pd

# pylint: disable=line-too-long, trailing-whitespace, trailing-newlines, missing-final-newline


# Import csv file with pandas
def import_csv(csv_path: str) -> pd.DataFrame:
    """
    Import csv file into a pandas dataframe and make it globally available

    Args:
    csv_path (str): The path to the csv file

    Returns:
    pd.DataFrame: The dataframe containing the csv data
    """
    # Return the dataframe
    return pd.read_csv(csv_path)


# Filter the DataFrame to include only Porsche owners.
def filter_porsche(filter_df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter the DataFrame to include only Porsche owners.

    Args:
    df (pd.DataFrame): The dataframe containing the csv data

    Returns:
    pd.DataFrame: The dataframe containing only Porsche owners
    """
    # Filter the DataFrame to include only Porsche owners
    return filter_df[filter_df["Make"] == "Porsche"]


# Calculate the Depreciation:
def calculate_depreciation(initial_price: float, years: int, annual_rate: float) -> float:
    """
    Calculate the depreciated value after a certain number of years.

    Args:
        initial_price (float): The initial price of the car
        years (int): The number of years to run depreciation
        annual_rate (float): The annual depreciation rate

    Returns:
        float: The calculated depreciated value
    """
    return initial_price * (1 - annual_rate) ** years


# Aggregate depreciation data
def aggregate_depreciation(dep_porsche_df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate the depreciation data for Porsche car sales.

    Args:
        dep_porsche_df (pd.DataFrame): The dataframe containing the Porsche car sales data to depreciate

    Returns:
        pd.DataFrame: The dataframe containing the aggregated depreciation data
    """
    # Rename depreciation rate column
    dep_porsche_df = dep_porsche_df.rename(
        columns={"Annual Deprecation Rate": "Annual Depreciation Rate"}
    )

    # Calculate the depreciated value for each row after 3 years and round to 2 decimal places.
    dep_porsche_df["Accrued Depreciation"] = round(
        dep_porsche_df.apply(
            lambda row: calculate_depreciation(
                row["Sale Price"], 3, row["Annual Depreciation Rate"]
            ),
            axis=1,
        ),
        2,
    )

    # Convert 'MM/DD/YY Purchase Date' to datetime values from strings
    dep_porsche_df["MM/DD/YY Purchase Date"] = pd.to_datetime(
        dep_porsche_df["MM/DD/YY Purchase Date"]
    )

    # Create a new column with the date 3 years after the initial purchase date.
    dep_porsche_df["Depreciated Date"] = dep_porsche_df["MM/DD/YY Purchase Date"].apply(
        lambda x: x + pd.DateOffset(years=3)
    )

    # Calculate new depreciated value and round to 2 decimal places.:
    dep_porsche_df["Depreciated Value"] = round(
        dep_porsche_df["Sale Price"] - dep_porsche_df["Accrued Depreciation"], 2
    )

    # Create a new DataFrame with only the relevant information (MM/DD/YY Purchase Date, Depreciated Date, Sale Price, Depreciated Value).
    new_porsche_df = dep_porsche_df[
        [
            "MM/DD/YY Purchase Date",
            "Depreciated Date",
            "Sale Price",
            "Depreciated Value",
        ]
    ]

    # Rename column for display purposes.
    new_porsche_df = new_porsche_df.rename(
        columns={
            "MM/DD/YY Purchase Date": "Original Purchase Date",
            "Sale Price": "Original Sale Price",
        }
    )

    # Return the new DataFrame
    return new_porsche_df


def print_results(new_df: pd.DataFrame) -> None:
    """
    Format and print the results

    Args:
        new_df (pd.DataFrame): The dataframe containing the results
    """
    # Format and print the results
    print("\nDepreciated Values after 3 Years:")
    print("=" * 55)
    print(f"{'Depreciated Date':<25} {'Depreciated Value':<25}")
    print("=" * 55)
    for _, row in new_df.iterrows():
        if isinstance(row["Depreciated Date"], str):
            formatted_date = row["Depreciated Date"]
        else:
            formatted_date = row["Depreciated Date"].strftime("%Y-%m-%d")
        formatted_value = f"${row['Depreciated Value']:.2f}"
        print(f"{formatted_date:<25} {formatted_value:<25}")


if __name__ == "__main__":
    df = import_csv("car_sales_dataset.csv")
    porsche_df = filter_porsche(df)
    agg_df = aggregate_depreciation(porsche_df)
    print_results(agg_df)
