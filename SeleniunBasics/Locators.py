# Locators


#- ID, NAME, LINK_TEXT, PARTIAL_LINK_TEXT
#- CLASS_NAME and TAG_NAME are used to find more than one element.
#-  Because there are certain elements there class name value will be the same
#   ( eg: radio button, dropdown, here the ID or NAME may be different
#    but all comes under one category and that catergory is referred to class here.)



# -------------------------------------------------------#
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

srvc_obj = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=srvc_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window() # Maximize the browser window

# driver.find_element(by=By.CLASS_NAME, value="search-box-text").send_keys("Monitor")
# driver.find_element(by=By.XPATH, value='//*[@id="small-search-box-form"]/button').click()
# driver.find_element(by=By.LINK_TEXT, value="Register").click()
# driver.find_element(by=By.PARTIAL_LINK_TEXT, value="").click()

slides = driver.find_elements(by=By.CLASS_NAME, value="nivo-imageLink")
print(len(slides))

Total_links = driver.find_elements(by=By.TAG_NAME, value="a")
print(len(Total_links))

driver.close()