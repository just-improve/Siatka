import pandas as pd
from model import Player


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def create_list_of_players(self):
        wj = Player('Wieslaw', 4,4,4,4,4,4, self.view.wj_int_var)
        self.model.list_of_players.append(wj)

        gizzu = Player('Gizzu', 4, 4, 4, 4, 4, 4, self.view.gizzu_int_var)
        self.model.list_of_players.append(gizzu)

        kamil = Player('Kamil', 4, 4, 4, 4, 4, 4, self.view.kamil_int_var)
        self.model.list_of_players.append(kamil)

        sylwek_kolda = Player('Sylwek Kołda', 4, 4, 4, 4, 4, 4, self.view.kolda_int_var)
        self.model.list_of_players.append(sylwek_kolda)


    # def create_lits_int_vars(self):
    #     self.model.list_of_players_int_var = [self.view.kamil_int_var, self.view.wj_int_var, self.view.gizzu_int_var, self.view.kolda_int_var]



