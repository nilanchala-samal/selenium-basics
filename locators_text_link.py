from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("D:\\Selenium\\Drivers\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://www.facebook.com/")

# Finding the element using the link text selector - used to find the anchor tags
driver.find_element(By.LINK_TEXT, "Forgotten password?").click()
time.sleep(4)
driver.back()
# driver.find_element(By.LINK_TEXT, "Create new account").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "new account").click()
time.sleep(7)
