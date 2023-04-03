# Задание: принимаем alert

# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("http://suninjuly.github.io/alert_accept.html")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    alert = driver.switch_to.alert
    alert.accept()
    x = driver.find_element(By.ID, "input_value").text
    answer = str(math.log(abs(12*math.sin(int(x)))))
    driver.find_element(By.ID, "answer").send_keys(answer)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
