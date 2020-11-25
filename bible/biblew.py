
import tkinter as tk
from bible_util import *


def search():
    command = ent_command.get()
    print("search:" + command)
    args = command.split(":")
    print(args)
    if len(args)!= 3:
        print("Error format is book:ch#:v#")
    else:
        try:
              a_verse = book_verses[command] # i.e. Luke:1:1 as key
              text=a_verse.get_verse_text()
              print(text)
              txt_output.delete("1.0","end")
              txt_output.insert(tk.END, text)

        except KeyError: # Dictionary key error
            print('Verse Not Found')

def list():
    print("list")


def books():
    print("books")


def log():
    print("log")


def next():
    print("next")


window = tk.Tk()
window.title("KJV Bible")
window.columnconfigure(0, minsize=50)
window.rowconfigure(11, minsize=50)
lbl_message = tk.Label(master=window, text="Enter Command and hit Command Button")
lbl_message.pack()
ent_command = tk.Entry(master=window, width=50)
ent_command.pack()
txt_output = tk.Text(window)
txt_output.configure(height=5, width=50)
txt_output.pack()

btn_search = tk.Button(window, text="Search", command=search)
btn_search.pack()
btn_list = tk.Button(window, text="List", command=list)
btn_list.pack()
btn_books = tk.Button(window, text="Books", command=books)
btn_books.pack()
btn_log = tk.Button(window, text="Log", command=log)
btn_log.pack()
btn_next = tk.Button(window, text="Next Verse", command=next)
btn_next.pack()
window.mainloop()
