from os import path, getcwd


class Resources:
    """
    Class to controller the resources used in the game
    """

    @classmethod
    def get_resource(cls, name: str):
        return path.join(getcwd(), 'resources', 'graphics', name)
