
books = []
bookchv = {}
# loads the verses from given book .txt file and returns a Dictionary of verses.
def load_book(name):
    global books
    print('.', end='')
    books.append(name)
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
                if ord(book[i])!=0xa and ord(book[i])!=0xd:
                    verse_text+=book[i]
                i+=1
                if(i==len(book)): #break if at end of book
                    break
            i-=1 #backs us up to the open bracket {
            chapter,verse = split_verse(verse_num) #extract chapter and verse from key

            # print(name+':'+chapter+':'+verse)
            the_verse=Verse(name,chapter,verse, verse_text) #name is book name
            verses[the_verse.getId()]=the_verse # store the verse in the Dictionary
        i+=1

    return verses # Dictionary of verses

# return the number portions of chapter and verse from verse key {#:#}
def split_verse(verse_text):
    verse_split=verse_text.split(':') #split on {#:#} int {# and #}
    chapter=verse_split[0][1:] #return number part after open {
    verse=verse_split[1][:len(verse_split[1])-1] #return number part before close }
    return (chapter, verse)

# Returns number of chapters in book or verses in chapter.
def get_number_of(book_chapter):
    split = book_chapter.split(':')
    book = split[0]
    chapter = int(split[1])
    verse_ids=book_verses.keys()

    # if chapter = 0 then we are looking for number of chapters in a book.
    if chapter==0:
        chapter_count=0
        for verse_id in verse_ids:
            split = verse_id.split(':')
            verse_book=split[0]
            verse_chapter=int(split[1])
            if verse_book==book:
                if verse_chapter>chapter_count:
                    chapter_count=verse_chapter
        return chapter_count
    # if chapter > 0 then we are looking for number of verses in chapter.
    elif chapter>0:
        verse_count=0
        for verse_id in verse_ids:
            split = verse_id.split(':')
            verse_book=split[0]
            verse_chapter=int(split[1])
            verses_verse_num=int(split[2])
            if verse_book==book:
                if verse_chapter==chapter:
                    if verses_verse_num>verse_count:
                        verse_count=verses_verse_num
        return verse_count

# gets the percentage of verses read/viewed as int 0% to 100%
# so if number is 1 then returns pecentage read at least once, 2 then at least twice etc.
# this is brute force, needs recoding
def get_percent_chapter_log(verse_ids,book,chapter,number):
    log_count=0
    verse_count=0
    for verse_id in verse_ids:
        split = verse_id.split(':')
        verse_book=split[0]
        verse_chapter=int(split[1])
        verses_verse_num=int(split[2])
        if verse_book==book:
            if verse_chapter==chapter:
                if verses_verse_num>verse_count:
                    verse_log=book_verses[verse_id].get_verse_log()
                    if(verse_log>=number):
                        log_count+=1
                    verse_count=verses_verse_num
    return int((log_count/verse_count)*100) # return int percent of verses read/viewed

# Returns number of chapters in book or verses in chapter.
# this is brute force, needs recoding
def get_percent_log(book_chapter_number):
    book, chapter, number = book_chapter_number.split(':')
    chapter=int(chapter)
    number=int(number)
    verse_ids=book_verses.keys()
    chapter_percent_total=0
    # if chapter = 0 then we are looking for number of chapters in a book.
    if chapter==0:
        chapter_count=0
        for verse_id in verse_ids:
            split = verse_id.split(':')
            verse_book=split[0]
            verse_chapter=int(split[1])
            if verse_book==book:
                if verse_chapter>chapter_count:
                    chapter_percent_total+=get_percent_chapter_log(verse_ids, book, chapter, number)
                    chapter_count=verse_chapter
        return int(chapter_percent_total/chapter_count)
    # if chapter > 0 then we are looking for number of verses in chapter.
    elif chapter>0:
        return get_percent_chapter_log(verse_ids,book,chapter,number)

# build the verse ID from book name and verse_input return name:#:#
# this may not be used! consider removing it
def build_verse_id(book, verse_input):
    chapter, verse = split_verse(verse_input)
    return book+':'+chapter+':'+verse
# A class to hold the verse for storage in a Dicitonary.
# holds book name, chapter number, verse number and verse text. Also returns an ID book:#:# used as a key.

def write_log():
    log_file = open('log.txt','w')
    verse_ids=book_verses.keys()
    verse=None
    for verse_id in verse_ids:
        verse=book_verses[verse_id]
        log=verse.get_verse_log()
        if log>0:
            log_file.write(verse_id+'='+str(log)+'\n')

def read_log():
    print()
    try:
        log_file = open('log.txt', 'r')
        log = log_file.readlines()
    except FileNotFoundError:
        return
    else:
        for verse_log in log:
            verse_id, log_num= verse_log.split('=')
            verse = book_verses[verse_id]
            verse.set_verse_log(int(log_num))



class Verse:

    def __init__(self, book, chapter, verse, verse_text):
        self.book = book
        self.chapter = chapter
        self.verse = verse
        self.verse_text = verse_text.strip()
        self.verse_log = 0
        self.verse_note = ''

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
    def get_verse_log(self):
        return self.verse_log
    def set_verse_log(self,verse_log):
        self.verse_log=verse_log
    def get_verse_note(self):
        return self.verse_note
    def add_verse_note(self, note):
        self.verse_note+=note
    def inc_verse_log(self):
        self.verse_log+=1

# loads books
print('Loading Books of Bible...')
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
book_verses.update(load_book('1Chron')) #Chronicles
book_verses.update(load_book('2Chron'))
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

print("\nStarting")
read_log()

selected_verse=''
current_verse=''
logging=False

