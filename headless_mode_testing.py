from selenium import webdriver


def get_chrome_driver():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")  # enable headless mode
    ops.add_argument("--disable-gpu")  # disabled gpu usage, recommended in headless mode

    d = webdriver.Chrome(options=ops)
    d.get("https://demo.nopcommerce.com")
    d.maximize_window()
    return d


driver = get_chrome_driver()
print(driver.title)
print(driver.current_url)

# Comparing the time taken by the headless mode to that of the Non-headless mode

# from selenium import webdriver
# import time
#
#
# def get_chrome_driver(headless=True):
#     ops = webdriver.ChromeOptions()
#     if headless:
#         ops.add_argument("--headless")  # Enable headless mode
#         ops.add_argument("--window-size=1920,1080")  # Set the window size if needed
#         ops.add_argument("--disable-gpu")  # Disable GPU usage, recommended in headless mode
#
#     d = webdriver.Chrome(options=ops)
#     d.get("https://demo.nopcommerce.com")
#     return d
#
#
# # Measure time for headless mode
# start_time = time.time()
# driver_headless = get_chrome_driver(headless=True)
# headless_duration = time.time() - start_time
# print(
#     f"Headless mode - Title: {driver_headless.title}, URL: {driver_headless.current_url}, Time: {headless_duration} seconds")
# driver_headless.quit()
#
# # Measure time for non-headless mode
# start_time = time.time()
# driver_non_headless = get_chrome_driver(headless=False)
# non_headless_duration = time.time() - start_time
# print(
#     f"Non-headless mode - Title: {driver_non_headless.title}, URL: {driver_non_headless.current_url}, Time: {non_headless_duration} seconds")
# driver_non_headless.quit()
