from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    product_name = ''
    product_price = ''

    def add_product_to_cart(self):
        self.product_name_is()
        self.product_price_is()

        add_to_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_to_basket.click()
        self.solve_quiz_and_get_code()
        self.add_product_success_message()
        self.add_product_price_match()
        self.add_product_names_match()

    def product_name_is(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product Name is not found"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_price_is(self):
        assert  self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product Price is not found"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_product_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADD_MESSAGE), \
            "No message about successful addition "

    def add_product_names_match(self):
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert self.product_name == added_product_name, "Product and Added Product names don't match"

    def add_product_price_match(self):
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        assert self.product_price == added_product_price, "Product and Added Product prices don't match"
