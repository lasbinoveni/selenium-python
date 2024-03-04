from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver  = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.find_element(By.ID,"sex-0").click()

time.sleep(10)
driver.quit()