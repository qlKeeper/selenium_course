# Задание: использование метода find_elements


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")
time.sleep(1)

try:
    for form in browser.find_elements(By.TAG_NAME, "input"):
        form.send_keys("Мой ответ")
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(7)
    browser.quit()