
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
