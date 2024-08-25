import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

# sending the data through send_keys() method
# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("03/15/2000")

# the below is the date I want to select from the date-picker
exp_year = "2022"
exp_month = "April"
exp_date = "19"

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

while True:
    act_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    act_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text

    if act_month == exp_month and act_year == exp_year:
        break
    else:
        # driver.find_element(By.XPATH, "//a[@title='Next']").click()  # for future dates
        driver.find_element(By.XPATH, "//a[@title='Prev']").click()  # for past dates

# selecting the dates
dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in dates:
    if date.text == exp_date:
        date.click()
        break

time.sleep(5)
