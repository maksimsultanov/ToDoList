"""TkInter TodoList
Python 3.7"""
import tkinter.messagebox
from cls_ToDoListFrame import ToDoListFrame

# Create root window
root = tkinter.Tk()

# create a root object
tdf = ToDoListFrame(root)

# Start the main events loop
root.mainloop()
