import leitner.leitner
import keyboard, msvcrt, sys

# this gets keyboard key input and either promotes, 
# demotes or leaves the card where it is in boxes.
def process_card(card, cycle_id_list):
    while True:  
        if msvcrt.kbhit(): # get key input (windows)
            ch = msvcrt.getch()
            if ch == b'l':  # b'l' is byte l
                print('Leaving')
                leitner.remove_id_from_test_cycle(card.category_id)
                cycle_id_list.remove(card.category_id)
                break  
            elif ch == b'p': # byte p
                print('Promoting')
                leitner.move_id_to_box(card.category_id, card.box+1, card.box)
                card.box+=1
                leitner.remove_id_from_test_cycle(card.category_id)
                cycle_id_list.remove(card.category_id)
                break
            elif ch == b'd': # byte d
                
                if card.box>1: # can't demote if card is in box 1
                    print('Demoting')
                    leitner.move_id_to_box(card.category_id, card.box-1, card.box)
                    card.box-=1
                    leitner.remove_id_from_test_cycle(card.category_id)
                    cycle_id_list.remove(card.category_id)
                else:
                    print('Leaving')
                break
            else:
                continue # any key but l p or d and we keep looping
        
leitner.set_path('quizs\\')
leitner.set_test_cycle_file_name('algo_cards')
cards = leitner.load_cards()
leitner.set_test_cycle_file_name('data_struct_cards')
cards.update(leitner.load_cards())
leitner.set_test_cycle_file_name('oop_cards')
cards.update(leitner.load_cards())
leitner.set_test_cycle_file_name('uml_cards')
cards.update(leitner.load_cards())

cycle = leitner.load_test_cycle()

test_cycle_file_name='testcycle'+str(cycle.cycle_num)
print("Cycle number "+str(cycle.cycle_num))
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
