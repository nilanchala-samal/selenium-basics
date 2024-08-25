import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

time.sleep(2)
#
# driver.find_element(By.XPATH, "//input[@id='product_549']").click()
# driver.find_element(By.XPATH, "//input[@id='travname']").send_keys("Nilanchala")
# driver.find_element(By.XPATH, "//input[@id='travlastname']").send_keys("Samal")
# driver.find_element(By.XPATH, "//textarea[@id='order_comments']").send_keys("Call me while you deliver")
#
# # finding and clicking the date picker element
# datepicker = driver.find_element(By.XPATH, "//input[@id='dob']")
# datepicker.click()
#
# exp_year = "2022"
# exp_month = "Apr"
# exp_date = "19"
#
# year_select = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//select[@class='ui-datepicker-year']"))
# )
# years = Select(year_select)
# years.select_by_visible_text(exp_year)
#
# # Re-locate the month selector after selecting the year
# month_select = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//select[@class='ui-datepicker-month']"))
# )
# months = Select(month_select)
# months.select_by_visible_text(exp_month)
#
# dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
# for date in dates:
#     if date.text == exp_date:
#         date.click()
#         break
#
# driver.find_element(By.XPATH, "//input[@id='sex_1']").click()
# driver.find_element(By.XPATH, "//input[@id='fromcity']").send_keys("Bengaluru")
# driver.find_element(By.XPATH, "//input[@id='tocity']").send_keys("Bhubaneswar")

driver.find_element(By.XPATH, "//span[@id='select2-reasondummy-container']").click()
purposes = driver.find_elements(By.XPATH, "//span[@class='select2-results']//li")
for purpose in purposes:
    if purpose.text == "Visa extension":
        purpose.click()
        break

# driver.find_element(By.XPATH, "//input[@id='deliverymethod_2']").click()
#
# driver.find_element(By.XPATH, "//input[@id='billname']").send_keys("Nilanchala Samal")
# driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("7894364736")
# driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("nilanchal960@gmail.com")
#
# countries = driver.find_elements(By.XPATH, "//span[@class='select2-results']//li")
# for country in countries:
#     if country.text == "India":
#         country.click()
#         break
#
# driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("13, Lali ln")
# driver.find_element(By.XPATH, "//input[@id='billing_address_2']").send_keys("Shree Vaibhav")
# driver.find_element(By.XPATH, "//input[@id='billing_city']").send_keys("Bengaluru")
#
# # department_dropdown = Select(driver.find_element(By.XPATH, "//span[@id='select2-billing_state-container']"))
# # department_dropdown.select_by_visible_text("Comayagua")
# driver.find_element(By.XPATH, "//input[@id='billing_postcode']").send_keys("560037")

time.sleep(4)
