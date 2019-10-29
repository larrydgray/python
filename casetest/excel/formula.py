import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
sheet['C16']='=sum(C2:C15)'
wb.save('formula.xlsx')