
class Model:
    def __init__(self):
        # self.email = ''
        self.allow_diff_amount = 30
        self.list_of_players = []
        self.list_of_checked_players = []
        self.team1 = []
        self.team2 = []

        self.team1_sum_skills = -1
        self.team2_sum_skills = -1

        self.team1_sum_height = -1
        self.team2_sum_height = -1


class Player:
    def __init__(self, name, skills, height, int_var):
        self.name = name
        self.skills = skills
        self.height = height
        self.int_var = int_var



    @property
    def get_name(self):
        return self.name

    @staticmethod
    def sum_teams(team1, team2):
        sum1 = 0
        sum2 = 0
        for x in team1:
            sum1 += x.skills
        for y in team2:
            sum2 += y.skills
        return sum1, sum2

    @staticmethod
    def sum_height(team1, team2):
        sum_height_1 = 0
        sum_height_2 = 0
        for x in team1:
            sum_height_1 += x.height
        for y in team2:
            sum_height_2 += y.height
        return sum_height_1, sum_height_2

    # jeśli byśmy chcieli żeby ktoś się nie losował z kimś to wtedy do tej metody trzeba wstawić liste par zawodników którzy mają nie grać ze sobą
    # byłaby to lista tupli
    @staticmethod
    def check_wes_mz(team):
        mz = False
        wes = False
        both_play = False
        for x in team:
            if x.name == 'Krzysztof Wesołowski':
                wes = True
            elif x.name == 'Marcin Zapała':
                mz = True

        if mz is True and wes is True:
            both_play = True
        return both_play

    @staticmethod
    def check_list_of_black_pairs(team ,team2, dict_black_list_pairs):
        black_player_in_team = False
        value_player_in_team = False
        black_player_in_team2 = False
        value_player_in_team2 = False

        team = [x.name for x in team]
        team2 = [x.name for x in team2]

        for value, items in dict_black_list_pairs.items():

            print(f'\n {value} value player +\n')

            if value in team:
                value_player_in_team = True
            if value in team2:
                value_player_in_team2 = True

            for black_player in items:
                print(black_player)
                if black_player in team:
                    black_player_in_team = True
                    if value_player_in_team is black_player_in_team:
                        return False
                if black_player in team2:
                    black_player_in_team2 = True
                    if value_player_in_team2 is black_player_in_team2:
                        return False

            if value_player_in_team is black_player_in_team:
                return False

            if value_player_in_team2 is black_player_in_team2:
                return False

            print(team)
            print(f'{value_player_in_team} value player in team')
            print(f'{black_player_in_team} black player in team')
        return True