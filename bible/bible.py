
def load_book(name):
        
    bookFile = open("./kjv/"+name+".txt",'r')
    book=bookFile.read()
    verses={}

    i=0
    while(i<len(book)):
        verse_num=''
        verse_text=''
        #print(c,end='')
        if(book[i]=='{'):
            while(book[i]!='}'):
                verse_num+=book[i]
                i+=1
            verse_num+='}'
            
            i+=1
            while(book[i]!='{'):
                verse_text+=book[i]
                i+=1
                if(i==len(book)):
                    break
            i-=1
            chapter,verse = split_verse(verse_num)
            the_verse=Verse(name,chapter,verse, verse_text)
            verses[the_verse.getId()]=the_verse
        i+=1

    return verses
        
def split_verse(verse_text):
        verse_split=verse_text.split(':')
        chapter=verse_split[0][1:]
        verse=verse_split[1][:1]
        return (chapter, verse)

def build_verse_id(book, verse_input):
        chapter, verse = split_verse(verse_input)
        return book+':'+chapter+':'+verse

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

book_verses=load_book('Matthew')
book_verses.update(load_book('Mark'))
book_verses.update(load_book('Luke'))
book_verses.update(load_book('John'))

selected_verse=''
while(selected_verse!='stop'):
    print('Enter b:c:v or stop')
    selected_verse=input()
    if(selected_verse=='stop'):
        break
    try:
        a_verse = book_verses[selected_verse]
        print()
        print(a_verse.get_verse_text())
        print()
    except KeyError:
        print('Verse Not Found')
    







    