from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# creating a service path to open the webdriver
# chrome_service = Service("C:\selenium\chromedriver_win32\chromedriver")
edge_service = Service("C:\selenium\edgedriver\msedgedriver")

# assigning the webdriver to a object
# chrome_driver = webdriver.Chrome(service=chrome_service)
edge_driver = webdriver.Edge(service=edge_service)

#  accessing the webdriver
# chrome_driver.get("https://aravindraveendran.in/")
edge_driver.get("https://aravindraveendran.in/")

# print the title of the page
# print(chrome_driver.title)
print(edge_driver.title)

# print the url of the current page
# print(chrome_driver.current_url)
print(edge_driver.current_url)

# print the page source (html)
# print(chrome_driver.page_source)
# print(edge_driver.current_url)
# chrome_driver.quit()
edge_driver.quit()