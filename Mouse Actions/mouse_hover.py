import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.browserstack.com/guide/mouse-hover-in-selenium")

actions = ActionChains(driver)  # ActionChains object

developers = driver.find_element(By.XPATH, "//button[@id='developers-dd-toggle']")
documentations = driver.find_element(By.XPATH, "//span[normalize-space()='Documentation']")
supports = driver.find_element(By.XPATH, "//a[@title='Support']")
status = driver.find_element(By.XPATH, "//a[@title='Status']")

# a = actions.move_to_element(developers)
# time.sleep(1)
# b = a.move_to_element(documentations)
# time.sleep(1)
# c = b.move_to_element(supports)
# time.sleep(1)
# d = c.move_to_element(status)
# b.perform()

actions.move_to_element(developers).move_to_element(documentations).move_to_element(supports).move_to_element(
    status).click().perform()  # hovering elements one by one

# actions.move_to_element(developers).move_to_element(status).click().perform() # directly hovering over an element

time.sleep(2)
