"""Data manipulation class"""

import pandas as pd


class DataManipulation:
    """Data manipulation class"""

    def __init__(self, dt_table: pd.DataFrame) -> None:
        self.dt_table = dt_table
        self.column_email_name = "email"

    def get_column_list(self) -> pd.DataFrame:
        """Get column list"""

        raise NotImplementedError("Subclass must implement this method")

    def set_value(self, identification_value: str, email_value: str) -> None:
        """Set value"""

        raise NotImplementedError("Subclass must implement this method")

    def get_dt_table(self) -> pd.DataFrame:
        """Get data table"""

        return self.dt_table


class DataManipulationAposentados(DataManipulation):
    """Data manipulation class for aposentados"""

    def get_column_list(self) -> pd.DataFrame:
        """Get column cpf servidor"""

        return self.dt_table["CPF SERVIDOR"].tolist()

    def set_value(self, identification_value: str, email_value: str) -> None:
        """Set a data value for a specific column where 'CPF SERVIDOR' matches a given value"""

        self.dt_table.loc[
            self.dt_table["CPF SERVIDOR"] == identification_value,
            self.column_email_name,
        ] = email_value


class DataManipulationPensionistas(DataManipulation):
    """Data manipulation class for pensionistas"""

    def get_column_list(self) -> pd.DataFrame:
        """Get column matricula pensionista"""

        dt_table_pensao_column = self.dt_table["VÍNCULO PENSÃO (EDITADO)"].str.slice(14)

        return dt_table_pensao_column.tolist()

    def set_value(self, identification_value: str, email_value: str) -> None:
        """Set a data value for a specific column where 'MATRÍCULA PENSIONISTA' matches a given value"""

        self.dt_table.loc[
            self.dt_table["VÍNCULO PENSÃO (EDITADO)"].str.slice(14)
            == identification_value,
            self.column_email_name,
        ] = email_value
