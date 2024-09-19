"""Used Car Sales Technical Assessment"""

import pandas as pd

# pylint: disable=line-too-long, trailing-whitespace, trailing-newlines, missing-final-newline, singleton-comparison


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


# Ratio = Sales Price / Top Speed
def sales_ratio(ratio_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the sales ratio of the cars

    Args:
    df (pd.DataFrame): The dataframe containing the csv data

    Returns:
    pd.DataFrame: The dataframe containing the sales ratio
    """
    # Copy original dataframe
    new_df = ratio_df.copy()
    # Calculate the sales ratio
    new_df["Ratio"] = round(new_df["Sale Price"] / new_df["Top Speed"], 3)

    # Return the dataframe
    return new_df


# Print top 10 results from the dataframe where is_new)_car = False
def set_top_10(df_10: pd.DataFrame) -> pd.DataFrame:
    """
    Print the top 10 results from the dataframe where is_new_car = False

    Args:
    df (pd.DataFrame): The dataframe containing the csv data

    Returns:
    pd.DataFrame: The dataframe containing the top 10 results
    """
    # Copy dataframe before modifying
    top_10_df = df_10.copy()
    # Filter the dataframe
    top_10_df = top_10_df[top_10_df["is_new_car"] == False]

    # Sort the dataframe
    top_10_df = top_10_df.sort_values(by="Ratio", ascending=False)

    # Create new dataframe from original dataframe with Sale Price, Top Speed, and Ratio
    ratio_top_10_df = top_10_df[["Sale Price", "Top Speed", "Ratio"]]

    # Return the dataframe
    return ratio_top_10_df


def print_top_10(ratio_top_10_df: pd.DataFrame) -> None:
    """
    Print the top 10 cars by price to speed ratio
    Args:
        ratio_top_10_df (pd.DataFrame): The dataframe containing the top 10 results
    """
    # Create a copy of the DataFrame to avoid modifying the original
    formatted_df = ratio_top_10_df.copy()
    
    # Format the 'Sale Price' column to include the dollar sign without commas
    formatted_df["Sale Price"] = formatted_df["Sale Price"].apply(lambda x: f"${x:.2f}")
    
    # Print the top 10 cars by price to speed ratio
    print("\nTop 10 Cars by Price to Speed Ratio:")
    print("=" * 60)
    print(f"{'Sale Price':<15}{'Top Speed':<15}{'Ratio':<15}")
    for _, row in formatted_df.iterrows():
        print(f"{row['Sale Price']:<15}{row['Top Speed']:<15}{row['Ratio']:<15.3f}")
    print("=" * 60)



if __name__ == "__main__":
    df = import_csv("car_sales_dataset.csv")
    sales_df = sales_ratio(df)
    top_10 = set_top_10(sales_df)
    print_top_10(top_10.head(10))
