from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (e.g., for Chrome)
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Navigate to the webpage
driver.get('https://filebin.net/')

# Locate the hidden file input element
file_input = driver.find_element(By.XPATH, '//input[@id="fileField"]')

# Send the file path to the input element
file_input.send_keys('D:\\wallpapers\\946404.png')

time.sleep(10)

driver.quit()
