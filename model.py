
class Model:
    def __init__(self):
        self.email = ''
        self.list_of_players = []
        self.list_of_checked_players = []
        self.team1 = []
        self.team2 = []

        self.team1_sum_skills = -1
        self.team2_sum_skills = -1

class Player:
    def __init__(self, name, blok, atak, odbior, serwis, wystawa, sytuacyjne, int_var):
        self.name = name
        self.blok = blok
        self.atak = atak
        self.odbior = odbior
        self.serwis = serwis
        self.wystawa = wystawa
        self.sytuacyjne = sytuacyjne
        self.int_var = int_var
        self.sum_of_skills = self.sum_skills()

    def sum_skills(self):
        sum_of_skills = self.blok + self.atak + self.odbior + self.serwis + self.wystawa + self.sytuacyjne
        return sum_of_skills

    @property
    def get_name(self):
        return self.name

    @staticmethod
    def sum_team_skills(team):
        sum_team = 0
        for x in team:
            sum_team += x.sum_of_skills
        return sum_team

    @staticmethod
    def sum_teams(team1, team2):
        sum1 = 0
        sum2 = 0
        for x in team1:
            sum1 += x.sum_of_skills
        for y in team2:
            sum2 += y.sum_of_skills
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



