import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.get("https://www.google.com/")
# Wait_Time = WebDriverWait(driver,10) #explicit wait declaration
Wait_Time = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])
driver.maximize_window()

search_box = driver.find_element(by=By.XPATH, value="//input[@title='Search']")
search_box.send_keys("selenium")

search_box.submit()

search_text = Wait_Time.until(EC.presence_of_element_located((By.XPATH,"//h3[text() ='Selenium']")))
search_text.click()

# time.sleep(10)
driver.quit()

