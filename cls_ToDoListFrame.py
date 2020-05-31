import random
from tkinter import *
from tkinter.messagebox import *
from EditDoDialogWindow import EditDoDialogWindow
from cls_DBTodoList import DbWork


class ToDoListFrame(Frame):
    """the class of frame for todo list"""

    def __init__(self, master):
        """constructor the class"""
        # set the parent as root
        Frame.__init__(self, master=None)
        # set title the frame
        self.master.title("Мой список дел")
        # Set Frame size
        self.master.geometry("425x320")
        # frozen size of the Frame
        self.master.resizable(width=False, height=False)
        # Create an empty Do list
        self._myDoList = []
        # title label
        self.label_title = Label(self.master, text="Список дел")  # create object
        self.label_title.grid(column=0, row=0)  # append to the root window
        # display text
        self.label_display = Label(self.master, text="", width=25)  # create object
        self.label_display.grid(column=1, row=0)  # append to the root window
        # txt input field
        self.txt_input = Entry(self.master, width=15)  # create object
        self.txt_input.grid(column=1, row=1)  # append to the root window
        # set method on press enter button
        self.txt_input.bind("<Return>", self.addDo)
        # list box of Do
        self.lb_listDo = Listbox(self.master)
        self.lb_listDo.grid(column=1, row=2, rowspan=8)
        # set method on press enter button
        self.lb_listDo.bind("<Delete>", self.deleteDo)
        ###############################################
        # add btn
        self.btn_addDo = Button(self.master, text="Добавить задачу", width=24,
                                command=self.addDo)  # create object
        self.btn_addDo.grid(column=0, row=1)  # append to the root window
        # clear list btn
        self.btn_clrList = Button(self.master, text="Очистить список задач", width=24,
                                  command=self.clrList)  # create object
        self.btn_clrList.grid(column=0, row=2)  # append to the root window
        # edit btn
        self.btn_editDo = Button(self.master, text="Редактировать задачу", width=24,
                                 command=self.editDo)  # create object
        self.btn_editDo.grid(column=0, row=3)  # append to the root window
        # delete Do btn
        self.btn_deleteDo = Button(self.master, text="Удалить задачу", width=24,
                                   command=self.deleteDo)  # create object
        self.btn_deleteDo.grid(column=0, row=4)  # append to the root window
        # Sort ASC btn
        self.btn_sortASC = Button(self.master, text="Сортировать по возрастанию", width=24,
                                  command=self.sortASC)  # create object
        self.btn_sortASC.grid(column=0, row=5)  # append to the root window
        # sort DESC btn
        self.btn_sortDESC = Button(self.master, text="Сортировать по убыванию", width=24,
                                   command=self.sortDESC)  # create object
        self.btn_sortDESC.grid(column=0, row=6)  # append to the root window
        # Chose random btn
        self.btn_chRnd = Button(self.master, text="Выбрать случайно", width=24,
                                command=self.chRnd)  # create object
        self.btn_chRnd.grid(column=0, row=7)  # append to the root window
        # Number of task btn
        self.btn_numTask = Button(self.master, text="Количество дел в списке", width=24,
                                  command=self.numTask)  # create object
        self.btn_numTask.grid(column=0, row=8)  # append to the root window
        # exit btn
        self.btn_exitApp = Button(self.master, text="Выход", width=24,
                                  command=self.exitApp)  # create object
        self.btn_exitApp.grid(column=0, row=9)  # append to the root window
        #######################################################################
        ##################create#menu#bar######################################
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)
        #######################################################################
        self.file_menu = Menu(self.menu_bar)
        self.file_menu.add_command(label="Выход", command=self.exitApp)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)
        #######################################################################
        self.todo_menu = Menu(self.menu_bar)
        self.todo_menu.add_command(label="Добавить дело", command=self.addDo)
        self.todo_menu.add_command(label="Очистить список дел", command=self.clrList)
        self.todo_menu.add_command(label="Редактировать дело", command=self.editDo)
        self.todo_menu.add_command(label="Удалить дело", command=self.deleteDo)
        self.todo_menu.add_command(label="Сортировать список по алфавиту", command=self.sortASC)
        self.todo_menu.add_command(label="Сортировать список обратно алфавиту", command=self.sortDESC)
        self.todo_menu.add_command(label="Случайное дело", command=self.chRnd)
        self.todo_menu.add_command(label="Количество дел в списке", command=self.numTask)
        self.menu_bar.add_cascade(label="Список дел", menu=self.todo_menu)
        #######################################################################
        self.help_menu = Menu(self.menu_bar)
        self.help_menu.add_command(label="Справка")
        self.help_menu.add_command(label="О программе")
        self.menu_bar.add_cascade(label="Помощь", menu=self.help_menu)
        #######################################################################
        ##################add#create#or#reade#database#########################
        # set connection with db
        tmp_do_list = []
        with DbWork() as do_db:
            do_db.create_table("do_list")
            for row in do_db.read_all_from_table("do_list"):
                self._myDoList.append(row[1])
        self.updateDoListBox()
        #######################################################################

    def updateDoListBox(self):
        """populate the listbox"""
        # clear before populate
        self.clrDoListBox()
        # populate
        for myDo in self._myDoList:
            self.lb_listDo.insert("end", myDo)

    def update_do_in_db(self):
        """Update the db"""
        # set tmp copy for insert in db
        # tmp_myDo = self._myDoList.copy()
        tmp_myDo = []
        for i in range(0, len(self._myDoList)):
            tmp_myDo.append((i, self._myDoList[i]))
        # tmp_myDo = map(tuple, tmp_myDo)
        # write into db
        with DbWork() as db_do:
            db_do.delete_table("do_list")
            db_do.create_table("do_list")
            db_do.insert_into_table("do_list", tmp_myDo)

    def clrDoListBox(self):
        """clear the listbox"""
        self.lb_listDo.delete(0, "end")

    def addDo(self, event=None):
        """add new do into the listbox"""
        # add new Do
        myDo = self.txt_input.get()
        # append new Do if it is really new Do
        if (myDo != "") and not (myDo in self._myDoList):
            self._myDoList.append(myDo)
            self.label_display["text"] = "Задача успешно добавлена"
            # clear input after successfully add new Do
            self.txt_input.delete(0, "end")
        elif (myDo == ""):
            self.label_display["text"] = "Напиши что сделать"
        elif (myDo in self._myDoList):
            self.label_display["text"] = "Такое дело уже есть"
        self.updateDoListBox()
        # update data in db
        self.update_do_in_db()

    def clrList(self):
        """Delete all items from myDoList"""
        # create dialog for ask about delete all items from myDoList
        confirmed = askyesno("Подтверждение удаления", "Точно удалить всё?")
        if confirmed:
            # clr myDoList
            self._myDoList = []
            # upd listbox
            self.updateDoListBox()
            # msg about clr the list Do
            self.label_display['text'] = "Список задач пуст"
            # update db
            self.update_do_in_db()


    def editDo(self):
        """Method for create editDo dialog"""
        # edit if the Do is selected
        if self.lb_listDo.curselection():
            # get index the change do
            self._indexDo = self.lb_listDo.curselection()
            index_do = self._indexDo[0]
            # create dialog window for change the do
            edit_do_dialog = EditDoDialogWindow(self, self._myDoList[index_do])
            self.master.wait_window(edit_do_dialog.top)
            # after close the dialog window update listbox
            self.updateDoListBox()
            # tell about end of edit the do
            self.label_display['text'] = "Редактирование задачи завершено"

    def change_do(self, new_text_do: str):
        """Set new value to edit do"""
        # get index the change do
        index_do = self._indexDo[0]
        if new_text_do in self._myDoList:
            # if the same do exist in the list
            return "the same do"
        elif new_text_do == "" or len(new_text_do) == new_text_do.count(" "):
            # if entered empty do or only spaces
            return "empty do"
        else:
            # if entered correct value new text do
            self._myDoList[index_do] = new_text_do
            self.update_do_in_db()
            return "ok"

    def deleteDo(self, event=None):
        """Delete one Do from the list Do"""
        # if myDoList not empty
        if self._myDoList:
            # delete only selected items
            for selectDo in self.lb_listDo.curselection():
                # delete from list my Do
                del (self._myDoList[selectDo])
                # upd do listbox
                self.updateDoListBox()
                self.label_display['text'] = "Задача успешно удалена"
                # change do in db
            self.update_do_in_db()

    def sortASC(self):
        """Sort ASC the list of Do"""
        # if myDoList not empty
        if self._myDoList:
            # sort my Do
            self._myDoList.sort()
            # upd listbox
            self.updateDoListBox()
            # sort data in db

    def sortDESC(self):
        """Sort DESC the list of Do"""
        # if myDoList not empty
        if self._myDoList:
            # sort my Do
            self._myDoList.sort()
            # reverse the list
            self._myDoList.reverse()
            # upd listbox
            self.updateDoListBox()
            # sort data in db

    def chRnd(self):
        """choice a random Do"""
        # if myDoList not empty
        if self._myDoList:
            # Choose a random Do
            myDo = random.choice(self._myDoList)
            # upd the display label
            self.label_display["text"] = myDo

    def numTask(self):
        """count number of Do in the list"""
        #     number of task
        n_o_t = len(self._myDoList)
        # create message
        msg = "Количество дел в списке: {}".format(n_o_t)
        # Display
        self.label_display["text"] = msg

    def exitApp(self):
        """exit from the app"""
        # close the main window
        self.master.destroy()
