from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome()

browser.get('http://uitestingplayground.com/classattr')

button = browser.find_element(By.CLASS_NAME, 'btn-primary')

button.click()
sleep(15)
