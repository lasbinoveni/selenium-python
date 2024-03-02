from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.kompas.com/")

driver.find_element(By.NAME,"q").send_keys("pemilu 2024")
time.sleep(5)
tombol = driver.find_element(By.NAME,"submit")
tombol.click()