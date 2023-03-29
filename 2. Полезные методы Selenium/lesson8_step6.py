# Открыть страницу https://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, math

with webdriver.Firefox() as driver:
    driver.maximize_window()
    driver.get("http://suninjuly.github.io/execute_script.html")
    x = driver.find_element(By.ID, "input_value").text
    answer = str(math.log(abs(12 * math.sin(int(x)))))
    driver.find_element(By.ID, "answer").send_keys(answer)
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, 150);")
    driver.find_element(By.ID, "robotCheckbox").click()
    time.sleep(0.5)
    button = driver.find_element(By.ID, "robotsRule").click()
    time.sleep(0.5)
    #driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    time.sleep(6)