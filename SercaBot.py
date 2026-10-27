class SercaBot():
    def __init__(self, ABC):
        self.ABC = ABC
        self.karty = []
        self.symbole = {"H" : 0, "D" : 0, "C" : 0, "P" : 0}

    def lsymboli(self):
        for karta in self.karty:
            self.symbole[karta.wzor] +=1