import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))
print(wb.sheetnames)
sheet = wb['SalesTax']
print(sheet)
print(type(sheet))
print(sheet.title)
anotherSheet = wb.active
print(anotherSheet)