from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.main_shop_page import MainShopPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_shop_purchase():
    driver = webdriver.Firefox()
    driver.maximize_window()
        #Авторизация
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    #Добавление товара в корзину
    main = MainShopPage(driver)
    main.add_backpack_to_cart()
    main.add_bolt_tshirt_to_cart()
    main.add_onesie_to_cart()
    main.go_to_cart()
    # Нажимаем оформить
    cart = CartPage(driver)
    cart.click_checkout()
    # Заполняем форму
    form = CheckoutPage(driver)
    form.fill_checkout_form("Иван", "Петров", "123456")
    assert form.get_total_price() == "$58.29"

    driver.quit()