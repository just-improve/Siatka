
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

class Player:
    def __init__(self, name, skills, int_var):
        self.name = name
        self.skills = skills
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



