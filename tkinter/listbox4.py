from tkinter import *

#import ttk
#import Tkinter


def myListbox():
    top = Tk()
    top.title('This is it!')
    top.geometry('200x150+200+150')

    Lb1 = Listbox(top)
    Lb1.insert(1, "Aileen")
    Lb1.insert(2, "Hazel")
    Lb1.insert(3, "Rubie")
    Lb1.insert(4, "Mizchell")
    Lb1.insert(5, "Juvy")
    Lb1.insert(6, "Arlene")
    Lb1.insert(7, "Neil")
    Lb1.insert(8, "Rey")
    Lb1.insert(9, "Tricia")
    Lb1.insert(10, "Alona")
    Lb1.insert(11, "Melanie")
    Lb1.insert(12, "Mecca")
    Lb1.insert(13, "Ladera")
    Lb1.insert(14, "Anna")

    Lb1.pack()
    top.mainloop()

def quitter():
    if messagebox.askokcancel('Verify Exit', 'Are you sure you want to quit?'):
        quit()

app=Tk()
app.title('My Tkinter')
app.geometry('400x300+400+300')

button1=Button(app, text=' Listbox ', bg='white', fg='red',width=20, command=myListbox)
buttonfont=('georgia',12,'bold')
button1.config(font=buttonfont)
button1.pack(side='top',padx=35, pady=55)

button1=Button(app, text='Logout', bg='maroon', fg='white',width=20, relief=RAISED, command=quitter)
buttonfont=('georgia',12,'bold')
button1.config(font=buttonfont)
button1.pack(side='bottom', padx=15,pady=15)

app.mainloop()