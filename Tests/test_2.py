import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def test_second():
    browser.open('https://google.com')
    browser.driver.set_window_size(1920, 1080)
    browser.element('[name="qwerty"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    response = "Поиск не выдает результатов"
    return response
