""" Main module """

from .config.config import Config


def main():
    """Main"""

    config = Config(5)

    config.dump()


main()
