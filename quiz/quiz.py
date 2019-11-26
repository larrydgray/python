import leitner.leitner
import keyboard, msvcrt, sys

def processcard(card, cycle_idlist):
    while True:  
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            if ch == b'l':  
                print('Leaving')
                leitner.removeidfromtestcycle(card.catagory_id,'quizs\\', testcyclefilename)
                cycle_idlist.remove(card.catagory_id)
                break  
            elif ch == b'p':
                print('Promoting')
                leitner.moveidtobox(card.catagory_id,'quizs\\', card.box+1, card.box)
                card.box+=1
                leitner.removeidfromtestcycle(card.catagory_id,'quizs\\', testcyclefilename)
                cycle_idlist.remove(card.catagory_id)
                break
            elif ch == b'd':
                print('Demoting')
                if card.box>1:
                    leitner.moveidtobox(card.catagory_id,'quizs\\', card.box-1, card.box)
                    card.box-=1
                    leitner.removeidfromtestcycle(card.catagory_id,'quizs\\', testcyclefilename)
                    cycle_idlist.remove(card.catagory_id)
                break
            else:
                continue
        

cards = leitner.loadcards('quizs\\','cards')
cycle = leitner.loadtestcycle('quizs\\', cards)
testcyclefilename='testcycle'+str(cycle.cyclenum)
print("Cycle number "+str(cycle.cyclenum))
while True:
    print("Number of questions left in cycle is "+str(len(cycle.idlist)))
    if  cycle.idlist[0]=='':
        cycle.idlist[0]='empty'
        leitner.savetestcyclefile(cycle,'quizs\\', cards)
        print('End of test cycle.')
        sys.exit()
    card=cards[cycle.idlist[0]]
    print('ID:'+card.catagory_id+' Box '+str(card.box))
    print('QUESTION: '+card.question)
    print('Hit Enter when finnished reviewing question.')
    keyboard.wait('\r')
    print('ANSWER: '+card.answer)
    print('(P)romote, (D)emote, (L)eave in same box.')
    processcard(card,cycle.idlist)
    print('(N)ext question or (Q)uit')
    while True:
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            if ch == b'n':  
                break 
            elif ch == b'q': 
                print ('Quiting Cycle number '+str(cycle.cyclenum)+' with '+
                    str(len(cycle.idlist))+' questions left.')
                sys.exit()      
            else:
                continue 
    print()
