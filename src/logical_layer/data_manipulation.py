"""Data manipulation class"""

from abc import ABC, abstractmethod

import pandas as pd
import math


class DataManipulation(ABC):
    """Data manipulation class"""

    # init method
    def __init__(self, column_identification_name) -> None:
        self.column_email_name = "E-MAIL"
        self.column_identification_name = column_identification_name

    # get column list of identification values
    @abstractmethod
    def get_identification_column_list(self) -> pd.DataFrame:
        """Get column list"""

        raise NotImplementedError("Subclass must implement this method")

    # set the value in the email column if the value is different
    @abstractmethod
    def set_value_if_different(
        self, identification_value: str, email_value: str
    ) -> None:
        """Set value"""

        raise NotImplementedError("Subclass must implement this method")

    # get data table as dataframe
    @abstractmethod
    def get_dt_table(self) -> pd.DataFrame:
        """Get data table"""

        raise NotImplementedError("Subclass must implement this method")

    # identification column higienization
    @abstractmethod
    def identification_column_higienization(self) -> pd.DataFrame:
        """Column higienization"""

        raise NotImplementedError("Subclass must implement this method")


# Data manipulation class for aposentados
class DataManipulationAposentados(DataManipulation):
    """Data manipulation class for aposentados"""

    # init method
    def __init__(self, dt_table: pd.DataFrame, column_identification_name) -> None:
        super().__init__(column_identification_name)
        self.dt_table = self.identification_column_higienization(dt_table)

    def identification_column_higienization(self, dt_table) -> pd.DataFrame:
        """Higienize the identification column"""

        dt_table[self.column_identification_name] = dt_table[
            self.column_identification_name
        ].str.zfill(11)

        return dt_table

    # get column list of identification values (cpf)
    def get_identification_column_list(self) -> pd.DataFrame:
        """Get column cpf servidor"""

        return self.dt_table[self.column_identification_name].tolist()

    # set the value in the email column if the value is different
    def set_value_if_different(
        self, identification_value: str, email_value: str
    ) -> None:
        """Set a data value for a specific column where 'CPF SERVIDOR' matches a given value"""

        # verify if the value is a string or a NaN value
        if not isinstance(identification_value, str):
            # verify if the value is a NaN value
            if math.isnan(identification_value):
                pass
        else:
            # set the value in the email column if the column does not exist
            if self.column_email_name not in self.dt_table.columns:

                self.dt_table.loc[
                    self.dt_table[self.column_identification_name]
                    == identification_value,
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

    # get data table as dataframe
    def get_dt_table(self) -> pd.DataFrame:
        """Get data table"""

        return self.dt_table


# Data manipulation class for pensionistas
class DataManipulationPensionistas(DataManipulation):
    """Data manipulation class for pensionistas"""

    # init method
    def __init__(self, dt_table: pd.DataFrame, column_identification_name) -> None:
        super().__init__(column_identification_name)
        self.dt_table = self.identification_column_higienization(dt_table)

    def identification_column_higienization(self, dt_table) -> pd.DataFrame:
        """Higienize the identification column"""

        dt_table[self.column_identification_name] = (
            dt_table[self.column_identification_name].str.slice(-8).str.zfill(8)
        )

        return dt_table

    # get column list of identification values (matricula)
    def get_identification_column_list(self) -> list[str]:
        """Get column matricula pensionista"""

        return self.dt_table[self.column_identification_name].tolist()

    # set the value in the email column if the value is different
    def set_value_if_different(
        self, identification_value: str, email_value: str
    ) -> None:
        """Set a data value for a specific column where 'VÍNCULO PENSÃO (EDITADO)' matches a given value"""

        # verify if the value is a string or a NaN value
        if not isinstance(identification_value, str):
            # verify if the value is a NaN value
            if math.isnan(identification_value):
                pass
        else:
            # set the value in the email column if the column does not exist
            if self.column_email_name not in self.dt_table.columns:

                self.dt_table.loc[
                    self.dt_table[self.column_identification_name]
                    == identification_value,
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

    # get data table as dataframe
    def get_dt_table(self) -> pd.DataFrame:
        """Get data table"""

        return self.dt_table
