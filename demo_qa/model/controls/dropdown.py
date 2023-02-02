from selene import have
from selene.support.shared import browser


class Dropdown:

    def __int__(self, locator, text):
        self.locator = locator
        self.text = text

    @staticmethod
    def choose(locator, text):
        browser.element(locator).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(text)).click()
