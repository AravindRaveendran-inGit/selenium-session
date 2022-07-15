from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.implicitly_wait(10)



"""
#Scroll down page by pixcel
driver.execute_script("window.scrollBy(0,3000)","")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixcel moved:", value)

"""

"""
# Scroll down till the element is identified

flag = driver.find_element(By.XPATH, "//td[normalize-space()='India']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixcel moved:", value)

"""

#Scroll from top to bottom

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixcel moved:", value)