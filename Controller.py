import pandas as pd
from model import Player
import random
from model import Player


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def create_list_of_players(self):

        wj = Player('Wieslaw', 450, self.view.wj_int_var)
        self.model.list_of_players.append(wj)

        gizzu = Player('Gizzu', 430, self.view.gizzu_int_var)
        self.model.list_of_players.append(gizzu)

        kamil = Player('Kamil', 320, self.view.kamil_int_var)
        self.model.list_of_players.append(kamil)

        sylwek_kolda = Player('Sylwek Kołda', 375, self.view.sylwek_k_int_var)
        self.model.list_of_players.append(sylwek_kolda)

        robert_zapala = Player('Robert Zapała', 405, self.view.robert_z_int_var)
        self.model.list_of_players.append(robert_zapala)

        marcin_zapala = Player('Marcin Zapała', 295, self.view.marcin_z_int_var)
        self.model.list_of_players.append(marcin_zapala)

        pawel_zapala = Player('Paweł Zapała', 328, self.view.pawel_z_int_var)
        self.model.list_of_players.append(pawel_zapala)

        krzysztof_zapala = Player('Krzysztof Zapała', 340, self.view.krzys_z_int_var)
        self.model.list_of_players.append(krzysztof_zapala)

        krzysztof_wesolowski = Player('Krzysztof Wesołowski', 310, self.view.krzys_w_int_var)
        self.model.list_of_players.append(krzysztof_wesolowski)

        tomek = Player('Tomek', 400, self.view.tomek_int_var)
        self.model.list_of_players.append(tomek)
########################################################################################################
        marcin_janik = Player('Marcin Janik', 413, self.view.marcin_j_int_var)
        self.model.list_of_players.append(marcin_janik)

        przemek = Player('Przemek', 455, self.view.przemek_int_var)
        self.model.list_of_players.append(przemek)

        piotr_socha = Player('Piotr Socha', 408, self.view.piotr_s_int_var)
        self.model.list_of_players.append(piotr_socha)

        albert = Player('Albert', 379, self.view.albert_int_var)
        self.model.list_of_players.append(albert)

        sebastian = Player('Sebastian', 359, self.view.sebastian_int_var)
        self.model.list_of_players.append(sebastian)

        grzegorz_sokolowski = Player('Grzegorz Sokolowski', 275, self.view.grzegorz_s_int_var)
        self.model.list_of_players.append(grzegorz_sokolowski)

        zbyszek_staniec = Player('Zbyszek Staniec', 325, self.view.zbyszek_staniec_int_var)
        self.model.list_of_players.append(zbyszek_staniec)

        zbychu_stefanski = Player('Zbychu Stefanski', 395, self.view.zbychu_s_int_var)
        self.model.list_of_players.append(zbychu_stefanski)

        grzegorz_polanowski = Player('Grzegorz Polanowski', 415, self.view.grzegorz_p_int_var)
        self.model.list_of_players.append(grzegorz_polanowski)

    def create_list_of_checked_players(self):
        for x in self.model.list_of_players:
            if x.int_var.get() == 1 and x not in self.model.list_of_checked_players:
                self.model.list_of_checked_players.append(x)

            if x.int_var.get() == 0:
                if x in self.model.list_of_checked_players:
                    self.model.list_of_checked_players.remove(x)

    def create_teams_from_checked_players(self):
        equal_teams = False
        team1 = []
        team2 = []
        while equal_teams is False:
            copy_li_players = self.model.list_of_checked_players.copy()
            team1.clear()
            team2.clear()
            first_team = True
            let_attemtp = True
            while let_attemtp is True:
                player = copy_li_players.pop(random.randrange(len(copy_li_players)))
                if first_team is True:
                    team1.append(player)
                    first_team = False
                elif first_team is False:
                    team2.append(player)
                    first_team = True

                if len(copy_li_players) == 0:

                    wes_mz1 = Player.check_wes_mz(team1)
                    wes_mz2 = Player.check_wes_mz(team2)
                    # print(wes_mz1)
                    # print(wes_mz2)

                    sum1, sum2 = Player.sum_teams(team1, team2)
                    if wes_mz1 is True or wes_mz2 is True:
                        equal_teams = False
                        let_attemtp = False
                        # print('Wesoly z marcinem ')

                    elif abs(sum1 - sum2) < self.model.allow_diff_amount:
                        equal_teams = True
                        let_attemtp = False
                        print('Składy są równe')
                    else:
                        equal_teams = False
                        let_attemtp = False
                        print('za duża różnica sił ' + str(abs(sum1 - sum2)))
        for x in team1:
            print(x.name)

        print('')
        for x in team2:
            print(x.name)
        self.model.team1 = team1
        self.model.team2 = team2

        self.model.team1_sum_skills, self.model.team2_sum_skills = Player.sum_teams(self.model.team1, self.model.team2)

    def change_teams_to_string(self):
        team1_as_str = ''
        team2_as_str = ''
        for x in self.model.team1:
            team1_as_str += x.name + '\n'

        for x in self.model.team2:
            team2_as_str += x.name + '\n'

        tream_joned_str = 'Team1 \n' + str(self.model.team1_sum_skills) + '\n' + team1_as_str + '\n'  + 'Team2 \n' + str(self.model.team2_sum_skills) + '\n' + team2_as_str
        # tream_joned_str = 'Team1 \n' + '\n' + team1_as_str + '\n'  + 'Team2 \n' + '\n' + team2_as_str

        return tream_joned_str

    def display_teams(self):
        teams_joned_str = self.change_teams_to_string()
        self.view.display_teams(teams_joned_str)









