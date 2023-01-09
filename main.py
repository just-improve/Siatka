import random

import pandas as pd

class Player:
    def __init__(self):
        self.name = ''
        self.blok = 0
        self.atak = 0
        self.odbior = 0
        self.serwis = 0
        self.wystawa = 0
        self.sytuacyjne = 0
        self.suma = 0

    @staticmethod
    def sum_lis(team1, team2):
        sum1 = 0
        sum2 = 0
        for x in team1:
            sum1+= x.suma
        for y in team2:
            sum2+=y.suma
        return sum1, sum2

if __name__ == '__main__':
    list_of_players = []
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
        list_of_players.append(player)

    equal_teams = False
    let_attemtp = True
    team1 = []
    team2 = []
    while equal_teams is False:
        copy_li_players = list_of_players.copy()
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

                sum1, sum2 = Player.sum_lis(team1, team2)
                print(sum1)
                print(sum2)
                if abs(sum1-sum2) < 30:
                    equal_teams = True
                    let_attemtp = False
                    print('Składy są równe')
                else:
                    equal_teams = False
                    let_attemtp = False
                    print('za duża różnica sił ' + str(abs(sum1-sum2)))

                # print(f'suma 1 '{sum1} 'sum2'+{sum2})


    print('')
    for x in team1:
        print(x.name)
    print('')
    print('Koniec')
    print('')

    for x in team2:
        print(x.name)

