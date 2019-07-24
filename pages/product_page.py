from .base_page import BasePage
from .locators import ProductPageLocators
import math
import time
from selenium.common.exceptions import NoAlertPresentException
class ProductPage(BasePage):
    def add_to_basket_and_solve_quiz(self):
        self.should_be_promo_url()
        self.get_product_name()
        self.get_product_price()
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        #self.check_if_added()

    def should_be_promo_url(self):
        promo_url = self.browser.current_url
        
        # реализуйте проверку на корректный url адрес
        assert "?promo=" in promo_url, "URL address in incorrect"

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        print("Product name from header: {}".format(product_name.text))
        return product_name.text
        
    def get_product_price(self):
        product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        print("Product price from the page: {}".format(product_price.text))
        return product_price.text
        
    def check_if_added(self):
        #time.sleep(2)
        
        chk_prdct_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        print("Product name from the message: {}".format(chk_prdct_name.text))
        #chk_prdct_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).find_element(*ProductPageLocators.ADDED_PRODUCT_NAME_TEXT)
        pr_name=self.get_product_name()
        #pr_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        #print(pr_name.text, pr_price.text, chk_prdct_name.text, chk_prdct_price.text)
        assert pr_name == chk_prdct_name.text, "{}".format(chk_prdct_name.text)