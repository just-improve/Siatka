
class Model:
    def __init__(self):
        self.email = ''
        self.list_of_players = []
        self.list_of_players_int_var = []
        self.list_of_checked_players = []

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

    @property
    def get_name(self):
        return self.name



