from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/javascript_alerts')

btn = driver.find_element(by=By.XPATH, value="//button[contains(text(),'Click for JS Prompt')]")
btn.click() 

alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("Learned to handle the alert popup")
alertwindow.accept() # alertwindow.dismiss()

