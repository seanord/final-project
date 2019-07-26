from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import Remote
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage:
    def __init__(self, browser: Remote, url: str) -> None:

        super().__init__()
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)

    def open(self) -> None:

        self.browser.get(self.url)
    
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how: str, what: str) -> bool:

        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True


    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False