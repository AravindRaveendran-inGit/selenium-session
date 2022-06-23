from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

url = driver.current_url

print(url)

#find total number of links available.

links = driver.find_elements(By.TAG_NAME, value='a')

print(len(links))

for link in links:
    print(link.text)


driver.quit()

