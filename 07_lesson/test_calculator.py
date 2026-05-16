from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.calculator_page import SlowCalculatorPage


def test_slow_calculator():

    driver = webdriver.Chrome()
    page = SlowCalculatorPage(driver)
    page.open()
    page.set_delay(3)
    page.click_button_7()
    page.click_plus()
    page.click_button_8()
    page.click_equals()
    assert page.get_result() =="15"


    driver.quit()
