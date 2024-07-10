"""Graphical User Interface (GUI) for the application."""

# import textwrap
import PySimpleGUI as sg


class MakeWindow:
    """ "Creates the GUI window."""

    def __init__(self, theme=None) -> None:
        self.window = None
        self.theme = theme
        self.layout = None

    def make_window(self) -> sg.Window:
        """Make the GUI window."""

        sg.theme(self.theme)

        self.layout = [
            [
                sg.Text("Selecionar tipo de atualização", font=("", 14), pad=(10, 10)),
                sg.Radio(
                    "Aposentados",
                    "RADIO1",
                    font=("", 14),
                    pad=(10, 10),
                    enable_events=True,
                ),
                sg.Radio(
                    "Pensionistas",
                    "RADIO1",
                    font=("", 14),
                    pad=(10, 10),
                    enable_events=True,
                ),
            ],
            [sg.Text("Selecione o arquivo de dados:", font=("", 14), pad=(10, 10))],
            [
                sg.Input(key="data_file", font=("", 14), pad=(10, 10)),
                sg.FileBrowse(font=("", 14), pad=(10, 10)),
            ],
            [
                sg.Text(
                    "Nome da coluna de identificação:", font=("", 14), pad=(10, 10)
                ),
                sg.Input(
                    key="identification_column",
                    size=(30, 1),
                    font=("", 14),
                    default_text="Selecione o tipo de atualização",
                    # text_color="gray",
                    pad=(10, 10),
                    disabled=True,
                ),
            ],
            [
                sg.Text(
                    "Selecione o arquivo de coordenadas:", font=("", 14), pad=(10, 10)
                )
            ],
            [
                sg.Input(key="coordenates_file", font=("", 14), pad=(10, 10)),
                sg.FileBrowse(font=("", 14), pad=(10, 10)),
            ],
            [
                sg.Text("Atualizar a partir da linha:", font=("", 14), pad=(10, 10)),
                sg.Input(
                    key="start_line",
                    size=(5, 1),
                    default_text="1",
                    justification="center",
                    font=("", 14),
                    pad=(10, 10),
                ),
            ],
            [
                sg.Text("Linha atual:", font=("", 14), pad=(10, 10)),
                sg.Text("", key="current_line", font=("", 14), pad=(10, 10)),
            ],
            [
                sg.Text(
                    "",
                    key="text_execucao",
                    font=("", 14),
                    pad=(10, 10),
                    text_color="red",
                )
            ],
            [sg.Submit("Executar", key="execute", font=("", 14), pad=(10, 10))],
            [sg.Button("Sobre", key="about", font=("", 14), pad=(10, 10))],
        ]

        self.window = sg.Window(
            "Automatizador de atualização de E-mails - Aposentados e Pensionistas",
            self.layout,
            finalize=True,
            right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
            keep_on_top=False,
            element_justification="c",
            size=(700, 570),
        )

        return self.window
