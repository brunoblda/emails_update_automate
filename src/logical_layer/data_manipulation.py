"""Data manipulation class"""

import pandas as pd


class DataManipulation:
    """Data manipulation class"""

    # init method
    def __init__(self, dt_table: pd.DataFrame) -> None:
        self.dt_table = dt_table
        self.column_email_name = "E-MAIL"
        self.column_identification_name = None

    # get column list of identification values
    def get_identification_column_list(self) -> pd.DataFrame:
        """Get column list"""

        raise NotImplementedError("Subclass must implement this method")

    # set the value in the email column if the value is different
    def set_value_if_different(
        self, identification_value: str, email_value: str
    ) -> None:
        """Set value"""

        raise NotImplementedError("Subclass must implement this method")

    # get data table as dataframe
    def get_dt_table(self) -> pd.DataFrame:
        """Get data table"""

        return self.dt_table


# Data manipulation class for aposentados
class DataManipulationAposentados(DataManipulation):
    """Data manipulation class for aposentados"""

    # init method
    def __init__(self, dt_table: pd.DataFrame) -> None:
        super().__init__(dt_table)
        self.column_identification_name = "CPF SERVIDOR"

    # get column list of identification values (cpf)
    def get_identification_column_list(self) -> pd.DataFrame:
        """Get column cpf servidor"""

        return self.dt_table["CPF SERVIDOR"].tolist()

    # set the value in the email column if the value is different
    def set_value_if_different(
        self, identification_value: str, email_value: str
    ) -> None:
        """Set a data value for a specific column where 'CPF SERVIDOR' matches a given value"""

        # set the value in the email column if the column does not exist
        if self.column_email_name not in self.dt_table.columns:

            self.dt_table.loc[
                self.dt_table[self.column_identification_name] == identification_value,
                self.column_email_name,
            ] = email_value

        else:
            # set the value in the email column if the value is different
            if (
                self.dt_table.loc[
                    self.dt_table[self.column_identification_name]
                    == identification_value,
                    self.column_email_name,
                ].values[0]
                != email_value
            ):

                self.dt_table.loc[
                    self.dt_table[self.column_identification_name]
                    == identification_value,
                    self.column_email_name,
                ] = email_value


# Data manipulation class for pensionistas
class DataManipulationPensionistas(DataManipulation):
    """Data manipulation class for pensionistas"""

    # init method
    def __init__(self, dt_table: pd.DataFrame) -> None:
        super().__init__(dt_table)
        self.column_identification_name = "VÍNCULO PENSÃO (EDITADO)"

    # get column list of identification values (matricula)
    def get_identification_column_list(self) -> list[str]:
        """Get column matricula pensionista"""

        dt_table_pensao_column = self.dt_table[
            self.column_identification_name
        ].str.slice(-8)

        return dt_table_pensao_column.tolist()

    # set the value in the email column if the value is different
    def set_value_if_different(
        self, identification_value: str, email_value: str
    ) -> None:
        """Set a data value for a specific column where 'VÍNCULO PENSÃO (EDITADO)' matches a given value"""

        # set the value in the email column if the column does not exist
        if self.column_email_name not in self.dt_table.columns:

            self.dt_table.loc[
                self.dt_table[self.column_identification_name].str.slice(-8)
                == identification_value,
                self.column_email_name,
            ] = email_value
        else:
            # set the value in the email column if the value is different
            if (
                self.dt_table.loc[
                    self.dt_table[self.column_identification_name].str.slice(-8)
                    == identification_value,
                    self.column_email_name,
                ].values[0]
                != email_value
            ):

                self.dt_table.loc[
                    self.dt_table[self.column_identification_name].str.slice(-8)
                    == identification_value,
                    self.column_email_name,
                ] = email_value
