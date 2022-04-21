from pygame import Surface, transform, image, font
from .screen import Screen
from ..utils.resources import Resources


class Menu(Screen):
    def __init__(self, surface: Surface):
        super().__init__(surface)
        self.set_running(True)

    def setup_base(self):
        self.surface.fill(self.WHITE)

        background = transform.scale(
            image.load(Resources.get_resource("main_bg.png")),
            (self.WIDTH, self.HEIGHT),
        )
        self.surface.blit(background, (0, 0))

        astronaut = transform.scale(image.load(
            Resources.get_resource("astronaut.png")),
            (300, 400),
        )
        self.surface.blit(astronaut, (250, 0))

        title_font = font.SysFont(self.TITLE_FONT, 45)
        self.surface.blit(title_font.render(
            "AVENTURA", True, self.PINK),
            (50, 200),
        )
        self.surface.blit(title_font.render(
            "ESPACIAL", True, self.PINK),
            (550, 200),
        )

    def draw(self):
        self.setup_base()
        if self.is_running():
            pass
