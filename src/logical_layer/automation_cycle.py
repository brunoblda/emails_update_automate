"""Automation cycle class"""

import time
from tkinter import Tk
from tkinter import TclError
import pyautogui as pg


class AutomationCycle:
    """Automation cycle class"""

    _instance = None

    @staticmethod
    def get_instance():
        """Sigleton pattern to get instance of the class"""

        if not AutomationCycle._instance:
            AutomationCycle._instance = AutomationCycle()
        return AutomationCycle._instance

    def __init__(self) -> None:
        self.mouse_coordenates_list = None
        self.identification_value = None
        self.email_value = None

    def set_mouse_coordenates_list(
        self, mouse_coordenates_list: list[tuple[int, int]]
    ) -> None:
        """Set mouse coordenates list"""

        self.mouse_coordenates_list = mouse_coordenates_list

    def set_identification_value(self, identification_value: str) -> None:
        """Set identification value"""

        self.identification_value = identification_value

    def set_email_value(self, email_value: str) -> None:
        """Set email value"""

        self.email_value = email_value

    def execute_automation_cycle(self) -> None:
        """Execute automation cycle"""

        time.sleep(2)

        # Clean clipboard
        root = Tk()
        root.withdraw()
        root.clipboard_clear()
        root.update()

        # Click on radio select
        pg.click(self.mouse_coordenates_list.pop(0))

        pg.PAUSE = 1

        # Click on identification field
        pg.click(self.mouse_coordenates_list.pop(0))

        pg.PAUSE = 1

        # Write identification value
        pg.write(self.identification_value)

        pg.PAUSE = 1

        # Click on search button
        pg.click(self.mouse_coordenates_list.pop(0))

        # Click on email field
        pg.click(self.mouse_coordenates_list.pop(0))

        # Copy email value
        with pg.hold("ctrl"):
            pg.press("c")

        # Time added to avoid clipboard reading error
        time.sleep(0.5)

        root.update()
        try:
            self.set_email_value(root.clipboard_get())
        except TclError:
            self.set_email_value("email_nao_cadastrado")
        root.destroy()

        # Move mouse to user button
        pg.moveTo(self.mouse_coordenates_list.pop(0))

        # Click on atualizar endereco eletronico button
        pg.click(self.mouse_coordenates_list.pop(0))

    def get_email_value(self) -> str:
        """Get email value"""

        return self.email_value
