from bible_util import *

# main loop gets keyboard input commands
while True: #input of stop means quit
    print('Enter b:c:v , list:b:c, list:b:0, books:beginswith, log, log:b:c:#, log:b:0:# or stop') # to retrieve a verse enter book_name:chapter_number:verse_number ie.e Luke:1:1
    selected_verse=input() # input is more than selected verse now, also commands for display number verse in chapter or number of chapters in book and list book names.
    if selected_verse=='stop':
        break
    if selected_verse=='log': # toggle logging mode
        if logging==False:
            print('Logging on')
            logging=True
        else:
            print('Logging off')
            logging=False
        continue
    if selected_verse[:4]=='log:':
        print(str(get_percent_log(selected_verse[4:]))+'%')
        continue
    if selected_verse=='save':
        write_log()
    if selected_verse[:5]=='books': # list book names
        chars=selected_verse.split(':')[1] #books:name string to match with starts with
        for book in books:
            if book[0].isdigit(): #if first character in book name is a digit 1 2 or 3
                if book[1:].lower().startswith(chars.lower()): # if book name after digit begin with search string
                    print(book+' ',end ='') # print book name and end line with no char instead of new line
            if book.lower().startswith(chars.lower()): # if book name begins with search name
                print(book+' ',end ='')
        print() # print a new line after list of names
        continue
    if selected_verse[:4]=='list':
        print(get_number_of(selected_verse[5:])) #calls function to handle part after list:  i.e. list:John:5 or list:John:0
        continue
    if len(selected_verse)==0: # Handle enter on blank input for get next verse
        split=current_verse.split(':')
        book=split[0]
        chapter=int(split[1])
        verse=int(split[2])
        last_chapter=get_number_of(book+':0') # get the number for last chapter in this book
        last_verse=get_number_of(book+':'+str(chapter)) # get the number for the last verse in this chapter
        if verse<last_verse:
            selected_verse=book+':'+str(chapter)+':'+str(verse+1) #make verse id for next verse
            print(selected_verse, end='')
        elif verse==last_verse: # if at last verse inn this chapter get first verse in next chapter
            if chapter<last_chapter:
                selected_verse=book+':'+str(chapter+1)+':1' # get verse id for first verse in next chapter
                print(selected_verse, end='')
            elif chapter==last_chapter: # we are at end of book
                print('End of '+book)
        
    try:
        a_verse = book_verses[selected_verse] # i.e. Luke:1:1 as key
        if(logging):
            a_verse.inc_verse_log()
        print(' log:'+str(book_verses[selected_verse].get_verse_log()))
        print(a_verse.get_verse_text())
        print()
        current_verse=selected_verse
    except KeyError: # Dictionary key error
        print('Verse Not Found')
    







    