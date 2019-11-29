import leitner.leitner
import keyboard, msvcrt, sys

def process_card(card, cycle_id_list):
    while True:  
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            if ch == b'l':  
                print('Leaving')
                leitner.remove_id_from_test_cycle(card.category_id,'quizs\\', test_cycle_file_name)
                cycle_id_list.remove(card.category_id)
                break  
            elif ch == b'p':
                print('Promoting')
                leitner.move_id_to_box(card.category_id,'quizs\\', card.box+1, card.box)
                card.box+=1
                leitner.remove_id_from_test_cycle(card.category_id,'quizs\\', test_cycle_file_name)
                cycle_id_list.remove(card.category_id)
                break
            elif ch == b'd':
                
                if card.box>1:
                    print('Demoting')
                    leitner.move_id_to_box(card.category_id,'quizs\\', card.box-1, card.box)
                    card.box-=1
                    leitner.remove_id_from_test_cycle(card.category_id,'quizs\\', test_cycle_file_name)
                    cycle_id_list.remove(card.catagory_id)
                else:
                    print('Leaving')
                break
            else:
                continue
        

cards = leitner.load_cards('quizs\\','cards')
cycle = leitner.load_test_cycle('quizs\\', cards)
test_cycle_file_name='testcycle'+str(cycle.cycle_num)
print("Cycle number "+str(cycle.cycle_num))
while True:
    print("Number of questions left in cycle is "+str(len(cycle.id_list)))
    if  len(cycle.id_list)==0:
        cycle.id_list.append('empty')
        
        leitner.save_test_cycle_file(cycle.id_list,'quizs\\', test_cycle_file_name)
        print('End of test cycle '+str(cycle.cycle_num))
        sys.exit()
    card=cards[cycle.id_list[0]]
    print('ID:'+card.category_id+' Box '+str(card.box))
    print('QUESTION: '+card.question)
    print('Hit Enter when finnished reviewing question.')
    keyboard.wait('\r')
    print('ANSWER: '+card.answer)
    print('(P)romote, (D)emote, (L)eave in same box.')
    process_card(card,cycle.id_list)
    print('(N)ext question or (Q)uit')
    while True:
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            if ch == b'n':  
                break 
            elif ch == b'q': 
                print ('Quiting Cycle number '+str(cycle.cycle_num)+' with '+
                    str(len(cycle.id_list))+' questions left.')
                sys.exit()      
            else:
                continue 
    print()
