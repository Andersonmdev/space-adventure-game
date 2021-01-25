# pylint: disable=no-member
import pygame as pg

from .game import game
from .score import score
from .help import howPlay
from ..utils.constants import (
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    MAIN_FONT,
    TITLE_FONT,
    DEFAULT_FONT_FIZE,
    WHITE,
    PINK,
)
from ..utils.path import getImagePath


def drawButton(screen, isHover, positionButton, buttonSize, text, positionText):
    font = pg.font.SysFont(MAIN_FONT, DEFAULT_FONT_FIZE)
    buttonIcon = pg.transform.scale(
        pg.image.load(getImagePath("\\icons\\button.jpg")), buttonSize
    )
    buttonIconPressed = pg.transform.scale(
        pg.image.load(getImagePath("\\icons\\button-pressed.jpg")), buttonSize
    )
    rect = pg.Rect(positionButton, buttonSize)
    if isHover:
        screen.blit(buttonIconPressed, positionButton)
    else:
        screen.blit(buttonIcon, positionButton)
    screen.blit(font.render(text, True, WHITE), positionText)
    return rect


def drawMenuButtons(screen, buttonHover):
    # Draw Buttons
    buttonSize = (250, 60)
    buttonRects = []
    # Play Button
    buttonRects.append(
        drawButton(screen, buttonHover[0], (275, 400), buttonSize, "JOGAR", (345, 405))
    )
    # Score Button
    buttonRects.append(
        drawButton(
            screen, buttonHover[1], (275, 500), buttonSize, "PONTUAÇÃO", (294, 505)
        )
    )
    # Help Button
    buttonRects.append(
        drawButton(
            screen, buttonHover[2], (275, 600), buttonSize, "COMO JOGAR", (287, 605)
        )
    )
    # Exit Button
    buttonRects.append(
        drawButton(screen, buttonHover[3], (275, 700), buttonSize, "SAIR", (359, 705))
    )
    return buttonRects


def drawBaseMenu(screen):
    screen.fill(WHITE)
    # Draw Images
    background = pg.transform.scale(
        pg.image.load(getImagePath("\\background\\main-bg.jpg")),
        (DISPLAY_WIDTH, DISPLAY_HEIGHT),
    )
    astronautIcon = pg.transform.scale(
        pg.image.load(getImagePath("\\icons\\astronaut.png")), (300, 400)
    )
    screen.blit(background, (0, 0))
    screen.blit(astronautIcon, (250, 0))
    # Draw Title
    fontTitle = pg.font.SysFont(TITLE_FONT, 45)
    screen.blit(fontTitle.render("AVENTURA", True, PINK), (50, 200))
    screen.blit(fontTitle.render("ESPACIAL", True, PINK), (550, 200))


def menu(screen):
    running = True
    drawBaseMenu(screen)
    buttonHover = [0, 0, 0, 0]
    while running:
        buttonRects = drawMenuButtons(screen, buttonHover)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                for index, button in enumerate(buttonRects):
                    if button.collidepoint(event.pos):
                        if index == 0:
                            game(screen)
                            drawBaseMenu(screen)
                            buttonHover = [0, 0, 0, 0]
                        elif index == 1:
                            score(screen)
                            drawBaseMenu(screen)
                            buttonHover = [0, 0, 0, 0]
                        elif index == 2:
                            howPlay(screen)
                            drawBaseMenu(screen)
                            buttonHover = [0, 0, 0, 0]
                        elif index == 3:
                            pg.quit()
                            quit()

        for index, button in enumerate(buttonRects):
            if button.collidepoint(pg.mouse.get_pos()):
                if index == 0:
                    buttonHover[index] = 1
                elif index == 1:
                    buttonHover[index] = 1
                elif index == 2:
                    buttonHover[index] = 1
                elif index == 3:
                    buttonHover[index] = 1
            else:
                buttonHover[index] = 0

        pg.display.update()
