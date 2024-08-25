import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

curr_directory = os.getcwd()


def chrome_setup():
    """ setting up the driver in the chrome for downloading files """

    # for downloading the file in the desired location
    preferences = {
        "download.default_directory": curr_directory,
        "plugins.always_open_pdf_externally": True
    }
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    d = webdriver.Chrome(options=ops)
    return d


def edge_setup():
    """ setting up the driver in the edge for downloading files """

    # for downloading the file in the desired location
    preferences = {
        "download.default_directory": curr_directory,
        "plugins.always_open_pdf_externally": True # directly download the file instead of opening
    }
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)

    d = webdriver.Edge(options=ops)
    return d


def firefox_setup():
    """ setting up the driver in the firefox for downloading files """

    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)  # 0 - desktop, 1 - default, 2 - desired
    ops.set_preference("browser.download.dir", curr_directory) # pass the desired directory
    ops.set_preference("pdfjs.disabled", True)  # for directly downloading the pdf file

    d = webdriver.Firefox(options=ops)
    return d


# Automation code for downloading

# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()


driver.get(
    "https://www.google.com/search?q=pdf+download+sites+for+automation+testing&sca_esv=b97a298801241196&sca_upv=1&rlz=1C1GCEJ_enIN1024IN1024&sxsrf=ADLYWILqZxoYpm45YCzfn0eLqx9_BHYXWA%3A1722058529336&ei=IYekZvyPFIK74-EP7YjkuQY&ved=0ahUKEwi8pLH3v8aHAxWC3TgGHW0EOWcQ4dUDCBA&uact=5&oq=pdf+download+sites+for+automation+testing&gs_lp=Egxnd3Mtd2l6LXNlcnAiKXBkZiBkb3dubG9hZCBzaXRlcyBmb3IgYXV0b21hdGlvbiB0ZXN0aW5nMgUQIRigATIFECEYoAEyBRAhGKABMgUQIRigATIFECEYnwUyBRAhGJ8FMgUQIRifBTIFECEYnwUyBRAhGJ8FMgUQIRifBUi5KFDUBliLJnABeACQAQCYAcABoAG8GaoBBDAuMjS4AQPIAQD4AQGYAhigAsQZwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigXCAg4QABiwAxjkAhjWBNgBAcICGRAuGIAEGLADGNEDGEMYxwEYyAMYigXYAQLCAgUQABiABMICBhAAGBYYHsICCxAAGIAEGIYDGIoFwgIIEAAYgAQYogTCAggQABiiBBiJBcICBBAhGBXCAgcQIRigARgKmAMAiAYBkAYRugYGCAEQARgJugYGCAIQARgIkgcEMS4yM6AHjd0B&sclient=gws-wiz-serp")

download_btn = driver.find_element(By.XPATH, "//h3[normalize-space()='Automated Testing Handbook']")
download_btn.click()
time.sleep(4)
