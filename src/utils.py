"""Utils fuctions"""

import pandas as pd


def verify_if_data_is_csv_or_excel(path: str) -> str:
    """Verify if the data is csv or excel"""
    if path.endswith(".csv"):
        return "csv"
    elif path.endswith(".xlsx"):
        return "excel"
    elif path.endswith(".xls"):
        return "excel"
    else:
        return "false"


def read_data(path: str) -> pd.DataFrame:
    """Read data from csv or excel"""
    if path.endswith(".csv"):
        df = pd.read_csv(path)
    else:
        df = pd.read_excel(path)
    return df
