import bs4, pprint
myArticle = open('trapping1.html')
exampleSoup = bs4.BeautifulSoup(myArticle.read(), features="html5lib")
elems = exampleSoup.select('div.entry')
pprint.pprint(elems)