from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.get("https://ifsc.bankifsccode.com/")
driver.maximize_window()

Ifsc_page = driver.find_element(by=By.XPATH, value="//a[@href='https://ifsc.bankifsccode.com/']//img")
Ifsc_page.click()

Search_Ifsc = driver.find_element(by=By.XPATH, value="//input[@id='ifsccode']")
Search_Ifsc.send_keys("HDFC0000683")
print(Search_Ifsc.text)
print(Search_Ifsc.get_attribute("value"))
print(Search_Ifsc.get_property("id"))
print(Search_Ifsc.get_dom_attribute("name"))

# text --> will return if inner text is available.
# get_attribute --> will return value of any attribute in the webelement
driver.close()