from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.thinkjubilee.com")
driver.refresh()
driver.get("https:/www.selenium.com")
time.sleep(10)

driver.quit()