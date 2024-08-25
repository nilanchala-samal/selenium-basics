import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

country_box = driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']")
driver.execute_script("arguments[0].scrollIntoView();", country_box)
country_box.click()

countries = driver.find_elements(By.XPATH, "//span[@class='select2-results']//li")

print(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        break

time.sleep(1)
