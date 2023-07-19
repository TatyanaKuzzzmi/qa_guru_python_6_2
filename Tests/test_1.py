import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def test_first():
    browser.open('https://google.com')
    browser.driver.set_window_size(1920, 1080)
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
