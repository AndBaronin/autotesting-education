from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, 'btn').click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text

    def func(x):
        return math.log(abs(12*math.sin(int(x))))
    
    y = func(x)
    
    browser.find_element(By.ID, 'answer').send_keys(y)

    browser.find_element(By.CLASS_NAME, 'btn').click()

    alert = browser.switch_to.alert
    alert.accept()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



