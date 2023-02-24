import tkinter as tk
from tkinter import ttk
from tkinter import*

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.rsi_lab1 = ttk.Label(self, text='Akceptowalna różnica sił ')
        self.rsi_lab1.grid(row=0, column=3)
        # self.
        self.e_allow_value = ttk.Entry(self, justify='right')
        self.e_allow_value.insert(1, 300)
        self.e_allow_value.grid(row=1, column=3)

        self.wj_int_var = tk.IntVar()
        self.wj_int_var.set(0)
        ttk.Checkbutton(self, text='Wiesław', variable=self.wj_int_var, onvalue=1, offvalue=0).grid(row=1, column=1)

        self.gizzu_int_var = tk.IntVar()
        self.gizzu_int_var.set(0)
        ttk.Checkbutton(self, text='Michał Guzik', variable=self.gizzu_int_var, onvalue=1, offvalue=0).grid(row=2, column=1)

        self.sylwek_k_int_var = tk.IntVar()
        self.sylwek_k_int_var.set(0)
        ttk.Checkbutton(self, text='Sylwek Kołda', variable=self.sylwek_k_int_var, onvalue=1, offvalue=0).grid(row=3, column=1)

        self.kamil_int_var = tk.IntVar()
        self.kamil_int_var.set(0)
        ttk.Checkbutton(self, text='Kamil Michalski', variable=self.kamil_int_var, onvalue=1, offvalue=0).grid(row=4, column=1)

        self.robert_z_int_var = tk.IntVar()
        self.robert_z_int_var.set(0)
        ttk.Checkbutton(self, text='Robert Zapała', variable=self.robert_z_int_var, onvalue=1, offvalue=0).grid(row=5, column=1)

        self.marcin_z_int_var = tk.IntVar()
        self.marcin_z_int_var.set(0)
        ttk.Checkbutton(self, text='Marcin Zapała', variable=self.marcin_z_int_var, onvalue=1, offvalue=0).grid(row=6, column=1)

        self.pawel_z_int_var = tk.IntVar()
        self.pawel_z_int_var.set(0)
        ttk.Checkbutton(self, text='Paweł Zapała', variable=self.pawel_z_int_var, onvalue=1, offvalue=0).grid(row=7, column=1)

        self.krzys_z_int_var = tk.IntVar()
        self.krzys_z_int_var.set(0)
        ttk.Checkbutton(self, text='Krzysztof Zapała', variable=self.krzys_z_int_var, onvalue=1, offvalue=0).grid(row=8, column=1)

        self.krzys_w_int_var = tk.IntVar()
        self.krzys_w_int_var.set(0)
        ttk.Checkbutton(self, text='Krzysztof Wesołowski', variable=self.krzys_w_int_var, onvalue=1, offvalue=0).grid(row=9,
                                                                                                                  column=1)
        self.tomek_int_var = tk.IntVar()
        self.tomek_int_var.set(0)
        ttk.Checkbutton(self, text='Tomek', variable=self.tomek_int_var, onvalue=1, offvalue=0).grid(
            row=10,
            column=1)

        self.marcin_j_int_var = tk.IntVar()
        self.marcin_j_int_var.set(0)
        ttk.Checkbutton(self, text='Marcin Janik', variable=self.marcin_j_int_var, onvalue=1, offvalue=0).grid(
            row=11,
            column=1)

        self.przemek_int_var = tk.IntVar()
        self.przemek_int_var.set(0)
        ttk.Checkbutton(self, text='Przemek', variable=self.przemek_int_var, onvalue=1, offvalue=0).grid(
            row=12,
            column=1)

        self.piotr_s_int_var = tk.IntVar()
        self.piotr_s_int_var.set(0)
        ttk.Checkbutton(self, text='Piotr Socha', variable=self.piotr_s_int_var, onvalue=1, offvalue=0).grid(
            row=13,
            column=1)

        self.albert_int_var = tk.IntVar()
        self.albert_int_var.set(0)
        ttk.Checkbutton(self, text='Albert', variable=self.albert_int_var, onvalue=1, offvalue=0).grid(
            row=14,
            column=1)

        self.sebastian_int_var = tk.IntVar()
        self.sebastian_int_var.set(0)
        ttk.Checkbutton(self, text='Sebastian', variable=self.sebastian_int_var, onvalue=1, offvalue=0).grid(
            row=15,
            column=1)

        self.grzegorz_s_int_var = tk.IntVar()
        self.grzegorz_s_int_var.set(0)
        ttk.Checkbutton(self, text='Grzegorz Sokolowski', variable=self.grzegorz_s_int_var, onvalue=1, offvalue=0).grid(
            row=16,
            column=1)

        self.zbyszek_staniec_int_var = tk.IntVar()
        self.zbyszek_staniec_int_var.set(0)
        ttk.Checkbutton(self, text='Zbyszek Staniec', variable=self.zbyszek_staniec_int_var, onvalue=1, offvalue=0).grid(
            row=17,
            column=1)

        self.zbychu_s_int_var = tk.IntVar()
        self.zbychu_s_int_var.set(0)
        ttk.Checkbutton(self, text='Zbychu Stefanski', variable=self.zbychu_s_int_var, onvalue=1, offvalue=0).grid(
            row=18,
            column=1)

        self.grzegorz_p_int_var = tk.IntVar()
        self.grzegorz_p_int_var.set(0)
        ttk.Checkbutton(self, text='Grzegorz Polanowski', variable=self.grzegorz_p_int_var, onvalue=1, offvalue=0).grid(
            row=19,
            column=1)

        self.jacek_s_p_int_var = tk.IntVar()
        self.jacek_s_p_int_var.set(0)
        ttk.Checkbutton(self, text='Jacek Salwa', variable=self.jacek_s_p_int_var, onvalue=1, offvalue=0).grid(
            row=20,
            column=1)

        self.zbyszek_l_int_var = tk.IntVar()
        self.zbyszek_l_int_var.set(0)
        ttk.Checkbutton(self, text='Zbyszek Lagner', variable=self.zbyszek_l_int_var, onvalue=1, offvalue=0).grid(
            row=21,
            column=1)

        self.marcin_s_int_var = tk.IntVar()
        self.marcin_s_int_var.set(0)
        ttk.Checkbutton(self, text='Marcin Stąpór', variable=self.marcin_s_int_var, onvalue=1, offvalue=0).grid(
            row=22,
            column=1)

        # marcin_s_int_var
        # zbyszek_l_int_var

        # save button
        self.save_button = ttk.Button(self, text='Losuj', command=self.losuj_i_pokaz_teamy)
        self.save_button.grid(row=2, column=3, padx=10)

        # self.e_black_list_dict = ttk.Entry(self, justify='right')
        # self.e_black_list_dict.insert(1, "Wieslaw:Piotr Socha.Michal Guzik:Marcin Zapała,Kamil")
        # self.e_black_list_dict.insert(1, "Wieslaw:Kamil,Piotr Socha.Michal Guzik:Marcin Zapała,Kamil")
        # self.e_black_list_dict.grid(row=3, column=3)

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