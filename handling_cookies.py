from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

cookies = driver.get_cookies()  # returns a list of cookies in which each cookie is a dictionary
print("Number of cookies created: ", len(cookies))
print(type(cookies))
# print(type(cookies[0]))

# information about the cookies
for cookie in cookies:
    print(cookie)

# cookie names and values
# for cookie in cookies:
#     # print(cookie['name'])
#     print(cookie.get('name'), ":", cookie.get('value'))

# adding cooking to the browser
driver.add_cookie({"name": "myCookie", "value": "nilanchala_samal_cookie"})
cookies = driver.get_cookies()
print("Number of cookies after adding one:", len(cookies))

# deleting a specific cookie
driver.delete_cookie("myCookie")
cookies = driver.get_cookies()
print("Number of cookies after deleting one:", len(cookies))

# deleting all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Number of cookies after deleting all cookies:", len(cookies))
