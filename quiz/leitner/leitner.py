import os, sys
import logging, random
#logging.disable(logging.DEBUG)



def find_test_cycle_file(path):
    
    # create a list of file and sub directories 
    # names in the given directory 
    list_of_files = os.listdir(path)
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_files:
        # Create full path
        full_path = os.path.join(path, entry)
        # If entry is a directory then get the list of files in this directory 
        if not os.path.isdir(full_path):
            all_files.append(entry)
    for file_name in all_files:
        logging.debug(file_name[:len(file_name)-4])
        if file_name[:9]=='testcycle':
            return file_name[:len(file_name)-4]
    return None

def load_test_cycle_file(path, test_cycle_file_name):
    
    cycle_file = open(path+test_cycle_file_name+".txt",'r')
    cycle=cycle_file.readlines()
    new_cycle=[]
    for line in cycle:
        new_cycle.append(line.strip())
    return new_cycle    

def save_test_cycle_file(test_cycle, path, test_cycle_file_name): 
    logging.debug("Save Test Cycle")
    cycle_file = open(path+test_cycle_file_name+".txt",'w')
    
    for id in test_cycle:
        cycle_file.write(id+'\n')
    cycle_file.close()

def remove_id_from_test_cycle(id, path, test_cycle_file_name):
    logging.debug("Remove From Test Cycle")
    test_cycle = load_test_cycle_file(path, test_cycle_file_name)
    test_cycle.remove(id)
    save_test_cycle_file(test_cycle, path, test_cycle_file_name)

def remove_id_from_box(id, path, box_num):
    logging.debug("Remove From Box")
    box = load_box(path, box_num)
    box.remove(id)
    if len(box) == 0:
        box.append('empty')
    save_box(box, path, box_num)

def add_id_to_box(id, path, box_num):
    logging.debug("Add To Box")
    box = load_box(path, box_num)
    if box[0]=='empty':
        box.remove('empty')
    box.append(id)
    save_box(box, path, box_num)

def move_id_to_box(id, path, to_box_num, from_box_num):
    logging.debug("Moving to Box")
    remove_id_from_box(id, path, from_box_num)
    add_id_to_box(id,path, to_box_num)

def find_box_file(path, box_num):
    
    # create a list of file and sub directories 
    # names in the given directory 
    list_of_files = os.listdir(path)
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_files:
        # Create full path
        full_path = os.path.join(path, entry)
        # If entry is a directory then get the list of files in this directory 
        if not os.path.isdir(full_path):
            all_files.append(entry)
    for file_name in all_files:
        logging.debug(file_name[:len(file_name)-4])
        if file_name[:4]==('box'+str(box_num)):
            return file_name[:len(file_name)-4]
    return None

def new_cycle(path, cards):
    logging.debug('No Test Cycle File Found. Creating new Cycle 1.')
    cycle_file = open(path+'testcycle1.txt','w')
    ids_keys=cards.keys()
    ids = [] 
    for key in ids_keys: 
        ids.append(key) 
    print('Number of cards '+str(len(ids)))
    print(ids)
    for id in ids:
        cycle_file.write(id+'\n')
    print('Done making ids')
    cycle_file.close()
    print('Loading cards into Box1')
    for id in ids:
        cards[id].box=1
    print('Set Cards to Box1')
    test_cycle = TestCycle(1,ids)
    print('Made TestCycle')
    box_file = open(path+'box1.txt','w')
    print('Making box1')
    for id in ids:
        box_file.write(id+'\n')
    box_file.close()
    print('Making box2')
    box_file = open(path+'box2.txt','w')
    box_file.write('empty')
    box_file.close()
    print('Making box3')
    box_file = open(path+'box3.txt','w')
    box_file.write('empty')
    box_file.close()
    print('Making box4')
    box_file = open(path+'box4.txt','w')
    box_file.write('empty')
    box_file.close()
    print('Making box5')
    box_file = open(path+'box5.txt','w')
    box_file.write('empty')
    box_file.close()
    print('Making box6')
    box_file = open(path+'box6.txt','w')
    box_file.write('empty')
    box_file.close()
    
    return test_cycle

def start_next_cycle(path, cards, test_cycle_num):
    logging.debug('Starting new cycle number '+str(test_cycle_num))
    highest_box=1
    if(test_cycle_num%2==0):
        highest_box+=1
    if(test_cycle_num%4==0):
        highest_box+=1
    if(test_cycle_num%8==0):
        highest_box+=1
    if(test_cycle_num%16==0):
        highest_box+=1
    logging.debug('highestbox '+str(highest_box))
    cycle_ids=[]

    keys=cards.keys()
    print('Loading box1 to box'+str(highest_box))
    for key in keys:
        card=cards[key]
        if(card.box>0 and card.box<=highest_box):
            cycle_ids.append(key)
    os.rename(path+'testcycle'+str(test_cycle_num)+'.txt', 
        path+'testcycle'+str(test_cycle_num+1)+'.txt')
    test_cycle_file = open(path+'testcycle'+str(test_cycle_num+1)+'.txt','w')
    for id in cycle_ids:
        test_cycle_file.write(id+'\n')
    
    testcycle = TestCycle(test_cycle_num+1,cycle_ids)

    return testcycle
    
def load_test_cycle(path,cards):
    
    test_cycle_file_name=find_test_cycle_file(path)
    logging.debug(test_cycle_file_name)
    logging.debug(path)
    # None means brand new study cycle starting at 1
    if(test_cycle_file_name==None):
       return new_cycle(path, cards)
    else:
        #else not brand new cycle, continuing cycle
        cycle_ids=load_test_cycle_file(path, test_cycle_file_name)
        test_cycle_num=int(test_cycle_file_name[9:])
        # if empty test cycle file then beginning next cycle
        if(cycle_ids[0]=='empty'):
            return start_next_cycle(path, cards, test_cycle_num)
        # else load current saved cycle state and begin testing
        else:
            test_cycle = TestCycle(test_cycle_num,cycle_ids)
            return test_cycle

def save_box(box, path, box_num):
     box_file = open(path+'box'+str(box_num)+'.txt','w')
     for id in box:
         box_file.write(id+'\n')
     box_file.close()

def load_box(path, box_num):
    if box_num<1 or box_num>6:
        logging.debug('Box number '+str(box_num)+' out of range. Should be 1 to 6.')
        sys.exit()
    box_file = open(path+'box'+str(box_num)+'.txt','r')
    box=box_file.readlines()
    new_box=[]
    for line in box:
        new_box.append(line.strip())
    return new_box        

def load_boxes(path, cards):
    box_file = find_box_file(path, 1)
    if(box_file==None):
         return cards
    else:
        card_ids=load_box(path,1)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=1
    box_file = find_box_file(path, 2)
    if(box_file==None):
         return cards
    else:
        card_ids=load_box(path, 2)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=2
    box_file = find_box_file(path, 3)
    if(box_file==None):
         return cards
    else:
        card_ids=load_box(path, 3)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=3
    box_file = find_box_file(path, 4)
    if(box_file==None):
         return cards
    else:
        card_ids=load_box(path, 4)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=4
    box_file = find_box_file(path, 5)
    if(box_file==None):
         return cards
    else:
        card_ids=load_box(path, 5)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=5
    box_file = find_box_file(path, 6)
    if(box_file==None):
         return cards
    else:
        card_ids=load_box(path, 6)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=6
    return cards

def load_cards(path,file_name):
    logging.debug(os.getcwd())
    quiz_file = open(path+file_name+".txt",'r')
    aquiz = quiz_file.read()
    card_parser = CardParser(aquiz)
    cards={}
    while True:
        card_id=''
        question=''
        answer=''
        
        # not an elegant way to do this, but it will work
        # need to rewrite this
        data=card_parser.get_block()
        if(data==''):
            if(cards!=False):
                
                load_boxes(path, cards)
                return cards
            else:
                print('Parse Error! Unexpected end of file. No Data')
                return None
        if(data[:3]!='ID:'):
            print('Parse Error! ID: Expected.')
            return None
        else:
            card_id=data[3:].strip()

        data=card_parser.get_block()
        if(data==''):
            print('Parse Error! Unexpected end of file.')
            return None
        if(data[:9]!='QUESTION:'):
            print('Parse Error! QUESTION: Expected.')
            return None
        else:
            question=data[9:]

        data=card_parser.get_block()
        if(data==''):
            print('Parse Error! Unexpected end of file.')
            return None
        if(data[:7]!='ANSWER:'):
            print('Parse Error! ANSWER: Expected.')
            return None
        else:
            answer=data[7:]
        logging.debug(card_id)
        logging.debug(question)
        logging.debug(answer)
        the_card = Card(card_id,0,question,answer)
        cards[card_id]=the_card

class CardParser:
    
    def __init__(self, cards_file_text):
        self.pos=0
        self.cards_file_text = cards_file_text
    def get_block(self):
        if(self.pos==-1):
            return ''
        text=''
        if(self.pos<=len(self.cards_file_text)):
            
            while(self.cards_file_text[self.pos]!='{'):
                self.pos+=1
                if(self.pos==len(self.cards_file_text)):
                    self.pos=-1
                    return ''
            self.pos+=1
            while(self.cards_file_text[self.pos]!='}'):
                text+=self.cards_file_text[self.pos]
                self.pos+=1
            logging.debug(str(self.pos)+' '+self.cards_file_text[self.pos])
            return text.strip()

class Card:

    def __init__(self, category_id, box, question, answer):
        self.category_id=category_id
        self.box=box
        self.question=question
        self.answer=answer
    
class TestCycle:

    def __init__(self, cycle_num, id_list):
        self.cycle_num=int(cycle_num)
        random.seed()
        random.shuffle(id_list)
        self.id_list=id_list


            

