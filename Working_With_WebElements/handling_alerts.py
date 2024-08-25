# Handling alerts and pop-ups
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# opening the alert window
# driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']").click()
# driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()

time.sleep(3)
#  switching the control to alert window
alert_window = driver.switch_to.alert

# passing the values to input box of the alert window
alert_window.send_keys("James Bond")
print(alert_window.text)
# alert_window.accept()
alert_window.dismiss()



