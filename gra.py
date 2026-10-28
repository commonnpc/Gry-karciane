import random
import pygwidgets
import pygame
import sys
import time
from MakaoBot import *
from Karta import *
from SercaBot import *

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
WZORY2 = ['H', 'C', 'D', 'P']
WARTOSCI = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
WARTOSCI_ROSNAC = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
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

Przycisk_Serca = pygwidgets.TextButton(ekran, (450,250), "Serca",
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

Tekst_ZasadyMakao1 = pygwidgets.DisplayText(ekran, (50, 80), "Aby pobrać kartę ze stosu, naciśnij na sos kart odwróconych lewym przyciskiem", fontSize = 25, width = 700, height = 400)
Tekst_ZasadyMakao2 = pygwidgets.DisplayText(ekran, (50, 110), "myszy, a by położyć kartę na stos naciśnij ją prawym przyciskiem myszy.", fontSize = 25, width = 700, height = 400)
Tekst_ZasadyMakao3 = pygwidgets.DisplayText(ekran, (50, 140), "By zakończyć turę, naciśnij przycisk Zakończ Turę.", fontSize = 25, width = 700, height = 400)

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

Przycisk_Zasady_Pasjans = pygwidgets.TextButton(ekran, (100, 100), "Zasady pasjansa", fontSize = 30, 
                                        width = 250, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Zasady_Oczko = pygwidgets.TextButton(ekran, (450, 100), "Zasady oczka", fontSize = 30, 
                                              width = 250, height = 100, 
                                            upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Zasady_Makao = pygwidgets.TextButton(ekran, (100, 250), "Zasady makao", fontSize = 30, 
                                              width = 250, height = 100, 
                                            upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))



Tekst_Oczko_Ponownie = pygwidgets.DisplayText(ekran, (200, 80), "#", fontSize = 30, width = 400, height = 100)
Tekst_Makao_Ponownie = pygwidgets.DisplayText(ekran, (200, 80), "#", fontSize = 30, width = 500, height = 100)

przyciski_autorzy = [Przycisk_Wroc_Z_Autorow]
przyciski_koniec_ponownie = [Przycisk_Zagraj_Ponownie, Przycisk_Wroc_Do_Menu_Z_Grami]
przyciski = [Przycisk_Od_Nowa_Gra, Przycisk_Wroc_Gra]
przyciski_gry = [Przycisk_Wroc_Z_Menu_Gier, Przycisk_Pasjans, Przycisk_Oczko, Przycisk_Makao, Przycisk_Serca]
przyciski_menu = [Przycisk_Graj, Przycisk_Opcje, Przycisk_Wyjscie]
przyciski_opcje = [Przycisk_Zasady, Przycisk_Wroc, Przycisk_Autorzy]
przyciski_zasady = [Przycisk_Zasady_Wroc, Przycisk_Zasady_Pasjans, Przycisk_Zasady_Oczko, Przycisk_Zasady_Makao]
pygame.init()
pygame.display.set_caption("Zbiór gier")

def serca(Tpunkty, Apunkty, Bpunkty, Cpunkty):
    ApunktyNieostateczne = 0
    TpunktyNieostateczne = 0
    BpunktyNieostateczne = 0
    CpunktyNieostateczne = 0
    global karty_do_otrzymania_mieszaniaT, botA, botB, botC
    botA = SercaBot("A")
    botB = SercaBot("B")
    botC = SercaBot("C")
    boty = [botA, botB, botC]
    KartySerca = KARTY.copy()
    random.shuffle(KartySerca)
    for i in range(13):
        for bot in boty:
            bot.karty.append(KartySerca[0])
            KartySerca.pop(0)
    twoje_karty = KartySerca.copy()
    tkarty = []
    while len(twoje_karty) != 0:
        kartaS = None
        for karta in twoje_karty:
            if (kartaS == None) or (WZORY2.index(kartaS.wzor) > WZORY2.index(karta.wzor)) or ((kartaS.wzor == karta.wzor) and (WARTOSCI_ROSNAC.index(kartaS.wartosc) > WARTOSCI_ROSNAC.index(karta.wartosc))):
                kartaS = karta
        tkarty.append(kartaS)
        twoje_karty.remove(kartaS)
    twoje_karty = tkarty.copy()
    tkarty = []
    pygame.init()
    pygame.display.set_caption("SERCA")
    program = True
    kiery = False
    wystawione_karty = {"T" : None, "A" : None, "B" : None, "C" : None}
    wybrany_kolor = ""
    wylozone_karty = 0
    kolejki = ["T", "A", "B", "C"]
    for karta in twoje_karty:
        if karta.wzor == "C" and karta.wartosc == "2":
            kolej = 0
    for karta in botA.karty:
        if karta.wzor == "C" and karta.wartosc == "2":
            kolej = 1
    for karta in botB.karty:
        if karta.wzor == "C" and karta.wartosc == "2":
            kolej = 2
    for karta in botC.karty:
        if karta.wzor == "C" and karta.wartosc == "2":
            kolej = 3
    mieszanieT = 0
    karty_do_otrzymania_mieszaniaT = []
    wymieszano = False
    while program:
        if len(twoje_karty) == 0 and len(botA.karty) == 0 and len(botB.karty) == 0 and len(botC.karty) == 0:
            if (Apunkty + ApunktyNieostateczne >= 100) or (Bpunkty + BpunktyNieostateczne >= 100) or (Cpunkty + CpunktyNieostateczne >= 100) or (Tpunkty + TpunktyNieostateczne >= 100):
                pass #wynik
            time.sleep(1)
            if TpunktyNieostateczne == 26:
                serca(Tpunkty, Apunkty + 26, Bpunkty + 26, Cpunkty + 26)
            elif ApunktyNieostateczne == 26:
                serca(Tpunkty + 26, Apunkty, Bpunkty + 26, Cpunkty + 26)
            elif BpunktyNieostateczne == 26:
                serca(Tpunkty + 26, Apunkty + 26, Bpunkty, Cpunkty + 26)
            elif CpunktyNieostateczne == 26:
                serca(Tpunkty + 26, Apunkty + 26, Bpunkty + 26, Cpunkty)
            else:
                serca(Tpunkty + TpunktyNieostateczne, Apunkty + ApunktyNieostateczne, Bpunkty + BpunktyNieostateczne, Cpunkty + CpunktyNieostateczne)
        if ((mieszanieT + botA.mieszanie + botB.mieszanie + botC.mieszanie) == 12) and not wymieszano:
            for bot in boty:
                bot.karty.extend(bot.karty_do_otrzymanaia_mieszania)
                bot.karty_do_otrzymanaia_mieszania.clear()
            twoje_karty.extend(karty_do_otrzymania_mieszaniaT)
            karty_do_otrzymania_mieszaniaT.clear()
            wymieszano = True
            botA.lsymboli()
            botB.lsymboli()
            botC.lsymboli()
            twoje_symbole = {"H" : 0, "D" : 0, "C" : 0, "P" : 0}
            for karta in twoje_karty:
                twoje_symbole[karta.wzor] += 1
            while len(twoje_karty) != 0:
                kartaS = None
                for karta in twoje_karty:
                    if (kartaS == None) or (WZORY2.index(kartaS.wzor) > WZORY2.index(karta.wzor)) or ((kartaS.wzor == karta.wzor) and (WARTOSCI_ROSNAC.index(kartaS.wartosc) > WARTOSCI_ROSNAC.index(karta.wartosc))):
                        kartaS = karta
                tkarty.append(kartaS)
                twoje_karty.remove(kartaS)
            twoje_karty = tkarty.copy()
            tkarty = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if mieszanieT < 3:
                for karta in twoje_karty:
                    if twoje_karty.index(karta) != len(twoje_karty) - 1:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and karta.prostokat.collidepoint(pygame.mouse.get_pos()) and not twoje_karty[twoje_karty.index(karta)+1].prostokat.collidepoint(pygame.mouse.get_pos()):
                            mieszanie_kart(karta, "A")
                            twoje_karty.remove(karta)
                            mieszanieT += 1
                    else:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and karta.prostokat.collidepoint(pygame.mouse.get_pos()):
                            mieszanie_kart(karta, "A")
                            twoje_karty.remove(karta)
                            mieszanieT += 1
            if kolejki[kolej % len(kolejki)] == "T" and wylozone_karty == 0 and wymieszano:
                for karta in twoje_karty:
                    if twoje_karty.index(karta) != len(twoje_karty) - 1:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and karta.prostokat.collidepoint(pygame.mouse.get_pos()) and (kiery or karta.wzor != "H") and not twoje_karty[twoje_karty.index(karta)+1].prostokat.collidepoint(pygame.mouse.get_pos()):
                            wystawione_karty = wystawienie_serca(karta, kolejki[kolej % len(kolejki)], wystawione_karty)
                            wybrany_kolor = karta.wzor
                            wylozone_karty = 1
                            karta_zabierajaca = karta
                            zabierajacy = "T"
                            twoje_symbole[wybrany_kolor] -= 1
                            twoje_karty.remove(karta)
                    else:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and karta.prostokat.collidepoint(pygame.mouse.get_pos()) and (kiery or karta.wzor != "H"):
                            wystawione_karty = wystawienie_serca(karta, kolejki[kolej % len(kolejki)], wystawione_karty)
                            wybrany_kolor = karta.wzor
                            wylozone_karty = 1
                            karta_zabierajaca = karta
                            zabierajacy = "T"
                            twoje_symbole[wybrany_kolor] -= 1
                            twoje_karty.remove(karta)
            if kolejki[(kolej + wylozone_karty) % len(kolejki)] == "T" and wylozone_karty != 0 and wymieszano:
                for karta in twoje_karty:
                    if twoje_karty.index(karta) != len(twoje_karty) - 1:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and karta.prostokat.collidepoint(pygame.mouse.get_pos()) and not twoje_karty[twoje_karty.index(karta)+1].prostokat.collidepoint(pygame.mouse.get_pos()):
                            if (karta.wzor == wybrany_kolor) or (twoje_symbole[wybrany_kolor] == 0):
                                if (WARTOSCI_ROSNAC.index(karta_zabierajaca.wartosc) < WARTOSCI_ROSNAC.index(karta.wartosc)) and (karta.wzor == wybrany_kolor):
                                    karta_zabierajaca = karta
                                    zabierajacy = "T"
                                if (karta.wzor == "H" or (karta.wzor == "P" and karta.wartosc == "Q")) and not kiery:
                                    kiery = True
                                twoje_symbole[karta.wzor] -= 1
                                wystawione_karty = wystawienie_serca(karta, kolejki[(kolej + wylozone_karty) % len(kolejki)], wystawione_karty)
                                wylozone_karty += 1
                                twoje_karty.remove(karta)
                    else:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and karta.prostokat.collidepoint(pygame.mouse.get_pos()):
                            if (karta.wzor == wybrany_kolor) or (twoje_symbole[wybrany_kolor] == 0):
                                if (karta_zabierajaca.wartosc < karta.wartosc) and (karta.wzor == wybrany_kolor):
                                    karta_zabierajaca = karta
                                    zabierajacy = "T"
                                if (karta.wzor == "H" or (karta.wzor == "P" and karta.wartosc == "Q")) and not kiery:
                                    kiery = True
                                twoje_symbole[karta.wzor] -= 1
                                wystawione_karty = wystawienie_serca(karta, kolejki[(kolej + wylozone_karty) % len(kolejki)], wystawione_karty)
                                twoje_karty.remove(karta)
                                wylozone_karty += 1
        for bot in boty:
            if bot.mieszanie < 3:
                kartaS = None
                for karta in bot.karty:
                    if kartaS == None or WARTOSCI_ROSNAC.index(karta.wartosc) > WARTOSCI_ROSNAC.index(kartaS.wartosc):
                        kartaS = karta
                bot.karty.remove(kartaS)
                bot.mieszanie += 1
                mieszanie_kart(kartaS, kolejki[(kolejki.index(bot.ABC) + 1) % len(kolejki)])
        if kolejki[kolej % len(kolejki)] != "T" and wylozone_karty == 0 and wymieszano:
            time.sleep(1)
            if kolejki[kolej % len(kolejki)] == "A":
                botX = botA
            elif kolejki[kolej % len(kolejki)] == "B":
                botX = botB
            else:
                botX = botC
            wartosc_karty_do_wylozenia = "A"
            for karta in botX.karty:
                if WARTOSCI_ROSNAC.index(karta.wartosc) <= WARTOSCI_ROSNAC.index(wartosc_karty_do_wylozenia) and (kiery or karta.wzor != "H"):
                    wybrana_karta = karta
                    wartosc_karty_do_wylozenia = karta.wartosc
                    karta_zabierajaca = karta
                    zabierajacy = kolejki[kolej % len(kolejki)]
            wystawione_karty = wystawienie_serca(wybrana_karta, kolejki[kolej % len(kolejki)], wystawione_karty)
            wybrany_kolor = wybrana_karta.wzor
            wylozone_karty = 1
            botX.symbole[wybrany_kolor] -= 1
            botX.karty.remove(wybrana_karta)  
        if kolejki[(kolej + wylozone_karty) % len(kolejki)] != "T" and wylozone_karty != 0 and wymieszano:
            time.sleep(1)
            if kolejki[(kolej + wylozone_karty) % len(kolejki)] == "A":
                botX = botA
            elif kolejki[(kolej + wylozone_karty) % len(kolejki)] == "B":
                botX = botB
            else:
                botX = botC
            kartaS = None
            for karta in botX.karty:
                if (karta.wzor == wybrany_kolor) and WARTOSCI_ROSNAC.index(karta.wartosc) < WARTOSCI_ROSNAC.index(karta_zabierajaca.wartosc) and (kartaS == None or WARTOSCI_ROSNAC.index(karta.wartosc) > WARTOSCI_ROSNAC.index(kartaS.wartosc)):
                    kartaS = karta
            if kartaS != None:
                botX.symbole[kartaS.wzor] -= 1
                wystawione_karty = wystawienie_serca(kartaS, kolejki[(kolej + wylozone_karty) % len(kolejki)], wystawione_karty)
                wylozone_karty += 1
            else:
                for karta in botX.karty:
                    if (karta.wzor == wybrany_kolor) and (kartaS == None or WARTOSCI_ROSNAC.index(karta.wartosc) < WARTOSCI_ROSNAC.index(kartaS.wartosc)):
                        kartaS = karta
                if kartaS != None:
                    wybrana_karta = kartaS
                    wartosc_karty_do_wylozenia = kartaS.wartosc
                    karta_zabierajaca = kartaS
                    zabierajacy = kolejki[(kolej + wylozone_karty) % len(kolejki)]
                    botX.symbole[kartaS.wzor] -= 1
                    wystawione_karty = wystawienie_serca(kartaS, kolejki[(kolej + wylozone_karty) % len(kolejki)], wystawione_karty)
                    wylozone_karty += 1
                else:
                    for karta in botX.karty:
                        if (karta.wzor == wybrany_kolor) and (kartaS == None or WARTOSCI_ROSNAC.index(karta.wartosc) > WARTOSCI_ROSNAC.index(kartaS.wartosc)):
                            kartaS = karta
                    if kartaS != None:
                        botX.symbole[kartaS.wzor] -= 1
                        wystawione_karty = wystawienie_serca(kartaS, kolejki[(kolej + wylozone_karty) % len(kolejki)], wystawione_karty)
                        wylozone_karty += 1
                    else:
                        for karta in botX.karty:
                            if kartaS == None or WARTOSCI_ROSNAC.index(karta.wartosc) > WARTOSCI_ROSNAC.index(kartaS.wartosc):
                                kartaS = karta
                        botX.symbole[kartaS.wzor] -= 1
                        wystawione_karty = wystawienie_serca(kartaS, kolejki[(kolej + wylozone_karty) % len(kolejki)], wystawione_karty)  
                        wylozone_karty += 1
            botX.karty.remove(kartaS)
            if (kartaS.wzor == "H" or (kartaS.wzor == "P" and kartaS.wartosc == "Q")) and not kiery:
                kiery = True
            
        ekran.fill(TLO)
        if wystawione_karty.get("T") != None:
            wystawione_karty.get("T").obrocenie()
            wystawione_karty.get("T").rysuj(ekran, 510, 420)
        if wystawione_karty.get("A") != None:
            wystawione_karty.get("A").obrocenie()
            wystawione_karty.get("A").rysuj(ekran, 400, 280)
        if wystawione_karty.get("B") != None:
            wystawione_karty.get("B").obrocenie()
            wystawione_karty.get("B").rysuj(ekran, 510, 120)
        if wystawione_karty.get("C") != None:
            wystawione_karty.get("C").obrocenie()
            wystawione_karty.get("C").rysuj(ekran, 620, 280)
        for karta in twoje_karty:
            karta.obrocenie()
            karta.rysuj(ekran, 390 + (0 if len(twoje_karty) <= 1 else 240/(len(twoje_karty)-1)) * twoje_karty.index(karta), 500)
        for karta in botA.karty:
            karta.zakrycie()
            karta.rysuj(ekran, 320, 160 + (0 if len(botA.karty) <= 1 else 240/(len(botA.karty)-1)) * botA.karty.index(karta), obrocenie = True)
        for karta in botC.karty:
            karta.zakrycie()
            karta.rysuj(ekran, 680, 160 + (0 if len(botC.karty) <= 1 else 240/(len(botC.karty)-1)) * botC.karty.index(karta), obrocenie = True)
        for karta in botB.karty:
            karta.zakrycie()
            karta.rysuj(ekran, 390 + (0 if len(botB.karty) <= 1 else 240/(len(botB.karty)-1)) * botB.karty.index(karta), 40)
        pygame.display.update()
        clock.tick(KLATKI_NA_SEKUNDE)
        if wystawione_karty.get("T") != None and wystawione_karty.get("A") != None and wystawione_karty.get("B") != None and wystawione_karty.get("C"):
            for karta in wystawione_karty.values():
                if karta.wzor == "H":
                    if zabierajacy == "T":
                        TpunktyNieostateczne += 1
                    elif zabierajacy == "A":
                        ApunktyNieostateczne += 1
                    elif zabierajacy == "B":
                        BpunktyNieostateczne += 1
                    else:
                        CpunktyNieostateczne += 1
                elif karta.wzor == "P" and karta.wartosc == "Q":
                    if zabierajacy == "T":
                        TpunktyNieostateczne += 13
                    elif zabierajacy == "A":
                        ApunktyNieostateczne += 13
                    elif zabierajacy == "B":
                        BpunktyNieostateczne += 13
                    else:
                        CpunktyNieostateczne += 13
            wystawione_karty = {"T" : None, "A" : None, "B" : None, "C" : None}
            #zabierający zabiera punkty
            kolej = kolejki.index(zabierajacy)
            wylozone_karty = 0
            wybrany_kolor = ""
            karta_zabierajaca = None
            zabierajacy = None
            time.sleep(1)

def mieszanie_kart(karta, kto):
    if kto == "T":
        karty_do_otrzymania_mieszaniaT.append(karta)
    else:
        if kto == "A":
            botA.karty_do_otrzymanaia_mieszania.append(karta)
        elif kto == "B":
            botB.karty_do_otrzymanaia_mieszania.append(karta)
        else:
            botC.karty_do_otrzymanaia_mieszania.append(karta)
        
def wystawienie_serca(karta, kto, wystawione_karty):
    wystawione_karty[kto] = karta
    return wystawione_karty

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
    suma_blokad = 0
    twoje_bloki = 0
    kartaS = 0
    t = 1
    pA = False
    dobrana = None
    global stan, program, kolej
    Tekst_Kolor = pygwidgets.DisplayText(ekran, (50, 20), "Wybrany kolor: #", fontSize = 20)
    Tekst_Rzadanie = pygwidgets.DisplayText(ekran, (50, 20), "Rządana wartość: #", fontSize = 20)
    Tekst_Dobieranie = pygwidgets.DisplayText(ekran, (100, 20), "Karty do dobrania (2, 3): #", fontSize = 20)
    Tekst_DobieranieK = pygwidgets.DisplayText(ekran, (100, 20), "Karty do dobrania (K): #", fontSize = 20)
    przycisk_koniec_tury = pygwidgets.TextButton(ekran, (50, 250), "Zakończ turę",
                                                fontSize = 30, width = 200, height = 100, 
                                                upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))
    przycisk_ponownie = pygwidgets.TextButton(ekran, (50, 140), "Zagraj ponownie",
                                            fontSize = 30, width = 200, height = 100, 
                                            upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))
    przycisk_powrot = pygwidgets.TextButton(ekran, (50, 30), "Powrót do menu",
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

    przycisk_5 = pygwidgets.TextButton(ekran, (50, 375), "5",
                                        fontSize = 40, width = 60, height = 50, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

    przycisk_6 = pygwidgets.TextButton(ekran, (120, 375), "6",
                                        fontSize = 40, width = 60, height = 50, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

    przycisk_7 = pygwidgets.TextButton(ekran, (190, 375), "7",
                                        fontSize = 40, width = 60, height = 50, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

    przycisk_8 = pygwidgets.TextButton(ekran, (50, 450), "8",
                                        fontSize = 40, width = 60, height = 50, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))
    
    przycisk_9 = pygwidgets.TextButton(ekran, (120, 450), "9",
                                        fontSize = 40, width = 60, height = 50, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))
    
    przycisk_10 = pygwidgets.TextButton(ekran, (190, 450), "10",
                                        fontSize = 40, width = 60, height = 50, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))
        
    przyciski_makao = [przycisk_koniec_tury, przycisk_ponownie, przycisk_powrot]
    przyciski_A = [przycisk_kier, przycisk_karo, przycisk_trefl, przycisk_pik]
    przyciski_J = [przycisk_5, przycisk_6, przycisk_7, przycisk_8, przycisk_9, przycisk_10]

    stos_dobieranie = KARTY.copy()
    random.shuffle(stos_dobieranie)
    pygame.init()
    pygame.display.set_caption("MAKAO")
    twoje_karty = []
    botA = MakaoBot("A")
    botB = MakaoBot("B")
    botC = MakaoBot("C")
    boty = [botA, botB, botC]

    for i in range(len(stos_dobieranie)):
        if stos_dobieranie[i].wartosc in ["5", "6", "7", "8", "9", "10"]:
            stos_kladzenia = [stos_dobieranie[i]]
            stos_dobieranie.pop(i)
            break
    for i in range(5):
        twoje_karty.append(stos_dobieranie[0])
        stos_dobieranie.pop(0)
        for bot in boty:
            bot.karty.append(stos_dobieranie[0])
            stos_dobieranie.pop(0)
    program = True
    ruchyT = True
    kolej = "T"
    cel_blokad = ""
    koniectury = 0
    kolorA = ""
    pobieranieTY = False
    pobieranieK = 0
    pobieranieTYK = 0
    pobieranie23 = 0
    rzadana = ""
    rzadajacy = ""
    rzadanie = False
    x = 1
    a = ""
    kolejZmiana = False
    while program:
        ekran.fill(TLO)
        if len(stos_kladzenia) > 1:
            stos_dobieranie.insert(-1, stos_kladzenia[0])
            stos_kladzenia.pop(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if kolej == "T":
                for karta in twoje_karty:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if stos_dobieranie[0].prostokat.collidepoint(pygame.mouse.get_pos()) and ruchyT and not pA and (suma_blokad == 0 or cel_blokad != "T") and twoje_bloki == 0:
                            if pobieranieTY:
                                for i in range(pobieranie23):
                                    twoje_karty.append(stos_dobieranie[0])
                                    stos_dobieranie.pop(0)
                                    if i == 0 and (twoje_karty[-1].wartosc == "2" or twoje_karty[-1].wartosc == "3"):
                                        time.sleep(0.1)
                                        while a == "":
                                            if stos_dobieranie[0].prostokat.collidepoint(pygame.mouse.get_pos()):
                                                a = "dobieranie"
                                            if twoje_karty[-1].prostokat.collidepoint(pygame.mouse.get_pos()):
                                                a = "podajdalej"
                                        if a == "podajdalej":
                                            if twoje_karty[-1].wartosc == "2":
                                                pobieranie23 += 2
                                            else:
                                                pobieranie23 += 3
                                            kartaS = twoje_karty[-1].wartosc
                                            stos_kladzenia.append(twoje_karty[-1])
                                            twoje_karty.pop(-1)
                                            pobieranieTY = False
                                            break
                                    else:
                                        x = 0
                                if x == 0:
                                    pobieranie23 = 0
                                    x = 1
                                a = ""
                            elif pobieranieTYK:
                                for i in range(pobieranieK):
                                    twoje_karty.append(stos_dobieranie[0])
                                    stos_dobieranie.pop(0)
                                    if i == 0 and twoje_karty[-1].wartosc == "K" and (twoje_karty[-1].wzor == "H" or twoje_karty[-1].wzor == "P"):
                                        time.sleep(0.1)
                                        while a == "":
                                            if stos_dobieranie[0].prostokat.collidepoint(pygame.mouse.get_pos()):
                                                a = "dobieranie"
                                            if twoje_karty[-1].prostokat.collidepoint(pygame.mouse.get_pos()):
                                                a = "podajdalej"
                                        if a == "podajdalej":
                                            if twoje_karty[-1].wzor == "H":
                                                pobieranieK += 5
                                                kolejZmiana = False
                                            else:
                                                pobieranieK += 5
                                                kolejZmiana = True
                                            kartaS = twoje_karty[-1].wartosc
                                            stos_kladzenia.append(twoje_karty[-1])
                                            twoje_karty.pop(-1)
                                            break
                                    else:
                                        x = 0
                                if x == 0:
                                    pobieranieK = 0
                                    pobieranieTYK = False
                                    x = 1
                            else:
                                twoje_karty.append(stos_dobieranie[0])
                                stos_dobieranie.pop(0)
                                dobrana = twoje_karty[-1]
                                if rzadajacy == "T":
                                    rzadajacy = ""
                                    rzadana = ""
                            ruchyT = False
                            t = 0
                        if dobrana != None and not pA and (dobrana.wartosc == "4" or (suma_blokad == 0 or not cel_blokad == "T")) and twoje_bloki == 0 and (rzadana == "" or rzadana == dobrana.wartosc or dobrana.wartosc == "J") and not rzadanie:
                            if dobrana.prostokat.collidepoint(pygame.mouse.get_pos()) and  t != 0:
                                if kolorA == "":
                                    if dobrana.wzor == stos_kladzenia[-1].wzor or dobrana.wartosc == stos_kladzenia[-1].wartosc or stos_kladzenia[-1].wartosc == "Q" or dobrana.wartosc == "Q" or dobrana.wartosc == rzadana:
                                        if rzadajacy == "T":
                                            rzadajacy = ""
                                            rzadana = ""
                                        if dobrana.wartosc == "A":
                                            pA = True
                                        elif dobrana.wartosc == "2":
                                            pobieranie23 += 2
                                            pobieranieTY = False
                                        elif dobrana.wartosc == "3":
                                            pobieranie23 += 3
                                            pobieranieTY = False
                                        elif dobrana.wartosc == "K" and dobrana.wzor == "H":
                                            pobieranieK += 5
                                            kolejZmiana = False
                                        elif dobrana.wartosc == "K" and dobrana.wzor == "P":
                                            pobieranieK += 5
                                            kolejZmiana = True
                                        elif dobrana.wartosc == "4":
                                            if botA.blok == 0:
                                                suma_blokad += 1
                                                cel_blokad = "A"
                                            else:
                                                suma_blokad += 1
                                                cel_blokad = "B"
                                        elif dobrana.wartosc == "J":
                                            rzadanie = True
                                        stos_kladzenia.append(twoje_karty[-1])
                                        twoje_karty.pop(-1)
                                        kartaS = stos_kladzenia[-1].wartosc
                                        kartaQ = stos_kladzenia[-1].wzor
                                        dobrana = None
                                else:
                                    if dobrana.wzor == kolorA or dobrana.wartosc == stos_kladzenia[-1].wartosc or dobrana.wartosc == "Q" or dobrana.wartosc == rzadana:
                                        if rzadajacy == "T":
                                            rzadajacy = ""
                                            rzadana = ""
                                        if dobrana.wartosc == "A":
                                            pA = True
                                        else:
                                            kolorA = ""
                                        if dobrana.wartosc == "2":
                                            pobieranie23 += 2
                                            pobieranieTY = False
                                        elif dobrana.wartosc == "3":
                                            pobieranie23 += 3
                                            pobieranieTY = False
                                        elif dobrana.wartosc == "K" and dobrana.wzor == "H":
                                            pobieranieK += 5
                                            kolejZmiana = False
                                        elif dobrana.wartosc == "K" and dobrana.wzor == "P":
                                            pobieranieK += 5
                                            kolejZmiana = True
                                        elif dobrana.wartosc == "4":
                                            if botA.blok == 0:
                                                suma_blokad += 1
                                                cel_blokad = "A"
                                            else:
                                                suma_blokad += 1
                                                cel_blokad = "B"
                                        elif dobrana.wartosc == "J":
                                            rzadanie = True
                                        stos_kladzenia.append(twoje_karty[-1])
                                        twoje_karty.pop(-1)
                                        kartaS = stos_kladzenia[-1].wartosc
                                        kartaQ = stos_kladzenia[-1].wzor
                                        dobrana = None
                        if kolorA == "":
                            if karta.prostokat.collidepoint(pygame.mouse.get_pos()) and (karta.wzor == stos_kladzenia[-1].wzor or karta.wartosc == stos_kladzenia[-1].wartosc or karta.wartosc == "Q" or stos_kladzenia[-1].wartosc == "Q" or karta.wartosc == rzadana) and not pA and (rzadana == "" or rzadana == karta.wartosc or karta.wartosc == "J") and not rzadanie:
                                if (not pobieranieTY or (karta.wartosc == "2" or karta.wartosc == "3")) and (not pobieranieTYK or (karta.wartosc == "K" and (karta.wzor == "H" or karta.wzor == "P"))) and (karta.wartosc == "4" or (suma_blokad == 0 or not cel_blokad == "T")) and twoje_bloki == 0:
                                    if ruchyT:
                                        if rzadajacy == "T":
                                            rzadajacy = ""
                                            rzadana = ""
                                        if karta.wartosc == "A":
                                            pA = True
                                        elif karta.wartosc == "2":
                                            pobieranie23 += 2
                                            pobieranieTY = False
                                        elif karta.wartosc == "3":
                                            pobieranie23 += 3
                                            pobieranieTY = False
                                        elif karta.wartosc == "K" and karta.wzor == "H":
                                            pobieranieK += 5
                                            kolejZmiana = False
                                        elif karta.wartosc == "K" and karta.wzor == "P":
                                            pobieranieK += 5
                                            kolejZmiana = True
                                        elif karta.wartosc == "4":
                                            if botA.blok == 0:
                                                suma_blokad += 1
                                                cel_blokad = "A"
                                            else:
                                                suma_blokad += 1
                                                cel_blokad = "B"
                                        elif karta.wartosc == "J":
                                            rzadanie = True
                                        stos_kladzenia.append(karta)
                                        twoje_karty.remove(karta)
                                        ruchyT = False
                                        kartaS = karta.wartosc
                                        kartaQ = karta.wzor
                                    elif karta.wartosc == kartaS:
                                        if not (kartaS == "K" and (kartaQ == "H" or kartaQ == "P") and (kartaQ == "H" or kartaQ == "P")):
                                            if rzadajacy == "T":
                                                rzadajacy = ""
                                                rzadana = ""
                                            if karta.wartosc == "A":
                                                pA = True
                                            elif karta.wartosc == "2":
                                                pobieranie23 += 2
                                                pobieranieTY = False
                                            elif karta.wartosc == "3":
                                                pobieranie23 += 3
                                                pobieranieTY = False
                                            elif karta.wartosc == "K" and karta.wzor == "H":
                                                pobieranieK += 5
                                                kolejZmiana = False
                                            elif karta.wartosc == "K" and karta.wzor == "P":
                                                pobieranieK += 5
                                                kolejZmiana = True
                                            elif karta.wartosc == "4":
                                                if botA.blok == 0:
                                                    suma_blokad += 1
                                                    cel_blokad = "A"
                                                else:
                                                    suma_blokad += 1
                                                    cel_blokad = "B"
                                            elif karta.wartosc == "J":
                                                rzadanie = True
                                            stos_kladzenia.append(karta)
                                            twoje_karty.remove(karta)
                        else:
                            if karta.prostokat.collidepoint(pygame.mouse.get_pos()) and (karta.wzor == kolorA or karta.wartosc == stos_kladzenia[-1].wartosc or karta.wartosc == "Q" or karta.wartosc == rzadana) and not pA and (not pobieranieTY or (karta.wartosc == "2" or karta.wartosc == "3")) and (not pobieranieTYK or (karta.wartosc == "K" and (karta.wzor == "H" or karta.wzor == "P"))) and (karta.wartosc == "4" or (suma_blokad == 0 or not cel_blokad == "T")) and twoje_bloki == 0 and (rzadana == "" or rzadana == karta.wartosc or karta.wartosc == "J") and not rzadanie:
                                if ruchyT:
                                    if rzadajacy == "T":
                                        rzadajacy = ""
                                        rzadana = ""
                                    if karta.wartosc == "A":
                                        pA = True
                                    else:
                                        kolorA = ""
                                    if karta.wartosc == "2":
                                        pobieranie23 += 2
                                        pobieranieTY = False
                                    if karta.wartosc == "3":
                                        pobieranie23 += 3
                                        pobieranieTY = False
                                    elif karta.wartosc == "K" and karta.wzor == "H":
                                        pobieranieK += 5
                                        kolejZmiana = False
                                    elif karta.wartosc == "K" and karta.wzor == "P":
                                        pobieranieK += 5
                                        kolejZmiana = True
                                    elif karta.wartosc == "4":
                                        if botA.blok == 0:
                                            suma_blokad += 1
                                            cel_blokad = "A"
                                        else:
                                            suma_blokad += 1
                                            cel_blokad = "B"
                                    elif karta.wartosc == "J":
                                        rzadanie = True
                                    stos_kladzenia.append(karta)
                                    twoje_karty.remove(karta)
                                    ruchyT = False
                                    kartaS = karta.wartosc
                                    kartaQ = karta.wzor
                                elif karta.wartosc == kartaS:
                                    if not (kartaS == "K" and (kartaQ == "H" or kartaQ == "P") and (kartaQ == "H" or kartaQ == "P")):
                                        if rzadajacy == "T":
                                            rzadajacy = ""
                                            rzadana = ""
                                        if karta.wartosc == "A":
                                            pA = True
                                        else:
                                            kolorA = ""
                                        if karta.wartosc == "2":
                                            pobieranie23 += 2
                                            pobieranieTY = False
                                        if karta.wartosc == "3":
                                            pobieranie23 += 3
                                            pobieranieTY = False
                                        elif karta.wartosc == "K" and karta.wzor == "H":
                                            pobieranieK += 5
                                            kolejZmiana = False
                                        elif karta.wartosc == "K" and karta.wzor == "P":
                                            pobieranieK += 5
                                            kolejZmiana = True
                                        elif karta.wartosc == "4":
                                            if botA.blok == 0:
                                                suma_blokad += 1
                                                cel_blokad = "A"
                                            else:
                                                suma_blokad += 1
                                                cel_blokad = "B"
                                        elif karta.wartosc == "J":
                                            rzadanie = True
                                        stos_kladzenia.append(karta)
                                        twoje_karty.remove(karta)
            for przycisk in przyciski_makao:
                if przycisk.handleEvent(event):
                    if przycisk == przyciski_makao[0] and kolej == "T" and not pA and not rzadanie:
                        if not ruchyT or twoje_bloki != 0 or (suma_blokad != 0 and cel_blokad == "T"):
                            if suma_blokad != 0 and cel_blokad == "T":
                                twoje_bloki == suma_blokad
                                suma_blokad = 0
                            if kolejZmiana:
                                kolej = "C"
                                botC.ruchy = True
                                kolejZmiana = False
                            else:
                                kolej = "A"
                                botA.ruchy = True
                            if pobieranie23 != 0:
                                pobieranieTY = True
                            if pobieranieK != 0:
                                pobieranieTYK = True
                            dobrana = None
                            kartaS = 0
                            if twoje_bloki != 0:
                                twoje_bloki -= 1
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
            if rzadanie:
                for przycisk in przyciski_J:
                    if przycisk.handleEvent(event):
                        if przycisk == przyciski_J[0]:
                            rzadana = "5"
                        elif przycisk == przyciski_J[1]:
                            rzadana = "6"
                        elif przycisk == przyciski_J[2]:
                            rzadana = "7"
                        elif przycisk == przyciski_J[3]:
                            rzadana = "8"
                        elif przycisk == przyciski_J[4]:
                            rzadana = "9"
                        elif przycisk == przyciski_J[5]:
                            rzadana = "10"
                        rzadanie = False
                        rzadajacy  = "T"

        if kolej == "A" or kolej == "B" or kolej == "C":
            if kolej == "A":
                BOT = botA
            elif kolej == "B":
                BOT = botB
            else:
                BOT = botC
            koniectury = len(BOT.karty)
            for karta in BOT.karty:
                if kolorA == "":
                    if (not pobieranieTY or karta.wartosc == "2" or karta.wartosc == "3") and (not pobieranieTYK or (karta.wartosc == "K" and (karta.wzor == "H" or karta.wzor == "P"))) and (karta.wartosc == "4" or (suma_blokad == 0 or not cel_blokad == BOT.ABC)) and BOT.blok == 0 and (rzadana == "" or rzadana == karta.wartosc or karta.wartosc == "J"):
                        if karta.wzor == stos_kladzenia[-1].wzor or karta.wartosc == stos_kladzenia[-1].wartosc or karta.wartosc == "Q" or stos_kladzenia[-1].wartosc == "Q" or rzadana == karta.wartosc:
                            if BOT.ruchy:
                                if rzadajacy == BOT.ABC:
                                    rzadajacy = ""
                                    rzadana = ""
                                if karta.wartosc == "A":
                                    kolorA = BOT.zmiana_koloru()
                                elif karta.wartosc == "2":
                                    pobieranieTY = False
                                    pobieranie23 += 2
                                elif karta.wartosc == "3":
                                    pobieranieTY = False
                                    pobieranie23 += 3
                                elif karta.wartosc == "K" and karta.wzor == "H":
                                    pobieranieK += 5
                                    kolejZmiana = False
                                elif karta.wartosc == "K" and karta.wzor == "P":
                                    pobieranieK += 5
                                    kolejZmiana = True
                                elif karta.wartosc == "4":
                                    suma_blokad += 1
                                    if BOT.ABC == "A":
                                        if botB.blok == 0:
                                            cel_blokad = "B"
                                        else:
                                            cel_blokad = "C"
                                    elif BOT.ABC == "B":
                                        if botC.blok == 0:
                                            cel_blokad = "C"
                                        else:
                                            cel_blokad = "T"
                                    elif BOT.ABC == "C":
                                        if twoje_bloki == 0:
                                            cel_blokad = "T"
                                        else:
                                            cel_blokad = "C"
                                elif karta.wartosc == "J":
                                    rzadana, rzadajacy = BOT.rzadana()
                                stos_kladzenia.append(karta)
                                BOT.karty.remove(karta)
                                BOT.ruchy = False
                                kartaS = karta.wartosc
                                kartaQ = karta.wzor
                                continue
                            elif karta.wartosc == kartaS:
                                if not ((kartaS == "K" and (kartaQ == "H" or kartaQ == "P") and (kartaQ == "H" or kartaQ == "P"))):
                                    if rzadajacy == BOT.ABC:
                                        rzadajacy = ""
                                        rzadana = ""
                                    if karta.wartosc == "A":
                                        kolorA = BOT.zmiana_koloru()
                                    elif karta.wartosc == "2":
                                        pobieranieTY = False
                                        pobieranie23 += 2
                                    elif karta.wartosc == "3":
                                        pobieranieTY = False
                                        pobieranie23 += 3
                                    elif karta.wartosc == "K" and karta.wzor == "H":
                                        pobieranieK += 5
                                        kolejZmiana = False
                                    elif karta.wartosc == "K" and karta.wzor == "P":
                                        pobieranieK += 5
                                        kolejZmiana = True
                                    elif karta.wartosc == "4":
                                        suma_blokad += 1
                                        if BOT.ABC == "A":
                                            if botB.blok == 0:
                                                cel_blokad = "B"
                                            else:
                                                cel_blokad = "C"
                                        elif BOT.ABC == "B":
                                            if botC.blok == 0:
                                                cel_blokad = "C"
                                            else:
                                                cel_blokad = "T"
                                        elif BOT.ABC == "C":
                                            if twoje_bloki == 0:
                                                cel_blokad = "T"
                                            else:
                                                cel_blokad = "A"
                                    elif karta.wartosc == "J":
                                        rzadana, rzadajacy = BOT.rzadana()
                                    stos_kladzenia.append(karta)
                                    BOT.karty.remove(karta)
                                    continue
                else:
                    if (karta.wzor == kolorA or karta.wartosc == stos_kladzenia[-1].wartosc or karta.wartosc == "Q" or rzadana == karta.wartosc) and (not pobieranieTY or karta.wartosc == "2" or karta.wartosc == "3") and (not pobieranieTYK or (karta.wartosc == "K" and (karta.wzor == "H" or karta.wzor == "P"))) and (karta.wartosc == "4" or (suma_blokad == 0 or not cel_blokad == BOT.ABC)) and BOT.blok == 0 and (rzadana == "" or rzadana == karta.wartosc or karta.wartosc == "J"):
                        if BOT.ruchy:
                            if rzadajacy == BOT.ABC:
                                rzadajacy = ""
                                rzadana = ""
                            if karta.wartosc == "A":
                                kolorA = BOT.zmiana_koloru()
                            else:
                                kolorA = ""
                            if karta.wartosc == "2":
                                pobieranieTY = False
                                pobieranie23 += 2
                            elif karta.wartosc == "3":
                                pobieranieTY = False
                                pobieranie23 += 3
                            elif karta.wartosc == "K" and karta.wzor == "H":
                                pobieranieK += 5
                                kolejZmiana = False
                            elif karta.wartosc == "K" and karta.wzor == "P":
                                pobieranieK += 5
                                kolejZmiana = True
                            elif karta.wartosc == "4":
                                suma_blokad += 1
                                suma_blokad += 1
                                if BOT.ABC == "A":
                                    if botB.blok == 0:
                                        cel_blokad = "B"
                                    else:
                                        cel_blokad = "C"
                                elif BOT.ABC == "B":
                                    if botC.blok == 0:
                                        cel_blokad = "C"
                                    else:
                                        cel_blokad = "T"
                                elif BOT.ABC == "C":
                                    if twoje_bloki == 0:
                                        cel_blokad = "T"
                                    else:
                                        cel_blokad = "C"
                            elif karta.wartosc == "J":
                                rzadana, rzadajacy = BOT.rzadana()
                            stos_kladzenia.append(karta)
                            BOT.karty.remove(karta)
                            BOT.ruchy = False
                            kartaS = karta.wartosc
                            kartaQ = karta.wzor
                            continue
                        elif karta.wartosc == kartaS:
                            if not (kartaS == "K" and (kartaQ == "H" or kartaQ == "P") and (kartaQ == "H" or kartaQ == "P")):
                                if rzadajacy == BOT.ABC:
                                    rzadajacy = ""
                                    rzadana = ""
                                if karta.wartosc == "A":
                                    kolorA = BOT.zmiana_koloru()
                                else:
                                    kolorA = ""
                                if karta.wartosc == "2":
                                    pobieranieTY = False
                                    pobieranie23 += 2
                                elif karta.wartosc == "3":
                                    pobieranieTY = False
                                    pobieranie23 += 3
                                elif karta.wartosc == "K" and karta.wzor == "H":
                                    pobieranieK += 5
                                    kolejZmiana = False
                                elif karta.wartosc == "K" and karta.wzor == "P":
                                    pobieranieK += 5
                                    kolejZmiana = True
                                elif karta.wartosc == "4":
                                    suma_blokad += 1
                                    if BOT.ABC == "A":
                                        if botB.blok == 0:
                                            cel_blokad = "B"
                                        else:
                                            cel_blokad = "C"
                                    elif BOT.ABC == "B":
                                        if botC.blok == 0:
                                            cel_blokad = "C"
                                        else:
                                            cel_blokad = "T"
                                    elif BOT.ABC == "C":
                                        if twoje_bloki == 0:
                                            cel_blokad = "T"
                                        else:
                                            cel_blokad = "C"
                                elif karta.wartosc == "J":
                                    rzadana, rzadajacy = BOT.rzadana()
                                stos_kladzenia.append(karta)
                                BOT.karty.remove(karta)
                                continue
            if BOT.ruchy:
                if (suma_blokad == 0 or not cel_blokad == BOT.ABC) and BOT.blok == 0:
                    if pobieranieTY:
                        for i in range(pobieranie23):
                            BOT.karty.append(stos_dobieranie[0])
                            stos_dobieranie.pop(0)
                            if i == 0 and (BOT.karty[-1].wartosc == "2" or BOT.karty[-1].wartosc == "3"):
                                if BOT.karty[-1].wartosc == "2":
                                    pobieranie23 += 2
                                else:
                                    pobieranie23 += 3
                                pobieranieTY = False
                                stos_kladzenia.append(BOT.karty[-1])
                                kartaS = BOT.karty[-1].wartosc
                                kartaQ = BOT.karty[-1].wzor
                                BOT.karty.pop(-1)
                                break
                            else:
                                x = 0
                        if x == 0:
                            pobieranie23 = 0
                            pobieranieTY = False
                            x = 1
                    elif pobieranieTYK:
                        for i in range(pobieranieK):
                            BOT.karty.append(stos_dobieranie[0])
                            stos_dobieranie.pop(0)
                            if i == 0 and (BOT.karty[-1].wartosc == "K" and (BOT.karty[-1].wzor == "H" or BOT.karty[-1].wzor == "P")):
                                if BOT.karty[-1].wzor == "H":
                                    pobieranieK += 5
                                    kolejZmiana = False
                                else:
                                    pobieranieK += 5
                                    kolejZmiana = True
                                pobieranieTY = False
                                stos_kladzenia.append(BOT.karty[-1])
                                kartaS = BOT.karty[-1].wartosc
                                BOT.karty.pop(-1)
                                break
                            else:
                                x = 0
                        if x == 0:
                            pobieranieK = 0
                            pobieranieTYK = False
                            x = 1
                    else:
                        BOT.karty.append(stos_dobieranie[0])
                        stos_dobieranie.pop(0)
                        kartaS = BOT.karty[-1].wartosc
                        kartaQ = BOT.karty[-1].wartosc
                        if rzadajacy == BOT.ABC:
                            rzadajacy = ""
                            rzadana = ""
                    
                    BOT.ruchy = False
                    continue
                else:
                    if suma_blokad != 0:
                        BOT.blok = suma_blokad
                        suma_blokad = 0
                    BOT.blok -= 1
                    BOT.ruchy = False
                    continue
            kartaS = 0
            if koniectury == len(BOT.karty) and not BOT.ruchy:
                if pobieranie23 != 0:
                    pobieranieTY = True
                if pobieranieK != 0:
                    pobieranieTYK = True
                if kolejZmiana:
                    if kolej == "A":
                        kolej = "T"
                        ruchyT = True
                        kolejZmiana = False
                    elif kolej == "B":
                        kolej = "A"
                        botA.ruchy = True
                        kolejZmiana = False
                    elif kolej == "C":
                        kolej = "B"
                        botB.ruchy = True
                        kolejZmiana = False
                else:
                    if kolej == "A":
                        kolej = "B"
                        botB.ruchy = True
                    elif kolej == "B":
                        kolej = "C"
                        botC.ruchy = True
                    elif kolej == "C":
                        kolej = "T"
                        ruchyT= True
            koniectury = 0
        if len(stos_dobieranie) > 0:
            stos_dobieranie[0].zakrycie()
            stos_dobieranie[0].rysuj(ekran, 540, 270)
        else:
            stos_dobieranie = stos_kladzenia.copy()
            stos_kladzenia.append(stos_dobieranie[-1])
            stos_dobieranie.pop(-1)
        if rzadana != "":
            Tekst_Rzadanie = pygwidgets.DisplayText(ekran, (50, 10), "Żądana wartość: " + rzadana, fontSize = 20)
            Tekst_Rzadanie.show()
            Tekst_Rzadanie.draw()
        else:
            Tekst_Rzadanie.hide()
        if kolorA != "":
            if kolorA == "H":
                Tekst_Kolor = pygwidgets.DisplayText(ekran, (50, 10), "Wybrany kolor: KIER", fontSize = 20)
            elif kolorA == "D":
                Tekst_Kolor = pygwidgets.DisplayText(ekran, (50, 10), "Wybrany kolor: KARO", fontSize = 20)
            elif kolorA == "C":
                Tekst_Kolor = pygwidgets.DisplayText(ekran, (50, 10), "Wybrany kolor: TREFLE", fontSize = 20)
            elif kolorA == "P":
                Tekst_Kolor = pygwidgets.DisplayText(ekran, (50, 10), "Wybrany kolor: PIKI", fontSize = 20)
            Tekst_Kolor.show()
            Tekst_Kolor.draw()
        else:
            Tekst_Kolor.hide()
        if pobieranie23 != 0:
            Tekst_Dobieranie = pygwidgets.DisplayText(ekran, (50, 10), "Karty do dobrania (2, 3): " + str(pobieranie23), fontSize = 20)
            Tekst_Dobieranie.show()
            Tekst_Dobieranie.draw()
        else:
            Tekst_Dobieranie.hide()
        if pobieranieK != 0:
            Tekst_DobieranieK = pygwidgets.DisplayText(ekran, (50, 10), "Karty do dobrania (K): " + str(pobieranieK), fontSize = 20)
            Tekst_DobieranieK.show()
            Tekst_DobieranieK.draw()
        else:
            Tekst_DobieranieK.hide()
        for przycisk in przyciski_A:
            if pA:
                przycisk.show()
                przycisk.draw()
            else:
                przycisk.hide()
        for przycisk in przyciski_J:
            if rzadanie:
                przycisk.show()
                przycisk.draw()
            else:
                przycisk.hide()
        for przycisk in przyciski_makao:
            if kolej != "T":
                przycisk.disable()
            else:
                przycisk.enable()
            przycisk.show()
            przycisk.draw()
        for karta in twoje_karty:
            karta.obrocenie()
            karta.rysuj(ekran, 390 + (0 if len(twoje_karty) <= 1 else 240/(len(twoje_karty)-1)) * twoje_karty.index(karta), 500)
        for karta in botA.karty:
            karta.zakrycie()
            karta.rysuj(ekran, 320, 160 + (0 if len(botA.karty) <= 1 else 240/(len(botA.karty)-1)) * botA.karty.index(karta), obrocenie = True)
        for karta in botC.karty:
            karta.zakrycie()
            karta.rysuj(ekran, 680, 160 + (0 if len(botC.karty) <= 1 else 240/(len(botC.karty)-1)) * botC.karty.index(karta), obrocenie = True)
        for karta in botB.karty:
            karta.zakrycie()
            karta.rysuj(ekran, 390 + (0 if len(botB.karty) <= 1 else 240/(len(botB.karty)-1)) * botB.karty.index(karta), 40)
        if len(twoje_karty) == 0:
            stan = "wygranamakao"
            widzet()
        elif len(botA.karty) == 0 or len(botB.karty) == 0 or len(botC.karty) == 0:
            stan = "przegranamakao"
            widzet()
        stos_kladzenia[-1].obrocenie()
        stos_kladzenia[-1].rysuj(ekran, 480, 270)
        pygame.display.update()
        if kolej != "T":
            time.sleep(1)
        if t == 0:
            t = 1
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

            
def rysuj_stos(numerstosu, wybrane_karty):
    stos = eval(f'stos{numerstosu}')
    x = -10 + numerstosu * 50
    if len(stos) > 0:
        stos[-1].obrocenie()
        for karta in stos:
            karta.rysuj(ekran, x, 50 + (stos.index(karta)-1)*20, stan = stan, WYBRANA = WYBRANA, wybrane_karty = wybrane_karty)

def rysuj_stos_odrzucony(stos_odrzucony, wybrane_karty):
    x = 400
    if len(stos_odrzucony) > 0:
        stos_odrzucony[-1].obrocenie()
    for karta in stos_odrzucony:
        karta.rysuj(ekran, x, 50+(stos_odrzucony.index(karta)-1)*3, stan = stan, WYBRANA = WYBRANA, wybrane_karty = wybrane_karty)
 
def rysuj_stos_odrzucony2(stos_odrzucony2, wybrane_karty):
    x = 450
    for karta in stos_odrzucony2:
        karta.rysuj(ekran, x, 50+(stos_odrzucony2.index(karta)-1)*3, stan = stan, WYBRANA = WYBRANA, wybrane_karty = wybrane_karty)

def rysuj_stos_wzor(stos, x, wybrane_karty):
    if len(stos) > 0:
        stos[-1].rysuj(ekran, x, 50, stan = stan, WYBRANA = WYBRANA, wybrane_karty = wybrane_karty)


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
    global stan, TLO, ekran
    stos_kiery = []
    stos_karo = []
    stos_trefle = []
    stos_piki = []
    random.shuffle(KARTY)
    stos1 = KARTY[0:1]
    stos2 = KARTY[1:3]
    stos3 = KARTY[3:6]
    stos4 = KARTY[6:10]
    stos5 = KARTY[10:15]
    stos6 = KARTY[15:21]
    stos7 = KARTY[21:28]
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
                        stos_odrzucony.append(stos_odrzucony2[0])
                        stos_odrzucony2.pop(0)
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
        rysuj_stos(1, wybrane_karty)
        rysuj_stos(2)
        rysuj_stos(3)
        rysuj_stos(4)
        rysuj_stos(5)
        rysuj_stos(6)
        rysuj_stos(7)
        rysuj_stos_odrzucony(stos_odrzucony, wybrane_karty)
        rysuj_stos_odrzucony2(stos_odrzucony2, wybrane_karty)
        rysuj_stos_wzor(stos_kiery, 500, wybrane_karty)
        rysuj_stos_wzor(stos_karo, 540, wybrane_karty)
        rysuj_stos_wzor(stos_trefle, 580, wybrane_karty)
        rysuj_stos_wzor(stos_piki, 620, wybrane_karty)
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
                        elif przycisk == przyciski_gry[4]:
                            serca(0, 0, 0, 0)
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
                        elif przycisk == przyciski_zasady[3]:
                            stan = "zasadymakao"
            elif stan == "zasadypasjans" or stan == "zasadyoczko" or stan == "zasadymakao":
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

        if stan == "zasadymakao":
            Przycisk_Zasady_Wroc.show()
            Przycisk_Zasady_Wroc.draw()
            Tekst_ZasadyMakao1.show()
            Tekst_ZasadyMakao1.draw()
            Tekst_ZasadyMakao2.show()
            Tekst_ZasadyMakao2.draw()
            Tekst_ZasadyMakao3.show()
            Tekst_ZasadyMakao3.draw()
        else:
            Tekst_ZasadyMakao1.hide()
            Tekst_ZasadyMakao2.hide()
            Tekst_ZasadyMakao3.hide()
            
        if stan != "zasady" and stan != "zasadypasjans" and stan != "zasadyoczko" and stan != "zasadymakao":
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