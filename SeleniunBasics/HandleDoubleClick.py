from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()


driver.get("http://demo.guru99.com/test/simple_context_menu.html")

btn = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")

act = ActionChains(driver)

act.double_click(btn).perform()

alertPop = driver.switch_to.alert

alertPop.accept()