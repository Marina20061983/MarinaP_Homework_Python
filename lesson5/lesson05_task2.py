from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Настройка драйвера Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открытие браузера и переход на страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Ожидание загрузки страницы и поиск синей кнопки
    # Предполагаем, что кнопка имеет какой‑то отличительный класс или текст
    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

    # Клик по кнопке
    button.click()

    print("Клик выполнен успешно!")

finally:
    # Закрытие браузера через несколько секунд
    import time

    time.sleep(3)
    driver.quit()
