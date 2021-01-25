# pylint: disable=no-member
import pygame as pg

from ..utils.constants import (
    WHITE,
    PINK,
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    TITLE_FONT,
    MAIN_FONT,
    RULES,
)
from ..utils.path import getImagePath


def howPlay(screen):
    running = True
    screen.fill(WHITE)
    background = pg.transform.scale(
        pg.image.load(getImagePath("\\background\\main-bg.jpg")),
        (DISPLAY_WIDTH, DISPLAY_HEIGHT),
    )
    screen.blit(background, (0, 0))

    fontTitle = pg.font.SysFont(TITLE_FONT, 40)
    pg.draw.rect(screen, WHITE, (250, 30, 310, 80))
    screen.blit(fontTitle.render("COMO JOGAR:", True, PINK), (260, 40))

    font = pg.font.SysFont(MAIN_FONT, 33)
    pg.draw.rect(screen, WHITE, (20, 130, 760, 390))
    screen.blit(
        font.render("1) Para movimentar a nave é utilizado as", True, PINK), (30, 130)
    )
    screen.blit(
        font.render("setas do teclados (esquerda e direita)", True, PINK), (50, 170)
    )
    screen.blit(
        font.render("2) Para atirar é utilizado a tecla de", True, PINK), (30, 220)
    )
    screen.blit(font.render("espaço", True, PINK), (50, 260))
    screen.blit(
        font.render("3) Para pausar o jogo, é necessario", True, PINK), (30, 310)
    )
    screen.blit(font.render("pressionar a tecla P", True, PINK), (50, 350))
    screen.blit(
        font.render("4) O jogador possui 3 vidas, que são", True, PINK), (30, 400)
    )
    screen.blit(
        font.render("mostradas na parte inferior esquerda", True, PINK), (50, 440)
    )

    buttonIcon = pg.transform.scale(
        pg.image.load(getImagePath("\\icons\\button.jpg")), (200, 60)
    )
    rectButtonReturn = pg.Rect((70, 700), (200, 60))
    screen.blit(buttonIcon, (70, 715))
    screen.blit(fontTitle.render("Voltar", True, WHITE), (110, 715))

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if rectButtonReturn.collidepoint(pg.mouse.get_pos()):
                    return

        pg.display.update()
