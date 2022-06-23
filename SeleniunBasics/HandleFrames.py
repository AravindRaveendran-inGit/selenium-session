from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')

driver.switch_to.frame(0)
frame1 = driver.find_element(by=By.XPATH, value="//a[normalize-space()='org.openqa.selenium.chrome']")
frame1.click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
frame2 = driver.find_element(by=By.XPATH, value="//a[normalize-space()='ChromeDriverLogLevel']")
frame2.click()

driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
frame3 = driver.find_element(by=By.XPATH, value="//div[@class='topNav']//a[normalize-space()='Deprecated']")
frame3.click()

driver.quit()