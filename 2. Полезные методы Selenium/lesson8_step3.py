# Задание: работа с выпадающим списком

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    select = Select(browser.find_element(By.ID, "dropdown"))
    num_1 = int(browser.find_element(By.ID, "num1").text)
    num_2 = int(browser.find_element(By.ID, "num2").text)
    select.select_by_value(str(num_1 + num_2))
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

finally:
    time.sleep(4)
    browser.quit()