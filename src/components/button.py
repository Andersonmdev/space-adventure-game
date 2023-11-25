# font = pg.font.SysFont(MAIN_FONT, DEFAULT_FONT_FIZE)
#     buttonIcon = pg.transform.scale(
#         pg.image.load(getImagePath("\\icons\\button.jpg")), buttonSize
#     )
#     buttonIconPressed = pg.transform.scale(
#         pg.image.load(getImagePath("\\icons\\button-pressed.jpg")), buttonSize
#     )
#     rect = pg.Rect(positionButton, buttonSize)
#     if isHover:
#         screen.blit(buttonIconPressed, positionButton)
#     else:
#         screen.blit(buttonIcon, positionButton)
#     screen.blit(font.render(text, True, WHITE), positionText)
#     return rect
class Button:
    FONT = "Arial Black"
    FONT_SIZE = 30

    def __init__(self, text: str = "", position: tuple = (0, 0)):
        pass
