from tkinter import *
from tkinter.messagebox import showerror


class EditDoDialogWindow(Toplevel):
    """The class dialog of edit Do in Do list"""
    def __init__(self, parent, editText):
        """Constructor edit dialog"""
        # set edit text value
        self.editText = editText
        self._result_text = ""
        # set parent for the dialog
        self.top = Toplevel(parent)
        self.top.transient(parent)
        # create modal window
        self.top.grab_set()
        # set title the modal window
        self.top.title("Редактирование задачи с названием: " + self.editText)
        # if pressed enter key
        self.top.bind("<Return>", self.ok)
        # if pressed escape key
        self.top.bind("<Escape>", self.cancel)
        # set info label the modal window
        self.labelEditInfo = Label(self.top, text="Как теперь будет называться задача: {}".format(self.editText))
        self.labelEditInfo.pack(padx=15, fill=X)
        # set edit entry
        self.editEntry = Entry(self.top)
        # if pressed enter key
        self.editEntry.bind("<Return>", self.ok)
        # if pressed escape key
        self.editEntry.bind("<Escape>", self.cancel)
        # pad from left border
        self.editEntry.pack(padx=15, fill=X)
        # set focus at the entry
        self.editEntry.focus_set()
        # create btn ok
        btnOk = Button(self.top, text="Ok", command=self.ok)
        btnOk.pack(pady=5, side=RIGHT)
        # create btn cancel
        btnCancel = Button(self.top, text="Cancel", command=self.cancel)
        btnCancel.pack(pady=5, side=RIGHT)

    def ok(self, event=None):
        """method on event return or ok press btn"""
        # set result text
        self._result_text = self.editEntry.get()
        if self.top.master.change_do(self._result_text) == "ok":
            # if Do was change close the dialog window
            self.top.destroy()
        elif self.top.master.change_do(self._result_text) == "the same do":
            # if the same do exists in DoList show error
            showerror("Ошибка", "Такая задача уже есть")
        elif self.top.master.change_do(self._result_text) == "empty do":
            # if entered empty Do or with only space show error
            showerror("Ошибка", "нужно что-то написать словами")

    def cancel(self, event=None):
        """method on event escape or cancel press btn"""
        self.top.destroy()

    def get_result(self):
        """getter method for result edit text"""
        return self._result_text
