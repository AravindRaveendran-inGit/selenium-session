from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

#1) Count no: of rows and columns
#
# totRows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
# print("Total no:of rows = ",totRows)
# totCols = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
# print("Total no:of rows = ",totCols)

#2)Read specific row and column data
# data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[6]").text
# print(data)

#3) Read all rows and columns
# totRows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
# totCols = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
#
# for r in range(2,totRows+1):
#     for c in range(1,totCols+1):
#         data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end=" ")
#     print()

#4) Fetch specific data using condition

totRows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
totCols = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

for r in range(2,totRows+1):
    for c in range(1,totCols+1):
        author = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
        if author=="Mukesh":
            data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
            print(data,end=" ")



driver.quit()