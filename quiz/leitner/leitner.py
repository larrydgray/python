import os, sys
import logging, random
#logging.disable(logging.DEBUG)



def findtestcyclefile(path):
    
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(path)
    allfiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(path, entry)
        # If entry is a directory then get the list of files in this directory 
        if not os.path.isdir(fullPath):
            allfiles.append(entry)
    for filename in allfiles:
        logging.debug(filename[:len(filename)-4])
        if filename[:9]=='testcycle':
            return filename[:len(filename)-4]
    return None

def loadtestcyclefile(path, testcyclefilename):
    
    cycleFile = open(path+testcyclefilename+".txt",'r')
    cycle=cycleFile.readlines()
    newcycle=[]
    for line in cycle:
        newcycle.append(line.strip())
    return newcycle    

def savetestcyclefile(testcycle, path, testcyclefilename): 
    logging.debug("Save Test Cycle")
    cyclefile = open(path+testcyclefilename+".txt",'w')
    for id in testcycle:
        cyclefile.write(id+'\n')
    cyclefile.close()

def removeidfromtestcycle(id, path, testcyclefilename):
    logging.debug("Remove From Test Cycle")
    testcycle = loadtestcyclefile(path, testcyclefilename)
    testcycle.remove(id)
    savetestcyclefile(testcycle, path, testcyclefilename)

def removeidfrombox(id, path, boxnum):
    logging.debug("Remove From Box")
    box = loadbox(path, boxnum)
    box.remove(id)
    savebox(box, path, boxnum)

def addidtobox(id, path, boxnum):
    logging.debug("Add To Box")
    box = loadbox(path, boxnum)
    box.append(id)
    savebox(box, path, boxnum)

def moveidtobox(id, path, toboxnum, fromboxnum):
    logging.debug("Moving to Box")
    removeidfrombox(id, path, fromboxnum)
    addidtobox(id,path, toboxnum)

def findboxfile(path, boxnum):
    
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(path)
    allfiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(path, entry)
        # If entry is a directory then get the list of files in this directory 
        if not os.path.isdir(fullPath):
            allfiles.append(entry)
    for filename in allfiles:
        logging.debug(filename[:len(filename)-4])
        if filename[:4]==('box'+str(boxnum)):
            return filename[:len(filename)-4]
    return None

def newcycle(path, cards):
    logging.debug('No Test Cycle File Found. Creating new Cycle 1.')
    cyclefile = open(path+'testcycle1.txt','w')
    ids=cards.keys()
    for id in ids:
        cyclefile.write(id+'\n')
    
    cyclefile.close()
    for id in ids:
        cards[id].box=1

    testcycle = TestCycle(1,ids)
    
    boxfile = open(path+'box1.txt','w')
    for id in ids:
        boxfile.write(id+'\n')
    boxfile.close()
    boxfile = open(path+'box2.txt','w')
    boxfile.write('empty')
    boxfile.close()
    boxfile = open(path+'box3.txt','w')
    boxfile.write('empty')
    boxfile.close()
    boxfile = open(path+'box4.txt','w')
    boxfile.write('empty')
    boxfile.close()
    boxfile = open(path+'box5.txt','w')
    boxfile.write('empty')
    boxfile.close()
    boxfile = open(path+'box6.txt','w')
    boxfile.write('empty')
    boxfile.close()
    
    return testcycle

def startnextcycle(path, cards, testcyclenum):
    logging.debug('Starting new cycle number '+str(testcyclenum))
    highestbox=1
    if(testcyclenum%2==0):
        highestbox+=1
    if(testcyclenum%4==0):
        highestbox+=1
    if(testcyclenum%8==0):
        highestbox+=1
    if(testcyclenum%16==0):
        highestbox+=1
    logging.debug('highestbox '+str(highestbox))
    cycle_ids=[]

    keys=cards.keys()
    for key in keys:
        card=cards[key]
        if(card.box>0 and card.box<=highestbox):
            cycle_ids.append(key)
    os.rename(path+'testcycle'+str(testcyclenum)+'.txt', 
        path+'testcycle'+str(testcyclenum+1)+'.txt')
    testcyclefile = open(path+'testcycle'+str(testcyclenum+1)+'.txt','w')
    for id in cycle_ids:
        testcyclefile.write(id+'\n')
    
    testcycle = TestCycle(testcyclenum+1,cycle_ids)

    return testcycle
    
def loadtestcycle(path,cards):
    
    testcyclefilename=findtestcyclefile(path)
    logging.debug(testcyclefilename)
    logging.debug(path)
    # None means brand new study cycle starting at 1
    if(testcyclefilename==None):
       return newcycle(path, cards)
    else:
        #else not brand new cycle, continuing cycle
        cycle_ids=loadtestcyclefile(path, testcyclefilename)
        testcyclenum=int(testcyclefilename[9:])
        # if empty test cycle file then beginning next cycle
        if(cycle_ids[0]=='empty'):
            return startnextcycle(path, cards, testcyclenum)
        # else load current saved cycle state and begin testing
        else:
            testcycle = TestCycle(testcyclenum,cycle_ids)
            return testcycle

def savebox(box, path, boxnum):
     boxfile = open(path+'box'+str(boxnum)+'.txt','w')
     for id in box:
         boxfile.write(id+'\n')
     boxfile.close()

def loadbox(path, boxnum):
    if boxnum<1 or boxnum>6:
        logging.debug('Box number '+str(boxnum)+' out of range. Should be 1 to 6.')
        sys.exit()
    boxFile = open(path+'box'+str(boxnum)+'.txt','r')
    box=boxFile.readlines()
    newbox=[]
    for line in box:
        newbox.append(line.strip())
    return newbox        

def loadboxes(path, cards):
    boxfile = findboxfile(path, 1)
    if(boxfile==None):
         return cards
    else:
        card_ids=loadbox(path,1)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=1
    boxfile = findboxfile(path, 2)
    if(boxfile==None):
         return cards
    else:
        card_ids=loadbox(path, 2)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=2
    boxfile = findboxfile(path, 3)
    if(boxfile==None):
         return cards
    else:
        card_ids=loadbox(path, 3)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=3
    boxfile = findboxfile(path, 4)
    if(boxfile==None):
         return cards
    else:
        card_ids=loadbox(path, 4)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=4
    boxfile = findboxfile(path, 5)
    if(boxfile==None):
         return cards
    else:
        card_ids=loadbox(path, 5)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=5
    boxfile = findboxfile(path, 6)
    if(boxfile==None):
         return cards
    else:
        card_ids=loadbox(path, 6)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=6
    return cards

def loadcards(path,filename):
    logging.debug(os.getcwd())
    quizFile = open(path+filename+".txt",'r')
    aquiz = quizFile.read()
    cardparser = CardParser(aquiz)
    cards={}
    while True:
        cardid=''
        question=''
        answer=''
        
        # not an elegant way to do this, but it will work
        # need to rewrite this
        data=cardparser.getBlock()
        if(data==''):
            if(cards!=False):
                
                loadboxes(path, cards)
                return cards
            else:
                print('Parse Error! Unexpected end of file. No Data')
                return None
        if(data[:3]!='ID:'):
            print('Parse Error! ID: Expected.')
            return None
        else:
            cardid=data[3:].strip()

        data=cardparser.getBlock()
        if(data==''):
            print('Parse Error! Unexpected end of file.')
            return None
        if(data[:9]!='QUESTION:'):
            print('Parse Error! QUESTION: Expected.')
            return None
        else:
            question=data[9:]

        data=cardparser.getBlock()
        if(data==''):
            print('Parse Error! Unexpected end of file.')
            return None
        if(data[:7]!='ANSWER:'):
            print('Parse Error! ANSWER: Expected.')
            return None
        else:
            answer=data[7:]
        logging.debug(cardid)
        logging.debug(question)
        logging.debug(answer)
        thecard = Card(cardid,0,question,answer)
        cards[cardid]=thecard

class CardParser:
    
    def __init__(self, cardsfiletext):
        self.pos=0
        self.cardsfiletext = cardsfiletext
    def getBlock(self):
        if(self.pos==-1):
            return ''
        text=''
        if(self.pos<=len(self.cardsfiletext)):
            
            while(self.cardsfiletext[self.pos]!='{'):
                self.pos+=1
                if(self.pos==len(self.cardsfiletext)):
                    self.pos=-1
                    return ''
            self.pos+=1
            while(self.cardsfiletext[self.pos]!='}'):
                text+=self.cardsfiletext[self.pos]
                self.pos+=1
            logging.debug(str(self.pos)+' '+self.cardsfiletext[self.pos])
            return text.strip()

class Card:

    def __init__(self, catagory_id, box, question, answer):
        self.catagory_id=catagory_id
        self.box=box
        self.question=question
        self.answer=answer
    
class TestCycle:

    def __init__(self, cyclenum, idlist):
        self.cyclenum=int(cyclenum)
        random.seed()
        random.shuffle(idlist)
        self.idlist=idlist


            

