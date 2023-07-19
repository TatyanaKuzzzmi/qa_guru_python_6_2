from selene.support.shared import browser
from selene import be, have


def test_second():
    random_name = 'kjndsfgdfbgiperbg94q528tg245tyrtg'
    browser.element('[name="q"]').should(be.blank).type(random_name).press_enter()
    browser.element('[id="topstuff"]').should(have.text(f'По запросу {random_name} ничего не найдено.'))
    print('При поиске по произвольной строке ничего не находится')

