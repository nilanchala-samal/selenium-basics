import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.nseindia.com/")

driver.maximize_window()

actions = ActionChains(driver)
market_data = driver.find_element(By.XPATH, "(//a[@id='link_2'])[1]")
pre_open_market = driver.find_element(By.LINK_TEXT, "Pre-Open Market")

actions.move_to_element(market_data).move_to_element(pre_open_market).click().perform()
time.sleep(5)
driver.quit()
