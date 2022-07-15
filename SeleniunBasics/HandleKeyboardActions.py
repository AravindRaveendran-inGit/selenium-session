from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome = Service("C:\selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome)
driver.maximize_window()

""""
Select text from text box1 and copy to  text box2

"""

driver.get("https://text-compare.com/")

textBox1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
textBox2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

textBox1.send_keys("ZeroDimensinolUniverse")

act = ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


