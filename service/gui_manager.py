import tkinter as tk
from .operation_manager import OperationManager as op


def hideAllChild(window: tk.Tk):
    for widget in window.winfo_children():
        widget.place_forget()


def setPageLoad(window: tk.Tk):
    pass


def setDefaultPage(window: tk.Tk):
    hideAllChild(window)


def setInitPage(window: tk.Tk):
    setPageLoad(window)


class GUIManager:
    def __init__(self):

        # GUI Pack
        self.pack = {"DefaultPage": {}}

        # Theme
        self.theme = {}

        # Initalize

        self.window = tk.Tk()
        self.window.title("청춘 일상 다이어트 총력전")
        self.window.geometry("400x600")
        self.window.resizable(False, False)
        self.window.iconbitmap(op.GetSource("icon"))

        setInitPage(self.window)

        self.window.mainloop()
