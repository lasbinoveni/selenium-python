from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/text-box")

driver.find_element(By.ID,"userName").send_keys("noveni")
driver.find_element(By.ID,"userEmail").send_keys("lasbinoveni@gmail.com")
driver.find_element(By.ID,"currentAddress").send_keys("Cikupa, Tangerang")
driver.find_element(By.ID,"permanentAddress").send_keys("Tangerang, Banten")
driver.find_element(By.ID,"submit").click()


time.sleep(20)
driver.quit()