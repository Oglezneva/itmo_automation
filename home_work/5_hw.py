from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com')

user_name_input = driver.find_element(By.CSS_SELECTOR, '#user-name')
password_input = driver.find_element(By.CSS_SELECTOR, '#password')
login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')

if user_name_input is None or password_input is None or login_button is None:
    print('Элементы не найдены')
else:
    print('Элементы найдены')