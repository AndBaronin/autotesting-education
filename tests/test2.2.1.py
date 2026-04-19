from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    def func(x):
        return math.log(abs(12*math.sin(int(x))))
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = func(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    browser.find_element(By.ID, 'robotCheckbox').click()
    radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    button = browser.find_element(By.TAG_NAME, "button")
    
    button.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
