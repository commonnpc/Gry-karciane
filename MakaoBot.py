class MakaoBot():
    def __init__(self, ABC):
        self.ABC = ABC
        self.karty = []
        self.ruchy = True
        self.blok = 0

    def zmiana_koloru(self):
        self.kiery = 0
        self.karo = 0
        self.trefle = 0
        self.piki = 0
        for i in range(len(self.karty)):
            if self.karty[i].wzor == "H":
                self.kiery += 1
            elif self.karty[i].wzor == "D":
                self.karo += 1
            elif self.karty[i].wzor == "C":
                self.trefle += 1
            elif self.karty[i].wzor == "P":
                self.piki += 1
            if self.kiery >= self.karo and self.kiery >= self.trefle and self.kiery >= self.piki:
                return "H"
            elif self.karo >= self.trefle and self.karo >= self.piki:
                return "D"
            elif self.trefle >= self.piki:
                return "C"
            else:
                return "P"

    def rzadana(self):
        self.J5 = 0
        self.J6 = 0
        self.J7 = 0
        self.J8 = 0
        self.J9 = 0
        self.J10 = 0
        for i in range(len(self.karty)):
            if self.karty[i].wartosc == "5":
                self.J5 += 1
            elif self.karty[i].wartosc == "6":
                self.J6 += 1
            elif self.karty[i].wartosc == "7":
                self.J7 += 1
            elif self.karty[i].wartosc == "8":
                self.J8 += 1
            elif self.karty[i].wartosc == "9":
                self.J9 += 1
            elif self.karty[i].wartosc == "10":
                self.J10 += 1
        self.lJ = [self.J5, self.J6, self.J7, self.J8, self.J9, self.J10]
        self.lJ.sort()
        if self.lJ[-1] == self.J5:
            return "5", self.ABC
        elif self.lJ[-1] == self.J6:
            return "6", self.ABC
        elif self.lJ[-1] == self.J7:
            return "7", self.ABC
        elif self.lJ[-1] == self.J8:
            return "8", self.ABC
        elif self.lJ[-1] == self.J9:
            return "9", self.ABC
        elif self.lJ[-1] == self.J10:
            return "10", self.ABC