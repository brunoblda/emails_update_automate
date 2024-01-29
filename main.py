"""Main file for the project."""

import textwrap
import datetime
import PySimpleGUI as sg
from pandas import DataFrame
from src.logical_layer import AutomationCycle
from src.utils import Utils
from src.logical_layer import (
    DataManipulation,
    DataManipulationAposentados,
    DataManipulationPensionistas,
)
from src.gui_layer import MakeWindow


def verify_entries(input_values):
    """Verify entries"""

    if input_values[0] is False and input_values[1] is False:
        return (False, "Selecione uma opção.")

    if input_values["data_file"] == "":
        return (False, "Selecione o arquivo de dados.")

    if input_values["coordenates_file"] == "":
        return (False, "Selecione o arquivo de coordenadas.")

    if Utils.validate_file_exist(input_values["data_file"]) == "false":
        return (False, "Arquivo de dados não encontrado.")

    if Utils.validate_file_exist(input_values["coordenates_file"]) == "false":
        return (False, "Arquivo de coordenadas não encontrado.")

    if Utils.verify_if_data_is_csv_or_excel(input_values["data_file"]) == "false":
        return (False, "Arquivo de dados não suportado.")

    return (True, "Executando...")


def automation_data(
    input_values,
) -> tuple[DataManipulation, DataFrame, list[tuple[int, int]]]:
    """Automation data for automation cycle"""
    table_df = Utils.read_data_to_df(input_values["data_file"])
    atualization_type = "aposentados" if input_values[0] else "pensionistas"
    coordenates_data_list = Utils.mouse_coordenates_to_list(
        input_values["coordenates_file"]
    )

    if atualization_type == "aposentados":
        table_df = DataManipulationAposentados(table_df)
    else:
        table_df = DataManipulationPensionistas(table_df)

    identification_list = table_df.get_identification_column_list()

    return (table_df, identification_list, coordenates_data_list)


def execute_automation_cycle(
    table_df, identification_list, coordenates_data_list, start_line
):
    """Execute automation cycle"""

    coordenates_list_copy = coordenates_data_list.copy()

    automation_cycle = AutomationCycle()

    index_line = start_line

    for i in range(index_line, index_line + 10):
        if i >= len(identification_list):
            break
        automation_cycle.set_mouse_coordenates_list(coordenates_list_copy)
        automation_cycle.set_identification_value(str(identification_list[i]))
        automation_cycle.execute_automation_cycle()
        table_df.set_value_if_different(
            identification_list[i], automation_cycle.get_email_value()
        )
        coordenates_list_copy = coordenates_data_list.copy()
        index_line = i

    return (table_df, index_line)


def about_text() -> str:
    """About text"""

    text_about = textwrap.dedent(
        """
        Sistema de automação de atualização de e-mail de aposentados e pensionistas

        O nome da coluna de resposta é "E-MAIL"

        O sistema somente irá atualizar o e-mail se o valor na planilha for diferente do valor encontrado.

        Os e-mails são salvos em caixa alta.

        Informações do sobre os dados:

            A coluna de referência para a atualização de e-mail dos aposentados é a coluna "CPF SERVIDOR".

            A coluna de referencia para a atualização de e-mail dos pensionistas é a coluna "VÍNCULO PENSÃO (EDITADO)".

        Informações sobre o arquivo de coordenadas:

            A quantidade de coordenadas deve ser igual a 6.

            1 - Coordenada do radio button de seleção de aposentados ou pensionistas.

            2 - Coordenada do campo de identificação (cpf do servidor ou matricula do pensionista).

            3 - Coordenada do botão de pesquisa.

            4 - Coordenada do campo de selecao e-mail.

            5 - Coordenada do botão de usuário.

            6 - Coordenada do botão de atualizar endereço eletrônico.

        Autor: Bruno Luiz de Deus Adão
        Github: https://github.com/brunoblda
        """
    )

    return text_about


def gui_controller():
    """GUI controller"""

    window_instance = MakeWindow("DarkBlue").make_window()
    while True:
        event, values = window_instance.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "about":
            sg.popup("Sobre", about_text(), keep_on_top=True, font=("", 14))
        if event == "execute":
            verify_entries_result = verify_entries(values)
            window_instance["text_execucao"].update(verify_entries_result[1])
            if verify_entries_result[0] is True:
                automation_data_result = automation_data(values)
                data_manipulation = automation_data_result[0]
                start_line = int(values["start_line"]) - 1
                start_line = max(start_line, 0)
                if start_line >= len(automation_data_result[1]):
                    window_instance["text_execucao"].update(
                        "Inicio informado é maior do que o tamanho da planilha."
                    )
                    window_instance["current_line"].update(
                        len(automation_data_result[1])
                    )
                    window_instance.refresh()
                else:
                    while True:
                        execute_automation_cycle_result = execute_automation_cycle(
                            data_manipulation,
                            automation_data_result[1],
                            automation_data_result[2],
                            start_line,
                        )
                        if execute_automation_cycle_result[1] >= len(
                            automation_data_result[1]
                        ):
                            window_instance["text_execucao"].update(
                                "Executado até o final da planilha."
                            )
                            window_instance["current_line"].update(
                                len(automation_data_result[1])
                            )
                            current_time = datetime.datetime.now()
                            current_time = current_time.strftime("%Y-%m-%d %H_%M_%S")
                            Utils.table_df_export_to_xlsx(
                                execute_automation_cycle_result[0].get_dt_table(),
                                f"data/output_{current_time}.xlsx",
                            )
                            window_instance.refresh()
                            break
                        pop_up_yes_no_text = textwrap.dedent(
                            f"""
                            Executado até a linha {execute_automation_cycle_result[1] + 1}.

                            Deseja continuar a execução?
                            """
                        )
                        continue_execution = sg.popup_yes_no(
                            pop_up_yes_no_text, keep_on_top=True, font=("", 14)
                        )
                        window_instance.refresh()
                        if continue_execution == "No":
                            window_instance["text_execucao"].update(
                                "Você parou a execução."
                            )
                            window_instance["current_line"].update(
                                execute_automation_cycle_result[1] + 1
                            )
                            current_time = datetime.datetime.now()
                            current_time = current_time.strftime("%Y-%m-%d %H_%M_%S")
                            window_instance.refresh()
                            Utils.table_df_export_to_xlsx(
                                execute_automation_cycle_result[0].get_dt_table(),
                                f"output_{current_time}.xlsx",
                            )
                            break
                        start_line = execute_automation_cycle_result[1] + 1
                        window_instance["current_line"].update(
                            execute_automation_cycle_result[1] + 1
                        )
                        window_instance.refresh()
                        data_manipulation = execute_automation_cycle_result[0]

    window_instance.close()


if __name__ == "__main__":
    gui_controller()
