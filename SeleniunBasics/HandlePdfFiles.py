from selenium import webdriver
from selenium.webdriver.common.by import By

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
    location = str("C:\\Users\\aravi\PycharmProjects\\Selenium\\SeleniunBasics\\Downloads")
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally":True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(service=chrome, options=ops)
    return driver

driver = chrome_setup()
driver.maximize_window()
driver.get("https://www.sampledocs.in/BrowseFile/DummyFiles/pdf")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//a[@href='/DownloadFiles/SampleFile?filename=SampleDocs-sample-pdf-file&ext=pdf']").click()

"""
ops=webdriver.FirefoxOptions()
ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
ops.set_preference("browser.download.manager.showWhenStarting",False)
ops.set_preference("browser.download.folderList",2)#0-desktop1-downloads folder 2- Desired
ops.set_preference("browser.download.dir",location)
ops.set_preference("pdfjs.disabled",True)#for pdf
driver=webdriver.Firefox(service=serv_obj,options=ops)
return driver
                                       I

"""