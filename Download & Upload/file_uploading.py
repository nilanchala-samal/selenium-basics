import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://upload-pdf.pdffiller.com/")

driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='uploader-filepicker-input']").send_keys("D:\\wallpapers\\obito.jpg")


my_wait = WebDriverWait(driver, 10, ignored_exceptions=[Exception]) # WebDriverWait instance

# waiting for the done button to be appeared on the page and then perform the click action
done_btn = my_wait.until(EC.presence_of_element_located((By.XPATH, "//button[@title='Finish editing the document']")))
done_btn.click()

time.sleep(10)
