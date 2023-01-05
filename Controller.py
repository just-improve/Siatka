import pandas as pd
from model import Player


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def creating_players_from_csv(self):
        siatkarze_dt = pd.read_csv('Siatka.csv')
        for x in siatkarze_dt.iterrows():
            player = Player()
            player.name = x[1][0]
            player.blok = x[1][1]
            player.atak = x[1][2]
            player.odbior = x[1][3]
            player.serwis = x[1][4]
            player.wystawa = x[1][5]
            player.sytuacyjne = x[1][6]
            player.suma = x[1][7]
            self.model.list_of_players.append(player)

    def open_new_window(self):
        for x in self.model.list_of_players:
            print(x.get_name)
            print(x.serwis)

    def choose_players(self):
        self.view.show_players_and_choose(self.model.list_of_players)

    def show_checked_players(self):
        self.view.show_checked_players(self.model.list_of_checked_players)




