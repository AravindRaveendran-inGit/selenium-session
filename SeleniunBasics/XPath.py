from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get('http://automationpractice.com/index.php')
driver.maximize_window()

# Absolute XPath

# driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]').send_keys('lipstick')
# driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button').click()

#  Relative XPath

# driver.find_element(by=By.XPATH, value="//input[@id='search_query_top']").send_keys('Tshirt')
# driver.find_element(by=By.XPATH, value=" //button[@name='submit_search']").click()

# or, # and
# //input[@name="search_query"]
# //input[@id="search_query_top"]
# //button[@name="submit_search"]
# //button[@class='btn btn-default button-search']
# driver.find_element(by=By.XPATH, value='//input[@name="search_query"]' or '//input[@id="search_query_top"]').send_keys("Pants")
# driver.find_element(by=By.XPATH, value='//button[@name="submit_search"]' and '//button[@class="btn btn-default button-search"]').click()

# Contains() & Startwith()

driver.find_element(by=By.XPATH,value='//input[contains(@id,"_top")]').send_keys("Pants")
driver.find_element(by=By.XPATH, value='//button[starts-with(@name,"submit_")] ').click()
