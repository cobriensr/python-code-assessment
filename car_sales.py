
"""Used Car Sales Technical Assessment"""
import pandas as pd
import PySimpleGUI as sg

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

if __name__ == "__main__":
    df = import_csv('car_sales_dataset.csv')