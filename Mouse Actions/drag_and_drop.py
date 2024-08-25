from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

actions = ActionChains(driver)

oslo = driver.find_element(By.ID, "box1")
norway = driver.find_element(By.ID, "box101")

stockholm = driver.find_element(By.ID, "box2")
sweden = driver.find_element(By.ID, "box102")

washington = driver.find_element(By.ID, "box3")
united_states = driver.find_element(By.ID, "box103")

copenhagen = driver.find_element(By.ID, "box4")
denmark = driver.find_element(By.ID, "box104")

seoul = driver.find_element(By.ID, "box5")
south_korea = driver.find_element(By.ID, "box105")

rome = driver.find_element(By.ID, "box6")
italy = driver.find_element(By.ID, "box106")

madrid = driver.find_element(By.ID, "box7")
spain = driver.find_element(By.ID, "box107")

actions.drag_and_drop(oslo, norway).perform()
actions.drag_and_drop(stockholm, sweden).perform()
actions.drag_and_drop(washington, united_states).perform()
actions.drag_and_drop(madrid, spain).perform()
actions.drag_and_drop(rome, italy).perform()
actions.drag_and_drop(seoul, south_korea).perform()
actions.drag_and_drop(copenhagen, denmark).perform()

driver.close()