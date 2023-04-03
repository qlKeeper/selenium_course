# Задание: переход на новую вкладку

# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("http://suninjuly.github.io/redirect_accept.html")
    time.sleep(1)
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    driver.switch_to.window(windows[1])
    x = driver.find_element(By.ID, "input_value").text
    answer = str(math.log(abs(12*math.sin(int(x)))))
    driver.find_element(By.ID, "answer").send_keys(answer)
    driver.find_element(By.TAG_NAME, 'button').click()
    time.sleep(5)