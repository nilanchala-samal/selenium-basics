from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# 1. Navigating to the site
driver.get("https://demoqa.com/")
driver.maximize_window()
my_wait = WebDriverWait(driver, 10)

element_btn = driver.find_element(By.XPATH, "//div/h5[normalize-space()='Elements']")
driver.execute_script("arguments[0].scrollIntoView();", element_btn)
# 2. click on the element
element_btn.click()

# 3. get the list of items under elements
elements = driver.find_elements(By.XPATH, "//div[@class='element-list collapse show']//li")
for element in elements:
    print(element.text)

# 4. select the text box
driver.find_element(By.XPATH, "//span[normalize-space()='Text Box']").click()

# 5. Entering the details and submit the form
name = driver.find_element(By.XPATH, "//input[@id='userName']")
name.send_keys("Nilanchala Samal")

email = driver.find_element(By.XPATH, "//input[@id='userEmail']")
email.send_keys("nilanchal960@gmail.com")

current_address = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
current_address.send_keys("Demo Current Address")

permanent_address = driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
permanent_address.send_keys("Demo Permanent Address")

driver.find_element(By.XPATH, "//button[@id='submit']").click()

# time.sleep(2)

# 6. Fetching the values post submission and verify

fetched_name = driver.find_element(By.XPATH, "//p[@id='name']").text
print(fetched_name.split(":")[1] == name.get_attribute("value"))

fetched_email = driver.find_element(By.XPATH, "//p[@id='email']").text
print(fetched_email.split(":")[1] == email.get_attribute("value"))

fetched_cur_address = driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
print(fetched_cur_address.split(":")[1] == current_address.get_attribute("value"))

fetched_per_address = driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text
print(fetched_per_address.split(":")[1] == permanent_address.get_attribute("value"))

# 7. click on Alerts, Frames & Windows
driver.find_element(By.XPATH, "//div[normalize-space()='Alerts, Frame & Windows']").click()
# time.sleep(10)
frames = my_wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Frames']")))
frames.click()

# 8. get details from both textboxes
# frame1
driver.switch_to.frame("frame1")
box1_text = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']").text
print(box1_text)
driver.switch_to.parent_frame()

# frame2
driver.switch_to.frame("frame1")
box1_text = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']").text
print(box1_text)
driver.switch_to.parent_frame()

# 9. click on alerts
driver.find_element(By.XPATH, "//span[normalize-space()='Alerts']").click()

# actions on alert
driver.find_element(By.XPATH, "//button[@id='alertButton']").click()
driver.switch_to.alert.accept()

confirm_btn = driver.find_element(By.XPATH, "//button[@id='confirmButton']")
driver.execute_script("arguments[0].scrollIntoView();", confirm_btn)
confirm_btn.click()
driver.switch_to.alert.accept()
confirm_result = driver.find_element(By.XPATH, "//span[@id='confirmResult']").text
print(confirm_result)

prompt_btn = driver.find_element(By.XPATH, "//button[@id='promtButton']")
prompt_btn.click()
alert_window = driver.switch_to.alert
alert_window.send_keys("Nilanchala")
print(alert_window.text, end=': ')
alert_window.accept()
prompt_result = driver.find_element(By.XPATH, "//span[@id='promptResult']").text
print(prompt_result)

# 10. click on Browser Windows
driver.find_element(By.XPATH, "//span[normalize-space()='Browser Windows']").click()

# 11. click on new tab
driver.find_element(By.XPATH, "//button[@id='tabButton']").click()

window_ids = driver.window_handles
driver.switch_to.window(window_ids[1])
new_tab_text = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']").text
print(new_tab_text)
# closing the newly opened tab
driver.close()
# switch back to the previous tab
driver.switch_to.window(window_ids[0])

# 12. click on new window
driver.find_element(By.XPATH,"//button[@id='windowButton']").click()
window_ids = driver.window_handles

driver.switch_to.window(window_ids[1])
new_window_text = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']").text
print(new_window_text)
driver.close()
driver.switch_to.window(window_ids[0])




