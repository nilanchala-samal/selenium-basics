import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")

# Element with no innerText
"""
email_box = driver.find_element(By.XPATH, "//input[@id='Email']")
email_box.clear()
email_box.send_keys("roshanhappyhappy@gmail.com")

print("Result of text:", email_box.text)

print("'value' =", email_box.get_attribute('value'))
print("'class' =", email_box.get_attribute('class'))
print("'id' =", email_box.get_attribute('id'))
print("'type' =", email_box.get_attribute('type'))
print("'name' =", email_box.get_attribute('name'))
print("'hidden' =", email_box.get_attribute('hidden'))   # None
"""
# Element with innerText

login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

print(login_btn.text)

print(login_btn.get_attribute("type"))
print(login_btn.get_attribute("class"))
print(login_btn.get_attribute("value"))   # empty space - as button cannot have value attribute
# print(login_btn.get_attribute("hidden")) # None - as hidden attribute is not present
