import requests
res = requests.get('http://brinkoffreedom.net/outdoor-activities/trapping-for-winter-survival-or-all-around-for-food-fur-and-fun-part-1/')
res.raise_for_status()
playFile = open('trapping1-2.html','wb')
i=0
for chunk in res.iter_content(100000):
    print(str(i))
    i+=1
    playFile.write(chunk)
playFile.close()
