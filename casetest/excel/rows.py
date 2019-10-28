import openpyxl, pprint
wb = openpyxl.load_workbook('example.xlsx', data_only=True)
sheet = wb['SalesTax']

pprint.pprint(sheet['3'])
for cellObj in sheet['3']:
    print(cellObj.value)