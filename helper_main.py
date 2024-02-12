"""Main file for the project."""

import PySimpleGUI as sg
from src.logical_layer import AutomationCycle
from src.utils import Utils
from src.logical_layer import DataManipulationPensionistas
from src.gui_layer import MakeWindow


def test_automation_cycle():
    """Test automation cycle"""

    table_df = None
    coordenates_list = None

    if Utils.validate_file_exist("data/pensionistas.xlsx"):
        if Utils.verify_if_data_is_csv_or_excel("data/pensionistas.xlsx") != "false":
            table_df = Utils.read_data_to_df("data/pensionistas.xlsx")
            table_df = DataManipulationPensionistas(table_df)
        else:
            print("File not supported")
    else:
        print("File not found")

    # coordenates_mouse_path = 'data/coordenadas_mouse_aposentados.txt'
    coordenates_mouse_path = "data/coordenadas_mouse_pens.txt"

    if Utils.validate_file_exist(coordenates_mouse_path):
        coordenates_list = Utils.mouse_coordenates_to_list(coordenates_mouse_path)

    else:
        print("File not found")

    # cfp_list = table_df.get_column_cpf_servidor_list()
    matricula_list = table_df.get_identification_column_list()

    coordenates_list_copy = coordenates_list.copy()

    automation_cycle = AutomationCycle()

    for i in range(0, 3):
        automation_cycle.set_mouse_coordenates_list(coordenates_list_copy)
        automation_cycle.set_identification_value(str(matricula_list[i]))
        automation_cycle.execute_automation_cycle()
        print(automation_cycle.get_email_value())
        table_df.set_value_if_different(
            matricula_list[i], automation_cycle.get_email_value()
        )
        coordenates_list_copy = coordenates_list.copy()

    Utils.table_df_export_to_xlsx(
        table_df.get_dt_table(), "data/pensionistas_output.xlsx"
    )


def show_gui():
    """Show GUI window"""
    window_started = MakeWindow("DarkAmber").make_window()
    while True:
        event, values = window_started.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "Submit":
            print("You entered ", values[0])
            print("You entered ", values[1])
            window_started.close()
            break
    window_started.close()


if __name__ == "__main__":
    test_automation_cycle()
    # show_gui()
