# Задание: ждем нужный текст на странице

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.get(" http://suninjuly.github.io/explicit_wait2.html")
    wait = WebDriverWait(driver, 13)
    
    if wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100')):
        driver.find_element(By.ID, 'book').click()
    x = driver.find_element(By.ID, 'input_value').text
    answer = str(math.log(abs(12*math.sin(int(x)))))
    driver.find_element(By.ID, 'answer').send_keys(answer)
    driver.find_element(By.ID, 'solve').click()
    
    time.sleep(5)
