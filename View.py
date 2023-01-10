import tkinter as tk
from tkinter import ttk
from tkinter import*

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.wj_int_var = tk.IntVar()
        self.wj_int_var.set(1)
        ttk.Checkbutton(self, text='Wj', variable=self.wj_int_var, onvalue=1, offvalue=0).grid(row=1, column=1)

        self.gizzu_int_var = tk.IntVar()
        self.gizzu_int_var.set(1)
        ttk.Checkbutton(self, text='Gizzu', variable=self.gizzu_int_var, onvalue=1, offvalue=0).grid(row=2, column=1)

        self.sylwek_k_int_var = tk.IntVar()
        self.sylwek_k_int_var.set(1)
        ttk.Checkbutton(self, text='Sylwek Kołda', variable=self.sylwek_k_int_var, onvalue=1, offvalue=0).grid(row=3, column=1)

        self.kamil_int_var = tk.IntVar()
        self.kamil_int_var.set(1)
        ttk.Checkbutton(self, text='Kamil', variable=self.kamil_int_var, onvalue=1, offvalue=0).grid(row=4, column=1)

        self.robert_z_int_var = tk.IntVar()
        self.robert_z_int_var.set(1)
        ttk.Checkbutton(self, text='Robert Zapała', variable=self.robert_z_int_var, onvalue=1, offvalue=0).grid(row=5, column=1)

        self.marcin_z_int_var = tk.IntVar()
        self.marcin_z_int_var.set(1)
        ttk.Checkbutton(self, text='Marcin Zapałą', variable=self.marcin_z_int_var, onvalue=1, offvalue=0).grid(row=6, column=1)

        self.pawel_z_int_var = tk.IntVar()
        self.pawel_z_int_var.set(1)
        ttk.Checkbutton(self, text='Paweł Zapałą', variable=self.pawel_z_int_var, onvalue=1, offvalue=0).grid(row=7, column=1)

        self.krzys_z_int_var = tk.IntVar()
        self.krzys_z_int_var.set(1)
        ttk.Checkbutton(self, text='Krzysztof Zapałą', variable=self.krzys_z_int_var, onvalue=1, offvalue=0).grid(row=8, column=1)

        self.krzys_w_int_var = tk.IntVar()
        self.krzys_w_int_var.set(1)
        ttk.Checkbutton(self, text='Krzysztof Wesołowski', variable=self.krzys_w_int_var, onvalue=1, offvalue=0).grid(row=9,
                                                                                                                  column=1)
        self.tomek_int_var = tk.IntVar()
        self.tomek_int_var.set(1)
        ttk.Checkbutton(self, text='Tomek', variable=self.tomek_int_var, onvalue=1, offvalue=0).grid(
            row=10,
            column=1)

        # save button
        self.save_button = ttk.Button(self, text='Losuj', command=self.losuj_i_pokaz_teamy)
        self.save_button.grid(row=1, column=3, padx=10)

        # set the controller
        self.controller = None

    def losuj_i_pokaz_teamy(self):
        self.controller.create_list_of_checked_players()
        self.controller.create_teams_from_checked_players()
        self.controller.display_teams()

    def display_teams(self, teams_joined_str):
        root = Tk()
        root.title('Wylosowane teamy')
        lab_stats = Label(root, text=teams_joined_str)
        lab_stats.pack()
        root.geometry('400x400')

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller



#command=lambda:self.complete_list(self.kamil_int_var)