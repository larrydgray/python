import leitner.leitner
cards=leitner.loadcards('..\\quizs\\','cards')
testcycle = leitner.loadtestcycle('..\\quizs\\', cards)
cyclenum = testcycle.cyclenum
ids = testcycle.idlist
print(cyclenum)
for id in ids:
    print(id+' box '+str(cards[id].box))
