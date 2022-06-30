from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import datetime

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=chrome)
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

monthNeeded = "October"
yearNeeded = "1998"
dateNeeded = "12"



toDay = datetime.datetime.now()

monthToday = toDay.strftime("%B")
yearToday = toDay.strftime("%Y")
monthPicker = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
yearPicker = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

if monthPicker==monthToday and yearPicker==yearToday:
    while True:
        monthPicker = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        yearPicker = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        if monthNeeded==monthPicker and yearNeeded==yearPicker:
            break;
        else:
            driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()



datePicker = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")

for date in datePicker:
    if date.text==dateNeeded:
        date.click()
        break;




# print(yearNow)

# print(mydate.strftime("%B"))

driver.quit()