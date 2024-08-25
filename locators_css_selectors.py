from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")

#  1. tag and id
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("demoemail@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("demoemail@gmail.com")

# 2. tag and class
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("demoemail@gmail.com")
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("demoemail@gmail.com")

# 3. tag and attribute
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("nilanchal@gmail.com")
driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("nilanchal@gmail.com")

# 4 tag, class and attribute
# driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("Nothing")
driver.find_element(By.CSS_SELECTOR, ".inputtext[data-testid=royal_pass]").send_keys("Nothing")
