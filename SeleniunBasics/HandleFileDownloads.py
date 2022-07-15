from selenium import webdriver
from selenium.webdriver.common.by import By

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
    location = str("C:\\Users\\aravi\PycharmProjects\\Selenium\\SeleniunBasics\\Downloads")
    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(service=chrome, options=ops)
    return driver

driver = chrome_setup()
driver.maximize_window()
driver.get("https://www.sampledocs.in/BrowseFile/DummyFiles/docx")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//tbody/tr[2]/td[4]/a[1]").click()

"""
Firefox setup

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj=Service("C:\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe")
    #settings
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword") #here we use different mime for different file types
    ops.set_preference("browser.download.manager.showWhenStarting",False)
    ops.set_preference("browser.download.folderList",2)#0-desktop, 1-downloads, 2- mentioned location
    location = str("C:\\Users\\aravi\PycharmProjects\\Selenium\\SeleniunBasics\\Downloads")
    ops.set_preference("browser.download.dir",location)
    driver = webdriver.Firefox(service=serv_obj, options=ops)
    return driver

"""