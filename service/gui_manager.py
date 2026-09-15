import tkinter as Tk
from .operation_manager import OperationManager as Op

class GUIManager:

    # 데이터 아직 안씀
    def __init__(self):
        self.window = Tk.Tk()
        self.window.title("청춘 일상 다이어트 총력전")
        self.window.geometry("400x600")
        self.window.resizable(False, False)
        self.window.iconbitmap(Op.GetSource("icon"))
        self.window.mainloop()
