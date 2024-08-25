from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import time

driver = wb.Edge()
driver.get("https://www.facebook.com/")
driver.maximize_window()

#  Finding the element using id selector
email_address = driver.find_element(By.ID, "email")
email_address.send_keys("roshan200098@gmail.com")
time.sleep(3)

# Finding the element using name selector
password = driver.find_element(By.NAME, "pass")
password.send_keys("Geetanjali@#2359")
time.sleep(3)

login = driver.find_element(By.NAME, "login")
login.click()
time.sleep(5)