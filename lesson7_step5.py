from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    time.sleep(1)
    x = browser.find_element(By.ID, "input_value").text
    answer = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
finally:
    time.sleep(5)
    browser.quit()
