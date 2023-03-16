# Задание: поиск элемента по тексту в ссылке

import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")
text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:
    browser.find_element(By.LINK_TEXT, text).click()
    browser.find_element(By.NAME, "first_name").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(5)
    browser.quit()