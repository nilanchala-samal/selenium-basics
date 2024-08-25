import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import mysql.connector as db

d = webdriver.Chrome()
d.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
d.maximize_window()
time.sleep(3)

# creating the connection to the database
try:
    conn = db.connect(host="localhost", port=3306, user="root", passwd="root", db="data_driven_testing_selenium")
    cursor = conn.cursor()
    cursor.execute("select * from fixed_deposit_calculator")
    for row in cursor:
        # extracting the data from the database from each row
        principal = row[0]
        rate_of_interest = row[1]
        per1 = row[2]
        per2 = row[3]
        frequency = row[4]
        exp_mvalue = row[5]

        # passing the values to the application
        principal_ele = d.find_element(By.XPATH, "//input[@id='principal']")
        principal_ele.send_keys(principal)

        rate_of_interest_ele = d.find_element(By.XPATH, "//input[@id='interest']")
        rate_of_interest_ele.send_keys(rate_of_interest)

        period1_ele = d.find_element(By.XPATH, "//input[@id='tenure']")
        period1_ele.send_keys(per1)

        period_dropdown = Select(d.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
        period_dropdown.select_by_visible_text(per2)

        frequency_dropdown = Select(d.find_element(By.XPATH, "//select[@id='frequency']"))
        frequency_dropdown.select_by_visible_text(frequency)

        calculate_btn = d.find_element(By.XPATH, "//div[@class='CTR PT15']/a[1]/img")
        calculate_btn.click()
        time.sleep(1)

        calc_mvalue = d.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        # validation
        if float(exp_mvalue) == float(calc_mvalue):
            print("test passed")
        else:
            print("test failed")

        # clearing all the fields
        clear_btn = d.find_element(By.XPATH, "//img[@class='PL5']")
        clear_btn.click()
    conn.close()
except:
    print("Connection Unsuccessful...Cannot connect to the database")

d.close()
