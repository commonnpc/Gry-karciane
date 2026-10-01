import pygame
import pygwidgets
import sys

CZARNY = (0, 0, 0)
SZEROKOSC = 800
WYSOKOSC = 600
KLATKI_NA_SEKUNDE = 60

pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Pasjans")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ekran.fill(CZARNY)
    pygame.display.flip()
    clock.tick(KLATKI_NA_SEKUNDE)