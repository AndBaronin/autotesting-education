from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    num1_element = browser.find_element(By.ID, 'num1') 
    num1 = num1_element.text
    num2_element = browser.find_element(By.ID, 'num2')
    num2 = num2_element.text
    summ = int(num1) + int(num2)
    value = f'[value="{summ}"]'

    browser.find_element(By.ID, 'dropdown').click()
    browser.find_element(By.CSS_SELECTOR, value).click()

    browser.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    time.sleep(10)
    browser.quit()
