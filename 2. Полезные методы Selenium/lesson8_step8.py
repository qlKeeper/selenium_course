# Задание: загрузка файла

# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Firefox() as driver:
    driver.maximize_window()
    driver.get("http://suninjuly.github.io/file_input.html")
    forms = driver.find_elements(By.XPATH, "//input[@type='text']")
    forms[0].send_keys("Pasha")
    forms[1].send_keys("Rogov")
    forms[2].send_keys("rogovVip@ya.ru")
    time.sleep(0.5)
    driver.find_element(By.ID, "file").send_keys("~/Downloads/test.txt")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    time.sleep(6)