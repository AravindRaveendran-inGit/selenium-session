from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get("http://www.testyou.in/")
driver.get("https://technopark.org/")

driver.back()
driver.forward()
driver.refresh()
print("navigated")

driver.close()