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
            [sg.Text("Selecione o arquivo de dados:")],
            [sg.Input(), sg.FileBrowse()],
            [sg.Text("Selecione o arquivo de coordenadas:")],
            [sg.Input(), sg.FileBrowse()],
            [sg.Submit(), sg.Cancel()],
        ]

        self.window = sg.Window(
            "Automatizador de atualização de E-mails - Aposentados e Pensionistas",
            self.layout,
            finalize=True,
            right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
            keep_on_top=True,
            element_justification="c",
            size=(700, 350),
        )

        return self.window
