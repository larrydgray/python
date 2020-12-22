
import tkinter as tk
from tkinter import *
from bible_util import *
from PIL import ImageTk, Image


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def search():
    print("search:")
    book=ent_book.get()
    chapter=ent_chapter.get()
    verse=ent_verse.get()
    error=False
    searchkey=""
    error_message=""

    if book in books:
        searchkey+=book
    else:
        error=True
        error_message+="Book name\""+book+"\" not found!\n"
    if is_number(chapter):
        searchkey+=":"+chapter
    else:
        error=True
        error_message+="Chapter must be a number!\n"

    if is_number(verse):
        searchkey+=":"+verse
    else:
        error=True
        error_message+="Verse must be a number!\n"
    if error:
        txt_output.delete("1.0","end")
        txt_output.insert(tk.END, error_message)
    else:
        try:
            a_verse = book_verses[searchkey] # i.e. Luke:1:1 as key
            text=a_verse.get_verse_text()
            txt_output.delete("1.0","end")
            txt_output.insert(tk.END, text)
            prevverse=a_verse
            display_log_count(a_verse.get_verse_log())
            write_log()
            return a_verse
        except KeyError: # Dictionary key error
            txt_output.delete("1.0","end")
            txt_output.insert(tk.END, "Verse not found! "+searchkey)


def count():
    print("list")
    error=False
    book=ent_book.get()
    chapter=ent_chapter.get()
    if book in books:
        pass
    else:
        error=True
        error_message+="Book name\""+book+"\" not found!\n"
    if is_number(chapter):
        pass
    else:
        error=True
        error_message+="Chapter must be a number!\n"
    if error:
        txt_output.delete("1.0","end")
        txt_output.insert(tk.END, error_message)
    else:
        if chapter=='':
            last_chapter=get_number_of(book+':0') # get the number for last chapter in this book
            txt_output.delete("1.0","end")
            txt_output.insert(tk.END, "Number of chapters in the book "+book+" are "+last_chapter)
        else:
            last_chapter=get_number_of(book+':0') # get the number for last chapter in this book
            if int(chapter)<=last_chapter and int(chapter)>0:
                last_verse=get_number_of(book+':'+str(chapter)) # get the number for the last verse in this chapter
                txt_output.delete("1.0","end")
                txt_output.insert(tk.END, "Number of verses in the book "+book+" chapter "+chapter+" are "+str(last_verse))
            else:
                txt_output.delete("1.0","end")
                txt_output.insert(tk.END, "Chapter number not valid!")

def list_books():
    print("books")
    txt_output.delete("1.0","end")
    chars=ent_book.get()
    for book in books:
        if book[0].isdigit(): #if first character in book name is a digit 1 2 or 3
            if book[1:].lower().startswith(chars.lower()): # if book name after digit begin with search string
                txt_output.insert(tk.END, book+"\n")
        if book.lower().startswith(chars.lower()): # if book name begins with search name
            txt_output.insert(tk.END, book+"\n")

def log():
    if lbl_log_state["text"]=="Off":
        lbl_log_state["text"]="On"
    else:
        lbl_log_state["text"]="Off"
    print("log")
def prev():
    book=ent_book.get()
    chapter=ent_chapter.get()
    verse=ent_verse.get()
    error=False
    searchkey=""
    error_message=""

    if book in books:
        searchkey+=book
    else:
        error=True
        error_message+="Book name\""+book+"\" not found!\n"
    if is_number(chapter):
        searchkey+=":"+chapter
    else:
        error=True
        error_message+="Chapter must be a number!\n"

    if is_number(verse):
        searchkey+=":"+verse
    else:
        error=True
        error_message+="Verse must be a number!\n"
    if error:
        txt_output.delete("1.0","end")
        txt_output.insert(tk.END, error_message)
    else:
        try:
            a_verse = book_verses[searchkey] # i.e. Luke:1:1 as key
            last_chapter=get_number_of(book+':0') # get the number for last chapter in this book
            last_verse=get_number_of(book+':'+str(chapter)) # get the number for the last verse in this chapter
            book=searchkey.split(':')[0]
            chapter=searchkey.split(':')[1]
            verse=searchkey.split(':')[2]
            prevbook=book
            if int(verse)==1:
                if int(chapter)==1:
                    if book=="Matthew":
                        prevbook="Malachi"
                    else:
                        prevbook=books[books.index(book)-1]
                    chapter=str(get_number_of(prevbook+':0')) # get the number for last chapter in this book
                    verse=str(get_number_of(prevbook+':'+str(chapter))) # get the number for the last verse in this chapter
                else:
                    chapter=str(int(chapter)-1)
                    verse='1'
            else:
                verse=str(int(verse)-1)
            ent_book.delete(0,END)
            ent_book.insert(END,prevbook)
            ent_chapter.delete(0,END)
            ent_chapter.insert(END, chapter)
            ent_verse.delete(0,END)
            ent_verse.insert(END, verse)

            searchkey=prevbook+":"+chapter+":"+verse
            a_verse = book_verses[searchkey] # i.e. Luke:1:1 as key

            text=a_verse.get_verse_text()
            txt_output.delete("1.0","end")
            txt_output.insert(tk.END, text)
            prevverse=a_verse
            display_log_count(a_verse.get_verse_log())
            write_log()
        except KeyError: # Dictionary key error
            txt_output.delete("1.0","end")
            txt_output.insert(tk.END, "Verse not found! "+searchkey)

def next():

    print("search:")
    book=ent_book.get()
    chapter=ent_chapter.get()
    verse=ent_verse.get()
    error=False
    searchkey=""
    error_message=""

    if book in books:
        searchkey+=book
    else:
        error=True
        error_message+="Book name\""+book+"\" not found!\n"
    if is_number(chapter):
        searchkey+=":"+chapter
    else:
        error=True
        error_message+="Chapter must be a number!\n"

    if is_number(verse):
        searchkey+=":"+verse
    else:
        error=True
        error_message+="Verse must be a number!\n"
    if error:
        txt_output.delete("1.0","end")
        txt_output.insert(tk.END, error_message)
    else:
        try:
            a_verse = book_verses[searchkey] # i.e. Luke:1:1 as key
            last_chapter=get_number_of(book+':0') # get the number for last chapter in this book
            last_verse=get_number_of(book+':'+str(chapter)) # get the number for the last verse in this chapter
            book=searchkey.split(':')[0]
            chapter=searchkey.split(':')[1]
            verse=searchkey.split(':')[2]
            nextbook=book
            if int(verse)==last_verse:
                if int(chapter)==last_chapter:
                    if book=="Malachi":
                        nextbook="Matthew"
                    else:
                        nextbook=books[books.index(book)+1]
                else:
                    chapter=str(int(chapter)+1)
                    verse='1'
            else:
                verse=str(int(verse)+1)
            ent_book.delete(0,END)
            ent_book.insert(END,nextbook)
            ent_chapter.delete(0,END)
            ent_chapter.insert(END, chapter)
            ent_verse.delete(0,END)
            ent_verse.insert(END, verse)

            searchkey=nextbook+":"+chapter+":"+verse
            a_verse = book_verses[searchkey] # i.e. Luke:1:1 as key

            text=a_verse.get_verse_text()
            txt_output.delete("1.0","end")
            txt_output.insert(tk.END, text)
            prevverse=a_verse
            display_log_count(a_verse.get_verse_log())
            write_log()
        except KeyError: # Dictionary key error
            txt_output.delete("1.0","end")
            txt_output.insert(tk.END, "Verse not found! "+searchkey)


def plus():
    verse=search()
    if verse is None:
        pass
    else:
        log_count=verse.get_verse_log()
        log_count+=1
        verse.set_verse_log(log_count)
        display_log_count(log_count)
        write_log()

def minus():
    verse=search()
    if verse is None:
        pass
    else:
        log_count=verse.get_verse_log()
        if log_count>0:
            log_count-=1
        verse.set_verse_log(log_count)
        display_log_count(log_count)
        write_log()


def display_log_count(log_count):
    hashes = int(log_count/5)
    endhash = log_count%5
    if hashes == 0:
        hash1=endhash
        hash2=0
        hash3=0
        hash4=0
    if hashes == 1:
        hash1=5
        hash2=endhash
        hash3=0
        hash4=0
    if hashes == 2:
        hash1=5
        hash2=5
        hash3=endhash
        hash4=0
    if hashes ==3:
        hash1=5
        hash2=5
        hash3=5
        hash4=endhash
    if hashes >=4:
        hash1=5
        hash2=5
        hash3=5
        hash4=5

    lbl_hash1.configure(image=hash_images[hash1])
    lbl_hash1.image = hash_images[hash1]
    lbl_hash2.configure(image=hash_images[hash2])
    lbl_hash2.image = hash_images[hash2]
    lbl_hash3.configure(image=hash_images[hash3])
    lbl_hash3.image = hash_images[hash3]
    lbl_hash4.configure(image=hash_images[hash4])
    lbl_hash4.image = hash_images[hash4]





window = tk.Tk()
window.title("KJV Bible")
photo = PhotoImage(file = "./images/bible.png")
window.iconphoto(False, photo)
window.columnconfigure(0, minsize=50)
window.rowconfigure(11, minsize=50)

mark0image = Image.open("images/mark0.png")
img_mark0 = ImageTk.PhotoImage(mark0image)
mark1image = Image.open("images/mark1.png")
img_mark1 = ImageTk.PhotoImage(mark1image)

mark2image = Image.open("images/mark2.png")
img_mark2 = ImageTk.PhotoImage(mark2image)

mark3image = Image.open("images/mark3.png")
img_mark3 = ImageTk.PhotoImage(mark3image)

mark4image = Image.open("images/mark4.png")
img_mark4 = ImageTk.PhotoImage(mark4image)

mark5image = Image.open("images/mark5.png") #image1 = img.resize((50, 50), Image.ANTIALIAS)
img_mark5 = ImageTk.PhotoImage(mark5image)
hash_images=[img_mark0, img_mark1, img_mark2, img_mark3, img_mark4, img_mark5]
frm_search = Frame(window)
btn_prev = tk.Button(frm_search, text="Prev", command=prev)
btn_prev.grid(row=0,column=0,padx=1)
btn_search = tk.Button(frm_search, text="Search", command=search)
btn_search.grid(row=0, column=1, padx=1)
btn_next = tk.Button(frm_search, text="Next", command=next)
btn_next.grid(row=0, column=2, padx=1)

lbl_book = tk.Label(master=frm_search, text="Book")
lbl_book.grid(row=0, column=3, padx=1)
ent_book = tk.Entry(master=frm_search, width=15)
ent_book.insert(END, 'Genesis')
ent_book.grid(row=0, column=4, padx=1)

lbl_chapter = tk.Label(master=frm_search, text="Chapter")
lbl_chapter.grid(row=0, column=5, padx=1)
ent_chapter = tk.Entry(master=frm_search, width=3)
ent_chapter.insert(END, '1')
ent_chapter.grid(row=0, column=6, padx=1)

lbl_verse = tk.Label(master=frm_search, text="Verse")
lbl_verse.grid(row=0, column=7, padx=1)
ent_verse = tk.Entry(master=frm_search, text="1", width=3)
ent_verse.insert(END, '1')
ent_verse.grid(row=0, column=8, padx=1)

frm_search.pack()

frm_log=Frame(window);
btn_plus = tk.Button(frm_log, text="+", command=plus)
btn_plus.grid(row=0,column=0,padx=1)
btn_minus = tk.Button(frm_log, text="-", command=minus)
btn_minus.grid(row=0, column=1, padx=1)
lbl_hash1 = tk.Label(frm_log, image=img_mark2)
lbl_hash1.grid(row=0,column=2,padx=1)
lbl_hash2 = tk.Label(frm_log, image=img_mark2)
lbl_hash2.grid(row=0,column=3)
lbl_hash3 = tk.Label(frm_log, image=img_mark2)
lbl_hash3.grid(row=0,column=4)
lbl_hash4 = tk.Label(frm_log, image=img_mark2)
lbl_hash4.grid(row=0,column=5)
display_log_count(8)
frm_log.pack();

txt_output = tk.Text(window)
txt_output.configure(height=5, width=50)
txt_output.pack()

frm_command = Frame(window)
btn_count = tk.Button(frm_command, text="Count", command=count)
btn_count.grid(row = 0, column = 0 , padx = 1)
btn_books = tk.Button(frm_command, text="Books", command=list_books)
btn_books.grid(row = 0, column = 1, padx = 1)
btn_log = tk.Button(frm_command, text="Log", command=log)
btn_log.grid(row = 0, column = 3)
lbl_log = tk.Label(master=frm_command, text="Logging")
lbl_log.grid(row=0, column=4, padx=1)
lbl_log_state = tk.Label(master=frm_command, fg="blue", text="Off")
lbl_log_state.grid(row=0, column=5, padx=1)
frm_command.pack()
search()
window.mainloop()
