import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

search_box = driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']")
search_box.send_keys("Anime")
search_box.submit()
time.sleep(2)

driver.find_element(By.XPATH, "//a[normalize-space()='Anime']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Anime-influenced animation']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Anime and manga fandom']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Anime Expo']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Anime song']").click()
time.sleep(3)

# print(driver.current_window_handle) # this is the current window id

all_window_ids = driver.window_handles
print("Total", len(all_window_ids), "windows opened...")

for window_id in all_window_ids:
    driver.switch_to.window(window_id)
    time.sleep(2)
    print(driver.title)
    driver.close()
