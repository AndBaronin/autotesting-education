from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, 'trollface').click()
    browser.switch_to.window(browser.window_handles[1])

    def func(x):
        return math.log(abs(12*math.sin(int(x))))
    x = browser.find_element(By.ID, 'input_value').text
    y = func(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(5)

    alert = browser.switch_to.alert
    alert.accept()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
