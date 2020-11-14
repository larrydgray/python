import tkinter as tk
window = tk.Tk()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

window.mainloop()


