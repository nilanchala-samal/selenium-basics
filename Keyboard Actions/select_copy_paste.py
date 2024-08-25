import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://text-compare.com/")
driver.maximize_window()
driver.implicitly_wait(10)

textarea1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
textarea2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

textarea1.send_keys("Wake up-to reality")

actionChains = ActionChains(driver)

# selecting the textarea1 text
# actionChains.key_down(Keys.CONTROL)
# actionChains.send_keys("a")
# actionChains.key_up(Keys.CONTROL)
# actionChains.perform()

actionChains.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# copying the text
# actionChains.key_down(Keys.CONTROL)
# actionChains.send_keys('c')
# actionChains.key_up(Keys.CONTROL)
# actionChains.perform()

actionChains.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# changing the focus to textarea2
# actionChains.send_keys(Keys.TAB)
# actionChains.perform()

actionChains.send_keys(Keys.TAB).perform()

# pasting the text in textarea2
# actionChains.key_down(Keys.CONTROL)
# actionChains.send_keys('v')
# actionChains.key_up(Keys.CONTROL)
# actionChains.perform()

actionChains.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

time.sleep(2)
driver.close()
