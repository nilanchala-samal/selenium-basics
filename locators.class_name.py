from selenium import webdriver as wb
from selenium.webdriver.common.by import By

driver = wb.Firefox()
driver.maximize_window()


driver.get("https://www.facebook.com/")
# finding elements using class name selector - It gives multiple tags
matched_elements = driver.find_elements(By.CLASS_NAME, '_6lux')
print(len(matched_elements))
print(matched_elements)
matched_elements[0].send_keys("nilanchala@gmail.com")
driver.close()


# driver.get("http://127.0.0.1:5500/index.html")
# input_elements = driver.find_elements(By.CLASS_NAME, "form-input")
# print(len(input_elements))
# input_elements[0].send_keys("roshan2000@gmail.com")
# # input_elements[1].send_keys("demopassword")
#
#
# driver.close()