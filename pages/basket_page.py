from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_empty()
        self.should_be_empty_basket_message()

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CHECKOUT), "Basket is not empty, but should be"

    def should_be_empty_basket_message(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        print(basket_message)
        assert "Your basket is empty" in basket_message, \
            "Basket empty message is not present or different from expected"

