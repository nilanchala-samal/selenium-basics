from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://www.nopcommerce.com/en")
driver.maximize_window()

# Writing Absolute XPath for 'get started' element manually
driver.find_element(By.XPATH, "html/body/div[7]/section/div/div/div/div/div/div/div[1]/div/div[1]/div/a[1]").click()
time.sleep(2)
driver.back()
time.sleep(2)

# Writing Relative path for 'view demo' element manually
driver.find_element(By.XPATH, "//div[@class='home-banner-button']/a[2]").click()
time.sleep(2)

# ---------------------   Testing another website    ------------------------------
# and in XPath
driver.get("http://www.flipkart.com")
driver.find_element(By.XPATH, "//*[@class='Pke_EE' and @name='q']").send_keys("Moto Edge 50 Fusion")


# or in XPath
driver.find_element(By.XPATH, "//*[@href='/account/login?re/' or @title='Login']").click()
