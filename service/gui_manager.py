import tkinter as tk
from tkinter import messagebox
from .operation_manager import OperationManager as op


class GUI:
    # -----------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------

    # GUI Pack

    pages = None

    def objectsLoad(window: tk.Tk):
        temp_pages = {
            "defaultpage": {
                # 1 라인
                "날짜 타이틀": tk.Label(
                    window,
                    bg="#D1D6FF",
                    highlightbackground="#919CFD",
                    highlightthickness=3,
                    text="날짜",
                    font=("Malgun Gothic", 25, "bold"),
                    fg="#919CFD",
                ),
                "날짜": tk.Label(
                    window,
                    bg="#D1D6FF",
                    highlightbackground="#919CFD",
                    highlightthickness=3,
                    text="2026-01-12",
                    font=("Malgun Gothic", 18, "bold"),
                    fg="#919CFD",
                    justify="left",
                ),
                "조회": tk.Button(
                    window,
                    bg="#D1D6FF",
                    highlightbackground="#919CFD",
                    highlightthickness=3,
                    text="식단 조회",
                    font=("Malgun Gothic", 14, "bold"),
                    fg="#919CFD",
                    command=lambda: None,
                ),
                "관리": tk.Button(
                    window,
                    bg="#D1D6FF",
                    highlightbackground="#919CFD",
                    highlightthickness=3,
                    text="식단 관리",
                    font=("Malgun Gothic", 14, "bold"),
                    fg="#919CFD",
                    command=lambda: None,
                ),
                # 2 라인
                "식단표 타이틀": tk.Label(
                    window,
                    bg="#8C62FF",
                    highlightbackground="#653CD6",
                    highlightthickness=3,
                    text="식  단  표",
                    font=("Malgun Gothic", 25, "bold"),
                    fg="#D9DDFF",
                ),
                "식단표": tk.Label(
                    window,
                    bg="#D1D6FF",
                    highlightbackground="#919CFD",
                    highlightthickness=3,
                    text="아침 : 피자 \n점심 : 피자 \n저녁 : 피자 \n야식 : 피자 \n\n체중 : 99.5 (Kg)\n일일 섭취 열량 : 231 (Kcal)",
                    font=("Malgun Gothic", 18, "bold"),
                    fg="#919CFD",
                    justify="left",
                    anchor="nw",
                ),
            }
        }

        # object attributes

        # placetype, placevalue, call <- 필수

        # defaultpage
        dp = temp_pages["defaultpage"]

        # 1 라인
        date_title = dp["날짜 타이틀"]
        date_title.placetype = "place"
        date_title.placevalue = {
            "anchor": "w",
            "x": 20,
            "y": 50,
            "width": 120,
            "height": 60,
        }
        date_title.call = lambda: None

        date_text = dp["날짜"]
        date_text.placetype = "place"
        date_text.placevalue = {
            "anchor": "w",
            "x": 160,
            "y": 50,
            "width": 180,
            "height": 60,
        }
        date_text.call = lambda: None

        read = dp["조회"]
        read.placetype = "place"
        read.placevalue = {
            "anchor": "w",
            "x": 360,
            "y": 50,
            "width": 100,
            "height": 40,
        }
        read.call = lambda: None

        manage = dp["관리"]
        manage.placetype = "place"
        manage.placevalue = {
            "anchor": "w",
            "x": 480,
            "y": 50,
            "width": 100,
            "height": 40,
        }
        manage.call = lambda: None

        # 2 라인
        record_title = dp["식단표 타이틀"]
        record_title.placetype = "place"
        record_title.placevalue = {
            "anchor": "w",
            "x": 20,
            "y": 130,
            "width": 560,
            "height": 60,
        }
        record_title.call = lambda: None

        record = dp["식단표"]
        record.placetype = "place"
        record.placevalue = {
            "anchor": "w",
            "x": 20,
            "y": 300,
            "width": 560,
            "height": 240,
        }
        record.call = lambda: None

        return temp_pages

    # -----------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------

    # Static Functions

    def hideAllObjects(frame: (tk.Frame | tk.Widget)):
        for widget in frame.winfo_children():
            match widget.placetype:
                case "pack":
                    widget.pack_forget()
                case "grid":
                    widget.grid_forget()
                case "place":
                    widget.pack_forget()

            for child_widget in widget.winfo_children():
                GUI.hideAllObjects(child_widget)

    def setAllObjects(state):
        # Inner Function
        def setObject(widget: tk.Widget):
            widget.call()
            match widget.placetype:
                case "pack":
                    widget.pack(widget.placevalue)
                case "grid":
                    widget.grid(widget.placevalue)
                case "place":
                    widget.place(widget.placevalue)

        # Main
        if state == None:
            return
        else:
            for widget in GUI.pages[state].values():
                setObject(widget)

    def setPageLoad(window: tk.Tk, newstate: (str | None) = None):
        if window.state == None:
            window.state = "defaultpage"
            GUI.hideAllObjects(window)
            GUI.setAllObjects(window.state)
        elif newstate == None or window.state == newstate:
            return
        else:
            window.state = newstate
            GUI.hideAllObjects(window)
            GUI.setAllObjects(window.state)

    def InitPage(window: tk.Tk):
        GUI.setPageLoad(window)

    # -----------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        # Initalize

        self.window = tk.Tk()
        self.window.title("청춘 일상 다이어트 총력전")
        self.window.configure(bg="#B7BEFF")
        self.window.geometry("600x820")
        self.window.resizable(False, False)
        self.window.iconbitmap(op.GetSource("icon"))
        self.window.state = None
        GUI.pages = GUI.objectsLoad(self.window)

        GUI.InitPage(self.window)

        self.window.mainloop()
