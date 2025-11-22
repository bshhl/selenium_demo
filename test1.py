from ssl import Options
from xmlrpc.client import Server

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.bilibili.com/")
driver.maximize_window()
find_result = driver.find_element(By.XPATH, '//*[@id="nav-searchform"]/div[1]/input').send_keys("全运会")
driver.find_element(By.XPATH, '//*[@id="nav-searchform"]/div[2]').click()
time.sleep(3)
driver.quit()