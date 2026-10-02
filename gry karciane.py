import pygame
import pygwidgets
import sys
import random

def rysuj_stos(numerstosu):
    stos = eval(f'stos{numerstosu}')
    x = -10 + numerstosu * 50
    if len(stos) > 0:
        stos[-1].obrocenie()
        for karta in stos:
            karta.rysuj(ekran, x, 50 + (stos.index(karta)-1)*20)

def rysuj_stos_odrzucony():
    x = 400
    if len(stos_odrzucony) > 0:
        stos_odrzucony[-1].obrocenie()
    for karta in stos_odrzucony:
        karta.rysuj(ekran, x, 50+(stos_odrzucony.index(karta)-1)*3)
 

def rysuj_stos_odrzucony2():
    x = 450
    for karta in stos_odrzucony2:
        karta.rysuj(ekran, x, 50+(stos_odrzucony2.index(karta)-1)*3)

def rysuj_stos_wzor(stos, x):
    if len(stos) > 0:
        stos[-1].rysuj(ekran, x, 50)
    



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

    def rysuj(self, ekran, x, y):
        self.prostokat.topleft = (x, y)
        ekran.blit(self.tyl if self.czyzakryta else self.obrazek, (x, y))

wybrana_karta = []
KARTY = []
CZARNY = (0, 0, 0)
SZEROKOSC = 800
WYSOKOSC = 600
KLATKI_NA_SEKUNDE = 60
WZORY = ['H', 'D', 'C', 'P']
WARTOSCI = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
stos_kiery = []
stos_karo = []
stos_trefle = []
stos_piki = []
stos_kiery2 = []
stos_karo2 = []
stos_trefle2 = []
stos_piki2 = []
for wzor in WZORY:
    for wartosc in WARTOSCI:
        KARTY.append(Karta(wzor, wartosc))
for karta in KARTY:
    if karta.wzor == "H":
        stos_kiery2.append(karta)
    elif karta.wzor == "D":
        stos_karo2.append(karta)
    elif karta.wzor == "C":
        stos_trefle2.append(karta)
    if karta.wzor == "P":
        stos_piki2.append(karta)
random.shuffle(KARTY)
stos1 = []
stos1.append(KARTY[0])
stos2 = []
stos2.append(KARTY[1])
stos2.append(KARTY[2])
stos3 = []
stos3.append(KARTY[3])
stos3.append(KARTY[4]) 
stos3.append(KARTY[5])
stos4 = []
stos4.append(KARTY[6])
stos4.append(KARTY[7])
stos4.append(KARTY[8])
stos4.append(KARTY[9])
stos5 = []
stos5.append(KARTY[10])
stos5.append(KARTY[11])
stos5.append(KARTY[12])
stos5.append(KARTY[13])
stos5.append(KARTY[14])
stos6 = []
stos6.append(KARTY[15])
stos6.append(KARTY[16])
stos6.append(KARTY[17])
stos6.append(KARTY[18])
stos6.append(KARTY[19])
stos6.append(KARTY[20])
stos7 = []
stos7.append(KARTY[21])
stos7.append(KARTY[22])
stos7.append(KARTY[23])
stos7.append(KARTY[24])
stos7.append(KARTY[25])
stos7.append(KARTY[26])
stos7.append(KARTY[27])
stos_odrzucony = KARTY[28:]
stos_odrzucony2 = []
wybrany_stos = []
    


pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Gry karciane")
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if len(stos_odrzucony) > 0:
                        karta = stos_odrzucony[-1]
                        stos_odrzucony.remove(karta)
                        stos_odrzucony2.append(karta)
                        karta.zakrycie()
                    else:
                        stos_odrzucony = stos_odrzucony2
                        stos_odrzucony2 = []
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for stos in [stos1, stos2, stos3, stos4, stos5, stos6, stos7, stos_odrzucony]:
                if len(stos) > 0:
                    karta = stos[-1]
                    if karta.prostokat.collidepoint(pygame.mouse.get_pos()):
                        if karta.wartosc == stos_piki2[0].wartosc and karta.wzor == "P":
                            stos_piki.append(karta)
                            stos_piki2.remove(karta)
                            stos.remove(karta)
                        elif karta.wartosc == stos_trefle2[0].wartosc and karta.wzor == "C":
                            stos_trefle.append(karta)
                            stos_trefle2.remove(karta)
                            stos.remove(karta)
                        elif karta.wartosc == stos_karo2[0].wartosc and karta.wzor == "D":
                            stos_karo.append(karta)
                            stos_karo2.remove(karta)
                            stos.remove(karta)
                        elif karta.wartosc == stos_kiery2[0].wartosc and karta.wzor == "H":
                            stos_kiery.append(karta)
                            stos_kiery2.remove(karta)
                            stos.remove(karta)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for stos in [stos1, stos2, stos3, stos4, stos5, stos6, stos7, stos_odrzucony, stos_karo, stos_kiery, stos_piki, stos_trefle]:
                if len(stos) > 0:
                    karta = stos[-1]
                    if karta.prostokat.collidepoint(pygame.mouse.get_pos()):
                        if wybrana_karta == []:
                            wybrana_karta.append(karta)
                            wybrany_stos = stos
                        else:
                            if ((wybrana_karta[0].wzor == "P" or wybrana_karta[0].wzor == "C") and (karta.wzor == "H" or karta.wzor == "D")) or ((wybrana_karta[0].wzor == "H" or wybrana_karta[0].wzor == "D") and (karta.wzor == "P" or karta.wzor == "C")):
                                if WARTOSCI.index(wybrana_karta[0].wartosc) == WARTOSCI.index(karta.wartosc) - 1:
                                    if stos != stos_odrzucony and stos != stos_piki and stos != stos_trefle and stos != stos_karo and stos != stos_kiery:
                                        stos.append(wybrana_karta[0])
                                        wybrany_stos.remove(wybrana_karta[0])
                                        wybrana_karta = []
                                    else:
                                        wybrana_karta = []
                                else:
                                    wybrana_karta = []
                            else:
                                wybrana_karta = []




    ekran.fill(CZARNY)
    clock.tick(KLATKI_NA_SEKUNDE)

    rysuj_stos(1)
    rysuj_stos(2)
    rysuj_stos(3)
    rysuj_stos(4)
    rysuj_stos(5)
    rysuj_stos(6)
    rysuj_stos(7)
    rysuj_stos_odrzucony()
    rysuj_stos_odrzucony2()
    rysuj_stos_wzor(stos_kiery, 500)
    rysuj_stos_wzor(stos_karo, 540)
    rysuj_stos_wzor(stos_trefle, 580)
    rysuj_stos_wzor(stos_piki, 620)

    pygame.display.update()
    



