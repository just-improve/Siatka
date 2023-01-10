import pandas as pd
from model import Player
import random
from model import Player


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def create_list_of_players(self):

        wj = Player('Wieslaw', 9, 9, 9, 9, 9, 9, self.view.wj_int_var)
        self.model.list_of_players.append(wj)

        gizzu = Player('Gizzu', 8, 8, 8, 8, 8, 8, self.view.gizzu_int_var)
        self.model.list_of_players.append(gizzu)

        kamil = Player('Kamil', 4, 4, 4, 4, 4, 4, self.view.kamil_int_var)
        self.model.list_of_players.append(kamil)

        sylwek_kolda = Player('Sylwek Kołda', 6, 6, 6, 6, 6, 6, self.view.sylwek_k_int_var)
        self.model.list_of_players.append(sylwek_kolda)

        robert_zapala = Player('Robert Zapała', 6, 6, 6, 6, 6, 6, self.view.robert_z_int_var)
        self.model.list_of_players.append(robert_zapala)

        marcin_zapala = Player('Marcin Zapała', 6, 6, 6, 6, 6, 6, self.view.marcin_z_int_var)
        self.model.list_of_players.append(marcin_zapala)

        pawel_zapala = Player('Paweł Zapała', 6, 6, 6, 6, 6, 6, self.view.pawel_z_int_var)
        self.model.list_of_players.append(pawel_zapala)

        krzysztof_zapala = Player('Krzysztof Zapała', 6, 6, 6, 6, 6, 6, self.view.krzys_z_int_var)
        self.model.list_of_players.append(krzysztof_zapala)

        krzysztof_wesolowski = Player('Krzysztof Wesołowski', 6, 6, 6, 6, 6, 6, self.view.krzys_w_int_var)
        self.model.list_of_players.append(krzysztof_wesolowski)

        tomek = Player('Tomek', 6, 6, 6, 6, 6, 6, self.view.tomek_int_var)
        self.model.list_of_players.append(tomek)


    def create_list_of_checked_players(self):
        for x in self.model.list_of_players:
            if x.int_var.get() == 1 and x not in self.model.list_of_checked_players:
                self.model.list_of_checked_players.append(x)

            if x.int_var.get() == 0:
                if x in self.model.list_of_checked_players:
                    self.model.list_of_checked_players.remove(x)

        # for y in self.model.list_of_checked_players:
        #     print(y.name)

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

                    sum1, sum2 = Player.sum_teams(team1, team2)
                    print(sum1)
                    print(sum2)
                    if abs(sum1 - sum2) < 30:
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

        self.model.team1_sum_skills = Player.sum_team_skills(self.model.team1)
        self.model.team2_sum_skills = Player.sum_team_skills(self.model.team2)


    def display_teams(self):
        teams_joned_str = self.change_teams_to_string()
        self.view.display_teams(teams_joned_str)

    def change_teams_to_string(self):
        team1_as_str = ''
        team2_as_str = ''
        for x in self.model.team1:
            team1_as_str += x.name + '\n'

        for x in self.model.team2:
            team2_as_str += x.name + '\n'

        tream_joned_str = 'Team1 \n' + str(self.model.team1_sum_skills) + '\n' + team1_as_str + '\n'  + 'Team2 \n' + str(self.model.team2_sum_skills) + '\n' + team2_as_str

        return tream_joned_str






