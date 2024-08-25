from selenium import webdriver
from selenium.webdriver.common.by import By
import os

curr_directory = os.getcwd()


def chrome_setup():
    """ setting up the driver in the chrome for downloading files """

    # for downloading the file in the desired location
    preferences = {"download.default_directory": curr_directory}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    d = webdriver.Chrome(options=ops)
    return d


def edge_setup():
    """ setting up the driver in the edge for downloading files """

    # for downloading the file in the desired location
    preferences = {"download.default_directory": curr_directory}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)

    d = webdriver.Edge(options=ops)
    return d


def firefox_setup():
    """ setting up the driver in the firefox for downloading files """

    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)
    ops.set_preference("browser.download.dir", curr_directory)

    d = webdriver.Firefox(options=ops)
    return d


# Automation code for downloading

# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()
driver.get("https://demo.automationtesting.in/FileDownload.html")

download_btn = driver.find_element(By.LINK_TEXT, "Download")
driver.execute_script("arguments[0].scrollIntoView();", download_btn)
download_btn.click()
