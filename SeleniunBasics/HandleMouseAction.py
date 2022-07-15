from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()


driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()

Admin = driver.find_element(By.XPATH,"//b[normalize-space()='Admin']")
UserManagement = driver.find_element(By.XPATH,"//a[@id='menu_admin_UserManagement']")
Users = driver.find_element(By.XPATH,"//a[@id='menu_admin_viewSystemUsers']")

act = ActionChains(driver)

act.move_to_element(Admin).move_to_element(UserManagement).move_to_element(Users).click().perform()

name = driver.find_element(By.XPATH,"//input[@id='searchSystemUser_userName']")
name.click()
act.context_click(name).perform()

