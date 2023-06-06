from .base_page import BasePage
from .locators import ProductPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        self.basket_should_be_empty()
        self.text_about_empty_basket_should_be()

    def basket_should_be_empty(self):
        status_basket = self.browser.find_element(*ProductPageLocators.BASKET_IS_EMPTY)
        status_should_be = "Your basket is empty. Continue shopping"
        assert status_basket.text == status_should_be, "Корзина не является пустой"

    def text_about_empty_basket_should_be(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_IS_EMPTY), "Текст о пустой корзине отсутствует"
