import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.get("https://www.google.com/")
driver.implicitly_wait(10) #seconds
driver.maximize_window()

search_box = driver.find_element(by=By.XPATH, value="//input[@title='Search']")
search_box.send_keys("selenium")

search_box.submit()

heading = driver.find_element(by=By.XPATH, value="//h3[text() ='Selenium']")

# time.sleep(10)

heading.click()

driver.quit()

