import openpyxl, pprint
wb = openpyxl.load_workbook('example.xlsx', data_only=True)
sheet = wb['SalesTax']

pprint.pprint(sheet['A'])
for cellObj in sheet['A']:
    print(cellObj.value)
