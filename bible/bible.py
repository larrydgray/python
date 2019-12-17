
# loads the verses from given book .txt file and returns a Dictionary of verses.
def load_book(name):
        
    bookFile = open("./kjv/"+name+".txt",'r')
    book=bookFile.read()
    verses={}

    i=0
    # process book file char by char
    while(i<len(book)):
        verse_num=''
        verse_text=''
        # print(c,end='')
        if(book[i]=='{'):  # verses are {chap#:verse#} i.e. {5:2} chapter 5 verse 2
            # process {book:verse} key For Dictionary
            while(book[i]!='}'): # while not closing bracket in {#:#}
                verse_num+=book[i]
                i+=1
            verse_num+='}'
            
            i+=1
            # Process verse text
            while(book[i]!='{'): # stop when at next verse id begining with {
                verse_text+=book[i]
                i+=1
                if(i==len(book)): #break if at end of book
                    break
            i-=1 #backs us up to the open bracket {
            chapter,verse = split_verse(verse_num) #extract chapter and verse from key
            the_verse=Verse(name,chapter,verse, verse_text) #name is book name
            verses[the_verse.getId()]=the_verse # store the verse in the Dictionary
        i+=1

    return verses # Dictionary of verses

# return the number portions of chapter and verse from verse key {#:#}       
def split_verse(verse_text):
        verse_split=verse_text.split(':') #split on {#:#} int {# and #}
        chapter=verse_split[0][1:] #return number part after open {
        verse=verse_split[1][:1] #return number part before close }
        return (chapter, verse) 

# Returns number of chapters in book or verses in chapter.
def get_number_of(book_chapter):
    print()



# build the verse ID from book name and verse_input return name:#:#
# this may not be used! consider removing it
def build_verse_id(book, verse_input):
        chapter, verse = split_verse(verse_input)
        return book+':'+chapter+':'+verse
# A class to hold the verse for storage in a Dicitonary.
# holds book name, chapter number, verse number and verse text. Also returns an ID book:#:# used as a key.
class Verse:

    def __init__(self, book, chapter, verse, verse_text):
        self.book = book
        self.chapter = chapter
        self.verse = verse
        self.verse_text = verse_text.strip()

    def getId(self):
        return self.book+':'+self.chapter+':'+self.verse
    def get_book(self):
        return self.book
    def get_chapter(self):
        return self.chapter
    def get_verse(self):
        return self.verse
    def get_verse_text(self):
        return self.verse_text

# loads books
book_verses=load_book('Matthew')
book_verses.update(load_book('Mark'))
book_verses.update(load_book('Luke'))
book_verses.update(load_book('John'))
book_verses.update(load_book('Acts'))
book_verses.update(load_book('Romans'))
book_verses.update(load_book('1Cor')) #Corinthians
book_verses.update(load_book('2Cor'))
book_verses.update(load_book('Gal')) #Galatians
book_verses.update(load_book('Eph')) #Ephesians
book_verses.update(load_book('Philip')) #Philippians
book_verses.update(load_book('Col')) #Colossians
book_verses.update(load_book('1Thes')) #Thessalonians
book_verses.update(load_book('2Thes'))
book_verses.update(load_book('1Tim')) #Timothy
book_verses.update(load_book('2Tim'))
book_verses.update(load_book('Titus'))
book_verses.update(load_book('Philemon'))
book_verses.update(load_book('Hebrews'))
book_verses.update(load_book('James'))
book_verses.update(load_book('1Peter'))
book_verses.update(load_book('2Peter'))
book_verses.update(load_book('1John'))
book_verses.update(load_book('2John'))
book_verses.update(load_book('3John'))
book_verses.update(load_book('Jude'))
book_verses.update(load_book('Rev')) #Revelation

book_verses.update(load_book('Genesis'))
book_verses.update(load_book('Exodus'))
book_verses.update(load_book('Lev')) #Leviticus
book_verses.update(load_book('Num')) #Numbers
book_verses.update(load_book('Deut')) #Deuteronomy
book_verses.update(load_book('Joshua'))    
book_verses.update(load_book('Judges'))
book_verses.update(load_book('Ruth'))
book_verses.update(load_book('1Sam')) #Samuel
book_verses.update(load_book('2Sam'))
book_verses.update(load_book('1Kings'))
book_verses.update(load_book('2Kings'))
book_verses.update(load_book('1Cron')) #Chronicles
book_verses.update(load_book('2Cron'))
book_verses.update(load_book('Ezra'))
book_verses.update(load_book('Nehemiah'))    
book_verses.update(load_book('Esther'))
book_verses.update(load_book('Job'))    
book_verses.update(load_book('Psalms'))    
book_verses.update(load_book('Proverbs'))
book_verses.update(load_book('Eccl'))  #Ecclesiastes
book_verses.update(load_book('Song')) #Song of Solomon
book_verses.update(load_book('Isaiah'))
book_verses.update(load_book('Jeremiah'))
book_verses.update(load_book('Lament'))  #Lamentations
book_verses.update(load_book('Ezekiel'))
book_verses.update(load_book('Daniel'))    
book_verses.update(load_book('Hosea'))   
book_verses.update(load_book('Joel'))   
book_verses.update(load_book('Amos'))   
book_verses.update(load_book('Obadiah'))
book_verses.update(load_book('Jonah'))
book_verses.update(load_book('Micah'))    
book_verses.update(load_book('Nahum'))    
book_verses.update(load_book('Habakkuk'))   
book_verses.update(load_book('Zeph')) #Zephaniah
book_verses.update(load_book('Haggai'))  
book_verses.update(load_book('Zech')) #Zechariah
book_verses.update(load_book('Malachi'))
    



selected_verse=''
# main loop gets keyboard input commands
while(selected_verse!='stop'): #input of stop means quit
    print('Enter b:c:v or stop') # to retrieve a verse enter book_name:chapter_number:verse_number ie.e Luke:1:1
    selected_verse=input()
    if selected_verse=='stop':
        break
    if selected_verse[:4]=='list':
        print(get_number_of(selected_verse[5:]))
    try:
        a_verse = book_verses[selected_verse] # i.e. Luke:1:1 as key
        print()
        print(a_verse.get_verse_text())
        print()
    except KeyError: # Dictionary key error
        print('Verse Not Found')
    







    