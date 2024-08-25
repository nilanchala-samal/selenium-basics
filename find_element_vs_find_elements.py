import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

# find_element() method  - Returns a single WebElement

# 1 - Locator matching with a single WebElement
# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("Apple")
# time.sleep(2)

# 2 - Locator matching with multiple Working_With_WebElements
# element = driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(element.text)

# 3 - Locator doesn't match with any WebElement - (It will throw NoSuchElementException - Unable to locate the element)
# login_element = driver.find_element(By.LINK_TEXT, "Log")
# login_element.click()
# time.sleep(2)


# find_elements() method  -  returns multiple Working_With_WebElements in a list

# 1 - Locator matching with a single WebElement
# elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(elements))
# elements[0].send_keys("Apple Macbook Pro")
# time.sleep(2)

# 2 - Locator matching with multiple Working_With_WebElements
# elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(len(elements))
# # print(elements[0].text)
#
# for element in elements:
#     print(element.text)


# 3 - Locator doesn't match with any WebElement - (It will not throw any exception - returns an empty list)
elements = driver.find_elements(By.LINK_TEXT, "Log")
print(elements)
print(f"The element list has {len(elements)} items")
time.sleep(2)

