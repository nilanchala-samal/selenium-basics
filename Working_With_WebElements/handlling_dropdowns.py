from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

country_dropdown = driver.find_element(By.XPATH, '(//select)[1]')
country_dropdown_obj = Select(country_dropdown)

# select option from dropdown
# 3 in-built methods are there to do so

# country_dropdown_obj.select_by_visible_text("India")
# country_dropdown_obj.select_by_value("IRQ")
# country_dropdown_obj.select_by_index(10)


# Get all the options
countries = country_dropdown_obj.options
print("Total number of countries are:", len(countries))

# for country in countries:
#     print(country.text)

# select the option without using any built-in methods
for country in countries:
    if country.text == "Singapore":
        country.click()
        break

# to find which option is selected
selected_countries = country_dropdown_obj.all_selected_options
print(selected_countries[0].text)


driver.close()
