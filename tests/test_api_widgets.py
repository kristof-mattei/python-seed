from python_seed.api import widgets


def test_widgets_get() -> None:
    assert widgets.get() == ["Widget1", "Widget2"]
