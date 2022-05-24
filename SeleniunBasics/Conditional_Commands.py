from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/register")

# is_displayed()  is_enabled()

# search_box = driver.find_element(by=By.XPATH, value="(//input[@name='q'])[1]")
#
# print("Is Displayed: ",search_box.is_displayed())
# print("Is Enabled: ",search_box.is_enabled())

# is_selected: use only for radio buttons and checkboxes

rad_male = driver.find_element(by=By.XPATH, value="//input[@value='M']")
rad_female = driver.find_element(by=By.XPATH, value="//input[@value='F']")

print("default radio button status....")
print("Is radio button of male selected:", rad_male.is_selected())
print("Is radio button of female selected:", rad_female.is_selected())

print("If male is clicked")
rad_male.click()
print("Clicked on of male radio button:", rad_male.is_selected())
print("Is radio button of female selected:", rad_female.is_selected())

print("If female is clicked")
rad_female.click()
print("Is radio button of male selected:", rad_male.is_selected())
print("Clicked on of female radio button:", rad_female.is_selected())

driver.close()


