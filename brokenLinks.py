from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
from selenium.webdriver.common.by import By

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get("http://www.deadlinkcity.com/")

links=driver.find_elements(By.TAG_NAME,'a')
brknLink=0
activeLink=0

for link in links:
    url=link.get_attribute('href')

    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url, "is broken")
        brknLink+=1
    else:
        print(url,"is valid")
        activeLink+=1

print("total number of broken links", brknLink)
print("total number of active links", activeLink)
print(len(links))