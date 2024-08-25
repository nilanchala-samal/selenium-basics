import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

dropdown = driver.find_element(By.ID, "dropdown-class-example")
dropdown_obj = Select(dropdown)

all_options = dropdown_obj.options  # getting all the options
print(len(all_options))

# printing all the option values
for option in all_options:
    print(option.text)

# dropdown_obj.select_by_visible_text("Option1")
# dropdown_obj.select_by_value("option2")
# dropdown_obj.select_by_index(3)


#  selecting the options without using built-in functions
for option in all_options:
    if option.text == 'Option2':
        option.click()
        break
time.sleep(2)

driver.close()