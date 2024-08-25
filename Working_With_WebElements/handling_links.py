from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://google.com/")

# 1. click on the link
# driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

# 2. find the number of links in a page
# total_links = driver.find_elements(By.TAG_NAME, 'a')
total_links = driver.find_elements(By.XPATH, '//a')
print("Total", len(total_links), "links are present")

# 3. printing all the links
for link in total_links:
    print(link.get_attribute('href'))

driver.close()