from pasjans_gra import pasjans
import pygwidgets
import pygame
import sys
import zmienne_wspólne

stan = "menu"
przyciski_gry = []
przyciski_menu = []
przyciski_opcje = []
pygame.init()
pygame.display.set_caption("Zbiór gier")

Przycisk_Pasjans = pygwidgets.TextButton(zmienne_wspólne.ekran, (100,100), "Pasjans",
                                          fontSize = 30, width = 250, height = 100, 
                                          upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Graj = pygwidgets.TextButton(zmienne_wspólne.ekran, (200, 190), "Graj",
                                          fontSize = 30, width = 400, height = 100, 
                                          upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Opcje = pygwidgets.TextButton(zmienne_wspólne.ekran, (200, 320), "Opcje",
                                        fontSize = 30, width = 400, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Wyjscie = pygwidgets.TextButton(zmienne_wspólne.ekran, (200, 450), "Wyjście",
                                        fontSize = 30, width = 400, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Tekst_Tytul = pygwidgets.DisplayText(zmienne_wspólne.ekran, (200, 50), "Gry Karciane", 
                                     fontSize = 90, width = 400, height = 100)

Przycisk_Zasady = pygwidgets.TextButton(zmienne_wspólne.ekran, (200, 190), "Zasady",
                                        fontSize = 30, width = 400, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Przycisk_Wroc = pygwidgets.TextButton(zmienne_wspólne.ekran, (200, 450), "Wróć",
                                        fontSize = 30, width = 400, height = 100, 
                                        upColor = (38, 132, 232), overColor = (42, 187, 223), downColor = (42, 223, 187))

Kwadracik_Tryb_Ciemny = pygwidgets.TextCheckBox(zmienne_wspólne.ekran, (200, 320), "Tryb ciemny", value = False, fontSize = 60, size = 50)


przyciski_gry.append(Przycisk_Pasjans)
przyciski_menu.append(Przycisk_Graj)
przyciski_menu.append(Przycisk_Opcje)
przyciski_menu.append(Przycisk_Wyjscie)
przyciski_opcje.append(Przycisk_Zasady)
przyciski_opcje.append(Przycisk_Wroc)

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
                        pasjans()
        elif stan == "opcje":
            for przycisk in przyciski_opcje:
                if przycisk.handleEvent(event):
                    if przycisk == przyciski_opcje[0]:
                        stan = "zasady"
                    if przycisk == przyciski_opcje[1]:
                        stan = "menu"
                if Kwadracik_Tryb_Ciemny.handleEvent(event):
                    if Kwadracik_Tryb_Ciemny.value == True:
                        zmienne_wspólne.zmientlo((49, 61, 41))
                    else:
                        zmienne_wspólne.zmientlo((178, 227, 146))

    zmienne_wspólne.ekran.fill(zmienne_wspólne.TLO)
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


    pygame.display.update()
    zmienne_wspólne.clock.tick(zmienne_wspólne.KLATKI_NA_SEKUNDE)