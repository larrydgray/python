import datetime

print(datetime.datetime.now())
dt = datetime.datetime(2015,10,21,16,29,0)
# old pyton formatting strings
print('yr %s mo %s dy %s' %(dt.year, dt.month,dt.day))
print('hr %s m %s s %s' %(dt.hour, dt.minute, dt.second))
# new methods
print(f'yr {dt.year} mo {dt.month} dy {dt.day}')
print(f'hr {dt.hour} m {dt.minute} s {dt.second}')
# and
print(dt.strftime("yr %Y mo %m dy %d"))
print(dt.strftime("hr %H m %M s %S"))
# and
print('yr {} mo {} dy {}'.format(dt.year, dt.month, dt.day))
print('hr {} m {} s {}'.format(dt.hour, dt.minute, dt.second))

