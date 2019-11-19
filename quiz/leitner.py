import os, sys

def findtestcyclefile():
    dirname='quizs'
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir('./'+dirname)
    allfiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirname, entry)
        # If entry is a directory then get the list of files in this directory 
        if not os.path.isdir(fullPath):
            allfiles.append(entry)
    for filename in allfiles:
        #print(filename[:len(filename)-4])
        if filename[:9]=='testcycle':
            return filename[:len(filename)-4]
    return None
def loadtestcyclefile(testcyclefilename):
    
    cycleFile = open("./quizs/"+testcyclefilename+".txt",'r')
    cycle=cycleFile.readlines()
    newcycle=[]
    for line in cycle:
        newcycle.append(line.strip())
    return newcycle      

def findboxfile(boxnum):
    dirname='quizs'
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir('./'+dirname)
    allfiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirname, entry)
        # If entry is a directory then get the list of files in this directory 
        if not os.path.isdir(fullPath):
            allfiles.append(entry)
    for filename in allfiles:
        #print(filename[:len(filename)-4])
        if filename[:4]==('box'+str(boxnum)):
            return filename[:len(filename)-4]
    return None



def loadtestcycle(cards):
    
    testcyclefilename=findtestcyclefile()
    if(testcyclefilename==None):
        print('No Test Cycle File Found. Creating new Cycle 1.')
        cyclefile = open('./quizs/testcycle1.txt','w')
        ids=cards.keys()

        cyclefile.writelines(ids)
        cyclefile.close()
        for id in ids:
            cards[id].box=1

        testcycle = TestCycle(1,ids)
        
        boxfile = open('./quizs/box1.txt','w')
        boxfile.writelines(ids)
        boxfile.close()
        boxfile = open('./quizs/box2.txt','w')
        boxfile.write('empty')
        boxfile.close()
        boxfile = open('./quizs/box3.txt','w')
        boxfile.write('empty')
        boxfile.close()
        boxfile = open('./quizs/box4.txt','w')
        boxfile.write('empty')
        boxfile.close()
        boxfile = open('./quizs/box5.txt','w')
        boxfile.write('empty')
        boxfile.close()
        boxfile = open('./quizs/box6.txt','w')
        boxfile.write('empty')
        boxfile.close()
        
        return testcycle
    else:
        cycle_ids=loadtestcyclefile(testcyclefilename)
        testcyclenum=int(testcyclefilename[9:])
        if(cycle_ids[0]=='empty'):
            print('Starting new Cycle')
        else:
            testcycle = TestCycle(testcyclenum,cycle_ids)

            return testcycle
    

def loadbox(boxnum):
    if(boxnum<1|boxnum>6):
        print('Box number '+boxnum+' out of range. Should be 1 to 6.')
        sys.exit()
    boxFile = open("./quizs/box"+str(boxnum)+".txt",'r')
    box=boxFile.readlines()
    newbox=[]
    for line in box:
        newbox.append(line.strip())
    return newbox        

def loadboxes(cards):
    boxfile = findboxfile(1)
    if(boxfile==None):
         return cards
    else:
        card_ids=loadbox(1)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=1
    boxfile = findboxfile(2)
    if(boxfile==None):
         return cards
    else:
        card_ids=loadbox(2)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=2
    boxfile = findboxfile(3)
    if(boxfile==None):
         return cards
    else:
        card_ids=loadbox(3)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=3
    boxfile = findboxfile(4)
    if(boxfile==None):
         return cards
    else:
        card_ids=loadbox(4)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=4
    boxfile = findboxfile(5)
    if(boxfile==None):
         return cards
    else:
        card_ids=loadbox(5)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=5
    boxfile = findboxfile(6)
    if(boxfile==None):
         return cards
    else:
        card_ids=loadbox(6)
        if card_ids[0]!='empty':
            for id in card_ids:
                cards[id].box=6
    return cards

def loadcards(filename):
    quizFile = open("./quizs/"+filename+".txt",'r')
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
                loadboxes(cards)
                return cards
            else:
                print('Parse Error! Unexpected end of file. No Data')
                return None
        if(data[:3]!='ID:'):
            print('Parse Error! ID: Expected.')
            return None
        else:
            cardid=data[3:]

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
            answer=data[:9]
        thecardid=cardid[:len(cardid)-2]
        box=cardid[len(cardid)-1:]
        thecard = Card(thecardid,box,question,answer)
        cards[thecardid]=thecard

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
            #print(str(self.pos)+' '+self.cardsfiletext[self.pos])
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
        self.idlist=idlist

            

