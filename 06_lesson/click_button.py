from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

# Открываем страницу
driver.get("http://uitestingplayground.com/ajax")

# Ждём появления кликабельной кнопки и находим её
wait = WebDriverWait(driver, 10)
button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
)
button.click()

# Ожидание появления зелёной плашки и получение текста
green_alert = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
)
text = green_alert.text

# Вывод в консоль
print(text)  # Ожидается: "Data loaded with AJAX get request."

# Закрытие браузера
driver.quit()
