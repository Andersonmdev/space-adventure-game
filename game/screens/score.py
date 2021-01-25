# pylint: disable=no-member
import pygame as pg

from ..utils.constants import (
    WHITE,
    PINK,
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    TITLE_FONT,
    MAIN_FONT,
)
from ..utils.path import getImagePath
from ..utils.data import load


def showScores(screen, data, font):
    dy = 165
    for index, value in enumerate(data):
        if value != "":
            screen.blit(
                font.render(
                    str(index + 1)
                    + ") "
                    + str(value["score"])
                    + " pontos em "
                    + value["date"],
                    True,
                    PINK,
                ),
                (100, dy),
            )
            dy += 40


def score(screen):
    running = True
    screen.fill(WHITE)
    background = pg.transform.scale(
        pg.image.load(getImagePath("\\background\\main-bg.jpg")),
        (DISPLAY_WIDTH, DISPLAY_HEIGHT),
    )
    screen.blit(background, (0, 0))
    fontTitle = pg.font.SysFont(TITLE_FONT, 40)
    pg.draw.rect(screen, WHITE, (80, 50, 650, 80))
    screen.blit(fontTitle.render("AS 10 MAIORES PONTUAÇÕES:", True, PINK), (90, 60))

    font = pg.font.SysFont(MAIN_FONT, 30)
    data = load()[1]
    data = data.split(";")
    finalData = []
    for value in data[:-1]:
        value = value.split(",")
        aux = {"score": value[0], "date": value[1]}
        finalData.append(aux)
    data = sorted(finalData, key=lambda k: int(k["score"]), reverse=True)

    showScores(screen, data[0:10], font)

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
