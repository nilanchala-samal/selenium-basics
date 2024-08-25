import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://orangehrm.qedgetech.com/symfony/web/index.php/auth/login")

# getting the current window id
# print("The window id of current window is:", driver.current_window_handle)


# If we have multiple windows, window_handles is used which returns a list of windowIds.

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()  # opening another window
time.sleep(3)

window_ids = driver.window_handles  # returns all the windowIds of opening windows
# approach - 1
# parent_window_id = window_ids[0]
# child_window_id = window_ids[1]
#
# print("parent window id:", parent_window_id)
# print("child window id:", child_window_id)
#
# driver.switch_to.window(child_window_id)
# print("child window title: ", driver.title)
#
# driver.switch_to.window(parent_window_id)
# print("parent window title:", driver.title)


# approach - 2
for window_id in window_ids:
    driver.switch_to.window(window_id)
    print(driver.title)

# If we want to close a specific window
for window_id in window_ids:
    driver.switch_to.window(window_id)
    if driver.title == 'Human Resources Management Software | OrangeHRM':
        driver.close()
time.sleep(2)
