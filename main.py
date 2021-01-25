# pylint: disable=no-member
import pygame as pg

from game.utils.constants import DISPLAY_WIDTH, DISPLAY_HEIGHT
from game.screens.menu import menu

pg.init()
screen = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("AVENTURA ESPACIAL")


def main():
    while True:
        menu(screen)


main()
pg.quit()
quit()
