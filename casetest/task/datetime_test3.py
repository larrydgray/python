import datetime, time
oct24th = datetime.datetime(2019,10,24,16,29,0)
print('Formatted dates.')
print(oct24th.strftime('%Y/%m/%d #H:%M:%S'))
print(oct24th.strftime('%I:%M %p'))
print(oct24th.strftime("%B of '%y"))
print('Date String to date object.')
print('October 24, 2019 is')
print(datetime.datetime.strptime('October 24, 2019', 
    '%B %d, %Y'))
print('2019/10/24 16:29:00 is')
print(datetime.datetime.strptime('2019/10/24 16:29:00', 
    '%Y/%m/%d %H:%M:%S'))
print("October of '19 is")
print(datetime.datetime.strptime("October of '19",
    "%B of '%y"))
print("November of '63 is")
print(datetime.datetime.strptime("November of '63",
    "%B of '%y"))