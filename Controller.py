import pandas as pd
from model import Player
import random
from model import Player


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def create_list_of_players(self):

        wj = Player('Wieslaw', 440, 184, self.view.wj_int_var)  #455
        self.model.list_of_players.append(wj)

        gizzu = Player('Michal', 420, 180, self.view.gizzu_int_var)
        self.model.list_of_players.append(gizzu)

        kamil = Player('Kamil', 375, 195, self.view.kamil_int_var)
        self.model.list_of_players.append(kamil)

        sylwek_kolda = Player('Sylwek', 400, 184, self.view.sylwek_k_int_var)
        self.model.list_of_players.append(sylwek_kolda)

        robert_zapala = Player('Robert', 420, 187, self.view.robert_z_int_var)
        self.model.list_of_players.append(robert_zapala)

        marcin_zapala = Player('Marcin Z', 320, 180, self.view.marcin_z_int_var)
        self.model.list_of_players.append(marcin_zapala)

        pawel_zapala = Player('Pawel', 410, 180, self.view.pawel_z_int_var)
        self.model.list_of_players.append(pawel_zapala)

        krzysztof_zapala = Player('Krzysztof Z', 345, 180, self.view.krzys_z_int_var)
        self.model.list_of_players.append(krzysztof_zapala)

        krzysztof_wesolowski = Player('Krzysztof W', 320, 177, self.view.krzys_w_int_var)
        self.model.list_of_players.append(krzysztof_wesolowski)

        tomek = Player('Tomek', 380, 174, self.view.tomek_int_var)
        self.model.list_of_players.append(tomek)
########################################################################################################
        marcin_janik = Player('Marcin J', 400, 181, self.view.marcin_j_int_var)
        self.model.list_of_players.append(marcin_janik)

        przemek = Player('Przemek', 430, 175, self.view.przemek_int_var)
        self.model.list_of_players.append(przemek)

        piotr_socha = Player('Piotr', 430, 178, self.view.piotr_s_int_var)
        self.model.list_of_players.append(piotr_socha)

        albert = Player('Albert', 400, 180, self.view.albert_int_var)
        self.model.list_of_players.append(albert)

        sebastian = Player('Sebastian', 380, 180, self.view.sebastian_int_var)
        self.model.list_of_players.append(sebastian)

        grzegorz_sokolowski = Player('Grzes S', 320, 167, self.view.grzegorz_s_int_var)
        self.model.list_of_players.append(grzegorz_sokolowski)

        zbyszek_staniec = Player('Zbyszek S', 340, 173, self.view.zbyszek_staniec_int_var)
        self.model.list_of_players.append(zbyszek_staniec)

        zbychu_stefanski = Player('Zbychu S', 395, 180, self.view.zbychu_s_int_var)
        self.model.list_of_players.append(zbychu_stefanski)

        grzegorz_polanowski = Player('Polan', 370, 180, self.view.grzegorz_p_int_var)
        self.model.list_of_players.append(grzegorz_polanowski)

        jacek_salwa = Player('Jacek', 320, 178, self.view.jacek_s_p_int_var)
        self.model.list_of_players.append(jacek_salwa)

        zbyszek_lagner = Player('Zbyszek L', 390, 180, self.view.zbyszek_l_int_var)
        self.model.list_of_players.append(zbyszek_lagner)

        marcin_stapor = Player('Marcin S', 480, 184, self.view.marcin_s_int_var)
        self.model.list_of_players.append(marcin_stapor)

        adam = Player('Adam', 350, 179, self.view.adam_int_var)
        self.model.list_of_players.append(adam)

        michal_w = Player('Michal W', 390, 176, self.view.michal_w_int_var)
        self.model.list_of_players.append(michal_w)

        robert_p = Player('Robert P', 420, 183, self.view.robert_p_w_int_var)
        self.model.list_of_players.append(robert_p)

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

                    sum1, sum2 = Player.sum_teams(team1, team2)
                    black_list_dict = self.convert_entry_string_to_dict(self.view.e_black_list_dict.get())  #self.view.e_black_list_dict.get()
                    white_list_dict = self.convert_entry_string_to_dict(self.view.e_white_list_dict.get())

                    let_play = Player.check_list_of_black_pairs3(team1, team2, black_list_dict)

                    if let_play is False:
                        equal_teams = False
                        let_attemtp = False
                        continue

                    let_play = Player.choose_white_list(team1, team2, white_list_dict)

                    if let_play is False:
                        equal_teams = False
                        let_attemtp = False
                        continue
                        # print(' mam Kamila nie losujemy dalej')

                    elif abs(sum1 - sum2) < int(self.view.e_allow_value.get()):  #self.model.allow_diff_amount:
                        equal_teams = True
                        let_attemtp = False
                        print('Składy są równe')
                    else:
                        equal_teams = False
                        let_attemtp = False
                        print('za duża różnica sił ' + str(abs(sum1 - sum2)))

        self.model.team1 = team1
        self.model.team2 = team2

        self.model.team1_sum_skills, self.model.team2_sum_skills = Player.sum_teams(self.model.team1, self.model.team2)
        self.model.team1_sum_height, self.model.team2_sum_height = Player.sum_height(self.model.team1, self.model.team2)

    def change_teams_to_string(self):
        team1_as_str = ''
        team2_as_str = ''
        for x in self.model.team1:
            team1_as_str += x.name + '\n'

        for x in self.model.team2:
            team2_as_str += x.name + '\n'

        tream_joned_str = 'Team1 \n' + str(self.model.team1_sum_skills) + '\n' + 'wzrost '+str(self.model.team1_sum_height) + '\n' + '\n'+ team1_as_str + '\n'+ '\n'  + 'Team2 \n' + str(self.model.team2_sum_skills) + '\n' + 'wzrost '+str(self.model.team2_sum_height) + '\n'+ '\n' + team2_as_str
        return tream_joned_str

    def display_teams(self):
        teams_joned_str = self.change_teams_to_string()
        self.view.display_teams(teams_joned_str)

    def convert_entry_string_to_dict(self, my_string):
        my_dict = {}
        for item in my_string.split("."):
            key, values = item.split(":")
            if "," in values:
                values = values.split(",")
            my_dict[key] = values
        my_dict = self.change_single_str_dict_value_to_list(my_dict)
        return my_dict

    def get_amount_of_checked_players(self):
        self.create_list_of_checked_players()
        len_check_players = str(len(self.model.list_of_checked_players))
        checked_players_list = ''
        count = 0
        for x in self.model.list_of_checked_players:
            if count < 1:
                checked_players_list += '   '+x.name
                count += 1
            else:
                checked_players_list += '   '+x.name + '\n'
                count = 0

        return len_check_players, checked_players_list

    def change_single_str_dict_value_to_list(self, dict_to_modify):
        new_dict = {}
        # new_dict = {k: [v] for k, v in dict_to_modify.items()}

        for k, v in dict_to_modify.items():
            if isinstance(v, str):
                new_dict[k]= [v]
            else:
                new_dict[k] = v

        return new_dict

