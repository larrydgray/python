
import leitner.leitner

#load text from file
#disply one block after the other with user continue
name='cards'
cards = leitner.loadcards('..\\quizs\\', name)
keys = cards.keys()
for key in keys:
    print(cards[key].catagory_id+' box '+str(cards[key].box))


