from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get("https://itera-qa.azurewebsites.net/home/automation")

drpdwn = Select(driver.find_element(By.XPATH,value="//select[@class='custom-select']"))
# drpdwn.select_by_visible_text("Sweden")

options = drpdwn.options
print(len(options))

for opt in options:
    print(opt.text)
    if opt.text=="Sweden":
        opt.click()



