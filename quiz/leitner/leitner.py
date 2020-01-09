import os, sys
import logging, random
#logging.disable(logging.DEBUG)

# Test Info class holds inforation about the current test so that
# Not so many parameters have to passed around.
class TestInfo:
    def __init__(self, path, file_names):
        self.path=path
        # Tuple of card file names
        self.test_cycle_file_names=file_names
        # Dictionary of Cards
        self.cards=None
# Makes sure its not simply None
test_info = TestInfo('bla','bla.txt')

# Sets the file name for the current test cycle which in 'testcycle5.txt' is 'testcycle5'
def set_test_cycle_file_names(file_names):
    test_info.test_cycle_file_names = file_names

# Sets the path to the testcycle#.txt, box#.txt and cards.txt files for this test
# Which is for the example 'quizs//'
def set_path(the_path):
    test_info.path = the_path

# Returns test cylce file name if it exist or
# Returns None if doesn't exist, meaning starting a fresh cycle #1 from square 1
def _find_test_cycle_file():
    
    # create a list of file and sub directories 
    # names in the given directory 
    list_of_files = os.listdir()
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_files:
        # Create full path
        full_path = os.path.join( entry)
        # If entry is a directory then get the list of files in this directory 
        if not os.path.isdir(full_path):
            all_files.append(entry)
    # Look for a file that begins with 'testcycle'
    for file_name in all_files:
        logging.debug(file_name[:len(file_name)-4])
        if file_name[:9]=='testcycle':
            return file_name[:len(file_name)-4] # 'testcycle#.txt'  would be 'testcycle#'
    return None

# Loads the test cycle file  'testcycle#.txt'
# Returns a List of Card IDs
def _load_test_cycle_file():
    
    cycle_file = open(test_info.path+test_info.test_cycle_file_name+".txt",'r')
    cycle=cycle_file.readlines()
    new_cycle=[]
    # Append line with \n removed
    for line in cycle:
        new_cycle.append(line.strip())
    return new_cycle    

# Used to save the test cycle file after each question
def save_test_cycle_file(test_cycle): 
    logging.debug("Save Test Cycle")
    cycle_file = open(test_info.path+test_info.test_cycle_file_name+".txt",'w')
    # Put newline on end of id's and write to file
    for id in test_cycle:
        cycle_file.write(id+'\n')
    cycle_file.close()

# Used to remove the Card ID from the last question tested from the cycle file.
def remove_id_from_test_cycle(id):
    logging.debug("Remove From Test Cycle")
    test_cycle = _load_test_cycle_file()
    test_cycle.remove(id)
    save_test_cycle_file(test_cycle)

# Used to remove an ID from current Cards box when moving an ID
def _remove_id_from_box(id, box_num):
    logging.debug("Remove From Box")
    box = _load_box(box_num)
    box.remove(id)
    # If we emptied the box set it to empty
    if len(box) == 0:
        box.append('empty')
    _save_box(box, box_num)


def _add_id_to_box(id, box_num):
    logging.debug("Add To Box")
    box = _load_box(box_num)
    # removes the tag empty from the file
    if box[0]=='empty':
        box.remove('empty')
    box.append(id)
    _save_box(box, box_num)

def move_id_to_box(id, to_box_num, from_box_num):
    logging.debug("Moving to Box")
    _remove_id_from_box(id, from_box_num)
    _add_id_to_box(id, to_box_num)

def _find_box_file(box_num):
    
    # create a list of file and sub directories 
    # names in the given directory 
    list_of_files = os.listdir(test_info.path)
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_files:
        # Create full path
        full_path = os.path.join(entry)
        # If entry is a directory then get the list of files in this directory 
        if not os.path.isdir(full_path):
            all_files.append(entry)
    for file_name in all_files:
        logging.debug(file_name[:len(file_name)-4])
        if file_name[:4]==('box'+str(box_num)):
            return file_name[:len(file_name)-4]
    return None

def _new_cycle():
    logging.debug('No Test Cycle File Found. Creating new Cycle 1.')
    cycle_file = open(test_info.path+'testcycle1.txt','w')
    ids_keys=test_info.cards.keys()
    # apparently keys() does not return a List but a keys object or something like this.
    # So we convert it to a List which is what I needed. There may be a better way.
    ids = [] 
    for key in ids_keys: 
        ids.append(key) 
    logging.debug('Number of cards '+str(len(ids)))
    logging.debug(ids)
    # write out all card id's with new line to file for first time cycle
    for id in ids:
        cycle_file.write(id+'\n')
    logging.debug('Done making ids')
    cycle_file.close()
    # Now create box files
    logging.debug('Loading cards into Box1')
    # Load all cards into box 1 by setting their box to 1
    for id in ids:
        test_info.cards[id].box=1
    logging.debug('Set Cards to Box1')
    # Make new TestCycle to be returned.
    test_cycle = TestCycle(1,ids)
    logging.debug('Made TestCycle')
    # There is room for improvement here, mayb make a
    # _make_box_file() method.
    # Make box1.txt and write out card id's
    box_file = open(test_info.path+'box1.txt','w')
    logging.debug('Making box1')
    for id in ids:
        box_file.write(id+'\n') # add new line
    box_file.close()
    # Make box2.txt and write empty
    logging.debug('Making box2')
    box_file = open(test_info.path+'box2.txt','w')
    box_file.write('empty')
    box_file.close()
    # Make box3.txt and write empty
    logging.debug('Making box3')
    box_file = open(test_info.path+'box3.txt','w')
    box_file.write('empty')
    box_file.close()
    # Make box4.txt and write empty
    logging.debug('Making box4')
    box_file = open(test_info.path+'box4.txt','w')
    box_file.write('empty')
    box_file.close()
    # Make box5.txt and write empty
    logging.debug('Making box5')
    box_file = open(test_info.path+'box5.txt','w')
    box_file.write('empty')
    box_file.close()
    # Make box6.txt and write empty
    # Box6 will be for cards that are no longer
    # being tested
    logging.debug('Making box6')
    box_file = open(test_info.path+'box6.txt','w')
    box_file.write('empty')
    box_file.close()
    # return the fresh new start test cycle 1
    return test_cycle

# Starts the next test cycle if the testcycle#.txt file only contains
# an 'empty' tag
def _start_next_cycle(test_cycle_num):
    logging.debug('Starting new cycle number '+str(test_cycle_num))
    # find highest box in cycle to be used
    # box 1 every cycle, box 2 every other cycle, box 3 every 4th cycle
    # box 4 eveery 8th cycle and box 5 every 16th cycle
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
    keys=test_info.cards.keys()
    logging.debug('Loading box1 to box'+str(highest_box))
    # keys work like List here
    for key in keys:
        card=test_info.cards[key]
        # card in box 1 to highest for cycle
        if(card.box>0 and card.box<=highest_box):
            cycle_ids.append(key)
    # rename testcycle file with new cycle number
    os.rename(test_info.path+'testcycle'+str(test_cycle_num)+'.txt', 
        test_info.path+'testcycle'+str(test_cycle_num+1)+'.txt')
    # write id's from all boxes for this cycle in the cycle file
    test_cycle_file = open(test_info.path+'testcycle'+str(test_cycle_num+1)+'.txt','w')
    for id in cycle_ids:
        test_cycle_file.write(id+'\n')
    # make and return new Test Cycle object for beginning current cycle
    testcycle = TestCycle(test_cycle_num+1,cycle_ids)
    return testcycle

# loads and returns a test cycle under 3 conditions
# 1. there is no testcycle#.txt file found therefor beginning a fresh start cycle 1
# 2. a cycle file is found but has 'empty' tag in it therefor begin next cycle
# 3. a cycle file with ID's in it means continue the current cycle testing
def load_test_cycle():
    #look for test cycle file
    file_name=_find_test_cycle_file()
    logging.debug(file_name)
    logging.debug(test_info.path)
    # None means brand new study cycle starting at 1
    if(file_name==None):
       return _new_cycle()
    else:
        # else not brand new cycle, continuing cycle
        cycle_ids=_load_test_cycle_file()
        test_cycle_num=int(file_name[9:])
        # if empty test cycle file then beginning next cycle
        if(cycle_ids[0]=='empty'):
            return _start_next_cycle(test_cycle_num)
        # else load current saved cycle state and begin testing
        else:
            test_cycle = TestCycle(test_cycle_num, cycle_ids)
            return test_cycle

# saves a List of card IDs for given box number
def _save_box(box, box_num):
     box_file = open(test_info.path+'box'+str(box_num)+'.txt','w')
     for id in box:
         box_file.write(id+'\n')
     box_file.close()

# loads a list of card IDs for given box number
# List will contain only the tag 'empty' if box is empty
# can load box 6 even though it is not used currently
def _load_box(box_num):
    # exit with error message if box number out of range
    if box_num<1 or box_num>6:
        logging.debug('Box number '+str(box_num)+' out of range. Should be 1 to 6.')
        sys.exit()
    
    box_file = open(test_info.path+'box'+str(box_num)+'.txt','r')
    box=box_file.readlines()
    new_box=[]
    # have to strip \n
    for line in box:
        new_box.append(line.strip()) # strip new lines
    return new_box        

# loads all boxes 1 to 6 
# sets box number on each card according to the box it is in based on card IDs
# returns the whole set of cards
# This might be rewritten a bit. May not have to return cards at all.
# Also could a helper _pull_cards(box_file, box_num) needs to be made
def _load_boxes():

    # if the boxfile isn't found then return the cards
    # it should be found unless someone deleted them
    # load box and if first element is not tagged with 'empty' then
    #  set the card with that ID to the box it was found in
    # therefore all cards will have box number of 0 or 1 to 6

    # handle box 1
    box_file = _find_box_file(1)
    if(box_file==None):
         return test_info.cards
    else:
        card_ids=_load_box(1)
        if card_ids[0]!='empty':
            for id in card_ids:
                test_info.cards[id].box=1
    # handle box 2            
    box_file = _find_box_file(2)
    if(box_file==None):
         return test_info.cards
    else:
        card_ids=_load_box(2)
        if card_ids[0]!='empty':
            for id in card_ids:
                test_info.cards[id].box=2
    # handle box 3
    box_file = _find_box_file(3)
    if(box_file==None):
         return test_info.cards
    else:
        card_ids=_load_box(3)
        if card_ids[0]!='empty':
            for id in card_ids:
                test_info.cards[id].box=3
    # handle box 4
    box_file = _find_box_file(4)
    if(box_file==None):
         return test_info.cards
    else:
        card_ids=_load_box(4)
        if card_ids[0]!='empty':
            for id in card_ids:
                test_info.cards[id].box=4
    # handle box 5
    box_file = _find_box_file(5)
    if(box_file==None):
         return test_info.cards
    else:
        card_ids=_load_box(5)
        if card_ids[0]!='empty':
            for id in card_ids:
                test_info.cards[id].box=5
    
    # handle box 6 
    box_file = _find_box_file(6)
    if(box_file==None):
         return test_info.cards
    else:
        card_ids=_load_box(6)
        if card_ids[0]!='empty':
            for id in card_ids:
                test_info.cards[id].box=6
    return test_info.cards

# loads and returns a dicitonary of Cards where the key is Card ID
# Card ID is 'category-category-#'  and any number of nested categories
# category and question number must be unique
# though I have no check for this coded yet
def load_cards():
    logging.debug(os.getcwd())
    aquiz=''
    for card_file in test_info.test_cycle_file_names:
        quiz_file = open(test_info.path+card_file+".txt",'r')
        aquiz += quiz_file.read()
    card_parser = CardParser(aquiz)
    cards={}
    while True:
        card_id=''
        question=''
        answer=''
        
        # not an elegant way to do this, but it will work
        # need to rewrite this
        data=card_parser.get_block()
        # if data is an empty string we may be at end of file
        if(data==''):
            # if cards is not an empty Dictionary
            # we are at end of cards file
            if(cards!=False):
                
                _load_boxes() # will set box numbers on each card if its in a box
                test_info.cards=cards
                return cards
            else: # if empty data and no cards we have a problem
                print('Parse Error! Unexpected end of file. No Data')
                return None
        #Cards are in 3 blocks
        #{ID:category-1} {QUESTION: A question?} {ANSWER: An answer.}
        
        # handle ID: block
        if(data[:3]!='ID:'): # if prefix is not ID:
            print('Parse Error! ID: Expected.')
            return None
        else: 
            card_id=data[3:].strip() # card id is the ID which follows the prefix

        # get next block and make sure its a {} block or not eof
        data=card_parser.get_block()
        if(data==''):
            print('Parse Error! Unexpected end of file.')
            return None
        
        # handle QUESTION: block
        if(data[:9]!='QUESTION:'): # if prefix is not QUESTION:
            print('Parse Error! QUESTION: Expected.')
            return None
        else:  
            question=data[9:] # question is the question that follows prefix
        
        # get next block and make sure its a {} block or not eof
        data=card_parser.get_block()
        if(data==''):
            print('Parse Error! Unexpected end of file.')
            return None
            
        # handle ANSWER: block
        if(data[:7]!='ANSWER:'): # if answer is not ANSWER: 
            print('Parse Error! ANSWER: Expected.')
            return None
        else:
            answer=data[7:] # answer is the answer that follows prefix
        logging.debug(card_id)
        logging.debug(question)
        logging.debug(answer)
        # Make the card
        the_card = Card(card_id,0,question,answer)
        # Put card in dictionary
        cards[card_id]=the_card

# Parses card file based on { and } And 
class CardParser:
    
    
    def __init__(self, cards_file_text):
        self.pos=0
        self.cards_file_text = cards_file_text
    
    # gets a block from the cards file that is wrapped with {  and  }
    # each card has 3 {}{}{}
    # this class does not yet validate the cards file for proper format
    def get_block(self):
        # are we at end of file text? I'm  not sure it this will ever be needed
        if(self.pos==-1): 
            return ''
        text=''
        if(self.pos<=len(self.cards_file_text)): #if position is within the card file text or not end of text
            
            while(self.cards_file_text[self.pos]!='{'): # loop while not a  new data block 
                self.pos+=1 # scanning the text skipping white space or anything between } and {
                if(self.pos==len(self.cards_file_text)): # at end of file text
                    self.pos=-1
                    return ''
            self.pos+=1 # scanning the text to the char after {
            while(self.cards_file_text[self.pos]!='}'): # while not at end of data block }
                text+=self.cards_file_text[self.pos] # building the data
                self.pos+=1 # scanning the text
            logging.debug(str(self.pos)+' '+self.cards_file_text[self.pos])
            return text.strip() # strip text of white space and return it

# Card that contains fields for ID, Box Num, Quesiton and Answer
# ID = Category-Category-#    Where there are any number of nested unique categories 
class Card:

    def __init__(self, category_id, box, question, answer):
        self.category_id=category_id
        self.box=box
        self.question=question
        self.answer=answer

# Represents the current test cycle for a single set of cards. 
class TestCycle:
    # sets cylce number ID list and shuffles the ID List or Cards
    # so that question are given in random order
    def __init__(self, cycle_num, id_list):
        self.cycle_num=int(cycle_num)
        random.seed() # always call seed() to get new random numbers each time app is run
        random.shuffle(id_list) # shuffle the cards
        self.id_list=id_list
        



            

