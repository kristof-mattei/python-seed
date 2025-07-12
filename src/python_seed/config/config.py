class Config:
    """Insert description here"""

    something: str

    def __init__(self, something: str):
        self.something = something

    def dump(self) -> None:
        print(self.something)

    def get_something(self) -> str:
        return self.something

    def get_something_2(self) -> int:
        return 5
