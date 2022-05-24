from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:\selenium\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.get("https://aravindraveendran.in/")
driver.maximize_window()

actual_title = driver.title
expected_title = "Aravind Raveendran"
 
actual_url = driver.current_url
expected_url = "https://aravindraveendran.in/"

source = driver.page_source

if actual_title == expected_title and actual_url == expected_url:
    print("actual result meets the expected result")
    print(actual_title,actual_url)
    print(source)

else:
    print("Bug reported")
    print(actual_title,actual_url)
    print(source)
    

driver.close()