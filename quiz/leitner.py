import os

def listfiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir('./'+dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if not os.path.isdir(fullPath):
            allFiles.append(entry)
                
    return allFiles

def loadtestcycle():
    print()
    #look for file named testcycle#.txt in quizs folder

def loadbox(boxnum):
    print()
    #load Box of ID numbers for given box number 1 to 5

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
        self.cyclenum=cyclenum
        self.idlist=idlist

            

