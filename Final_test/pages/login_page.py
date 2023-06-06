from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Word 'login' not in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        user_email_generator = str(time.time()) + "@fakemail.org"
        user_password = str(time.time())
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL).send_keys(user_email_generator)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_1).send_keys(user_password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_2).send_keys(user_password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
