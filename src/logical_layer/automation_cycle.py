"""Automation cycle class"""

import time
from tkinter import Tk
import pyautogui as pg


class AutomationCycle:
    """Automation cycle class"""

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

    def execute_automation_cycle(self) -> None:
        """Execute automation cycle"""

        time.sleep(2)

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
        root = Tk()
        root.withdraw()
        self.email_value = root.clipboard_get()

        # Move mouse to user button
        pg.moveTo(self.mouse_coordenates_list.pop(0))

        # Click on atualizar endereco eletronico button
        pg.click(self.mouse_coordenates_list.pop(0))

    def get_email_value(self) -> str:
        """Get email value"""

        return self.email_value
