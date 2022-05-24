from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=chrome)
driver.get("https://ifsc.bankifsccode.com/")
driver.maximize_window()

#### find_element() - returns single webelement

#1) Locator matching with the single webelement

# driver.find_element(by=By.XPATH, value="//a[@href='https://ifsc.bankifsccode.com/']//img").click()
# driver.find_element(by=By.XPATH, value="//input[@name='ifsccode']").send_keys("HDFC0000683")
# driver.find_element(by=By.XPATH, value="//input[@name='submit']").click()


#2) Locator matching with the multiple webelements

# element = driver.find_element(by=By.XPATH, value="//body[1]/table[1]/tbody[1]/tr[12]/td[1]/div[1]//a")
# print(element.text) #Only returns first webelement

#3) If element is not available then throw an NOSuchElementExpection

# element = driver.find_element(by=By.LINK_TEXT, value="HOME")
#################################################################

#1) Locator matching with the single webelement

driver.find_elements(by=By.XPATH, value="//a[@href='https://ifsc.bankifsccode.com/']//img")
elements = driver.find_elements(by=By.XPATH, value="//input[@name='ifsccode']")
print(len(elements))
print(elements[0].text)
elements[0].send_keys("HDFC0000683")
print(elements[0].text)
driver.find_element(by=By.XPATH, value="//input[@name='submit']").click()


driver.close()