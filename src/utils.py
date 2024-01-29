"""Utils fuctions"""

import os.path
import pandas as pd


class Utils:
    @staticmethod
    def verify_if_data_is_csv_or_excel(path: str) -> str:
        """Verify if the data is csv or excel"""

        if path.endswith(".csv"):
            return "csv"
        if path.endswith(".xlsx"):
            return "excel"
        if path.endswith(".xls"):
            return "excel"

        return "false"

    @staticmethod
    def read_data_to_df(path: str) -> pd.DataFrame:
        """Read data from csv or excel to dataframe"""

        if path.endswith(".csv"):
            df = pd.read_csv(path, sheet_name=0, dtype=str, engine="openpyxl")
        else:
            df = pd.read_excel(path, sheet_name=0, dtype=str, engine="openpyxl")
        return df

    @staticmethod
    def validate_file_exist(file_name: str) -> bool:
        """Validate if file exist"""

        if os.path.isfile(f"./{file_name}"):
            return True
        return False

    @staticmethod
    def mouse_coordenates_to_list(name_file: str) -> list[tuple[int, int]]:
        """Transform mouse coordenates to list"""

        with open(name_file, "r", encoding="utf-8") as file:
            file_list = file.readlines()
            file_list = [line.rstrip() for line in file_list]
            file_list = [line.split(". ") for line in file_list]
            file_list = [line[1].split(",") for line in file_list]
            file_list = [(int(line[0][1:]), int(line[1][1:-1])) for line in file_list]
        return file_list

    @staticmethod
    def table_df_export_to_xlsx(df: pd.DataFrame, name_file: str) -> None:
        """Export dataframe to xlsx"""
        name_file = f"./{name_file}"
        df.to_excel(name_file, index=False, engine="openpyxl")
