# Задание: поиск сокровища с помощью get_attribute

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    answer = str(math.log(abs(12*math.sin(int(x)))))
    time.sleep(1)
    browser.find_element(By.ID, "answer").send_keys(answer)
    time.sleep(1)
    browser.find_element(By.ID, "robotCheckbox").click()
    time.sleep(1)
    browser.find_element(By.ID, "robotsRule").click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

finally:
    time.sleep(4)
    browser.quit()
