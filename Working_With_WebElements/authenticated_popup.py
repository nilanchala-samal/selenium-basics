import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# the below is the actual url with authentication pop-up
driver.get("http://the-internet.herokuapp.com/basic_auth")

# driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(10)
