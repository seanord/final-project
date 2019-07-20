from pages.product_page import ProductPage

from selenium.common.exceptions import NoAlertPresentException # в начале файла

def test_guest_can_add_product_to_cart(browser):

    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_and_solve_quiz()

