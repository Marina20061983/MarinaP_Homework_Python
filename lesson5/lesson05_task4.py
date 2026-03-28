from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def main():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()

    try:
        # Открываем страницу логина
        driver.get("https://the-internet.herokuapp.com/login")

        # Ждём появления поля username и вводим значение
        wait = WebDriverWait(driver, 10)
        username_field = wait.until(
            EC.element_to_be_clickable((By.ID, "username"))
        )
        username_field.send_keys("tomsmith")
        print("Введено имя пользователя: tomsmith")

        # Находим поле password и вводим значение
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        print("Введён пароль: SuperSecretPassword!")

        # Находим и нажимаем кнопку Login
        login_button = driver.find_element(By.CSS_SELECTOR,
                                           "button[type='submit']")

        login_button.click()
        print("Нажата кнопка Login")

        # Ждём появления зелёной плашки с сообщением об успехе
        success_message = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "flash.success"))
        )

        # Получаем текст сообщения и выводим в консоль
        message_text = success_message.text.strip()
        # Убираем иконки «×» и прочие символы вокруг текста
        clean_message = message_text.replace("×", "").strip()
        print("\n=== ТЕКСТ С ЗЕЛЁНОЙ ПЛАШКИ ===")
        print(clean_message)
        print("=" * 30)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        # Даём немного времени, чтобы увидеть результат (опционально)
        time.sleep(2)
        # Закрываем браузер
        driver.quit()
        print("\nБраузер закрыт")


if __name__ == "__main__":
    main()
