from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get("https://itera-qa.azurewebsites.net/home/automation")

# 1) select specific checkbox

# driver.find_element(By.XPATH, value="//input[@id='thursday']").click()

# 2) selecet all the checkboxes

checkboxes = driver.find_elements(By.XPATH, value="//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

# Approach 1
# for i in range(len(checkboxes)):
#     print(checkboxes[i].text)
#     checkboxes[i].click()

# Approach 2
# for check in checkboxes:
#     check.click()
# driver.quit()

# 3 Select multiple checkboxes by chocies
# for check in checkboxes:
#     weekname = check.get_attribute('id')
#     if weekname=='friday'or weekname=='saturday'or weekname=='thursday':
#         check.click()

# 4 To select last two checkboxes

# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

# 5 unselect if all checkbox is selected
# for check in checkboxes:
#     if check.is_selected():
#         check.click()

# 6) To check first 3 check boxes
#
# for i in range(len(checkboxes)):
#     if i<3:
#         checkboxes[i].click()
