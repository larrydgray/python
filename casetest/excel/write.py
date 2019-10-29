import openpyxl
from openpyxl.styles import Font
#wb = openpyxl.Workbook()
wb = openpyxl.load_workbook('styled3.xlsx')


sheet = wb['Sheet']
sheet['A1']='Hello world!'
#wb.save('styled3.xlsx')
print(sheet['A1'].value)
italic24Font = Font(size=24, italic=True)
sheet['A1'].font = italic24Font

sheet.row_dimensions[1] = 30.0
sheet.column_dimensions['A'] = 80.0
wb.save('styled3.xlsx')

