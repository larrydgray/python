import tkinter as tk 
 
class MouseKeyboardApp(tk.Tk): 
    def __init__(self): 
        super().__init__() 
        frame = tk.Frame(self, bg="green", 
                         height=100, width=100) 
        frame.bind("<Button-1>", self.print_event) 
        frame.bind("<Double-Button-1>", self.print_event) 
        frame.bind("<ButtonRelease-1>", self.print_event) 
        frame.bind("<B1-Motion>", self.print_event) 
        frame.bind("<Enter>", self.print_event) 
        frame.bind("<Leave>", self.print_event) 
        frame.pack(padx=50, pady=50)
        entry = tk.Entry(self) 
        entry.bind("<FocusIn>", self.print_type)  
        entry.bind("<Key>", self.print_key) 
        entry.pack(padx=20, pady=20) 
 
    def print_event(self, event): 
        position = "(x={}, y={})".format(event.x, event.y) 
        print(event.type, "event", position)
        
 
    def print_type(self, event): 
        print(event.type) 
 
    def print_key(self, event): 
        args = event.keysym, event.keycode, event.char 
        print("Symbol: {}, Code: {}, Char: {}".format(*args)) 
 
 
if __name__ == "__main__": 
    mouse_keyboard_app = MouseKeyboardApp()
    
    mouse_keyboard_app.mainloop() 
