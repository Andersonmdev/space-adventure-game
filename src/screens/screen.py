from pygame import Surface


class Screen(object):
    """
    Base class for all screens, contains the surface to draw on
    """
    WIDTH = 800
    HEIGHT = 800

    TITLE_FONT = "Comic Sans MS"

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PINK = (206, 31, 242)
    BLUE = (140, 113, 226)

    def __init__(self, surface: Surface):
        self.surface = surface
        self.running = False

    def get_surface(self):
        return self.surface

    def set_running(self, running: bool):
        self.running = running

    def is_running(self):
        return self.running

    def draw(self):
        """
        Method to be implemented by the child classes
        for drawing on the surface
        """
        raise NotImplementedError("draw method not implemented")
