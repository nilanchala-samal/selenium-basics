import time
import os
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

# driver.save_screenshot("D:\\Downloads\\homepage.png")
# driver.save_screenshot("C:\\Users\\ASUS\\PycharmProjects\\Selenium\\Capturing Screenshot\\homepage.jpg")
# driver.save_screenshot(os.getcwd() + "\\nopcommerce.png")

# driver.get_screenshot_as_file(os.getcwd() + "\\nopcommerce.png")
# driver.get_screenshot_as_file("nopcommerce.png")  # just specify the name for saving the ss in the cwd
driver.get_screenshot_as_file("D:\\Downloads\\homepage.png")
