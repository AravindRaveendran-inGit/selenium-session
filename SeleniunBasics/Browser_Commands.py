import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get("http://www.testyou.in/")

driver.find_element(by=By.XPATH, value="//a[normalize-space()='Terms & Conditions']").click()


driver.close()


driver.quit()