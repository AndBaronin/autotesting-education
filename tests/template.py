from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
