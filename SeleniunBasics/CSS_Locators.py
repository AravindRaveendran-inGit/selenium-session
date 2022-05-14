from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:\selenium\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

# tag & ID: tagname#valueofID(syntax) e.g: input#email
# NB: tagname is optional.
# driver.find_element(by=By.CSS_SELECTOR, value="input#email").send_keys("example")

#tag & class: tagname.valueofCLASS
# NB: tagname is optional
# driver.find_element(by=By.CSS_SELECTOR, value="input.inputtext").send_keys("automation")

# tag & attribute
# NB: tagname is optional
# driver.find_element(by=By.CSS_SELECTOR, value="input[data-testid=royal_email]").send_keys("example123")

# tag class & attribute
# NB: tagname is optional
driver.find_element(by=By.CSS_SELECTOR, value="input.inputtext[data-testid=royal_email]").send_keys("example123")