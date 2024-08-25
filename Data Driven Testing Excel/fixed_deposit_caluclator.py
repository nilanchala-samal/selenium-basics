import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import ExcelUtils as utils

d = webdriver.Chrome()
d.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
d.maximize_window()
time.sleep(5)

file = "D:\\Selenium\\Excel files\\data_driven_test_case_1.xlsx"
sheet_name = "Sheet1"

rows = utils.get_row_count(file, sheet_name)

for r in range(2, rows + 1):
    principal = utils.read_data(file, sheet_name, r, 1)
    rate_of_interest = utils.read_data(file, sheet_name, r, 2)
    period1 = utils.read_data(file, sheet_name, r, 3)
    period2 = utils.read_data(file, sheet_name, r, 4)
    frequency = utils.read_data(file, sheet_name, r, 5)
    exp_maturity_value = utils.read_data(file, sheet_name, r, 6)

    # passing the values to the application
    principal_ele = d.find_element(By.XPATH, "//input[@id='principal']")
    principal_ele.send_keys(principal)

    rate_of_interest_ele = d.find_element(By.XPATH, "//input[@id='interest']")
    rate_of_interest_ele.send_keys(rate_of_interest)

    period1_ele = d.find_element(By.XPATH, "//input[@id='tenure']")
    period1_ele.send_keys(period1)

    period_dropdown = Select(d.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    period_dropdown.select_by_visible_text(period2)

    frequency_dropdown = Select(d.find_element(By.XPATH, "//select[@id='frequency']"))
    frequency_dropdown.select_by_visible_text(frequency)

    calculate_btn = d.find_element(By.XPATH, "//div[@class='CTR PT15']/a[1]/img")
    calculate_btn.click()
    time.sleep(1)

    calc_maturity_value = d.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    # validation

    if float(exp_maturity_value) == float(calc_maturity_value):
        print("test passed")
        utils.write_data(file, sheet_name, r, 8, "passed")
        utils.fill_green_color(file, sheet_name, r, 8)
    else:
        print("test failed")
        utils.write_data(file, sheet_name, r, 8, "failed")
        utils.fill_red_color(file, sheet_name, r, 8)

    # clearing all the fields
    clear_btn = d.find_element(By.XPATH, "//img[@class='PL5']")
    clear_btn.click()
    time.sleep(1)
