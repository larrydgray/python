import tkinter as tk
window = tk.Tk()
label=tk.Label(text="Name")
entry = tk.Entry()

label.pack()
entry.pack()
entry.insert(0, "Python")
name = entry.get()
entry.delete(2, tk.END)
print("Name:", name)
window.mainloop()