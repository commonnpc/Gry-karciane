import pygame
import pygwidgets
import sys
import random

stos1 = []
stos2 = []
stos3 = []
stos4 = []
stos5 = []
stos6 = []
stos7 = []
KARTY = []
CZARNY = (0, 0, 0)
SZEROKOSC = 800
WYSOKOSC = 600
KLATKI_NA_SEKUNDE = 60
WZORY = ['H', 'D', 'C', 'P']
WARTOSCI = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
KARTY = random.sample(KARTY, len(KARTY))

def p():
    stos1 = []
    stos1.append(KARTY[0])
    stos1[-1].obrocenie()
    for karta in stos1:
        karta.rysuj(ekran, 40, (stos1.index(karta)-1)*20+50)
    stos2 = []
    stos2.append(KARTY[1])
    stos2.append(KARTY[2])
    stos2[-1].obrocenie()
    for karta in stos2:
        karta.rysuj(ekran, 90, (stos2.index(karta)-1)*20+50)
    stos3 = []
    stos3.append(KARTY[3])
    stos3.append(KARTY[4]) 
    stos3.append(KARTY[5])
    stos3[-1].obrocenie()
    for karta in stos3:
        karta.rysuj(ekran, 140, (stos3.index(karta)-1)*20+50)
    stos4 = []
    stos4.append(KARTY[6])
    stos4.append(KARTY[7])
    stos4.append(KARTY[8])
    stos4.append(KARTY[9])
    stos4[-1].obrocenie()
    for karta in stos4:
        karta.rysuj(ekran, 190, (stos4.index(karta)-1)*20+50)
    stos5 = []
    stos5.append(KARTY[10])
    stos5.append(KARTY[11])
    stos5.append(KARTY[12])
    stos5.append(KARTY[13])
    stos5.append(KARTY[14])
    stos5[-1].obrocenie()
    for karta in stos5:
        karta.rysuj(ekran, 240, (stos5.index(karta)-1)*20+50)
    stos6 = []
    stos6.append(KARTY[15])
    stos6.append(KARTY[16])
    stos6.append(KARTY[17])
    stos6.append(KARTY[18])
    stos6.append(KARTY[19])
    stos6.append(KARTY[20])
    stos6[-1].obrocenie()
    for karta in stos6:
        karta.rysuj(ekran, 290, (stos6.index(karta)-1)*20+50)
    stos7 = []
    stos7.append(KARTY[21])
    stos7.append(KARTY[22])
    stos7.append(KARTY[23])
    stos7.append(KARTY[24])
    stos7.append(KARTY[25])
    stos7.append(KARTY[26])
    stos7.append(KARTY[27])
    stos7[-1].obrocenie()
    for karta in stos7:
        karta.rysuj(ekran, 340, (stos7.index(karta)-1)*20+50)







def pasjans():
    stos1 = []
    stos2 = []
    stos3 = []
    stos4 = []
    stos5 = []
    stos6 = []
    stos7 = []
    for stos in range(1, 8):
        for kartynastosie in range(stos):
            eval(f"stos{stos}").append(KARTY[stos-kartynastosie])
            if kartynastosie == stos-1:
                eval(f"stos{stos}")[kartynastosie].obrocenie()
            Karta.rysuj(eval(f"stos{stos}")[kartynastosie], ekran, 50+(stos-1)*40, 50+kartynastosie*20)


class Karta():
    def __init__(self, wzor, wartosc, zakrycie=True):
        self.wzor = wzor
        self.wartosc = wartosc
        self.zakrycie = zakrycie
        self.obrazek = pygame.transform.smoothscale(pygame.image.load(f'karty/{wartosc}-{wzor}.png'), (40, 60))
        self.tyl = pygame.transform.smoothscale(pygame.image.load(f'karty/BACK.png'), (40, 60))
        self.prostokat = self.obrazek.get_rect()
    def obrocenie(self):
        self.zakrycie = False

    def rysuj(self, ekran, x, y):
        ekran.blit(self.tyl if self.zakrycie else self.obrazek, (x, y))

for wzor in WZORY:
    for wartosc in WARTOSCI:
        KARTY.append(Karta(wzor, wartosc))
pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Gry karciane")
clock = pygame.time.Clock()

KARTY = random.sample(KARTY, len(KARTY))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ekran.fill(CZARNY)
    clock.tick(KLATKI_NA_SEKUNDE)
    p()
    pygame.display.update()
    




