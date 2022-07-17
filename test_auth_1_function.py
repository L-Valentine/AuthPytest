from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()


def test_login():
    driver.get(url='https://www.saucedemo.com/')
    time.sleep(2)
    user_name_field = driver.find_element(By.NAME, 'user-name')
    user_name_field.send_keys('standard_user')
    time.sleep(2)
    user_password_field = driver.find_element(By.NAME, 'password')
    user_password_field.send_keys('secret_sauce')
    time.sleep(2)
    login_button = driver.find_element(By.NAME, 'login-button')
    login_button.click()
    time.sleep(5)


def test_teardown():
    driver.close()
    driver.quit()
    print("Test completed")
