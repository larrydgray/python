# https://en.wikipedia.org/wiki/Web_colors#Hex_triplet
import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter", background="#34A2FE")
label = tk.Label(text="Hello, Tkinter", fg="white", bg="black")
label2 = tk.Label(
    text="Hello, Tkinter",
    fg="cyan",
    bg="blue",
    width=10, # 10 characters wide
    height=10 # 10 characters or lines tall
)

label2.pack()
label.pack()
greeting.pack()
window.mainloop()


