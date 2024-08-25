from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://jqueryui.com/resources/demos/slider/range.html")
driver.implicitly_wait(10)

actions = ActionChains(driver)

min_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[1]")
max_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[2]")

print("Before changing the location of slider: ")
print(min_slider.location)
print(max_slider.location)

actions.drag_and_drop_by_offset(min_slider, 61, 0).perform()
actions.drag_and_drop_by_offset(max_slider, -57, 0).perform()

print("After changing the location of slider: ")
print(min_slider.location)
print(max_slider.location)
