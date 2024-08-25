import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

actions = ActionChains(driver)

button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
actions.context_click(button).perform()


# def handle_alert():
#     """ This function is used for handling the alert on this website """
#     alert_window = driver.switch_to.alert
#     alert_window.accept()
#     time.sleep(1)

# edit = driver.find_element(By.CSS_SELECTOR, ".context-menu-item.context-menu-icon.context-menu-icon-edit")
# edit.click()

# handle_alert()

# again clicking the right click
# actions.context_click(button).perform()

# cut = driver.find_element(By.CSS_SELECTOR, ".context-menu-item.context-menu-icon.context-menu-icon-cut")
# cut.click()

# handle_alert()
time.sleep(3)
