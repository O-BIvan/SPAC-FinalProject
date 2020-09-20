from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_CHECKOUT = (By.CSS_SELECTOR, "a.btn-primary")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form button.btn-primary")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button.btn-primary")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    SUCCESS_ADD_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child")
    BASKET_ADD_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
