from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def add_to_basket_and_solve_quiz(self):
        self.should_be_promo_url()
        self.add_to_basket()
        self.solve_quiz_and_get_code()

    def should_be_promo_url(self):
        promo_url = self.browser.current_url
        
        # реализуйте проверку на корректный url адрес
        assert "?promo=newYear" in promo_url, "URL address in incorrect"

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