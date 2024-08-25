# //div[@class='rt-tr']/div/div[1]  - col
# //div[@class='rt-tbody']/div[4]/div - row
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://demoqa.com/webtables")
driver.maximize_window()

# finding the number of rows and columns
rows = driver.find_elements(By.XPATH, "//div[@class='rt-tbody']/div/div")
cols = driver.find_elements(By.XPATH, "//div[@class='rt-tr']/div/div[1]")

print("Number of rows:", len(rows))
print("Number of columns:", len(cols))

# read the specific column and row data ( row - 2, col - 3 )
data = driver.find_element(By.XPATH, "//div[@class='rt-tbody']/div[5]/div/div[1]").text
print("The data present at 5th row and 3rd column is:", data)

# read all rows and columns
for r in range(1, len(rows) + 1):
    for c in range(1, len(cols) + 1):
        data = driver.find_element(By.XPATH, f"//div[@class='rt-tbody']/div[{r}]/div/div[{c}]").text
        if data == " ":
            break
        else:
            print(data, end='     ')
    else:
        print()

# read the data based on some conditions ( print the names whose age is >= 30 )
names_list = []
for r in range(1, len(rows)+1):
    age = driver.find_element(By.XPATH, f"//div[@class='rt-tbody']/div[{r}]/div/div[3]").text
    if age == " ":
        break
    elif int(age) >= 30:
        name = driver.find_element(By.XPATH, f"//div[@class='rt-tbody']/div[{r}]/div/div[1]").text
        names_list.append(name)

print("First names of the person whose age is more than 30 are:", end=" ")
for name in names_list:
    print(name, end=", ")
print()

driver.close()
