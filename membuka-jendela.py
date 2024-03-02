from selenium import webdriver

driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()

driver1.get("https://www.detik.com")
driver2.get("https://www.kompas.com")
driver3.get("https://www.google.com")