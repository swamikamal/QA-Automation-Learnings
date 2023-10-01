import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# Open Google, maximise window and Search Jai HO !! {Chrome Browser}

driver = webdriver.Chrome()

OpenLink = "https://www.google.com/"

driver.get(OpenLink)
driver.maximize_window()

time.sleep(2)
# Locators
# id
# name
# linktext
# Partiallinktext
# XPATH

driver.find_element(By.LINK_TEXT, "मराठी").click()
elem = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
elem.send_keys("Jai Ho!!")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
# elem.send_keys(Keys.ENTER)
# driver.minimize_window()
time.sleep(2)
# driver.maximize_window()
time.sleep(5)
