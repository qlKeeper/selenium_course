# Задание: оформляем тесты в стиле unittest 

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first[required]")\
            .send_keys("Vasily")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, ".second[required]")\
            .send_keys("Bondarenko")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, ".third[required]")\
            .send_keys("test@gmail.com")
        time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        final = "Congratulations! You have successfully registered!"
        self.assertEqual(final, welcome_text, "Final text error")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first[required]")\
            .send_keys("Vasily")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, ".second[required]")\
            .send_keys("Bondarenko")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, ".third[required]")\
            .send_keys("test@gmail.com")
        time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        final = "Congratulations! You have successfully registered!"
        self.assertEqual(final, welcome_text, "Final text error!")



if __name__ == "__main__":
    unittest.main()