from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service

# assigned the service path for webdriver
edge_service = Service("C:\selenium\edgedriver\msedgedriver")

# assigned the webdriver
edge_driver = webdriver.Edge(service=edge_service)

# opening the webpage using the webdriver
edge_driver.get("http://demo.automationtesting.in/Windows.html")

# print the webpage title
print(edge_driver.title)

# print the url of the page
print(edge_driver.current_url)

# click on a particular element using xpath
ClickButton = edge_driver.find_element(by=By.XPATH, value="//*[@id='Tabbed']/a/button").click()

#close the parent/focused tab
# edge_driver.close()

# close all tabs
edge_driver.quit()