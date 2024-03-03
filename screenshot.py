from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.tokopedia.com/")
time.sleep(4)
driver.get_screenshot_as_file("noven.png")

driver.quit()