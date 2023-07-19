import pytest
@pytest.fixture(scope="module")
def browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080