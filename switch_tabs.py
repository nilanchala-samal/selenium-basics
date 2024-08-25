import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

# old way of clicking and opening the link in new window
"""
driver.find_element(By.XPATH, "//a[normalize-space()='Register']").send_keys(Keys.CONTROL + Keys.RETURN)
window_ids = driver.window_handles
print(len(window_ids))
driver.switch_to.window(window_ids[1])
time.sleep(2)
"""

# opens a new tab and switches to the new tab - selenium 4 feature
# driver.switch_to.new_window('tab')
# driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# time.sleep(2)

# opens a new window and switches to the new window - selenium 4 feature
driver.switch_to.new_window('window')
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
time.sleep(2)