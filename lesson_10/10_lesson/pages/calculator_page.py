import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

        self.delay_input = (By.ID, "delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.screen = (By.CLASS_NAME, "screen")

    @allure.step("Открыть сайт медленного калькулятора")
    def open(self):
        """метод открывает сайт"""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить задержку: {delay} сек")
    def set_delay(self, delay):
        element = self.wait.until(EC.element_to_be_clickable(self.delay_input))
        element.clear()
        element.send_keys(delay)

    @allure.step("Нажать кнопку 7")
    def click_button_7(self):
        self.wait.until(EC.element_to_be_clickable(self.button_7)).click()

    @allure.step("Нажать кнопку 8")
    def click_button_8(self):
        self.wait.until(EC.element_to_be_clickable(self.button_8)).click()

    @allure.step("Нажать кнопку +")
    def click_plus(self):
        self.wait.until(EC.element_to_be_clickable(self.button_plus)).click()

    @allure.step("Нажать кнопку =")
    def click_equals(self):
        self.wait.until(EC.element_to_be_clickable(self.button_equals)).click()

    @allure.step("Получить результат с экрана калькулятора")
    def get_result(self):
        # lambda можно оставить, но лучше явно ждать текст
        self.wait.until(lambda driver: self.driver.find_element(*self.screen).text == "15")
        element = self.wait.until(EC.visibility_of_element_located(self.screen))
        return element.text

    @allure.step("Выполнить расчёт 7 + 8")
    def perform_calculation_7_plus_8(self):
        self.click_button_7()
        self.click_plus()
        self.click_button_8()
        self.click_equals()