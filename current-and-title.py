from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://thinkjubilee.com")

alamat = driver.current_url
judul = driver.title
panjangjudul = len(judul)
print("Alamat situs {} dan judul adalah {}, dengan panjang {}".format(alamat, judul, panjangjudul))

time.sleep(15)

driver.forward()
driver.back()

time.sleep(10)
driver.close()