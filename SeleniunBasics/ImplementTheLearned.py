from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)

driver.maximize_window()
driver.get("https://itera-qa.azurewebsites.net/home/automation")

# Select web elements
Name = driver.find_element(By.XPATH, value="//input[@id='name']")
Contact = driver.find_element(By.XPATH, value="//input[@id='phone']")
Email = driver.find_element(By.XPATH, value="//input[@id='email']")
Password = driver.find_element(By.XPATH, value="//input[@id='password']")
Address = driver.find_element(By.XPATH, value="//textarea[@id='address']")
Gender  = driver.find_element(By.XPATH, value="//input[@id='male']")
weeks  = driver.find_elements(By.XPATH, value="//input[@type='checkbox' and contains(@id,'day')]")
drpwn = Select(driver.find_element(By.XPATH, value="//select[@class='custom-select']"))
experience = driver.find_element(By.XPATH, value="//label[normalize-space()='1 year']")
frameworkSelenium = driver.find_element(By.XPATH, value="//label[normalize-space()='Selenium Webdriver']")
frameworkTestNG = driver.find_element(By.XPATH, value="//label[normalize-space()='TestNG']")

# Pass the values

Name.send_keys("Aravind")
Contact.send_keys("+91 9746260667")
Email.send_keys("zerodimensionaluniverse")
Password.send_keys("Qwerty@12345")
Address.send_keys("KMRA-43 Trivandrum 695001")
Gender.click()
experience.click()
frameworkSelenium.click()
frameworkTestNG.click()

# Selecting weeks
for week in weeks:
    weekname = week.get_attribute("id")
    if weekname=="sunday" or weekname=="monday" or weekname=="tuesday" or weekname=="wednesday":
        week.click()


# Dropdown Country
options = drpwn.options
for opt in options:
    if opt.text=="Malta":
        opt.click()
        break


#  Dropdown Frameworks


