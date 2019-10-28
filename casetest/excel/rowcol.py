import openpyxl, pprint
wb = openpyxl.load_workbook('example.xlsx', data_only=True)
sheet = wb['SalesTax']
pprint.pprint(tuple(sheet['A1':'C15']))
for  rowOfCellObjects in sheet['A1':'C15']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')
