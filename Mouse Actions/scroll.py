import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://hianime.to/home")
driver.implicitly_wait(10)

# scroll down page by some pixel

# driver.execute_script("window.scrollBy(0, 1000)", "")
# pixels = driver.execute_script("return window.pageYOffset")
# print("Number of pixels moved:", pixels)

# scroll till a particular element is visible

# img = driver.find_element(By.XPATH, "//img[@alt='Twilight Out of Focus']")
# driver.execute_script("arguments[0].scrollIntoView();", img)
# time.sleep(2)
#
# pixels_scrolled = driver.execute_script("return window.pageYOffset")
# print("Number of pixels moved:", pixels_scrolled)

# scroll till the end of the page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
pixels_scrolled = driver.execute_script("return window.pageYOffset")
print("Number of pixels moved:", pixels_scrolled)

time.sleep(2)

# going to the top of the page
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")
pixels_scrolled = driver.execute_script("return window.pageYOffset")
print("Number of pixels moved:", pixels_scrolled)

time.sleep(2)
