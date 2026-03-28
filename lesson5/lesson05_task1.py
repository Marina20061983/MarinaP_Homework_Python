from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Ждём появления кликабельной кнопки и находим её
    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )

    # Кликаем на синюю кнопку
    button.click()
    print("Синяя кнопка успешно нажата!")

finally:
    # Закрываем браузер
    driver.quit()
    print("Браузер закрыт")
