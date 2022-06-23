from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()


# to bypass the authenticated popoup
# Syntax: http://username:password@URL
# Example: https://admin:Qwerty124@the-internet.herokuapp.com/basic_auth

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")