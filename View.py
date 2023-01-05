import tkinter as tk
from tkinter import ttk
from tkinter import*

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='Label :')
        self.label.grid(row=1, column=0)

        # email entry
        self.email_var = tk.StringVar()
        self.entry1 = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.entry1.grid(row=1, column=1, sticky=tk.NSEW)

        # save button
        self.save_button = ttk.Button(self, text='Btn1', command=self.open_new_window_bc)
        self.save_button.grid(row=1, column=3, padx=10)

        self.btn2 = ttk.Button(self, text='Choose players', command=self.choose_players_bc)
        self.btn2.grid(row=2, column=3, padx=10)

        self.btn3 = ttk.Button(self, text='Choose players', command=self.show_checked_players_bc3)
        self.btn3.grid(row=3, column=3, padx=10)


        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def open_new_window_bc(self):
        """
        Handle button click event-
        """
        if self.controller:
            self.controller.open_new_window()

    def choose_players_bc(self):
        """
        Handle button click event-
        """
        if self.controller:
            self.controller.choose_players()

    def show_players_and_choose(self, list_of_players):
        root = Tk()
        root.geometry("600x1000")
        count = 0
        var1 = tk.IntVar()
        for x in list_of_players:
            # x.int_var = tk.IntVar()
            tk.Checkbutton(root, text=x.name, variable=var1, onvalue=1, offvalue=0, command=lambda: self.store_names_in_model_list(var1)).grid(row=count, column=1)
            count += 1
        mainloop()

    def show_checked_players_bc3(self):
        """
        Handle button click event-
        """
        if self.controller:
            self.controller.show_checked_players()

    def show_checked_players(self, list_of_checked_players):
        root = Tk()
        root.geometry("600x1000")
        for x in list_of_checked_players:
            print(x)

    def store_names_in_model_list(self, int_var):
        print(int_var.get())
        # if name not in self.controller.model.list_of_checked_players:
        #     self.controller.model.list_of_checked_players.append(name)
        # self.controller.model.list_of_checked_players.append(name)
        # print(self.controller.model.list_of_checked_players)
