import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# Implicit wait

# driver.implicitly_wait(10)
#
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Selenium")
# search_box.submit()
#
# driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()


# Explicit wait
my_wait = WebDriverWait(driver, 10, ignored_exceptions=[Exception])

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()

search_link = my_wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
search_link.click()
