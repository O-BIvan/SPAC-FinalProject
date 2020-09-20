from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Page's URL doesn't contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Page doesn't contain: login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Page doesn't contain: register form"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        password_field.send_keys(password)
        password_confirm = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_CONFIRM)
        password_confirm.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_button.click()



