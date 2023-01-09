import tkinter as tk
from tkinter import ttk
from tkinter import*

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.wj_int_var = tk.IntVar()
        ttk.Checkbutton(self, text='Wj', variable=self.wj_int_var, onvalue=1, offvalue=0).grid(row=1, column=1)

        self.gizzu_int_var = tk.IntVar()
        ttk.Checkbutton(self, text='Gizzu', variable=self.gizzu_int_var, onvalue=1, offvalue=0).grid(row=2, column=1)

        self.kolda_int_var = tk.IntVar()
        ttk.Checkbutton(self, text='Sylwek Kołda', variable=self.kolda_int_var, onvalue=1, offvalue=0).grid(row=3, column=1)

        self.kamil_int_var = tk.IntVar()
        ttk.Checkbutton(self, text='Kamil', variable=self.kamil_int_var, onvalue=1, offvalue=0).grid(row=4, column=1)

        # save button
        self.save_button = ttk.Button(self, text='Losuj', command=self.create_list_of_checked_players)
        self.save_button.grid(row=1, column=3, padx=10)

        # set the controller
        self.controller = None

    def create_list_of_checked_players(self):
        for x in self.controller.model.list_of_players:
            if x.int_var.get() == 1 and x not in self.controller.model.list_of_checked_players:
                self.controller.model.list_of_checked_players.append(x)

            if x.int_var.get() == 0:
                if x in self.controller.model.list_of_checked_players:
                    self.controller.model.list_of_checked_players.remove(x)

        for y in self.controller.model.list_of_checked_players:
            print(y.name)



    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller



#command=lambda:self.complete_list(self.kamil_int_var)