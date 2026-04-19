from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)
    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()
    radio1 = browser.find_element(By.ID, 'robotsRule')
    radio1.click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
