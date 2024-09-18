
"""Used Car Sales Technical Assessment"""
import pandas as pd
import PySimpleGUI as sg

# pylint: disable=line-too-long

# View dataframe in a viewer window
def display_df(view_df: pd.DataFrame) -> None:
    """
    Displays the dataframe in a PySimpleGUI window

    Args:
        view_df (pd.DataFrame): pandas dataframe
    """
    data = view_df.values.tolist()
    header_list = view_df.columns.tolist()

    layout = [
        [sg.Table(values=data,
            headings=header_list,
            display_row_numbers=False,
            auto_size_columns=True,
            num_rows=min(25, len(view_df)))]
    ]

    window = sg.Window('DataFrame Viewer', layout, resizable=True)
    _, _ = window.read()
    window.close()

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
    zipped_df['zipcode'] = zipped_df['zipcode'].astype(str)
    # add 0 to the beginning of the zip code until it is 5 characters long
    zipped_df['zipcode'] = zipped_df['zipcode'].apply(lambda x: x.zfill(5))
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
    filtered_df['zipcode'] = filtered_df['zipcode'].astype(str)
    # filter by zip code on first 2 digits
    filtered_df = filtered_df[filtered_df['zipcode'].str[:2].between('00', '19')]
    # sort the dataframe by zip code in ascending order
    filtered_df = filtered_df.sort_values(by='zipcode')
    # return the filtered dataframe
    return filtered_df

# Calculate the difference: Resale price - Original sale price in new column called price_difference
def calculate_differences(difference_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate price differences for each car sale in these zip codes, we need to know the original sale price and the resale price

    Args:
        df (pd.DataFrame): The dataframe containing the csv data

    Returns:
        pd.DataFrame: The dataframe with the price differences calculated
    """
    # copy dataframe to avoid modifying the original
    price_df = difference_df.copy()
    # create new column called price_difference
    price_df['price_difference'] = pd.Series(dtype='float64')
    # calculate the absolute difference: Resale price - Original sale price and round to 2 digits
    price_df['price_difference'] = abs(round(price_df['Sale Price'] - price_df['Resell Price'], 2))
    # return the dataframe with the price differences calculated
    return price_df

# Find the average of these differences
# Sum all the price differences and divide by the number of car sales
# Find the median of these differences
# Arrange all price differences in order and find the middle value
# Round both results to 2 decimal places

if __name__ == "__main__":
    df = import_csv('car_sales_dataset.csv')
    zipped_zero_df = add_zero_to_zipcode(df)
    zipcode_df = filter_by_zipcode(zipped_zero_df)
    diff_df = calculate_differences(zipcode_df)
    display_df(view_df=diff_df)
