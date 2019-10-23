import requests, bs4
res = requests.get('http://mostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text,features="html.parser")
print(type(noStarchSoup))