# we need to install requests package

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
links = driver.find_elements(By.XPATH, "//a")

count_broken = count_valid = 0

for link in links:
    url = link.get_attribute("href")
    try:
        resp = requests.head(url)
    except:
        None
    if resp.status_code >= 400:
        print(url, "   is a broken link   ")
        count_broken += 1
    else:
        print(url, "   is a valid link   ")
        count_valid += 1

print("Broken links:", count_broken)
print("Valid links:", count_valid)
