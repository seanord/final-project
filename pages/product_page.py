from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_LINK).click()

        #if is_promo:
        self.solve_quiz_and_get_code()
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print(f"Your code: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def check_if_added(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not present"
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_CART), "No product has been added to cart"

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def should_be_present_in_cart(self):
        self.check_if_added()
        chk_prdct_name = self.browser.find_element(*ProductPageLocators.ADDED_TO_CART).text
        pr_name = self.get_product_name()
        assert pr_name == chk_prdct_name, "Wrong item has been added to cart"

    def check_total_cost(self) -> None:
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not present"
        assert self.is_element_present(*ProductPageLocators.CART_STATUS_LINK), "No alert with the price"
        chk_prdct_price = self.browser.find_element(*ProductPageLocators.CART_STATUS_LINK).text.split()[-1]
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_cost == chk_prdct_price, "Wrong cost"