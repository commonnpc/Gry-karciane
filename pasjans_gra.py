import pygame
import sys
import random
import zmienne_wspólne

def rysuj_stos(numerstosu):
    stos = eval(f'stos{numerstosu}')
    x = -10 + numerstosu * 50
    if len(stos) > 0:
        stos[-1].obrocenie()
        for karta in stos:
            karta.rysuj(zmienne_wspólne.ekran, x, 50 + (stos.index(karta)-1)*20)

def rysuj_stos_odrzucony():
    x = 400
    if len(stos_odrzucony) > 0:
        stos_odrzucony[-1].obrocenie()
    for karta in stos_odrzucony:
        karta.rysuj(zmienne_wspólne.ekran, x, 50+(stos_odrzucony.index(karta)-1)*3)
 
def rysuj_stos_odrzucony2():
    x = 450
    for karta in stos_odrzucony2:
        karta.rysuj(zmienne_wspólne.ekran, x, 50+(stos_odrzucony2.index(karta)-1)*3)

def rysuj_stos_wzor(stos, x):
    if len(stos) > 0:
        stos[-1].rysuj(zmienne_wspólne.ekran, x, 50)


def czy_mozna_przeniesc_na_stos_wzor(karta, stos_wzor):
    if len(stos_wzor) == 0:
        return karta.wartosc == 'A'

    ostatnia_karta = stos_wzor[-1]
    return (
        karta.wzor == ostatnia_karta.wzor and
        WARTOSCI.index(karta.wartosc) == WARTOSCI.index(ostatnia_karta.wartosc) + 1
    )

def czy_mozna_przeniesc_na_stos_tabeli(karta, stos_docelowy):
    if len(stos_docelowy) == 0:
        return karta.wartosc == 'K'

    ostatnia_karta = stos_docelowy[-1]
    czy_rozny_kolor = (
        (karta.wzor in ['H', 'D'] and ostatnia_karta.wzor in ['C', 'P']) or
        (karta.wzor in ['C', 'P'] and ostatnia_karta.wzor in ['H', 'D'])
    )
    return czy_rozny_kolor and WARTOSCI.index(karta.wartosc) == WARTOSCI.index(ostatnia_karta.wartosc) - 1

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
        if len(wybrane_karty) > 0:
            if wybrane_karty[0] == self:
                ekran.blit(WYBRANA, (x, y))

def pasjans():
    global WYBRANA, KARTY, WZORY, WARTOSCI, stos_kiery, stos_karo, stos_trefle, stos_piki, ekran, stos_odrzucony, stos_odrzucony2, wybrane_karty, stos1, stos2, stos3, stos4, stos5, stos6, stos7
    WYBRANA = pygame.transform.smoothscale(pygame.image.load(f'WYBRANA.png'), (40, 60))
    KARTY = []
    WZORY = ['H', 'D', 'C', 'P']
    WARTOSCI = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    stos_kiery = []
    stos_karo = []
    stos_trefle = []
    stos_piki = []
    for wzor in WZORY:
        for wartosc in WARTOSCI:
            KARTY.append(Karta(wzor, wartosc))
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
    wybrane_karty = []

    pygame.init()
    pygame.display.set_caption("Gry karciane")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        if len(stos_odrzucony) > 0:
                            karta = stos_odrzucony[-1]
                            stos_odrzucony.remove(karta)
                            stos_odrzucony2.append(karta)
                            karta.zakrycie()
                        else:
                            for x in stos_odrzucony2:
                                stos_odrzucony2.append(stos_odrzucony[0])
                                stos_odrzucony.pop[0]
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                wybrane_karty = []
                wybrany_stos = []
                for stos in [stos1, stos2, stos3, stos4, stos5, stos6, stos7, stos_odrzucony]:
                    if len(stos) > 0:
                        karta = stos[-1]
                        if karta.prostokat.collidepoint(pygame.mouse.get_pos()):
                            for stos_wzor, wzor in [(stos_piki, 'P'), (stos_trefle, 'C'), (stos_karo, 'D'), (stos_kiery, 'H')]:
                                if karta.wzor == wzor and czy_mozna_przeniesc_na_stos_wzor(karta, stos_wzor):
                                    stos_wzor.append(karta)
                                    stos.remove(karta)
                                    break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pozycja_myszy = pygame.mouse.get_pos()
                stosy_tabeli = [stos1, stos2, stos3, stos4, stos5, stos6, stos7]

                if not wybrane_karty:
                    stosy_zrodlowe = stosy_tabeli + [
                        stos_odrzucony, stos_karo, stos_kiery, stos_piki, stos_trefle
                    ]
                    for stos in stosy_zrodlowe:
                        if not stos:
                            continue

                        indeksy = range(len(stos) - 1, -1, -1)
                        for indeks in indeksy:
                            karta = stos[indeks]
                            if karta.czyzakryta or not karta.prostokat.collidepoint(pozycja_myszy):
                                continue

                            if any(stos is stos_specjalny for stos_specjalny in (
                                stos_odrzucony, stos_karo, stos_kiery, stos_piki, stos_trefle
                            )):
                                if karta != stos[-1]:
                                    continue
                                wybrane_karty = [karta]
                            else:
                                wybrane_karty = stos[indeks:]
                            wybrany_stos = stos
                            break

                        if wybrane_karty:
                            break
                else:
                    stos_docelowy = None
                    x_myszy, y_myszy = pozycja_myszy
                    for numer, stos in enumerate(stosy_tabeli, start=1):
                        if stos is wybrany_stos:
                            continue
                        if stos:
                            if stos[-1].prostokat.collidepoint(pozycja_myszy):
                                stos_docelowy = stos
                                break
                        else:
                            x_stosu = -10 + numer * 50
                            if x_stosu <= x_myszy <= x_stosu + 40 and 30 <= y_myszy <= 90:
                                stos_docelowy = stos
                                break

                    if stos_docelowy is not None and czy_mozna_przeniesc_na_stos_tabeli(wybrane_karty[0], stos_docelowy):
                        stos_docelowy.extend(wybrane_karty)
                        for karta in wybrane_karty:
                            wybrany_stos.remove(karta)

                        if any(wybrany_stos is stos for stos in stosy_tabeli) and wybrany_stos and wybrany_stos[-1].czyzakryta:
                            wybrany_stos[-1].obrocenie()
                        elif wybrany_stos is stos_odrzucony and wybrany_stos:
                            wybrany_stos[-1].obrocenie()

                    wybrane_karty = []
                    wybrany_stos = []

        zmienne_wspólne.ekran.fill(zmienne_wspólne.TLO)
        zmienne_wspólne.clock.tick(zmienne_wspólne.KLATKI_NA_SEKUNDE)

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

        if len(stos_kiery) + len(stos_karo) + len(stos_trefle) + len(stos_piki) == len(KARTY):
            print("Gratulacje!")
            sys.exit()