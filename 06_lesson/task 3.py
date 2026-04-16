from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Установка веб-драйвера для Chrome
browser = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()
    )
)

# Переход на сайт
browser.get("https://bonigarcia.dev/selenium-webdriver-java/\
loading-images.html")


wait = WebDriverWait(browser, 40)
img3 = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "#image-container img:nth-of-type(3)")
    )
)

print(img3[0].get_attribute("src"))

browser.quit()
