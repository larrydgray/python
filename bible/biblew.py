
import tkinter as tk
from tkinter import *
from bible_util import *



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
        except KeyError: # Dictionary key error
            txt_output.delete("1.0","end")
            txt_output.insert(tk.END, "Verse not found! "+searchkey)


def count():
    print("list")


def list_books():
    print("books")


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
        except KeyError: # Dictionary key error
            txt_output.delete("1.0","end")
            txt_output.insert(tk.END, "Verse not found! "+searchkey)


window = tk.Tk()
window.title("KJV Bible")
window.columnconfigure(0, minsize=50)
window.rowconfigure(11, minsize=50)

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
