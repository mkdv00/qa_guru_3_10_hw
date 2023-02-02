from selene import have
from selene.support.shared import browser


class Radio:

    def __int__(self, locator, value):
        self.locator = locator
        self.value = value

    @staticmethod
    def radio_button(locator, value):
        browser.all(locator).element_by(have.value(value)).element('..').click()
