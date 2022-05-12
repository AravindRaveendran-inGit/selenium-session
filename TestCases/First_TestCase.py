# Test scenario: Verify the title of the dashboard page.
# -------------------------------------------------------#

# TestSteps#

# 1) Open web browser(chrome/IE)
# 2) Open URL https://admin-demo.nopcommerce.com/login
# 3) Provide email (admin@yourstore.com)
# 4) Provide password (admin)
# 5) Click on login
# 6) Capture the title of the dashboard page (Actual Title)
# 7) Verify the title of the page: "Dashboard / nopCommerce administration" (Expected)
# 8) Close the browser
# -----------------------------------------------------------------------------------------#

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service #selenium4 update
from selenium.webdriver.common.by import By #selenium4 update

# selenium3

# driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver_win32\chromedriver.exe") # assigned the Chrome class in the web driver module to driver object
# driver.get("https://admin-demo.nopcommerce.com/login") #accesing the URL
# ClickButton = driver.find_element(by=By.CLASS_NAME, value="button-1").click()
# actual_title = driver.title
# expected_title = "Dashboard / nopCommerce administration"
# if actual_title == expected_title:
#     print("First testcase passed")
# else:
#     print("First test case failed")
# driver.close()
#######################################################################################

serv_obj = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://admin-demo.nopcommerce.com/login") #accesing the URL
driver.find_element(by=By.CLASS_NAME, value="email").clear()
driver.find_element(by=By.CLASS_NAME, value="email").send_keys("admin@yourstore.com")
driver.find_element(by=By.ID, value="Password").clear()
driver.find_element(by=By.ID, value="Password").send_keys("admin")
driver.find_element(by=By.CLASS_NAME, value="button-1").click()
actual_title = driver.title
expected_title = "Dashboard / nopCommerce administration"
if actual_title == expected_title:
    print("First testcase passed")
else:
    print("First test case failed")
driver.close()