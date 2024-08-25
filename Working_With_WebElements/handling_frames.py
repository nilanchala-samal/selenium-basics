import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
driver.switch_to.frame("courses-iframe")
value = driver.find_element(By.LINK_TEXT, "Courses")
print(value.text)
driver.switch_to.parent_frame()
time.sleep(2)
driver.find_element(By.ID, "checkBoxOption2").click()
time.sleep(3)

# for changing multiple frames and switch to parent
# driver.switch_to.default_content
