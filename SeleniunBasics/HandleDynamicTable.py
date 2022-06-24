from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()

driver.find_element(By.XPATH,"//b[normalize-space()='Admin']").click()
driver.find_element(By.XPATH,"//a[@id='menu_admin_UserManagement']").click()
driver.find_element(By.XPATH,"//a[@id='menu_admin_viewSystemUsers']").click()

#Totol rows
totRows = len(driver.find_elements(By.XPATH,"//table[@id='resultTable']//tbody/tr"))
totCols = len(driver.find_elements(By.XPATH,"//table[@id='resultTable']//th"))

#Active Employees

count=0
noUsr=0
# for r in range(1,totRows+1):
#     emplySts = driver.find_element(By.XPATH,"//table[@id='resultTable']//tbody/tr["+str(r)+"]/td[5]").text
#     if emplySts=="Enabled":
#         count = count+1

for i in range(1,totRows+1):
    usrRole = driver.find_element(By.XPATH,"//table[@id='resultTable']/tbody/tr["+str(i)+"]/td[3]").text
    usrName = driver.find_element(By.XPATH, "//table[@id='resultTable']/tbody/tr[" + str(i) + "]/td[2]").text
    if usrRole=="Admin":
        print(usrName,"is",usrRole)


        noUsr = noUsr+1

# print("Total no:of employees: ", totRows)
# print("Total employees working: ", count)
# print("Total employees left: ", (totRows-count))
print("Total no:of ESS employee: ",(totRows-noUsr) )
print("Total no:of Admin: ", noUsr)


# usrRole = driver.find_element(By.XPATH,"//table[@id='resultTable']/tbody/tr[1]/td[3]").text
# usr = driver.find_element(By.XPATH,"//table[@id='resultTable']/tbody/tr[1]/td[3]").text