from .base_page import BasePage
from .locators import ProductPageLocators


class MainPage(BasePage):
    class MainPage(BasePage):
        def __init__(self, *args, **kwargs):
            super(MainPage, self).__init__(*args, **kwargs)

    def push_button(self):
        button_1 = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button_1.click()
