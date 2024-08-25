import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# 1. selecting specific checkbox
# driver.find_element(By.XPATH, "//input[@id='checkBoxOption1']").click()

# 2. selecting all checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@value, 'option')]")
print(len(checkboxes))

# approach - 1 for clicking all the elements
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# approach - 2 for clicking all the elements
# for checkbox in checkboxes:
#     checkbox.click()

# 3. select multiple checkboxes by choice
# for checkbox in checkboxes:
#     option = checkbox.get_attribute('value')
#     if option == 'option1' or option == 'option3':
#         checkbox.click()

# 4. select first 2 checkboxes
# length = len(checkboxes)
# for i in range(2):
#     checkboxes[i].click()


# 5. select last 2 checkboxes
length = len(checkboxes)
for i in range(length - 2, length):
    checkboxes[i].click()
time.sleep(3)

# 6. clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():  # verifying if the checkbox is selected or not
        checkbox.click()
driver.close()
