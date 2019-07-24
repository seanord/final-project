from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators(object):
    BASKET_LINK = (By.CLASS_NAME, "btn-add-to-basket")
    
    #ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    #ADDED_PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, "strong")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    #ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")


