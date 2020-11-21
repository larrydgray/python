import tkinter as tk
window = tk.Tk()

text_box = tk.Text()
text_box.pack()
text_box.insert(0.0 ,"xHello\nWorld!")


text=text_box.get(0.0 ,tk.END)
print("TextBox:", text)
text_box.delete(1.0, 1.1) #line.column starts text box with line 1
text=text_box.get(0.0, tk.END)
print("\nTextBox:", text)
window.mainloop()