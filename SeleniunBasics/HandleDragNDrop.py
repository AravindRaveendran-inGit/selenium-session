from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()


driver.get("https://demo.guru99.com/test/drag_drop.html")

Bank = driver.find_element(By.XPATH,"//a[normalize-space()='BANK']")
Sales = driver.find_element(By.XPATH, "//a[normalize-space()='SALES']")



trgtBank = driver.find_element(By.XPATH, "//ol[@id='bank']//li[@class='placeholder']")
trgtSales = driver.find_element(By.XPATH, "//ol[@id='loan']//li[@class='placeholder']")
#
# amount = driver.find_element(By.XPATH, "//section[@id='g-container-main']//li[1]//a[1]")
act = ActionChains(driver)

act.drag_and_drop(Bank,trgtBank).perform()
act.drag_and_drop(Sales,trgtSales).perform()