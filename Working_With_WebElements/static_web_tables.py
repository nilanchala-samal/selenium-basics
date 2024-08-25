# Actions can be performed on web tables (static)
# 1. Read number of columns and rows in a table
# 2. Read specific column and row data
# 3. Read all the rows and column data
# 4. Read data based on some conditions

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1. Read number of columns and rows in a table
rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
columns = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th")

print("Number of rows:", len(rows))
print("Number of columns:", len(columns))

# 2. Read specific column and row data  (By reaching to the specific row and column in XPATH)
data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]").text
print(data)

# 3. Read all the rows and column data
print("----------------printing all the row and column data--------------")

for r in range(2, len(rows) + 1):
    for c in range(1, len(columns) + 1):
        data = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[{c}]").text
        print(data, end='         ')
    print()

# 4. Read data based on some conditions (print all the books whose author is Mukesh)
print("---------------- Books written by Mukesh are -------------------")
books_mukesh = []

for r in range(2, len(rows) + 1):
    author_name = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[2]").text
    if author_name == "Mukesh":
        book = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[1]").text
        books_mukesh.append(book)

# print(books_mukesh)
for book in books_mukesh:
    print(book)
driver.close()

