import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

# finding and clicking the date picker element
datepicker = driver.find_element(By.XPATH, "//input[@id='dob']")
datepicker.click()

exp_year = "2022"
exp_month = "Apr"
exp_date = "19"

year_select = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//select[@class='ui-datepicker-year']"))
)
years = Select(year_select)
years.select_by_visible_text(exp_year)

# Re-locate the month selector after selecting the year
month_select = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//select[@class='ui-datepicker-month']"))
)
months = Select(month_select)
months.select_by_visible_text(exp_month)

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if date.text == exp_date:
        date.click()
        break

print(datepicker.get_attribute('value'))

time.sleep(5)
