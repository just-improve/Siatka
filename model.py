
class Model:
    def __init__(self):
        self.email = ''
        self.list_of_players = []
        self.list_of_checked_players = []

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

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
        self.int_var = -1

    @property
    def get_name(self):
        return self.name



