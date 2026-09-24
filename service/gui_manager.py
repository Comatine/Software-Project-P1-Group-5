from __future__ import annotations

import tkinter as tk
from tkinter import messagebox

from .operation_manager import OperationManager as op


class Widget:
    # Precated Types
    Type = {  # noqa: RUF012
        # Command [O]
        "Button": lambda parent: tk.Button(parent),
        "Checkbutton": lambda parent: tk.Checkbutton(parent),
        "Radiobutton": lambda parent: tk.Radiobutton(parent),
        "Scale": lambda parent: tk.Scale(parent),
        "Spinbox": lambda parent: tk.Spinbox(parent),
        # Command [X]
        "Label": lambda parent: tk.Label(parent),
        "Entry": lambda parent: tk.Entry(parent),
        "Text": lambda parent: tk.Text(parent),
        "Frame": lambda parent: tk.Frame(parent),
        "Canvas": lambda parent: tk.Canvas(parent),
        "ListBox": lambda parent: tk.Listbox(parent),
    }

    isItCommand = {  # noqa: RUF012
        "Button": True,
        "Checkbutton": True,
        "Radiobutton": True,
        "Scale": True,
        "Spinbox": True,
        "Label": False,
        "Entry": False,
        "Text": False,
        "Frame": False,
        "Canvas": False,
        "ListBox": False,
    }

    # Info

    def __init__(
        self,
        parent: (Page | Widget),
        name: str = "",
        widgetType: str = None,
        style: dict[str, any] = None,
        placeType: str = None,
        placeAttribute: dict[str, any] = None,
        sync=None,
        event=None,
    ):
        # Set Attributes

        if widgetType not in Widget.Type:
            raise ValueError(f"Unknown widget type: {widgetType}")
        self._obj: tk.Widget = Widget.Type[widgetType](parent.obj)
        self._parent: Page | Widget = parent
        self._name: str = name
        self._widgetType: str = widgetType
        self._style: dict[str, any] = style or {}
        self._placeType: str = placeType
        self._placeAttribute: dict[str, any] = placeAttribute or {}
        self._sync = sync
        self._event = event

        self.__activated = False

        self.childWidgets: dict[str, Widget] = {}

        # Initalize

        widget = self._obj
        widget.cls = self
        if Widget.isItCommand[self._widgetType] == True:
            if self._event != None:
                widget.config(command=self.__command(self._event))
        if self._style:
            widget.config(self._style)
        self.placeWidget()

    # Attribute Changes

    @property
    def obj(self):  # Read Only
        return self._obj

    @property
    def parent(self):  # Read Only
        return self._parent

    @property
    def widgetType(self):  # Read Only
        return self._widgetType

    @property
    def placeType(self):  # Read Only
        return self._placeType

    @property
    def placeAttribute(self):  # Read Only
        return self._placeAttribute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if self._name != new_name:
            old_name = self._name
            self._name = new_name
            if isinstance(self._parent, Page):
                self._parent.widgets[self._name] = self._parent.widgets.pop(old_name)
            elif isinstance(self._parent, Widget):
                self._parent.childWidgets[self._name] = self._parent.childWidgets.pop(
                    old_name
                )

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, new_style):
        self._style = new_style
        self._obj.config(**self._style)

    @property
    def sync(self):
        return self._sync.__name__

    @sync.setter
    def sync(self, new_sync):
        if self._sync__name__ != new_sync.__name__:
            self._sync = new_sync

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, new_event):
        if self._event is not new_event:
            self._event = new_event
            if Widget.isItCommand[self._widgetType] == True:
                self._obj.config(command=self.__command(self._event))

    # Inner Member Methods

    def __command(self, event):
        def command():
            if self.__activated:
                return

            self.__activated = True
            event(self)
            self.__activated = False

        return command

    # Member Methods

    def hideWidget(self):
        match self.placeType:
            case "pack":
                self.obj.pack_forget()
            case "grid":
                self.obj.grid_forget()
            case "place":
                self.obj.place_forget()

    def placeWidget(self):
        match self.placeType:
            case "pack":
                self.obj.pack(**self.placeAttribute)
            case "grid":
                self.obj.grid(**self.placeAttribute)
            case "place":
                self.obj.place(**self.placeAttribute)

    def addChildWidget(
        self,
        name: str,
        widgetType: str = None,
        style: dict[str, any] = None,
        placeType: str = None,
        placeAttribute: dict[str, any] = None,
        sync=lambda: None,
        event=lambda: None,
    ):
        if name not in self.childWidgets:
            self.childWidgets[name] = Widget(
                self, name, widgetType, style, placeType, placeAttribute, sync, event
            )

    def removeChildWidget(self, name: str):
        if name in self.childWidgets:
            del self.childWidgets[name]

    def changePlaceAttribute(self, new_placeType, new_placeAttribute):
        self._placeType = new_placeType
        self._placeAttribute = new_placeAttribute
        self.placeWidget()

    def syncWidget(self):
        for child in self.childWidgets.values():
            child.syncWidget()
        if self._sync != None:
            print(1)
            self._sync(self)

    def destroy(self):
        for widget in list(self.childWidgets.values()):
            widget.destroy()

        self.childWidgets.clear()
        self._obj.destroy()


class Page:
    # Info

    def __init__(self, parent: Window, name: str = "", style: dict[str, any] = None):
        # Set Attributes

        self._obj: tk.Frame = tk.Frame(parent.obj)
        self._name: str = name
        self._parent = parent
        self._style = style or {}

        self.widgets: dict[str, Widget] = {}

        # Initalize

        page = self._obj
        page.cls = self
        page.config(**self._style)

    # Attribute Changes

    @property
    def obj(self):  # Read Only
        return self._obj

    @property
    def parent(self):  # Read Only
        return self._parent

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if self._name != new_name:
            old_name = self._name
            self._name = new_name
            self._parent.pages[self._name] = self._parent.pages.pop(old_name)

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, new_Style: dict[str, any]):
        self._style = new_Style
        self._obj.config(**self._style)
        if self.parent.currentPage is self:
            self.placePage()

    # Member Methods

    def hidePage(self):
        self.obj.pack_forget()

    def placePage(self):
        for widget in self.widgets.values():
            widget.syncWidget()
        self.obj.pack(fill="both", expand=1)

    def addWidget(
        self,
        name: str,
        widgetType: str = None,
        style: dict[str, any] = None,
        placeType: str = None,
        placeAttribute: dict[str, any] = None,
        sync=None,
        event=None,
    ):
        if name not in self.widgets:
            self.widgets[name] = Widget(
                self, name, widgetType, style, placeType, placeAttribute, sync, event
            )

    def removeWidget(self, name: str):
        if name in self.widgets:
            del self.widgets[name]

    def destroy(self):
        for widget in list(self.widgets.values()):
            widget.destroy()

        self.widgets.clear()
        self._obj.destroy()


class Window:
    # Info

    def __init__(
        self,
        name: str = "",
        size: str = "100x100",
        icon: any = None,
        resizable: list[bool] = [False, False],
    ):
        # Set Attributes

        self._obj: tk.Tk = tk.Tk()
        self._name: str = name
        self._size: str = size
        self._icon: any = icon
        self._resizable: list[bool] = resizable

        self.pages: dict[str, Page] = {}
        self.currentPage: Page = None

        # Initalize

        window = self.obj
        window.cls = self
        window.title(self._name)
        window.geometry(self._size)
        window.resizable(*self._resizable)
        if icon is not None:
            window.iconbitmap(icon)

    # Attribute Changes

    @property  # Read Only
    def obj(self):
        return self._obj

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if self._name != new_name:
            self._name = new_name
            self._obj.title(self._name)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size: str):
        if self._size != new_size:
            self._size = new_size
            self._obj.geometry(self._size)

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, new_icon: any):
        self._icon = new_icon
        self._obj.iconbitmap(self._icon)

    @property
    def resizable(self):
        return self._resizable

    @resizable.setter
    def resizable(self, new_resizable: list[bool]):
        self._resizable = new_resizable
        self._obj.resizable(*self._resizable)

    # Member Methods

    def addPage(self, name: str):
        if name not in self.pages:
            self.pages[name] = Page(self, name)

    def removePage(self, name: str):
        if name in self.pages:
            page = self.pages.pop(name)
            page.destroy()

    def changePage(self, name: str):
        if name not in self.pages:
            return
        if self.currentPage is not self.pages[name]:
            old_page = self.currentPage
            new_page = self.pages[name]
            self.currentPage = new_page
            if old_page is not None:
                old_page.hidePage()
            self.currentPage.placePage()

    def destroy(self):
        for page in list(self.pages.values()):
            page.destroy()

        self.pages.clear()
        self._obj.destroy()


# 메인 클래스 (자바 생각하면 편함)
class GUI:
    def __init__(self):
        main_window = Window(
            size="600x820",
            icon=op.GetSource("icon"),
            resizable=[False, False],
            name="청춘 일상 다이어트 총력전",
        )

        main_window.addPage("defaultpage")
        defaultpage = main_window.pages["defaultpage"]
        defaultpage.style = {"bg": "#B7BEFF"}

        defaultpage.addWidget(
            name="날짜 제목",
            widgetType="Label",
            style={
                "bg": "#D1D6FF",
                "highlightbackground": "#919CFD",
                "highlightthickness": 3,
                "text": "날짜",
                "font": ("Malgun Gothic", 25, "bold"),
                "fg": "#919CFD",
            },
            placeType="place",
            placeAttribute={
                "anchor": "w",
                "x": 20,
                "y": 50,
                "width": 120,
                "height": 60,
            },
        )

        defaultpage.addWidget(
            name="날짜",
            widgetType="Label",
            style={
                "bg": "#D1D6FF",
                "highlightbackground": "#919CFD",
                "highlightthickness": 3,
                "text": "2026-01-12",
                "font": ("Malgun Gothic", 18, "bold"),
                "fg": "#919CFD",
                "justify": "left",
            },
            placeType="place",
            placeAttribute={
                "anchor": "w",
                "x": 160,
                "y": 50,
                "width": 180,
                "height": 60,
            },
        )

        defaultpage.addWidget(
            name="조회",
            widgetType="Button",
            style={
                "bg": "#D1D6FF",
                "text": "식단 조회",
                "font": ("Malgun Gothic", 14, "bold"),
                "fg": "#919CFD",
                "activebackground": "#8997FF",
                "activeforeground": "#3140B3",
            },
            placeType="place",
            placeAttribute={
                "anchor": "w",
                "x": 360,
                "y": 50,
                "width": 100,
                "height": 40,
            },
        )

        def onReadButton(widget: Widget):
            if widget.parent.name == "defaultpage":
                page = widget.parent
                target = page.widgets["날짜"].obj

                if target["text"] == "어 형이야":
                    target.config(text="어 누나야")
                else:
                    target.config(text="어 형이야")

        defaultpage.widgets["조회"].event = onReadButton

        defaultpage.addWidget(
            name="관리",
            widgetType="Button",
            style={
                "bg": "#D1D6FF",
                "text": "식단 조회",
                "font": ("Malgun Gothic", 14, "bold"),
                "fg": "#919CFD",
                "activebackground": "#8997FF",
                "activeforeground": "#3140B3",
            },
            placeType="place",
            placeAttribute={
                "anchor": "w",
                "x": 480,
                "y": 50,
                "width": 100,
                "height": 40,
            },
        )

        defaultpage.addWidget(
            name="식단표 타이틀",
            widgetType="Label",
            style={
                "bg": "#8C62FF",
                "highlightbackground": "#653CD6",
                "highlightthickness": 3,
                "text": "식  단  표",
                "font": ("Malgun Gothic", 22, "bold"),
                "fg": "#D9DDFF",
            },
            placeType="place",
            placeAttribute={
                "anchor": "w",
                "x": 20,
                "y": 130,
                "width": 560,
                "height": 60,
            },
        )

        defaultpage.addWidget(
            name="식단표",
            widgetType="Label",
            style={
                "bg": "#D1D6FF",
                "highlightbackground": "#919CFD",
                "highlightthickness": 3,
                "text": "아침 : 피자 \n점심 : 피자 \n저녁 : 피자 \n야식 : 피자 \n\n체중 : 99.5 (Kg)\n일일 섭취 열량 : 231 (Kcal)",
                "font": ("Malgun Gothic", 18, "bold"),
                "fg": "#919CFD",
                "justify": "left",
                "anchor": "nw",
            },
            placeType="place",
            placeAttribute={
                "anchor": "w",
                "x": 20,
                "y": 300,
                "width": 560,
                "height": 240,
            },
        )

        defaultpage.addWidget(
            name="체중 현황 타이틀",
            widgetType="Label",
            style={
                "bg": "#8C62FF",
                "highlightbackground": "#653CD6",
                "highlightthickness": 3,
                "text": "최근 체중 변화",
                "font": ("Malgun Gothic", 22, "bold"),
                "fg": "#D9DDFF",
            },
            placeType="place",
            placeAttribute={
                "anchor": "w",
                "x": 20,
                "y": 470,
                "width": 560,
                "height": 60,
            },
        )

        defaultpage.addWidget(
            name="체중 현황",
            widgetType="Label",
            style={
                "bg": "#D1D6FF",
                "highlightbackground": "#919CFD",
                "highlightthickness": 3,
                "text": "7일전 88.8(Kg) -> 현재 65.4(Kg) / ▼23.4 (Kg)▼",
                "font": ("Malgun Gothic", 16, "bold"),
                "fg": "#919CFD",
                "justify": "left",
            },
            placeType="place",
            placeAttribute={
                "anchor": "w",
                "x": 20,
                "y": 560,
                "width": 560,
                "height": 80,
            },
        )

        defaultpage.addWidget(
            name="결과 타이틀",
            widgetType="Label",
            style={
                "bg": "#8C62FF",
                "highlightbackground": "#653CD6",
                "highlightthickness": 3,
                "text": "결과",
                "font": ("Malgun Gothic", 22, "bold"),
                "fg": "#D9DDFF",
            },
            placeType="place",
            placeAttribute={
                "anchor": "w",
                "x": 20,
                "y": 650,
                "width": 560,
                "height": 60,
            },
        )

        defaultpage.addWidget(
            name="결과",
            widgetType="Label",
            style={
                "bg": "#D1FFE6",
                "highlightbackground": "#91FDC2",
                "highlightthickness": 3,
                "text": "목표 달성 성공!",
                "font": ("Malgun Gothic", 20, "bold"),
                "fg": "#41A169",
                "justify": "left",
            },
            placeType="place",
            placeAttribute={
                "anchor": "w",
                "x": 20,
                "y": 740,
                "width": 560,
                "height": 80,
            },
        )

        main_window.changePage("defaultpage")

        main_window.obj.mainloop()
