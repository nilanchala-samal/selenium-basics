from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.facebook.com/")
matched_elems = driver.find_elements(By.TAG_NAME, 'a')
print(len(matched_elems))

driver.close()

# CLASS_NAME and TAG_NAME always used with find_elements() method as it returns a sized list of 'WebElement'.
