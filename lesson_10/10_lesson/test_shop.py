import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.main_shop_page import MainShopPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@allure.feature("Покупка в интернет-магазине")
@allure.story("Оформление заказа с заполнением формы")
def test_shop_purchase():
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        # Авторизация
        with allure.step("Авторизация пользователя"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

        # Добавление товаров в корзину
        with allure.step("Добавление товаров в корзину"):
            main = MainShopPage(driver)
            main.add_backpack_to_cart()
            main.add_bolt_tshirt_to_cart()
            main.add_onesie_to_cart()
            main.go_to_cart()

        # Переход к оформлению
        with allure.step("Переход к оформлению заказа"):
            cart = CartPage(driver)
            cart.click_checkout()

        # Заполнение формы и проверка суммы
        with allure.step("Заполнение формы и проверка итоговой суммы"):
            form = CheckoutPage(driver)
            form.fill_checkout_form("Иван", "Петров", "123456")
            total_price = form.get_total_price()
            assert total_price == "$58.29", f"Ожидалось $58.29, но получено: {total_price}"

    finally:
        driver.quit()