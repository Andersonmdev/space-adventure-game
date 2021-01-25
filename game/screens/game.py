# pylint: disable=no-member
import pygame as pg
import random
import time
from datetime import datetime

from ..utils.constants import (
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    TITLE_FONT,
    WHITE,
    PINK,
    BLUE,
    WORDS_LIST,
    MAIN_FONT,
)
from ..utils.path import getImagePath
from ..utils.data import save


def drawBaseGame(screen, background, heartIcon, lifes, word):
    screen.blit(background, (0, 0))
    pg.draw.rect(screen, PINK, (0, 0, DISPLAY_WIDTH, 50))
    pg.draw.rect(screen, BLUE, (0, 0, 100, 50))
    pg.draw.rect(screen, BLUE, (700, 0, 100, 50))
    font = pg.font.SysFont(TITLE_FONT, 30)
    text = font.render(word, True, WHITE)
    screen.blit(text, (DISPLAY_WIDTH / 2 - text.get_rect().width / 2, 5))
    if lifes == 3:
        screen.blit(heartIcon, (20, 750))
        screen.blit(heartIcon, (70, 750))
        screen.blit(heartIcon, (120, 750))
    elif lifes == 2:
        screen.blit(heartIcon, (20, 750))
        screen.blit(heartIcon, (70, 750))
    elif lifes == 1:
        screen.blit(heartIcon, (20, 750))


def drawFires(screen, fireIcon, fires, dt):
    for fire in fires:
        if fire[1] > 61:
            fire[1] -= 0.5 * dt
            screen.blit(fireIcon, (fire[0], fire[1]))
        else:
            fires.pop(0)
    return fires


def drawScore(screen, score):
    font = pg.font.SysFont(TITLE_FONT, 30)
    text = font.render(str(score), True, WHITE)
    screen.blit(text, (750 - text.get_rect().width / 2, 5))


def drawTime(screen, start):
    font = pg.font.SysFont(TITLE_FONT, 30)
    text = f"{int(time.time() - start)} s"
    screen.blit(font.render(text, True, WHITE), (5, 5))


def drawAlphabet(screen, alphabet, dt):
    for l in alphabet:
        screen.blit(l["icon"], (l["position"][0], l["position"][1] + 50))
        l["position"][1] += 0.2 * dt
        if l["position"][1] > 590:
            alphabet.pop(0)


def drawPlanet(screen, planets, dt):
    for p in planets:
        value = WORDS_LIST.index(p["value"])
        img = pg.transform.scale(
            pg.image.load(getImagePath(f"\\planets\\{value}.png")), (100, 100)
        )
        screen.blit(img, (p["position"][0], p["position"][1]))
        p["position"][1] += 0.2 * dt
        if p["position"][1] > 600:
            planets.pop(0)


def checkCollisionFires(fires, alphabet, planets):
    for i, fire in enumerate(fires):
        for j, l in enumerate(alphabet):
            if (
                fire[1] < l["position"][1] + 145
                and l["position"][0] - 5 < fire[0]
                and l["position"][0] + 105 > fire[0] + 30
            ):
                fires.pop(i)
                alphabet.pop(j)
                return 10
        for k, p in enumerate(planets):
            if (
                (fire[1] < p["position"][1] + 105)
                and (fire[0] > p["position"][0] - 5)
                and (fire[0] < p["position"][0] + 105)
            ):
                fires.pop(i)
                planets.pop(k)
                return 20
    return 0


def checkCollisionShip(shipPosition, alphabet, planets):
    shipRect = pg.Rect(shipPosition, (80, 140))
    for i, l in enumerate(alphabet):
        alphabetRect = ((l["position"][0], l["position"][1] + 40), (100, 100))
        if shipRect.colliderect(alphabetRect):
            alphabet.pop(i)
            return True
    for j, p in enumerate(planets):
        planetRect = ((p["position"][0], p["position"][1] + 5), (100, 100))
        if shipRect.colliderect(planetRect):
            planets.pop(j)
            return True
    return False


def pauseGame(screen):
    fontTitle = pg.font.SysFont(MAIN_FONT, 60)
    font = pg.font.SysFont(MAIN_FONT, 28)
    buttonIcon = pg.transform.scale(
        pg.image.load(getImagePath("\\icons\\button.jpg")), (200, 60)
    )
    rectButton1 = pg.Rect((160, 400), (200, 60))
    rectButton2 = pg.Rect((460, 400), (200, 60))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                return
            if event.type == pg.MOUSEBUTTONDOWN:
                if rectButton1.collidepoint(pg.mouse.get_pos()):
                    return
                if rectButton2.collidepoint(pg.mouse.get_pos()):
                    pg.quit()
                    quit()

        screen.blit(fontTitle.render("PAUSADO", True, WHITE), (250, 200))
        screen.blit(buttonIcon, (160, 400))
        screen.blit(font.render("Continuar", True, WHITE), (183, 410))
        screen.blit(buttonIcon, (460, 400))
        screen.blit(font.render("Sair", True, WHITE), (530, 410))
        pg.display.update()


def generateEnemy(alphabet, planets, currentPlanet, option):
    if option:
        letter = chr(random.randint(65, 90))
        random_x = random.randint(2, 698)
        aux = {
            "value": letter,
            "icon": pg.transform.scale(
                pg.image.load(getImagePath(f"\\alphabet\\{letter.lower()}.png")),
                (100, 100),
            ),
            "position": [random_x, 0],
        }
        alphabet.append(aux)
    else:
        random_x = random.randint(51, 549)
        newPlanet = {"value": currentPlanet, "position": [random_x, 105]}
        planets.append(newPlanet)


def isEnd(time, lifes):
    if time >= 120 or lifes <= 0:
        return True
    return False


def endGame(screen, score):
    fontTitle = pg.font.SysFont(MAIN_FONT, 50)
    font = pg.font.SysFont(MAIN_FONT, 28)
    buttonIcon = pg.transform.scale(
        pg.image.load(getImagePath("\\icons\\button.jpg")), (200, 60)
    )
    rectButton1 = pg.Rect((160, 400), (200, 60))
    rectButton2 = pg.Rect((460, 400), (200, 60))
    isSave = False

    date = datetime.now()
    if save(str(score) + "," + date.strftime("%d/%m/%Y-%H:%M:%S") + ";"):
        isSave = True

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                return
            if event.type == pg.MOUSEBUTTONDOWN:
                if rectButton1.collidepoint(pg.mouse.get_pos()):
                    return
                if rectButton2.collidepoint(pg.mouse.get_pos()):
                    pg.quit()
                    quit()

        if isSave:
            screen.blit(
                fontTitle.render(f"Sua pontuação foi salva!", True, WHITE), (70, 200)
            )
        else:
            screen.blit(fontTitle.render(f"Erro ao salvar!", True, WHITE), (100, 200))
        screen.blit(buttonIcon, (160, 400))
        screen.blit(font.render("Inicio", True, WHITE), (220, 410))
        screen.blit(buttonIcon, (460, 400))
        screen.blit(font.render("Sair", True, WHITE), (530, 410))
        pg.display.update()


def game(screen):
    running = True
    screen.fill(WHITE)
    # Load Images
    background = pg.transform.scale(
        pg.image.load(getImagePath("\\background\\game-bg.jpg")),
        (DISPLAY_WIDTH, DISPLAY_HEIGHT),
    )
    heartIcon = pg.transform.scale(
        pg.image.load(getImagePath("\\icons\\heart.png")), (40, 40)
    )
    shipIcon = pg.transform.scale(
        pg.image.load(getImagePath("\\icons\\space-ship.png")), (70, 130)
    )
    fireIcon = pg.transform.scale(
        pg.image.load(getImagePath("\\icons\\shot.png")), (30, 30)
    )

    alphabet = []
    shipPosition = [380, 600]
    fires = []
    lifes = 3
    score = 0
    currentTimePlanet = pg.time.get_ticks()
    currentTimeAlphabet = pg.time.get_ticks()
    startTime = time.time()
    currentPlanet = WORDS_LIST[random.randint(0, 7)]
    planets = []
    dt = pg.time.Clock().tick(60)
    while running:
        pressed = pg.key.get_pressed()
        if pressed[pg.K_LEFT]:
            if shipPosition[0] > 3:
                shipPosition[0] -= 0.8 * dt
        elif pressed[pg.K_RIGHT]:
            if shipPosition[0] < 707:
                shipPosition[0] += 0.8 * dt

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                fires.append([shipPosition[0] + 25, shipPosition[1] - 30])
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                startTimePause = time.time()
                pauseGame(screen)
                startTime += time.time() - startTimePause

        addValue = checkCollisionFires(fires, alphabet, planets)
        score += addValue

        if checkCollisionShip(shipPosition, alphabet, planets):
            lifes -= 1

        if (pg.time.get_ticks() - currentTimeAlphabet > 1000) and (
            pg.time.get_ticks() - currentTimePlanet < 10000
        ):
            generateEnemy(alphabet, planets, currentPlanet, True)
            currentTimeAlphabet = pg.time.get_ticks()
        elif pg.time.get_ticks() - currentTimePlanet >= 12000:
            generateEnemy(alphabet, planets, currentPlanet, False)
            currentPlanet = WORDS_LIST[random.randint(0, 7)]
            currentTimeAlphabet = pg.time.get_ticks()
            currentTimePlanet = pg.time.get_ticks()

        if isEnd(int(time.time() - startTime), lifes):
            endGame(screen, score)
            return

        drawBaseGame(
            screen, background, heartIcon, lifes, f"Planeta atual: {currentPlanet}"
        )
        drawScore(screen, score)
        drawTime(screen, startTime)
        screen.blit(shipIcon, shipPosition)
        drawFires(screen, fireIcon, fires, dt)
        drawAlphabet(screen, alphabet, dt)
        drawPlanet(screen, planets, dt)

        pg.display.update()
