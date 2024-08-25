import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")

actions = ActionChains(driver)

driver.switch_to.frame("iframeResult")


field1 = driver.find_element(By.ID, "field1")
field1.clear()
field1.send_keys("Ryoiki Tenkai")

copy_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

actions.double_click(copy_btn).perform()
time.sleep(3)
# print(actions)
# print(actions.double_click())
# print(actions.double_click(copy_btn).perform())

driver.close()