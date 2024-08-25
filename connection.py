from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

# Correct path to chromedriver.exe
# driver_path = "D:\Selenium\Drivers\chromedriver-win32\chromedriver.exe"

serv_obj = Service("D:\\Selenium\\Drivers\\chromedriver-win32\\chromedriver.exe")
browser = webdriver.Chrome(service=serv_obj)
browser.get("https://demo.nopcommerce.com/")
browser.maximize_window()

# browser.find_element(By.ID, value='small-searchterms').send_keys("Lenovo laptop")
# browser.find_element(By.NAME, value='q').send_keys("Lenovo laptop")
# time.sleep(10)

# browser.find_element(By.LINK_TEXT, "Register").click()
browser.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()
time.sleep(10)