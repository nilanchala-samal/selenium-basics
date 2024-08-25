import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://orangehrm.qedgetech.com/symfony/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "a[href='http://www.orangehrm.com']").click()
time.sleep(10)

driver.close()
time.sleep(4)
