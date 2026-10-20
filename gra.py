import random
import pygwidgets
import pygame
import sys
import time
import emoji

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
        if stan == 'pasjans':
            if len(wybrane_karty) > 0:
                if wybrane_karty[0] == self:
                    ekran.blit(WYBRANA, (x, y))

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
WYBRANA = pygame.transform.smoothscale(pygame.image.load(f'WYBRANA.png'), (40, 60))
KARTY = []
WZORY = ['H', 'D', 'C', 'P']
WARTOSCI = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
for wzor in WZORY:
    for wartosc in WARTOSCI:
        KARTY.append(Karta(wzor, wartosc))
KARTY_9_I_WYZEJ = []
for karta in KARTY:
    if karta.wartosc in ["9", "10", "J", "Q", "K", "A"]:
        KARTY_9_I_WYZEJ.append(karta)
Przycisk_Wroc_Gra = pygwidgets.TextButton(ekran, (500, 450), "Wróc do menu gier",
                                        fontSize = 30, width = 200, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Od_Nowa_Gra = pygwidgets.TextButton(ekran, (100, 450), "Spróbuj ponownie",
                                        fontSize = 30, width = 200, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Wroc_Z_Menu_Gier = pygwidgets.TextButton(ekran, (275 ,450), "Wróć do menu głównego",
                                          fontSize = 30, width = 250, height = 100, 
                                          upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Pasjans = pygwidgets.TextButton(ekran, (100,100), "Pasjans",
                                          fontSize = 30, width = 250, height = 100, 
                                          upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Oczko = pygwidgets.TextButton(ekran, (450,100), "Oczko",
                                          fontSize = 30, width = 250, height = 100, 
                                          upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Makao = pygwidgets.TextButton(ekran, (100,250), "Makao",
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

Przycisk_Wroc_Do_Menu_Z_Grami = pygwidgets.TextButton(ekran, (50, 450), "Wróć do menu z grami",
                                                        fontSize = 30, width = 300, height = 100, 
                                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Zagraj_Ponownie = pygwidgets.TextButton(ekran, (450, 450), "Zagraj ponownie",
                                                        fontSize = 30, width = 300, height = 100, 
                                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Tekst_Pasjans_Ponownie = pygwidgets.DisplayText(ekran, (200, 80), "Gratulacje wygranej!", 
                                     fontSize = 30, width = 400, height = 100)
                                                        
Tekst_ZasadyPasjans1 = pygwidgets.DisplayText(ekran, (50, 80), "Aby przenieść kartę na drugi stos naciśnij ją prawym przyciskiem myszy, po czym", fontSize = 25, width = 700, height = 400)
Tekst_ZasadyPasjans2 = pygwidgets.DisplayText(ekran, (50, 110), "tym samym przyciskiem naciśnij stos na który chcesz go przełożyć. Jezeli chcesz tą ", fontSize = 25, width = 700, height = 400)
Tekst_ZasadyPasjans3 = pygwidgets.DisplayText(ekran, (50, 140), "kartę przełożyć na stosy znaków naciśnij ją lewym przyciskiem myszy. Aby przełozyć ", fontSize = 25, width = 700, height = 400)
Tekst_ZasadyPasjans4 = pygwidgets.DisplayText(ekran, (50, 170), "kartę ze stosu kart niewykorzystanych, naciśnij klawisz spacja.", fontSize = 25, width = 700, height = 400)

Tekst_ZasadyOczko1 = pygwidgets.DisplayText(ekran, (50, 80), "Aby pobrać kartę, naciśnij lewy przycisk myszy, a żeby zakończyć turę naciśnij prawy", fontSize = 25, width = 700, height = 400)
Tekst_ZasadyOczko2 = pygwidgets.DisplayText(ekran, (50, 110), "przycisk myszy. Twoja tura kończy się automatycznie jezeli przebijesz 21 punktów.", fontSize = 25, width = 700, height = 400)
Tekst_ZasadyOczko3 = pygwidgets.DisplayText(ekran, (50, 140), "Dla sprawiedliwości bot nie zna twoich kart i nie wpływają one na jego decyzje.", fontSize = 25, width = 700, height = 400)

Tekst_Autorzy1 = pygwidgets.DisplayText(ekran, (50, 80), "Gra - Bartosz Kujawa", fontSize = 25, width = 700, height = 400)
Tekst_Autorzy2 = pygwidgets.DisplayText(ekran, (50, 110), "Efekty Muzyczne - pakiet 400 Sounds Pack", fontSize = 25, width = 700, height = 400)
Tekst_Autorzy3 = pygwidgets.DisplayText(ekran, (50, 140), "Muzyka - pakiet Cozy Tunes", fontSize = 25, width = 700, height = 400)
Tekst_Autorzy4 = pygwidgets.DisplayText(ekran, (50, 170), "Grafika - pakiet Pixel Poker Cards", fontSize = 25, width = 700, height = 400)

Przycisk_Wroc_Z_Autorow = pygwidgets.TextButton(ekran, (200, 450), "Wróć",
                                                        fontSize = 30, width = 400, height = 100, 
                                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Zasady_Wroc = pygwidgets.TextButton(ekran, (200, 450), "Wróć",
                                        fontSize = 30, width = 400, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Zasady_Pasjans = pygwidgets.TextButton(ekran, (150, 100), "Zasady pasjansa", fontSize = 30, 
                                        width = 200, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Zasady_Oczko = pygwidgets.TextButton(ekran, (450, 100), "Zasady oczka", fontSize = 30, 
                                              width = 200, height = 100, 
                                            upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Tekst_Oczko_Ponownie = pygwidgets.DisplayText(ekran, (200, 80), "#", fontSize = 30, width = 400, height = 100)
Tekst_Makao_Ponownie = pygwidgets.DisplayText(ekran, (200, 80), "#", fontSize = 30, width = 500, height = 100)

przyciski_autorzy = []
przyciski_koniec_ponownie = []
przyciski_gry = []
przyciski_menu = []
przyciski_opcje = []
przyciski_zasady = []
pygame.init()
pygame.display.set_caption("Zbiór gier")
przyciski_koniec_ponownie.append(Przycisk_Zagraj_Ponownie)
przyciski_koniec_ponownie.append(Przycisk_Wroc_Do_Menu_Z_Grami)
przyciski_gry.append(Przycisk_Wroc_Z_Menu_Gier)
przyciski_gry.append(Przycisk_Oczko)
przyciski_gry.append(Przycisk_Pasjans)
przyciski_gry.append(Przycisk_Makao)
przyciski_menu.append(Przycisk_Graj)
przyciski_menu.append(Przycisk_Opcje)
przyciski_menu.append(Przycisk_Wyjscie)
przyciski_opcje.append(Przycisk_Zasady)
przyciski_opcje.append(Przycisk_Wroc)
przyciski_opcje.append(Przycisk_Autorzy)
przyciski_zasady.append(Przycisk_Zasady_Wroc)
przyciski_zasady.append(Przycisk_Zasady_Pasjans)
przyciski_zasady.append(Przycisk_Zasady_Oczko)
przyciski_autorzy.append(Przycisk_Wroc_Z_Autorow)
przyciski = []
przyciski.append(Przycisk_Od_Nowa_Gra)
przyciski.append(Przycisk_Wroc_Gra)

def koniecoczko(wynik):
    global stan
    if wynik == "wygrana":
        stan = "wygranaoczko"
        wygranadzwiek.play()
    elif wynik == "remis":
        stan = "remisoczko"
    if wynik == "przegrana":
        stan = "przegranaoczko"
    widzet()

def makao():
    kartaS = 0
    t = 1
    pA = False
    dobrana = None
    global stan, program
    Tekst_Kolor = pygwidgets.DisplayText(ekran, (50, 20), " Wybrany kolor: #", fontSize = 20)
    przycisk_koniec_tury = pygwidgets.TextButton(ekran, (50, 250), "Zakończ turę",
                                                fontSize = 30, width = 200, height = 100, 
                                                upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))
    przycisk_ponownie = pygwidgets.TextButton(ekran, (550, 175), "Zagraj ponownie",
                                            fontSize = 30, width = 200, height = 100, 
                                            upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))
    przycisk_powrot = pygwidgets.TextButton(ekran, (550, 325), "Powrót do menu",
                                            fontSize = 30, width = 200, height = 100, 
                                            upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

    przycisk_kier = pygwidgets.TextButton(ekran, (50, 375), "kier",
                                          fontSize = 40, width = 90, height = 50, 
                                          upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))
    przycisk_karo = pygwidgets.TextButton(ekran, (160, 375), "karo",
                                        fontSize = 40, width = 90, height = 50, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))
    przycisk_trefl = pygwidgets.TextButton(ekran, (50, 450), "trefl",
                                        fontSize = 40, width = 90, height = 50, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))
    przycisk_pik = pygwidgets.TextButton(ekran, (160, 450), "pik",
                                        fontSize = 40, width = 90, height = 50, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))
        
    przyciski_makao = [przycisk_koniec_tury, przycisk_ponownie, przycisk_powrot]
    przyciski_A = [przycisk_kier, przycisk_karo, przycisk_trefl, przycisk_pik]

    stos_dobieranie = KARTY.copy()
    random.shuffle(stos_dobieranie)
    pygame.init
    pygame.display.set_caption("MAKAO")
    twoje_karty = []
    karty_bota = []
    for i in range(len(stos_dobieranie)):
        if stos_dobieranie[i].wartosc in ["5", "6", "7", "8", "9", "10"]:
            stos_kladzenia = [stos_dobieranie[i]]
            stos_dobieranie.pop(i)
            break
    for i in range(5):
        twoje_karty.append(stos_dobieranie[0])
        stos_dobieranie.remove(stos_dobieranie[0])
        karty_bota.append(stos_dobieranie[0])
        stos_dobieranie.remove(stos_dobieranie[0])
    program = True
    ruchyT = True
    ruchyB = True
    kolej = "T"
    kolorA = ""
    kiery_bota = 0
    karo_bota = 0
    trefle_bota = 0
    piki_bota = 0
    while program:
        ekran.fill(TLO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if kolej == "T":
                for karta in twoje_karty:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if stos_dobieranie[0].prostokat.collidepoint(pygame.mouse.get_pos()) and ruchyT and not pA:
                            twoje_karty.append(stos_dobieranie[0])
                            stos_dobieranie.pop(0)
                            ruchyT = False
                            dobrana = twoje_karty[-1]
                            dt = t
                        if dobrana != None and not pA:
                            if dobrana.prostokat.collidepoint(pygame.mouse.get_pos()) and dt != t:
                                if kolorA == "":
                                    if dobrana.wzor == stos_kladzenia[-1].wzor or dobrana.wartosc == stos_kladzenia[-1].wartosc:
                                        if dobrana.wartosc == "A":
                                            pA = True
                                        stos_kladzenia.append(twoje_karty[-1])
                                        twoje_karty.pop(-1)
                                        kartaS = stos_kladzenia[-1].wartosc
                                        dobrana = None
                                else:
                                    if dobrana.wzor == kolorA or dobrana.wartosc == stos_kladzenia[-1].wartosc:
                                        if dobrana.wartosc == "A":
                                            pA = True
                                        else:
                                            kolorA = ""
                                        stos_kladzenia.append(twoje_karty[-1])
                                        twoje_karty.pop(-1)
                                        kartaS = stos_kladzenia[-1].wartosc
                                        dobrana = None
                        if kolorA == "" :
                            if karta.prostokat.collidepoint(pygame.mouse.get_pos()) and (karta.wzor == stos_kladzenia[-1].wzor or karta.wartosc == stos_kladzenia[-1].wartosc) and not pA:
                                if ruchyT:
                                    if karta.wartosc == "A":
                                        pA = True
                                    stos_kladzenia.append(karta)
                                    twoje_karty.remove(karta)
                                    ruchyT = False
                                    kartaS = karta.wartosc
                                elif karta.wartosc == kartaS:
                                    if karta.wartosc == "A":
                                        pA = True
                                    stos_kladzenia.append(karta)
                                    twoje_karty.remove(karta)
                        else:
                            if karta.prostokat.collidepoint(pygame.mouse.get_pos()) and (karta.wzor == kolorA or karta.wartosc == stos_kladzenia[-1].wartosc) and not pA:
                                if ruchyT:
                                    if karta.wartosc == "A":
                                        pA = True
                                    else:
                                        kolorA = ""
                                    stos_kladzenia.append(karta)
                                    twoje_karty.remove(karta)
                                    ruchyT = False
                                    kartaS = karta.wartosc
                                elif karta.wartosc == kartaS:
                                    if karta.wartosc == "A":
                                        pA = True
                                    else:
                                        kolorA = ""
                                    stos_kladzenia.append(karta)
                                    twoje_karty.remove(karta)
            for przycisk in przyciski_makao:
                if przycisk.handleEvent(event):
                    if przycisk == przyciski_makao[0] and kolej == "T" and not pA:
                        if not ruchyT:
                            kolej = "B"
                            dobrana = None
                            ruchyB = True
                            kartaS = 0
                    elif przycisk == przyciski_makao[1]:
                        gra_ponownie("makao")
                    elif przycisk == przyciski_makao[2]:
                        stan = "gry"
                        widzet()
            if pA:
                for przycisk in przyciski_A:
                    if przycisk.handleEvent(event):
                        if przycisk == przyciski_A[0]:
                            kolorA = "H"
                        elif przycisk == przyciski_A[1]:
                            kolorA = "D"
                        elif przycisk == przyciski_A[2]:
                            kolorA = "C"
                        elif przycisk == przyciski_A[3]:
                            kolorA = "P"
                        pA = False
        if kolej == "B":
            for karta in karty_bota:
                if kolorA == "":
                    if karta.wzor == stos_kladzenia[-1].wzor or karta.wartosc == stos_kladzenia[-1].wartosc:
                        if ruchyB:
                            if karta.wartosc == "A":
                                for i in range(len(karty_bota)):
                                    if karty_bota[i].wzor == "H":
                                        kiery_bota += 1
                                    elif karty_bota[i].wzor == "D":
                                        karo_bota += 1
                                    elif karty_bota[i].wzor == "C":
                                        trefle_bota += 1
                                    elif karty_bota[i].wzor == "P":
                                        piki_bota += 1
                                if kiery_bota >= karo_bota and kiery_bota >= trefle_bota and kiery_bota >= piki_bota:
                                    kolorA = "H"
                                elif karo_bota >= trefle_bota and karo_bota >= piki_bota:
                                    kolorA = "D"
                                elif trefle_bota >= piki_bota:
                                    kolorA = "C"
                                else:
                                    kolorA = "P"
                                kiery_bota = 0
                                karo_bota = 0
                                trefle_bota = 0
                                piki_bota = 0
                            stos_kladzenia.append(karta)
                            karty_bota.remove(karta)
                            ruchyB = False
                        elif karta.wartosc == kartaS:
                            if karta.wartosc == "A":
                                for i in range(len(karty_bota)):
                                    if karty_bota[i].wzor == "H":
                                        kiery_bota += 1
                                    elif karty_bota[i].wzor == "D":
                                        karo_bota += 1
                                    elif karty_bota[i].wzor == "C":
                                        trefle_bota += 1
                                    elif karty_bota[i].wzor == "P":
                                        piki_bota += 1
                                if kiery_bota >= karo_bota and kiery_bota >= trefle_bota and kiery_bota >= piki_bota:
                                    kolorA = "H"
                                elif karo_bota >= trefle_bota and karo_bota >= piki_bota:
                                    kolorA = "D"
                                elif trefle_bota >= piki_bota:
                                    kolorA = "C"
                                else:
                                    kolorA = "P"
                                kiery_bota = 0
                                karo_bota = 0
                                trefle_bota = 0
                                piki_bota = 0
                            stos_kladzenia.append(karta)
                            karty_bota.remove(karta)
                else:
                    if karta.wzor == kolorA or karta.wartosc == stos_kladzenia[-1].wartosc:
                        if ruchyB:
                            if karta.wartosc == "A":
                                for i in range(len(karty_bota)):
                                    if karty_bota[i].wzor == "H":
                                        kiery_bota += 1
                                    elif karty_bota[i].wzor == "D":
                                        karo_bota += 1
                                    elif karty_bota[i].wzor == "C":
                                        trefle_bota += 1
                                    elif karty_bota[i].wzor == "P":
                                        piki_bota += 1
                                if kiery_bota >= karo_bota and kiery_bota >= trefle_bota and kiery_bota >= piki_bota:
                                    kolorA = "H"
                                elif karo_bota >= trefle_bota and karo_bota >= piki_bota:
                                    kolorA = "D"
                                elif trefle_bota >= piki_bota:
                                    kolorA = "C"
                                else:
                                    kolorA = "P"
                                kiery_bota = 0
                                karo_bota = 0
                                trefle_bota = 0
                                piki_bota = 0
                            stos_kladzenia.append(karta)
                            karty_bota.remove(karta)
                            ruchyB = False
                        elif karta.wartosc == kartaS:
                            if karta.wartosc == "A":
                                for i in range(len(karty_bota)):
                                    if karty_bota[i].wzor == "H":
                                        kiery_bota += 1
                                    elif karty_bota[i].wzor == "D":
                                        karo_bota += 1
                                    elif karty_bota[i].wzor == "C":
                                        trefle_bota += 1
                                    elif karty_bota[i].wzor == "P":
                                        piki_bota += 1
                                if kiery_bota >= karo_bota and kiery_bota >= trefle_bota and kiery_bota >= piki_bota:
                                    kolorA = "H"
                                elif karo_bota >= trefle_bota and karo_bota >= piki_bota:
                                    kolorA = "D"
                                elif trefle_bota >= piki_bota:
                                    kolorA = "C"
                                else:
                                    kolorA = "P"
                                kiery_bota = 0
                                karo_bota = 0
                                trefle_bota = 0
                                piki_bota = 0
                            time.sleep(1)
                            stos_kladzenia.append(karta)
                            karty_bota.remove(karta)
            if ruchyB:
                karty_bota.append(stos_dobieranie[0])
                stos_dobieranie.pop(0)
                ruchyB = False
                if kolorA == "":
                    if karty_bota[-1].wzor == stos_kladzenia[-1].wzor or karty_bota[-1].wartosc == stos_kladzenia[-1].wartosc:
                        if karty_bota[-1].wartosc == "A":
                            for i in range(len(karty_bota)):
                                if karty_bota[i].wzor == "H":
                                    kiery_bota += 1
                                elif karty_bota[i].wzor == "D":
                                    karo_bota += 1
                                elif karty_bota[i].wzor == "C":
                                    trefle_bota += 1
                                elif karty_bota[i].wzor == "P":
                                    piki_bota += 1
                            if kiery_bota >= karo_bota and kiery_bota >= trefle_bota and kiery_bota >= piki_bota:
                                kolorA = "H"
                            elif karo_bota >= trefle_bota and karo_bota >= piki_bota:
                                kolorA = "D"
                            elif trefle_bota >= piki_bota:
                                kolorA = "C"
                            else:
                                kolorA = "P"
                            kiery_bota = 0
                            karo_bota = 0
                            trefle_bota = 0
                            piki_bota = 0
                        stos_kladzenia.append(karta)
                        karty_bota.remove(karta)
                else:
                    if karty_bota[-1].wzor == kolorA or karty_bota[-1].wartosc == stos_kladzenia[-1].wartosc:
                        if karty_bota[-1].wartosc == "A":
                            for i in range(len(karty_bota)):
                                if karty_bota[i].wzor == "H":
                                    kiery_bota += 1
                                elif karty_bota[i].wzor == "D":
                                    karo_bota += 1
                                elif karty_bota[i].wzor == "C":
                                    trefle_bota += 1
                                elif karty_bota[i].wzor == "P":
                                    piki_bota += 1
                            if kiery_bota >= karo_bota and kiery_bota >= trefle_bota and kiery_bota >= piki_bota:
                                kolorA = "H"
                            elif karo_bota >= trefle_bota and karo_bota >= piki_bota:
                                kolorA = "D"
                            elif trefle_bota >= piki_bota:
                                kolorA = "C"
                            else:
                                kolorA = "P"
                            kiery_bota = 0
                            karo_bota = 0
                            trefle_bota = 0
                            piki_bota = 0
                        stos_kladzenia.append(karta)
                        karty_bota.remove(karta)
            kartaS = 0
            kolej = "T"
            ruchyT = True
        if len(stos_dobieranie) > 0:
            stos_dobieranie[0].zakrycie()
            stos_dobieranie[0].rysuj(ekran, 350, 270)
        else:
            stos_dobieranie = stos_kladzenia.copy()
            stos_kladzenia.append(stos_dobieranie[-1])
            stos_dobieranie.pop(-1)
        if kolorA != "":
            if kolorA == "H":
                Tekst_Kolor = pygwidgets.DisplayText(ekran, (50, 20), " Wybrany kolor: KIER", fontSize = 20)
            elif kolorA == "D":
                Tekst_Kolor = pygwidgets.DisplayText(ekran, (50, 20), " Wybrany kolor: KARO", fontSize = 20)
            elif kolorA == "C":
                Tekst_Kolor = pygwidgets.DisplayText(ekran, (50, 20), " Wybrany kolor: TREFLE", fontSize = 20)
            elif kolorA == "P":
                Tekst_Kolor = pygwidgets.DisplayText(ekran, (50, 20), " Wybrany kolor: PIKI", fontSize = 20)
            Tekst_Kolor.show()
            Tekst_Kolor.draw()
        else:
            Tekst_Kolor.hide()
        for przycisk in przyciski_A:
            if pA:
                przycisk.show()
                przycisk.draw()
            else:
                przycisk.hide()
        for przycisk in przyciski_makao:
            przycisk.show()
            przycisk.draw()
        for karta in twoje_karty:
            karta.obrocenie()
            karta.rysuj(ekran, 380 + 60*(len(twoje_karty)/2- twoje_karty.index(karta)), 500)
        for karta in karty_bota:
            karta.zakrycie()
            karta.rysuj(ekran, 380 + 60*(len(karty_bota)/2- karty_bota.index(karta)), 100)
        if len(twoje_karty) == 0:
            stan = "wygranamakao"
            widzet()
        elif len(karty_bota) == 0:
            stan = "przegranamakao"
            widzet()
        stos_kladzenia[-1].obrocenie()
        stos_kladzenia[-1].rysuj(ekran, 410, 270)
        pygame.display.update()
        t  = 100 - t
        clock.tick(KLATKI_NA_SEKUNDE)

def oczko():
    Tekst_Przebito = pygwidgets.DisplayText(ekran, (50, 10), "PRZEBITO!" , fontSize = 20)
    Tekst_Przebito_Bota = pygwidgets.DisplayText(ekran, (690, 10), "PRZEBITO!" , fontSize = 20)
    global stan, program
    koniec = False
    koniecB = False
    random.shuffle(KARTY_9_I_WYZEJ)
    pula_kart = KARTY_9_I_WYZEJ.copy()
    pula_twoich_kart = []
    pula_kart_bota = []
    pula_punktow = 0
    pula_punktow_bota = 0
    pygame.init()
    pygame.display.set_caption("OCZKO") 
    program = True
    while program:
        for event in pygame.event.get():
            for przycisk in przyciski:
                if przycisk.handleEvent(event):
                    if przycisk == przyciski[0]:
                        gra_ponownie("oczko")
                    if przycisk == przyciski[1]:
                        stan = "gry"
                        widzet()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not koniec:
                pula_twoich_kart.append(pula_kart[0])
                if pula_kart[0].wartosc == "A":
                    pula_punktow += 11
                elif pula_kart[0].wartosc == "K":
                    pula_punktow += 4
                elif pula_kart[0].wartosc == "Q":
                    pula_punktow += 3
                elif pula_kart[0].wartosc == "J":
                    pula_punktow += 2
                elif pula_kart[0].wartosc == "10":
                    pula_punktow += 10
                elif pula_kart[0].wartosc == "9":
                    pass
                pula_kart.remove(pula_kart[0])
                if pula_punktow > 21:
                    koniec = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and not koniec:
                koniec = True
        if koniec and not koniecB:
            lb = 0
            for i in [2, 3, 4, 9, 10, 11]:
                if i + pula_punktow_bota < 22:
                    lb += 1
            time.sleep(1)
            if random.randrange(0, 6) < lb:
                pula_kart_bota.append(pula_kart[0])
                if pula_kart[0].wartosc == "A":
                    pula_punktow_bota += 11
                elif pula_kart[0].wartosc == "K":
                    pula_punktow_bota += 4
                elif pula_kart[0].wartosc == "Q":
                    pula_punktow_bota += 3
                elif pula_kart[0].wartosc == "J":
                    pula_punktow_bota += 2
                elif pula_kart[0].wartosc == "10":
                    pula_punktow_bota += 10
                elif pula_kart[0].wartosc == "9":
                    pass
                pula_kart.remove(pula_kart[0])
            else:
                koniecB = True
        if koniec and koniecB:
            if pula_punktow_bota == pula_punktow or (pula_punktow_bota > 21 and pula_punktow > 21):
                koniecoczko("remis")
            elif (pula_punktow < 22 and pula_punktow > pula_punktow_bota) or pula_punktow_bota > 21:
                koniecoczko("wygrana")
            else:
                koniecoczko("przegrana")
            program = False
        ekran.fill(TLO)
        clock.tick(KLATKI_NA_SEKUNDE)
        for przycisk in przyciski:
            przycisk.show()
            przycisk.draw()
        if pula_punktow > 21:
            Tekst_Przebito.show()
            Tekst_Przebito.draw()
        else:
            Tekst_Przebito.hide()
        if pula_punktow_bota > 21:
            Tekst_Przebito_Bota.show()
            Tekst_Przebito_Bota.draw()
        else:
            Tekst_Przebito_Bota.hide()
        Tekst_Punkty = pygwidgets.DisplayText(ekran, (50, 20), "Punkty: " + str(pula_punktow), fontSize = 20)
        Tekst_Punkty_Bota = pygwidgets.DisplayText(ekran, (690, 20), "Punkty bota: " + str(pula_punktow_bota), fontSize = 20)
        Tekst_Punkty.show()
        Tekst_Punkty_Bota.show()
        Tekst_Punkty.draw()
        Tekst_Punkty_Bota.draw()
        for karta in pula_twoich_kart:
            ekran.blit(karta.obrazek, (60, 40 + pula_twoich_kart.index(karta)*60))
        for karta in pula_kart_bota:
            ekran.blit(karta.obrazek, (700, 40 + pula_kart_bota.index(karta)*60))
        pygame.display.update()

            
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


def gra_ponownie(gra):
    global program
    program = False
    if gra == "pasjans":
        pasjans()
    elif gra == "oczko":
        oczko()
    elif gra == "makao":
        makao()

def pasjans():
    global stan, TLO
    global stos_kiery, stos_karo, stos_trefle, stos_piki, ekran, stos_odrzucony, stos_odrzucony2, wybrane_karty, stos1, stos2, stos3, stos4, stos5, stos6, stos7
    stos_kiery = []
    stos_karo = []
    stos_trefle = []
    stos_piki = []
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
    program = True

    pygame.init()
    pygame.display.set_caption("PASJANS")
    while program:
        for event in pygame.event.get():
            for przycisk in przyciski:
                if przycisk.handleEvent(event):
                    if przycisk == przyciski[0]:
                        gra_ponownie("pasjans")
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
                    for i in range(len(stos_odrzucony2)):
                        stos_odrzucony2.append(stos_odrzucony[0])
                        stos_odrzucony.pop(0)
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
    global stan, TLO, Tekst_Oczko_Ponownie, Tekst_Makao_Ponownie
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
                            stan = "pasjans"
                            pasjans()
                        elif przycisk == przyciski_gry[2]:
                            oczko()
                        elif przycisk == przyciski_gry[3]:
                            makao()
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
                for przycisk in przyciski_koniec_ponownie:
                    if przycisk.handleEvent(event):
                        if przycisk == przyciski_koniec_ponownie[0]:
                            pasjans()
                        elif przycisk == przyciski_koniec_ponownie[1]:
                            stan = "gry"
            elif stan == "zasady":
                for przycisk in przyciski_zasady:
                    if przycisk.handleEvent(event):
                        if przycisk == przyciski_zasady[0]:
                            stan = "menu"
                        elif przycisk == przyciski_zasady[1]:
                            stan = "zasadypasjans"
                        elif przycisk == przyciski_zasady[2]:
                            stan = "zasadyoczko"
            elif stan == "zasadypasjans" or stan == "zasadyoczko":
                if Przycisk_Zasady_Wroc.handleEvent(event):
                    stan = "zasady"
            elif stan == "autorzy":
                for przycisk in przyciski_autorzy:
                    if przycisk.handleEvent(event):
                        if przycisk == przyciski_autorzy[0]:
                            stan = "menu"
            elif stan == "wygranaoczko" or stan == "przegranaoczko" or stan == "remisoczko":
                for przycisk in przyciski_koniec_ponownie:
                    if przycisk.handleEvent(event):
                        if przycisk == przyciski_koniec_ponownie[0]:
                            oczko()
                        elif przycisk == przyciski_koniec_ponownie[1]:
                            stan = "gry"
            elif stan == "wygranamakao" or stan == "przegranamakao":
                for przycisk in przyciski_koniec_ponownie:
                    if przycisk.handleEvent(event):
                        if przycisk == przyciski_koniec_ponownie[0]:
                            makao()
                        elif przycisk == przyciski_koniec_ponownie[1]:
                            stan = "gry"
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
            for przycisk in przyciski_koniec_ponownie:
                przycisk.show()
                przycisk.draw()
            Tekst_Pasjans_Ponownie.show()
            Tekst_Pasjans_Ponownie.draw()
        else:
            for przycisk in przyciski_koniec_ponownie:
                przycisk.hide()
            Tekst_Pasjans_Ponownie.hide()

        if stan == "wygranaoczko" or stan == "przegranaoczko" or stan == "remisoczko":
            for przycisk in przyciski_koniec_ponownie:
                przycisk.show()
                przycisk.draw()
            if stan == "wygranaoczko":
                Tekst_Oczko_Ponownie = pygwidgets.DisplayText(ekran, (200, 80), "Gratulacje wygranej! Czy chcesz grać dalej?", fontSize = 30, width = 500, height = 100)
            elif stan == "przegranaoczko":
                Tekst_Oczko_Ponownie = pygwidgets.DisplayText(ekran, (200, 80), "Przegrałeś! Czy chcesz grać dalej?", fontSize = 30, width = 500, height = 100)
            else:
                Tekst_Oczko_Ponownie = pygwidgets.DisplayText(ekran, (200, 80), "Zremisowałeś! Czy chcesz grać dalej?", fontSize = 30, width = 500, height = 100)
            Tekst_Oczko_Ponownie.show()
            Tekst_Oczko_Ponownie.draw()
        else:
            for przycisk in przyciski_koniec_ponownie:
                przycisk.hide()
            Tekst_Oczko_Ponownie.hide()

        if stan == "wygranamakao" or stan == "przegranamakao":
            for przycisk in przyciski_koniec_ponownie:
                przycisk.show()
                przycisk.draw()
            if stan == "wygranamakao":
                Tekst_Makao_Ponownie = pygwidgets.DisplayText(ekran, (200, 80), "Gratulacje wygranej! Czy chcesz grać dalej?", fontSize = 30, width = 500, height = 100)
            else:
                Tekst_Makao_Ponownie = pygwidgets.DisplayText(ekran, (200, 80), "Przegrałeś! Czy chcesz grać dalej?", fontSize = 30, width = 500, height = 100)
            Tekst_Makao_Ponownie.show()
            Tekst_Makao_Ponownie.draw()
        else:
            for przycisk in przyciski_koniec_ponownie:
                przycisk.hide()
            Tekst_Makao_Ponownie.hide()

        if stan == "zasady":
            for przycisk in przyciski_zasady:
                przycisk.show()
                przycisk.draw()
        else:
            for przycisk in przyciski_zasady:
                if przycisk != przyciski_zasady[0]:
                    przycisk.hide()

        if stan == "zasadypasjans":
            Przycisk_Zasady_Wroc.show()
            Przycisk_Zasady_Wroc.draw()
            Tekst_ZasadyPasjans1.show()
            Tekst_ZasadyPasjans1.draw()
            Tekst_ZasadyPasjans2.show()
            Tekst_ZasadyPasjans2.draw()
            Tekst_ZasadyPasjans3.show()
            Tekst_ZasadyPasjans3.draw()
            Tekst_ZasadyPasjans4.show()
            Tekst_ZasadyPasjans4.draw()
        else:
            Tekst_ZasadyPasjans1.hide()
            Tekst_ZasadyPasjans2.hide()
            Tekst_ZasadyPasjans3.hide()
            Tekst_ZasadyPasjans4.hide()

        if stan == "zasadyoczko":
            Przycisk_Zasady_Wroc.show()
            Przycisk_Zasady_Wroc.draw()
            Tekst_ZasadyOczko1.show()
            Tekst_ZasadyOczko1.draw()
            Tekst_ZasadyOczko2.show()
            Tekst_ZasadyOczko2.draw()
            Tekst_ZasadyOczko3.show()
            Tekst_ZasadyOczko3.draw()
        else:
            Tekst_ZasadyOczko1.hide()
            Tekst_ZasadyOczko2.hide()
            Tekst_ZasadyOczko3.hide()
        if stan != "zasady" and stan != "zasadypasjans" and stan != "zasadyoczko":
            Przycisk_Zasady_Wroc.hide()
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