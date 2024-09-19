
"""Used Car Sales Technical Assessment"""
import pandas as pd
import PySimpleGUI as sg

# pylint: disable=line-too-long, trailing-whitespace, trailing-newlines, missing-final-newline

# View dataframe in a viewer window
def display_df(view_df: pd.DataFrame) -> None:
    """
    Displays the dataframe in a PySimpleGUI window

    Args:
        view_df (pd.DataFrame): pandas dataframe
    """
    # Convert the dataframe to a list of lists
    data = view_df.values.tolist()
    header_list = view_df.columns.tolist()
    # Create the layout
    layout = [
        [sg.Table(values=data,
            headings=header_list,
            display_row_numbers=False,
            auto_size_columns=True,
            num_rows=min(25, len(view_df)))]
    ]
    # Create the window
    window = sg.Window('DataFrame Viewer', layout, resizable=True)
    # Read the window
    _, _ = window.read()
    # Close the window
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
