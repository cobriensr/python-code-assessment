"""Used Car Sales Technical Assessment"""

import pandas as pd

# pylint: disable=line-too-long, trailing-whitespace, trailing-newlines

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


# Add 0 to the beginning of the zip code until it is 5 characters long
def add_zero_to_zipcode(missing_digit_df: pd.DataFrame) -> pd.DataFrame:
    """
    Add 0 to the beginning of the zip code until it is 5 characters long

    Args:
        df (pd.DataFrame): The dataframe containing the csv data

    Returns:
        pd.DataFrame: The dataframe with the zip code formatted
    """
    # copy dataframe to avoid modifying the original
    zipped_df = missing_digit_df.copy()
    # convert zipcode to string
    zipped_df["zipcode"] = zipped_df["zipcode"].astype(str)
    # add 0 to the beginning of the zip code until it is 5 characters long
    zipped_df["zipcode"] = zipped_df["zipcode"].apply(lambda x: x.zfill(5))
    # return the formatted dataframe
    return zipped_df


# Filter car sales by zip code
def filter_by_zipcode(unfiltered_df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter car sales by zip code where the first two digits are between 00 and 19.

    Args:
        df (pd.DataFrame): The dataframe containing the csv data

    Returns:
        pd.DataFrame: The filtered dataframe
    """
    # copy dataframe to avoid modifying the original
    filtered_df = unfiltered_df.copy()
    # convert zipcode to string
    filtered_df["zipcode"] = filtered_df["zipcode"].astype(str)
    # filter by zip code on first 2 digits
    filtered_df = filtered_df[filtered_df["zipcode"].str[:2].between("00", "19")]
    # sort the dataframe by zip code in ascending order
    filtered_df = filtered_df.sort_values(by="zipcode")
    # return the filtered dataframe
    return filtered_df


# Calculate the difference: Resale price - Original sale price in new column called price_difference
def calculate_price_differences(prices_df: pd.DataFrame) -> dict[float]:
    """
    Calculate the average and median price differences

    Args:
        df (pd.DataFrame): The dataframe

    Returns:
        dict[float]: _description_
    """
    # Calculate the price difference
    prices_df["price_difference"] = prices_df["Resell Price"] - prices_df["Sale Price"]

    # Calculate regular average and median prices
    avg_diff = prices_df["price_difference"].mean()
    median_diff = prices_df["price_difference"].median()

    # Calculate absolute value average and median prices
    abs_avg_diff = prices_df["price_difference"].abs().mean()
    abs_median_diff = prices_df["price_difference"].abs().median()

    # return the results
    return {
        "Average Price Change": [avg_diff],
        "Median Price Change": [median_diff],
        "Average Absolute Price Change": [abs_avg_diff],
        "Median Absolute Price Change": [abs_median_diff],
    }


# print results into a output table
def print_results(analysis_results: dict[float]) -> None:
    """
    Print the results of the price change analysis

    Args:
        results (dict[float]): The price change analysis data
    """
    # Find the average change, median change, average absolute change, and median absolute change
    avg_change = analysis_results["Average Price Change"][0]
    median_change = analysis_results["Median Price Change"][0]
    avg_abs_change = analysis_results["Average Absolute Price Change"][0]
    median_abs_change = analysis_results["Median Absolute Price Change"][0]

    # Print the results
    print("\n" + "=" * 60)
    print("                Price Difference Analysis                ")
    print("=" * 60)
    print(f"Average:            ${avg_change:>13.2f}")
    print(f"Median:             ${median_change:>13.2f}")
    print(f"Average Absolute:   ${avg_abs_change:>13.2f}")
    print(f"Median Absolute:    ${median_abs_change:>13.2f}")
    print("=" * 60)


if __name__ == "__main__":
    df = import_csv("car_sales_dataset.csv")
    zipped_zero_df = add_zero_to_zipcode(df)
    zipcode_df = filter_by_zipcode(zipped_zero_df)
    results = calculate_price_differences(zipcode_df)
    print_results(results)
