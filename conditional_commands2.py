from selenium import webdriver as wb
from selenium.webdriver.common.by import By

driver = wb.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# is_selected() method especially used for radio button and check box

print("------------------  Testing the is_selected() method in radio buttons  ---------------------")

first_radioBtn = driver.find_element(By.XPATH, "//input[@value='radio1']")
second_radioBtn = driver.find_element(By.XPATH, "//input[@value='radio2']")
third_radioBtn = driver.find_element(By.XPATH, "//input[@value='radio3']")

print("Default status of the radio button: ")
print("Is radio button 1 selected:", first_radioBtn.is_selected())
print("Is radio button 2 selected:", second_radioBtn.is_selected())
print("Is radio button 3 selected:", third_radioBtn.is_selected())

first_radioBtn.click()  # first radio button is clicked

print("After clicking the first radio button:")
print("Is radio button 1 selected:", first_radioBtn.is_selected())
print("Is radio button 2 selected:", second_radioBtn.is_selected())
print("Is radio button 3 selected:", third_radioBtn.is_selected())

second_radioBtn.click()  # second radio button is clicked

print("After clicking the second radio button:")
print("Is radio button 1 selected:", first_radioBtn.is_selected())
print("Is radio button 2 selected:", second_radioBtn.is_selected())
print("Is radio button 3 selected:", third_radioBtn.is_selected())

third_radioBtn.click()  # third radio button is clicked

print("After clicking the third radio button: ")
print("Is radio button 1 selected:", first_radioBtn.is_selected())
print("Is radio button 2 selected:", second_radioBtn.is_selected())
print("Is radio button 3 selected:", third_radioBtn.is_selected())

print("------------------  Testing the is_selected() method in check boxes  ---------------------")

opt1_checkBox = driver.find_element(By.XPATH, "//*[@id='checkBoxOption1']")
opt2_checkBox = driver.find_element(By.XPATH, "//*[@id='checkBoxOption2']")
opt3_checkBox = driver.find_element(By.XPATH, "//*[@id='checkBoxOption3']")

print("Default status of the check boxes: ")
print("is option1 checkbox selected:", opt1_checkBox.is_selected())
print("is option2 checkbox selected:", opt2_checkBox.is_selected())
print("is option3 checkbox selected:", opt3_checkBox.is_selected())

opt1_checkBox.click()  # option1 checkbox selected

print("After selecting the option1 checkbox:")
print("is option1 checkbox selected:", opt1_checkBox.is_selected())
print("is option2 checkbox selected:", opt2_checkBox.is_selected())
print("is option3 checkbox selected:", opt3_checkBox.is_selected())

opt2_checkBox.click()

print("After selecting the option2 checkbox:")
print("is option1 checkbox selected:", opt1_checkBox.is_selected())
print("is option2 checkbox selected:", opt2_checkBox.is_selected())
print("is option3 checkbox selected:", opt3_checkBox.is_selected())

opt3_checkBox.click()

print("After selecting the option3 checkbox:")
print("is option1 checkbox selected:", opt1_checkBox.is_selected())
print("is option2 checkbox selected:", opt2_checkBox.is_selected())
print("is option3 checkbox selected:", opt3_checkBox.is_selected())
