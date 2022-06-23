from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get('https://www.codegrepper.com/code-examples/html/w3school+target+_top+_parent')
windId = driver.current_window_handle
print(windId)

socailLinks = driver.find_elements(by=By.XPATH, value="//section[@id='footer']//div[3]//a")
termLinks = driver.find_elements(by=By.XPATH, value="//section[@id='footer']//div[4]//a")

for link in socailLinks:
    link.click()
winIDs = driver.window_handles

for windId in winIDs:
    driver.switch_to.window(windId)
    print(windId)
    print(driver.title)
    if driver.title=="Grepper | LinkedIn":
        driver.close()



