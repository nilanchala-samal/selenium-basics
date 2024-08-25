import openpyxl

file = "D:\\Selenium\\Excel files\\empty_sheet.xlsx"
workbook = openpyxl.load_workbook(file)
sheet = workbook.active  # or  workbook["Sheet1"]

for r in range(1, 10):
    for c in range(1, 5):
        sheet.cell(r, c).value = "demo_data"

workbook.save(file)
