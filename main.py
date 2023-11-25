import sys
import pygame
from src.screens.menu import Menu

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Space Adventure")
    surface = pygame.display.set_mode((800, 800))
    menu = Menu(surface)
    while True:
        menu.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
