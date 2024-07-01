""" I'm a config module """


class Config:
    """I'm a config class"""

    some_thing: int

    def __init__(self, some_thing: int):
        self.some_thing = some_thing

    def dump(self):
        """I'm a method"""
        print(self.some_thing)
