from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Устанавливаем драйвер для Chrome
browser = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()
    )
)

try:
    # Переходим на указанный сайт
    browser.get("http://uitestingplayground.com/textinput")

    # Находим поле ввода и вводим текст "SkyPro"
    text_input = browser.find_element(By.ID, "newButtonName")
    text_input.send_keys("SkyPro")

    # Находим синюю кнопку и нажимаем на нее
    button = browser.find_element(By.ID, "updatingButton")
    button.click()

    # Получаем текст кнопки и выводим его в консоль
    button_text = button.text
    print(button_text)

finally:
    # Закрываем браузер
    browser.quit()
