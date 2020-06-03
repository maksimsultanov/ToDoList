from tkinter import *
from tkinter.messagebox import showerror


class AboutWindow(Toplevel):
    """the class describes about window"""

    def __init__(self, parent):
        # set parent for the dialog
        self.top = Toplevel(parent)
        self.top.transient(parent)
        # create modal window
        self.top.grab_set()
        # set title the dialog
        self.top.title("О программе")
        # if pressed return or escape btn
        self.top.bind("<Return>", self.close)
        self.top.bind("<Escape>", self.close)
        # info about app
        self._label_description = Label(self.top, text="Приложение для управления повседневными делами")
        self._label_description.pack(padx=15, fill=X)
        # info about rights
        self._label_right = Label(self.top, text="Свободно для личного использования")
        self._label_right.pack(padx=15, fill=X)
        # info about developer
        self._label_developer = Label(self.top, text="Максим Султанов")
        self._label_developer.pack(padx=15, fill=X)
        # info about wen the app was developed
        self._label_developed = Label(self.top, text="2020")
        self._label_developed.pack(padx=15, fill=X)
        # close btn
        self._btn_close = Button(self.top, text="Закрыть", command=self.close)
        self._btn_close.pack(pady=15, side=RIGHT)

    def close(self):
        """method on event press escape btn"""
        self.top.destroy()
