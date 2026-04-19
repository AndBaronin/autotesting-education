from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys('Ivan')
    browser.find_element(By.NAME, 'lastname').send_keys('Ivanov')
    browser.find_element(By.NAME, 'email').send_keys('ivanov@ivan.iv')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'text.txt') 
    browser.find_element(By.ID, 'file').send_keys(file_path)

    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
