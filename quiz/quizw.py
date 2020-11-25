import tkinter as tk
from quiz_util import *

def answer():
    print("answer")
    text=card.answer
    txt_answer.delete("1.0","end")
    txt_answer.insert(tk.END, text)
def promote():
    print("promote")
def leave():
    print("leave")
def demote():
    print("demote")
window = tk.Tk()
window.title("Leitner Quiz")
window.columnconfigure(0, minsize=50)
window.rowconfigure(11, minsize=50)
lbl_test_cycle = tk.Label(master = window,text = "Test Cycle 1")
lbl_test_cycle["text"]="Number of questions left in cycle is "+str(len(cycle.id_list))
lbl_test_cycle.pack()
card=cards[cycle.id_list[0]]
lbl_ID= tk.Label(master = window, text = "Question ID: bla-bla-1")
lbl_ID["text"]='Question ID: '+card.category_id
lbl_ID.pack()
lbl_box= tk.Label(master = window, text = "Box Number: 1")
lbl_box["text"]='Box Number: '+str(card.box)
lbl_box.pack()
lbl_question = tk.Label(master = window, text = "Question")
lbl_question.pack()
txt_question = tk.Text(window)
txt_question.configure(height=5,width=50)
text=card.question
txt_question.delete("1.0","end")
txt_question.insert(tk.END, text)
txt_question.pack()
lbl_answer = tk.Label(master = window, text = "Answer")
lbl_answer.pack()
btn_answer = tk.Button(window, text="Show Answer", command=answer)
btn_answer.pack()
txt_answer = tk.Text(window)
txt_answer.configure(height=5,width=50)
txt_answer.pack()
btn_promote = tk.Button(window, text="Promote", command=promote)
btn_promote.pack()
btn_leave = tk.Button(window, text="Leave", command=leave)
btn_leave.pack()
btn_demote = tk.Button(window, text="Demote", command=demote)
btn_demote.pack()
window.mainloop()