from selene import have
from selene.support.shared import browser


class Select:

    def __int__(self, locator, value):
        self.locator = locator
        self.value = value

    @staticmethod
    def select_by_text(locator, value):
        browser.element(locator).all('option').element_by(have.exact_text(value)).click()
