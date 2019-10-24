import csv, pprint

exampleFile = open('salestax.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
pprint.pprint(exampleData)