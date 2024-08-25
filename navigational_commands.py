import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://chatgpt.com/")
time.sleep(2)
driver.get("https://www.phind.com/search?home=true")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
