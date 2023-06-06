from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def can_add_product_to_basket(self):
        self.message_product_add()
        self.product_name_equal()
        self.message_product_price()
        self.product_price()

    def message_product_add(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADD), "НЕТ сообщение о добавлении товара в корзину"

    def product_name_equal(self):
        productname_1 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IS)
        productname_2 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_SHOULD_BE)
        assert productname_1.text == productname_2.text, "Названия товара отличаются"

    def message_product_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_PRICE), "НЕТ сообщения со стоимостью корзины"

    def product_price(self):
        productprice_1 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IS)
        productprice_2 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_SHOULD_BE)
        assert productprice_1.text == productprice_2.text, "Цены товара отличаются"

    def push_button(self):
        button_1 = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button_1.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение отображается, хотя должно исчезать после 4 сек"
