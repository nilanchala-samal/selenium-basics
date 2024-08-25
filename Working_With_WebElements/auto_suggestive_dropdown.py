import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "autocomplete").send_keys("ind")
time.sleep(3)

list_country = driver.find_elements(By.ID, "ui-id-1")

for country in list_country:
    # print(country.text)   # It will print all the country suggested after typing 'ind'
    if country.text == "India":
        country.click()
        break
time.sleep(4)
