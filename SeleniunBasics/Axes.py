from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

srv_obj = Service("C:\selenium\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=srv_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#self
# text = driver.find_element(by=By.XPATH, value='//a[contains(text(),"PCBL")]/self::a').text
#
# print(text)

#parent
# text = driver.find_element(by=By.XPATH, value="//a[contains(text(),'ICRA Ltd.')]/parent::td").text

# print(text)

# child
# childs = driver.find_elements(by=By.XPATH, value='//a[contains(text(),"PCBL")]/ancestor::tr/child::td')
#
# for child in childs:
#     print(child.text)
# print(len(childs))
# driver.close()

# ancestor
# text=driver.find_element(by=By.XPATH, value='//a[contains(text(),"PCBL")]/ancestor::tr').text
#
# print(text)

# descendant

# descendants =driver.find_element(by=By.XPATH, value='//a[contains(text(),"PCBL")]/ancestor::tr/descendant::*')

# print(len(descendants))

# following

# followings = driver.find_elements(by=By.XPATH, value='//a[contains(text(),"PCBL")]/ancestor::tr/following::*')
# print(len(followings))

# following-siblings
# following_siblings = driver.find_elements(by=By.XPATH, value='//a[contains(text(),"PCBL")]/ancestor::tr/following-sibling ::*')
# print(len(following-siblings))

# preceding

# precedings = driver.find_elements(by=By.XPATH, value='//a[contains(text(),"PCBL")]/ancestor::tr/preceding::*')
# print(len(precedings))

# preceding-siblings
preceding_siblings= driver.find_elements(by=By.XPATH, value='//a[contains(text(),"PCBL")]/ancestor::tr/preceding-sibling ::*')
print(len(preceding_siblings))
driver.close()