from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Firefox
driver = webdriver.Firefox()

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Ждём появления текстового поля и находим его (на странице это поле input)
    wait = WebDriverWait(driver, 10)
    input_field = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "input"))
    )

    # Вводим текст 12345
    input_field.send_keys("12345")
    print("Введён текст: 12345")

    # Очищаем поле
    input_field.clear()
    print("Поле очищено")

    # Вводим новый текст 54321
    input_field.send_keys("54321")
    print("Введён текст: 54321")

finally:
    # Закрываем браузер
    driver.quit()
    print("Браузер закрыт")
