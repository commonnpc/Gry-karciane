import pygame

TLO = (178, 227, 146)
SZEROKOSC = 800
WYSOKOSC = 600
KLATKI_NA_SEKUNDE = 60
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
clock = pygame.time.Clock()

def zmientlo(tlo):
    global TLO
    TLO = tlo