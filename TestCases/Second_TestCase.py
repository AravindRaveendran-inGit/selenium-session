# Test scenario: Verify the title of the home page.
# -------------------------------------------------------#

# TestSteps#

# 1) Open web browser(chrome/IE)
# 2) Open URL https://opensource-demo.orangehrmlive.com/
# 3) Provide Username (Admin)
# 4) Provide password (admin123)
# 5) Click on login
# 6) Capture the title of the home page (Actual Title)
# 7) Verify the title of the page: "OrangeHRM" (Expected)
# 8) Close the browser
# -----------------------------------------------------------------------------------------#
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\selenium\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(by=By.NAME, value="txtUsername").send_keys("Admin")
driver.find_element(by=By.ID, value="txtPassword").send_keys("admin123")
driver.find_element(by=By.XPATH, value='//*[@id="btnLogin"]').click()

act_title = driver.title
exct_title = "OrangeHRM"

if act_title==exct_title:
    print("testcase passed")
else:
    print("testcase failed")

driver.close()


