import random
import pygwidgets
import pygame
import sys

stan = "menu"
TLO = (178, 227, 146)
SZEROKOSC = 800
WYSOKOSC = 600
KLATKI_NA_SEKUNDE = 60
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load("Chickens in the Meadow.ogg")
pygame.mixer.music.play(-1)
kartydzwiek = pygame.mixer.Sound("card_draw_3.wav")
kartydzwiek.set_volume(0.5)
wygranadzwiek = pygame.mixer.Sound("match_xylophone_6.wav")
wygranadzwiek.set_volume(0.7)

Przycisk_Wroc_Pasjans = pygwidgets.TextButton(ekran, (500, 450), "Wróc do menu gier",
                                        fontSize = 30, width = 200, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Od_Nowa_Pasjans = pygwidgets.TextButton(ekran, (100, 450), "Spróbuj ponownie",
                                        fontSize = 30, width = 200, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Wroc_Z_Menu_Gier = pygwidgets.TextButton(ekran, (275 ,450), "Wróć do menu głównego",
                                          fontSize = 30, width = 250, height = 100, 
                                          upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Pasjans = pygwidgets.TextButton(ekran, (100,100), "Pasjans",
                                          fontSize = 30, width = 250, height = 100, 
                                          upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Graj = pygwidgets.TextButton(ekran, (200, 190), "Graj",
                                          fontSize = 30, width = 400, height = 100, 
                                          upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Opcje = pygwidgets.TextButton(ekran, (200, 320), "Opcje",
                                        fontSize = 30, width = 400, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Wyjscie = pygwidgets.TextButton(ekran, (200, 450), "Wyjście",
                                        fontSize = 30, width = 400, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Tekst_Tytul = pygwidgets.DisplayText(ekran, (200, 50), "Gry Karciane", 
                                     fontSize = 90, width = 400, height = 100)

Przycisk_Zasady = pygwidgets.TextButton(ekran, (200, 150), "Zasady",
                                        fontSize = 30, width = 400, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Wroc = pygwidgets.TextButton(ekran, (200, 300), "Wróć",
                                        fontSize = 30, width = 400, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Autorzy = pygwidgets.TextButton(ekran, (200, 450), "Autorzy",
                                        fontSize = 30, width = 400, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Kwadracik_Tryb_Ciemny = pygwidgets.TextCheckBox(ekran, (200, 80), "Tryb ciemny", value = False, fontSize = 60, size = 50)

Przycisk_Wroc_Do_Menu_Z_Grami = pygwidgets.TextButton(ekran, (100, 450), "Wróć do menu z grami",
                                                        fontSize = 30, width = 200, height = 100, 
                                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Zagraj_Ponownie_Pasjans = pygwidgets.TextButton(ekran, (500, 450), "Zagraj ponownie",
                                                        fontSize = 30, width = 200, height = 100, 
                                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Tekst_Pasjans_Ponownie = pygwidgets.DisplayText(ekran, (200, 80), "Gratulacje wygranej!", 
                                     fontSize = 30, width = 400, height = 100)
                                                        
Tekst_Zasady1 = pygwidgets.DisplayText(ekran, (50, 80), "Aby przenieść kartę na drugi stos naciśnij ją prawym przyciskiem myszy, po czym", fontSize = 25, width = 700, height = 400)
Tekst_Zasady2 = pygwidgets.DisplayText(ekran, (50, 110), "tym samym przyciskiem naciśnij stos na który chcesz go przełożyć. Jezeli chcesz tą ", fontSize = 25, width = 700, height = 400)
Tekst_Zasady3 = pygwidgets.DisplayText(ekran, (50, 140), "kartę przełożyć na stosy znaków naciśnij ją lewym przyciskiem myszy. Aby przełozyć ", fontSize = 25, width = 700, height = 400)
Tekst_Zasady4 = pygwidgets.DisplayText(ekran, (50, 170), "kartę ze stosu kart niewykorzystanych, naciśnij klawisz spacja.", fontSize = 25, width = 700, height = 400)

Tekst_Autorzy1 = pygwidgets.DisplayText(ekran, (50, 80), "Gra - Bartosz Kujawa", fontSize = 25, width = 700, height = 400)
Tekst_Autorzy2 = pygwidgets.DisplayText(ekran, (50, 110), "Efekty Muzyczne - pakiet 400 Sounds Pack", fontSize = 25, width = 700, height = 400)
Tekst_Autorzy3 = pygwidgets.DisplayText(ekran, (50, 140), "Muzyka - pakiet Cozy Tunes", fontSize = 25, width = 700, height = 400)
Tekst_Autorzy4 = pygwidgets.DisplayText(ekran, (50, 170), "Grafika - pakiet Pixel Poker Cards", fontSize = 25, width = 700, height = 400)

Przycisk_Wroc_Z_Autorow = pygwidgets.TextButton(ekran, (200, 450), "Wróć",
                                                        fontSize = 30, width = 400, height = 100, 
                                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Zasady_Wroc = pygwidgets.TextButton(ekran, (200, 300), "Wróć",
                                        fontSize = 30, width = 400, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))
przyciski_autorzy = []
przyciski_pasjans_ponownie = []
przyciski_gry = []
przyciski_menu = []
przyciski_opcje = []
przyciski_zasady = []
pygame.init()
pygame.display.set_caption("Zbiór gier")
przyciski_pasjans_ponownie.append(Przycisk_Zagraj_Ponownie_Pasjans)
przyciski_pasjans_ponownie.append(Przycisk_Wroc_Do_Menu_Z_Grami)
przyciski_gry.append(Przycisk_Wroc_Z_Menu_Gier)
przyciski_gry.append(Przycisk_Pasjans)
przyciski_menu.append(Przycisk_Graj)
przyciski_menu.append(Przycisk_Opcje)
przyciski_menu.append(Przycisk_Wyjscie)
przyciski_opcje.append(Przycisk_Zasady)
przyciski_opcje.append(Przycisk_Wroc)
przyciski_opcje.append(Przycisk_Autorzy)
przyciski_zasady.append(Przycisk_Zasady_Wroc)
przyciski_autorzy.append(Przycisk_Wroc_Z_Autorow)

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

def pasjans_ponownie():
    global program
    program = False
    pasjans()

def pasjans():
    global stan, TLO
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
    przyciski = []
    przyciski.append(Przycisk_Od_Nowa_Pasjans)
    przyciski.append(Przycisk_Wroc_Pasjans)
    program = True

    pygame.init()
    pygame.display.set_caption("Gry karciane")
    while program:
        for event in pygame.event.get():
            for przycisk in przyciski:
                if przycisk.handleEvent(event):
                    if przycisk == przyciski[0]:
                        pasjans_ponownie()
                    if przycisk == przyciski[1]:
                        stan = "gry"
                        widzet()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if len(stos_odrzucony) > 0:
                    kartydzwiek.play()
                    karta = stos_odrzucony[-1]
                    stos_odrzucony.remove(karta)
                    stos_odrzucony2.append(karta)
                    karta.zakrycie()
                else:
                    kartydzwiek.play()
                    for i in range (stos_odrzucony2):
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
                                    kartydzwiek.play()
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
                        kartydzwiek.play()
                        stos_docelowy.extend(wybrane_karty)
                        for karta in wybrane_karty:
                            wybrany_stos.remove(karta)
                        if any(wybrany_stos is stos for stos in stosy_tabeli) and wybrany_stos and wybrany_stos[-1].czyzakryta:
                            wybrany_stos[-1].obrocenie()
                        elif wybrany_stos is stos_odrzucony and wybrany_stos:
                            wybrany_stos[-1].obrocenie()
                    wybrane_karty = []
                    wybrany_stos = []
        ekran.fill(TLO)
        clock.tick(KLATKI_NA_SEKUNDE)
        for przycisk in przyciski:
            przycisk.show()
            przycisk.draw()
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
            stan = "zagrajznowuwpasjans"
            widzet()
            wygranadzwiek.play()
def widzet():
    global stan, TLO
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if stan == "menu":
                for przycisk in przyciski_menu:
                    if przycisk.handleEvent(event):
                        if przycisk == przyciski_menu[0]:
                            stan = "gry"
                        elif przycisk == przyciski_menu[1]:
                            stan = "opcje"
                        elif przycisk == przyciski_menu[2]:
                            pygame.quit()
                            sys.exit()
            elif stan == "gry":
                for przycisk in przyciski_gry:
                    if przycisk.handleEvent(event):
                        if przycisk == przyciski_gry[0]:
                            stan = "menu"
                        elif przycisk == przyciski_gry[1]:
                            pasjans()
            elif stan == "opcje":
                for przycisk in przyciski_opcje:
                    if przycisk.handleEvent(event):
                        if przycisk == przyciski_opcje[0]:
                            stan = "zasady"
                        elif przycisk == przyciski_opcje[1]:
                            stan = "menu"
                        elif przycisk == przyciski_opcje[2]:
                            stan = "autorzy"
                    if Kwadracik_Tryb_Ciemny.handleEvent(event):
                        if Kwadracik_Tryb_Ciemny.value == True:
                            TLO = (49, 61, 41)
                        else:
                            TLO = (178, 227, 146)
            elif stan == "zagrajznowuwpasjans":
                for przycisk in przyciski_pasjans_ponownie:
                    if przycisk.handleEvent(event):
                        if przycisk == przyciski_pasjans_ponownie[0]:
                            pasjans()
                        elif przycisk == przyciski_pasjans_ponownie[1]:
                            stan = "gry"
            elif stan == "zasady":
                for przycisk in przyciski_zasady:
                    if przycisk.handleEvent(event):
                        if przycisk == przyciski_zasady[0]:
                            stan = "menu"
            elif stan == "autorzy":
                for przycisk in przyciski_autorzy:
                    if przycisk.handleEvent(event):
                        if przycisk == przyciski_autorzy[0]:
                            stan = "menu"
        ekran.fill(TLO)
        if stan == "menu":
            for przycisk in przyciski_menu:
                przycisk.show()
                przycisk.draw()
            Tekst_Tytul.show()
            Tekst_Tytul.draw()
        else:
            for przycisk in przyciski_menu:
                przycisk.hide()
            Tekst_Tytul.hide()

        if stan == "gry":
            for przycisk in przyciski_gry:
                przycisk.show()
                przycisk.draw()
        else:
            for przycisk in przyciski_gry:
                przycisk.hide()

        if stan == "opcje":
            for przycisk in przyciski_opcje:
                przycisk.show()
                przycisk.draw()
            Kwadracik_Tryb_Ciemny.show()
            Kwadracik_Tryb_Ciemny.draw()
        else:
            for przycisk in przyciski_opcje:
                przycisk.hide()
            Kwadracik_Tryb_Ciemny.hide()

        if stan == "zagrajznowuwpasjans":
            for przycisk in przyciski_pasjans_ponownie:
                przycisk.show()
                przycisk.draw()
            Tekst_Pasjans_Ponownie.show()
            Tekst_Pasjans_Ponownie.draw()
        else:
            for przycisk in przyciski_pasjans_ponownie:
                przycisk.hide()
            Tekst_Pasjans_Ponownie.hide()

        if stan == "zasady":
            for przycisk in przyciski_zasady:
                przycisk.show()
                przycisk.draw()
            Tekst_Zasady1.show()
            Tekst_Zasady1.draw()
            Tekst_Zasady2.show()
            Tekst_Zasady2.draw()
            Tekst_Zasady3.show()
            Tekst_Zasady3.draw()
            Tekst_Zasady4.show()
            Tekst_Zasady4.draw()
        else:
            for przycisk in przyciski_zasady:
                przycisk.hide()
            Tekst_Zasady1.hide()
            Tekst_Zasady2.hide()
            Tekst_Zasady3.hide()
            Tekst_Zasady4.hide()

        if stan == "autorzy":
            for przycisk in przyciski_autorzy:
                przycisk.show()
                przycisk.draw()
            Tekst_Autorzy1.show()
            Tekst_Autorzy1.draw()
            Tekst_Autorzy2.show()
            Tekst_Autorzy2.draw()
            Tekst_Autorzy3.show()
            Tekst_Autorzy3.draw()
            Tekst_Autorzy4.show()
            Tekst_Autorzy4.draw()
        else:
            for przycisk in przyciski_autorzy:
                przycisk.hide()
            Tekst_Autorzy1.hide()
            Tekst_Autorzy2.hide()
            Tekst_Autorzy3.hide()
            Tekst_Autorzy4.hide()
        pygame.display.update()
        clock.tick(KLATKI_NA_SEKUNDE)
widzet()