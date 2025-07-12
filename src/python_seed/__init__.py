"""Main module"""

import traceback

from .config.config import Config


def main() -> None:
    """Main"""
    traceback.print_stack()

    print("Hello from python-seed!")

    config = Config("some value")

    config.dump()
