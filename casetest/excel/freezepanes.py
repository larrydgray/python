import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
sheet.freeze_panes = 'B2'
wb.save('example_freeze.xlsx')