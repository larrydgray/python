import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
refObj = openpyxl.chart.Reference(sheet, min_col=3, min_row=2,max_col=3,max_row=13)
seriesObj = openpyxl.chart.Series(refObj, title='First series')
chartObj = openpyxl.chart.BarChart()
chartObj.title='My Chart'
chartObj.append(seriesObj)
sheet.add_chart(chartObj, 'D13')
wb.save('sampleChart.xlsx')
