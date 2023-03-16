# Задание: поиск элемента по XPath

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

text_for_forms = ("Vasi", "Bon", "Moscow", "Russia")
count = 0

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    for form in browser.find_elements(By.TAG_NAME, 'input'):
        form.send_keys(text_for_forms[count])
        count += 1
    browser.find_element(By.XPATH, '/html/body/div[1]/form/div[6]/button[3]')\
    .click()
finally:
    time.sleep(4)
    browser.quit()