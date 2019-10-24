import csv, re
svg_file = open('shape1.svg', 'w', newline='')
csvWriter = csv.writer(svg_file, delimiter=',', lineterminator='\r\n')
while True:
    print('Enter (000,000,000,000) or (quit) ')
    in_str=input()
    if in_str=='quit':
        break
    if re.fullmatch(r"[0-9 ,]*", in_str) is None:
        print('Input not valid')
    else:
        coordinates=in_str.split(',')
        csvWriter.writerow(coordinates)
svg_file.close()


