from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chromeService = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
chromeops = webdriver.ChromeOptions()
chromeops.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=chromeService)
driver.maximize_window()
driver.get("https://whatmylocation.com/")

