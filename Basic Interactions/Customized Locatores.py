# Customized Locators
# CSS Selectors
# XPATH

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver = Service('E:/BrowserDrivers/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=chrome_driver)

OpenLink = "https://www.facebook.com/"

driver.get(OpenLink)

# CSS Selectors
# tag id
# tag class
# tag attribute
# tag class attribute
driver.maximize_window()
# tag id # is used
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
# tag class . is used
driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys(("chal hatt"))
# tag attribute
driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys(("chal hatt"))
# tag class attribute
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys(("chal hatt"))
time.sleep(2)

# XPATH Selectors
# Types of Xpath
# Absolute/Full Path
# Relative/Partial Path
