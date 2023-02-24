
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

    # ta metoda działa tak, że jak chcech z kimś zagrać to wybierz tak i losuje
    @staticmethod
    def choose_white_list(team1, team2, dict_black_list_pairs):
        # Check if any player in team1 cannot play with any player in team2
        team1 = [x.name for x in team1]
        team2 = [x.name for x in team2]
        for p1 in team1:
            for p2 in team2:
                print('kurek')
                kurek = dict_black_list_pairs.get(p2, [])
                if p1 in dict_black_list_pairs.get(p2, []):
                    print('mistake')
                    return False

        # Check if any player in team2 cannot play with any player in team1
        for p2 in team2:
            for p1 in team1:
                kurek = dict_black_list_pairs.get(p2, [])
                if p2 in dict_black_list_pairs.get(p1, []):
                    print('mistake')
                    return False

        # If no invalid pairs are found, return True
        return True

    @staticmethod
    def check_list_of_black_pairs3(team1, team2, dict_black_list_pairs):
        # Check if any player in team1 cannot play with any player in team2
        team1 = [x.name for x in team1]
        team2 = [x.name for x in team2]
        for p1 in team1:
            for p1_1 in team1:
                print('kurek')
                kurek = dict_black_list_pairs.get(p1_1, [])
                if p1 in dict_black_list_pairs.get(p1_1, []):
                    return False

        # Check if any player in team2 cannot play with any player in team1
        for p2 in team2:
            for p2_2 in team2:
                kurek = dict_black_list_pairs.get(p2_2, [])
                if p2 in dict_black_list_pairs.get(p2_2, []):
                    return False

        # If no invalid pairs are found, return True
        return True