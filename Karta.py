import pygame

class Karta():
    def __init__(self, wzor, wartosc, czyzakryta=True):
        self.wzor = wzor
        self.wartosc = wartosc
        self.czyzakryta = czyzakryta
        self.obrazek = pygame.transform.smoothscale(pygame.image.load(f'karty/{wartosc}-{wzor}.png'), (40, 60))
        self.tyl = pygame.transform.smoothscale(pygame.image.load(f'karty/BACK.png'), (40, 60))
        self.prostokat = self.obrazek.get_rect()

    def obrocenie(self):
        self.czyzakryta = False

    def zakrycie(self):
        self.czyzakryta = True

    def rysuj(self, ekran, x, y, stan = None, WYBRANA = None, wybrane_karty = None, obrocenie = False):
        self.prostokat.topleft = (x, y)
        if obrocenie:
            ekran.blit(pygame.transform.rotate(self.tyl, 90) if self.czyzakryta else pygame.transform.rotate(self.obrazek, 90), (x, y))
        else:
            ekran.blit(self.tyl if self.czyzakryta else self.obrazek, (x, y))
        if stan == 'pasjans':
            if len(wybrane_karty) > 0:
                if wybrane_karty[0] == self:
                    ekran.blit(WYBRANA, (x, y))
