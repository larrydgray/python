import leitner.leitner
import logging, keyboard, msvcrt, sys

test=1
logging.basicConfig(filename="quiz_log.txt",
                    level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
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
cards={}
if test==1:
    leitner.set_path('quizs\\')
    card_files=('algo_cards', 'data_struct_cards', 'oop_cards', 'python_cards', 'uml_cards')
else:
    leitner.set_path('quizs\\study\\')
    card_files=('interview_cards')
leitner.set_card_file_names(card_files)
cards = leitner.load_cards()

cycle = leitner.load_test_cycle()

test_cycle_file_name='testcycle'+str(cycle.cycle_num)
logging.debug("Cycle number "+str(cycle.cycle_num))