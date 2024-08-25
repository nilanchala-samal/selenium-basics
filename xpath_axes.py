from selenium import webdriver as wb
from selenium.webdriver.common.by import By

driver = wb.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# 1. self

# self_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Cochin Shipyard')]").text
# self_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Cochin Shipyard')]/self::a").text
# print(self_text)

# 2. parent
# parent_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Cochin Shipyard')]/parent::td").text
# print(parent_text)


# 3. child

# find_element() method
child_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Cochin Shipyard')]/ancestor::tr/child::td")
print(child_element.text)
child_element2 = driver.find_element(By.XPATH, "//*[contains(text(), 'Cochin Shipyard')]/ancestor::tr/child::td[2]")
print(child_element2.text)

# find_elements() method
child_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Cochin Shipyard')]/ancestor::tr/child::td")
print(child_elements)
print("The total number of child elements are:", len(child_elements))

# for child_element in child_elements:
#     print(child_element.text)


# * child axes returns multiple Working_With_WebElements, that's why we have to use find_elements() method along with child axes. If we're using find_element() method then it will give the first child WebElement. We can use the square bracket and element number to locate an element too i.e. If we want to find the third child, then we can use '[3]' after writing the xpath using xpath axes.

# The above concept is also applied to descendant axes.

# 4. ancestor
ancestor_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Cochin Shipyard')]/ancestor::tr").text
print("The ancestor text is:", ancestor_text)

# 5. descendant
descendant_element = driver.find_element(By.XPATH,
                                         "//a[contains(text(), 'Cochin Shipyard')]/ancestor::tr/descendant::a[2]")  # It will return a single WebElement as we're using find_element()
print(descendant_element.text)

all_descendants = driver.find_elements(By.XPATH,
                                       "//*[contains(text(), 'Cochin Shipyard')]/ancestor::tr/descendant::*")  # '*' is to get all the descendants
print("Total descendants:", len(all_descendants))

td_descendants = driver.find_elements(By.XPATH,
                                      "//*[contains(text(), 'Cochin Shipyard')]/ancestor::tr/descendant::td")  # descendants with 'td' tag
print("Total td tag descendants:", len(td_descendants))

a_descendants = driver.find_elements(By.XPATH,
                                     "//*[contains(text(), 'Cochin Shipyard')]/ancestor::tr/descendant::a")  # descendants with 'a' tag
print("Total anchor tag descendants:", len(a_descendants))

# 5. following

all_followings = driver.find_elements(By.XPATH,
                                      "//*[contains(text(), 'Cochin Shipyard')]/ancestor::tr/following::*")
print("Total followings:", len(all_followings))

# 6. preceding

all_precedings = driver.find_elements(By.XPATH,
                                      "//*[contains(text(), 'Cochin Shipyard')]/ancestor::tr/preceding::*")
print("Total precedings:", len(all_precedings))

# 7. following-sibling

all_following_siblings = driver.find_elements(By.XPATH,
                                              "//td[contains(text(), '2,544.60')]/ancestor::tr/following-sibling::*")
print("Total following-siblings:", len(all_following_siblings))

# 8. preceding-sibling
all_preceding_siblings = driver.find_elements(By.XPATH,
                                              "//td[contains(text(), '2,544.60')]/preceding-sibling::*")
print("Total preceding-siblings:", len(all_preceding_siblings))
