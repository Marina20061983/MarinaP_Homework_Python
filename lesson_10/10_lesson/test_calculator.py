import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.calculator_page import SlowCalculatorPage

@allure.title("Тест: проверка работы медленного калькулятора (7 + 8)")
def test_slow_calculator():
    driver = webdriver.Chrome()
    page = SlowCalculatorPage(driver)

    with allure.step("Открыть страницу медленного калькулятора"):
        page.open()

    with allure.step("Установить задержку 3 секунды"):
        page.set_delay(3)

    with allure.step("Нажать кнопки: 7, +, 8, ="):
        page.click_button_7()
        page.click_plus()
        page.click_button_8()
        page.click_equals()

    with allure.step("Проверить, что результат равен 15"):
        assert page.get_result() == "15"

    driver.quit()