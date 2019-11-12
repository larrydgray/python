
def load_book(name):
        
    bookFile = open("./kjv/"+name+".txt",'r')
    book=bookFile.read()
    verses={}

    i=0
    while(i<len(book)):
        verse=''
        verse_text=''
        #print(c,end='')
        if(book[i]=='{'):
            while(book[i]!='}'):
                verse+=book[i]
                i+=1
            verse+='}'
            i+=1
            while(book[i]!='{'):
                verse_text+=book[i]
                i+=1
                if(i==len(book)):
                    break
            i-=1
        i+=1
        verses[verse]=verse_text
    return verses


book_verses=load_book('Matthew')
selected_verse=''
while(selected_verse!='stop'):
    print('Enter {c:v} or stop')
    selected_verse=input()
    if(selected_verse=='stop'):
        break
    #print(selected_verse)
    print(book_verses[selected_verse])







    