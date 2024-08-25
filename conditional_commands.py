from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://chatgpt.com/")
driver.maximize_window()

uname_element = driver.find_element(By.XPATH, "//*[@id='prompt-textarea']")
# is_displayed() and is_enabled() method
print("Display Status:", uname_element.is_displayed())
print("Enable Status:", uname_element.is_enabled())


