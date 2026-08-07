import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Нажатие кнопки Checkout")
    def click_checkout(self) ->None:
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()
