from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

firstPoint = driver.find_element(By.XPATH, "//span[1]")

print(firstPoint.location)

secondPoint = driver.find_element(By.XPATH, "//span[2]")

print(secondPoint.location)

act = ActionChains(driver)

act.drag_and_drop_by_offset(firstPoint,100,0).perform()
act.drag_and_drop_by_offset(secondPoint,-50,0).perform()

