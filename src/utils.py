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
    def read_data_to_df(path: str, identification_column: str) -> pd.DataFrame:
        """Read data from csv or excel to dataframe"""

        if path.endswith(".csv"):
            df = pd.read_csv(path, dtype=str)
        else:
            dfs = pd.read_excel(path, sheet_name=None, dtype=str, engine="openpyxl")
            for df in dfs.values():
                if identification_column in df.columns:
                    return df

        return df

    @staticmethod
    def validate_column_exist(path: str, identification_column: str) -> bool:
        """Validate if column exist in dataframe"""

        if path.endswith(".csv"):
            df = pd.read_csv(path, dtype=str)
            return True
        else:
            dfs = pd.read_excel(path, sheet_name=None, dtype=str, engine="openpyxl")
            for df in dfs.values():
                if identification_column in df.columns:
                    return True
        return False

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
    def table_df_export_to_xlsx(
        df: pd.DataFrame, name_file: str, path: str, identification_column: str
    ) -> None:
        """Export dataframe to xlsx"""

        df_path = pd.DataFrame()
        dfs_path = dict()

        if path.endswith(".csv"):
            df_path = pd.read_csv(path, dtype=str)
        else:
            dfs_path = pd.read_excel(
                path, sheet_name=None, dtype=str, engine="openpyxl"
            )

        name_file = f"./{name_file}"
        df_first = pd.DataFrame()

        first_key = next(iter(dfs_path.keys()))

        df_first.to_excel(
            name_file, sheet_name=first_key, index=False, engine="openpyxl"
        )

        with pd.ExcelWriter(
            name_file, engine="openpyxl", if_sheet_exists="replace", mode="a"
        ) as writer:
            for sheet_name_path, df_path in dfs_path.items():
                if identification_column in df_path.columns:
                    df.to_excel(writer, sheet_name=sheet_name_path, index=False)
                else:
                    df_path.to_excel(writer, sheet_name=sheet_name_path, index=False)
