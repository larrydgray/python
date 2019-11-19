import leitner, pprint
cards = leitner.loadcards('cards')
keys=cards.keys()
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(list(keys))
for key in keys:
    print(key+' '+str(cards[key].box))