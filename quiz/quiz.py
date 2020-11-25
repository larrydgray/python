from quiz_util import *

while True:
    print("Number of questions left in cycle is "+str(len(cycle.id_list)))
    if  len(cycle.id_list)==0: #if we answered all questions in the cycle
        cycle.id_list.append('empty')
        # make sure the cycle file has empty tag in it
        leitner.save_test_cycle_file(cycle.id_list)
        print('End of test cycle '+str(cycle.cycle_num))
        sys.exit() # exit, then user restarts to begin next test cycle
    card=cards[cycle.id_list[0]] # gets 0 because after the question is answered it is removed from list
    # so 0 will always be the next random question
    print('ID:'+card.category_id+' Box '+str(card.box))
    print('QUESTION: '+card.question)
    print('Hit Enter when finnished reviewing question.')
    keyboard.wait('\r') # wait for enter key
    print('ANSWER: '+card.answer)
    print('(P)romote, (D)emote, (L)eave in same box.')
    process_card(card,cycle.id_list) # gets key input and moves or leaves card in boxes
    print('(N)ext question or (Q)uit')
    while True:
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            if ch == b'n':  # byte n
                break 
            elif ch == b'q': # byte q
                print ('Quiting Cycle number '+str(cycle.cycle_num)+' with '+
                    str(len(cycle.id_list))+' questions left.')
                sys.exit() # the cycle has already been saved after last card was processed
            else:
                continue # if not n or q keep getting key input
    print()
