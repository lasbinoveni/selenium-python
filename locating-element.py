from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.kompas.com/")
driver.find_element(By.name,"q")