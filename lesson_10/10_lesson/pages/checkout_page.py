import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_price_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнение формы оформления заказа: имя={first_name}, фамилия={last_name}, индекс={postal_code}")
    def fill_checkout_form(self, first_name, last_name, postal_code):
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        )
        first_name_field.send_keys(first_name)

        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_input)
        )
        last_name_field.send_keys(last_name)

        postal_code_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.postal_code_input)
        )
        postal_code_field.send_keys(postal_code)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    @allure.step("Получение итоговой суммы заказа")
    def get_total_price(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_price_label)
        )
        total_text = total_element.text.replace("Total: ", "")
        return total_text