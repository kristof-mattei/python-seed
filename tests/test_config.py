from python_seed.config.config import Config


def test_config_something() -> None:
    config = Config("something!")

    assert config.get_something() == "something!"


def test_config_something_2() -> None:
    # uncomment to validate type-checking works accross modules
    # config = Config(5)

    # assert config.get_something() == 5

    pass
