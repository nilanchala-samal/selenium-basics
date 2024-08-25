# Sites that are asking for permission for location, microphone and video
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=opts)

driver.get("https://whatmylocation.com/")
driver.maximize_window()

