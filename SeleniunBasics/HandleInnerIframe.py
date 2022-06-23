from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Frames.html")

driver.find_element(by=By.LINK_TEXT, value="Iframe with in an Iframe").click()

outerframe = driver.find_element(by=By.XPATH, value="//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe = driver.find_element(by=By.XPATH, value="//iframe[normalize-space()='<p>Your browser does not support iframes.</p>']")
driver.switch_to.frame(innerframe)

driver.find_element(by=By.XPATH, value="//input[@type='text']").send_keys("Aravind")
driver.switch_to.default_content()

driver.find_element(by=By.XPATH, value="//a[normalize-space()='Single Iframe']").click()
