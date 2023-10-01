from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Open Google, maximise window and Search Jai HO !! {Chrome Browser}
driver = webdriver.Chrome()

OpenLink="https://www.google.com/"

driver.get(OpenLink)
time.sleep(2)
driver.maximize_window()
elem=driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
elem.send_keys("Jai Ho!!")
elem.send_keys(Keys.ENTER)
time.sleep(5)
