import tkinter as tk
from quiz_util import *
from tkinter import *
def answer():
    global card
    print("answer")
    text=card.answer
    txt_answer.delete("1.0","end")
    txt_answer.insert(tk.END, text)
def promote():
    global card
    print("promote")
    leitner.move_id_to_box(card.category_id, card.box+1, card.box)
    card.box+=1
    leitner.remove_id_from_test_cycle(card.category_id)
    cycle.id_list.remove(card.category_id)
    next()
def leave():
    global card
    print("leave")
    leitner.remove_id_from_test_cycle(card.category_id)
    cycle.id_list.remove(card.category_id)
    next()
def demote():
    global card
    print("demote")
    if card.box>1: # can't demote if card is in box 1
        print('Demoting')
        leitner.move_id_to_box(card.category_id, card.box-1, card.box)
        card.box-=1
        leitner.remove_id_from_test_cycle(card.category_id)
        cycle.id_list.remove(card.category_id)
        next()
    else:
        print("leave")
        leitner.remove_id_from_test_cycle(card.category_id)
        cycle.id_list.remove(card.category_id)
        next()


def next():
    global card
    card=cards[cycle.id_list[0]]


    lbl_test_cycle_value["text"]=str(cycle.cycle_num)
    lbl_cycle_questions_value["text"]=str(len(cycle.id_list))
    lbl_ID_value["text"]=card.category_id
    lbl_box_value["text"]=str(card.box)
    text=card.question
    txt_question.delete("1.0","end")
    txt_question.insert(tk.END, text)
    txt_answer.delete("1.0","end")

card=cards[cycle.id_list[0]]
window = tk.Tk()
window.title("Leitner Quiz")
window.columnconfigure(0, minsize=50)
window.rowconfigure(11, minsize=50)
#"Cycle number "+str(cycle.cycle_num)

frm_info = Frame(window)
lbl_test_cycle = tk.Label(master = frm_info,justify=LEFT,text = "Test Cycle ")
lbl_test_cycle.grid(row=0, column=0, padx=1, sticky="E")
lbl_test_cycle_value = tk.Label(master = frm_info,fg="red", justify=LEFT,text = "1")
lbl_test_cycle_value.grid(row=0, column=1, padx=1,sticky="W")


lbl_cycle_questions = tk.Label(master=frm_info, text= "Number of questions left in test cycle ")
lbl_cycle_questions.grid(row=0, column=2, padx=1, sticky="E")
lbl_cycle_questions_value = tk.Label(master=frm_info,fg="red", text="1")
lbl_cycle_questions_value.grid(row=0, column=3, padx=1, sticky="W")

lbl_ID = tk.Label(master = frm_info, text = "Question ID ")
lbl_ID.grid(row=1, column=0, padx=1, sticky="E")
lbl_ID_value= tk.Label(master= frm_info, fg="red", text = "bla-bla-1")
lbl_ID_value.grid(row=1, column=1, padx=1, sticky="W")

lbl_box= tk.Label(master = frm_info, text = "Box Number ")
lbl_box.grid(row=1, column=2, padx=1, sticky="E")
lbl_box_value= tk.Label(master = frm_info, fg="red", text = "1")
lbl_box_value.grid(row=1, column=3, padx=1, sticky="W")

frm_info.pack()

lbl_question = tk.Label(master = window, fg="green", text = "Question")
lbl_question.pack()

txt_question = tk.Text(window)
txt_question.configure(height=5,width=50)
txt_question.pack()
frm_answer = Frame(window)
lbl_answer = tk.Label(master = frm_answer, fg="blue", text = "Answer")
lbl_answer.grid(row=0, column=0, padx=1)
btn_answer = tk.Button(frm_answer, fg="cyan", bg="blue", text="Show Answer", command=answer)
btn_answer.grid(row=1, column=0, padx=1, sticky="W")
txt_answer = tk.Text(frm_answer)
txt_answer.grid(row=2,column=0)
txt_answer.configure(height=5,width=50)
frm_answer.pack()

frm_results = Frame(window)
btn_promote = tk.Button(frm_results, bg="orange", text="Promote", command=promote)
btn_promote.grid(row=0, column=2, padx=1)
btn_leave = tk.Button(frm_results, bg="yellow", text="Leave", command=leave)
btn_leave.grid(row=0, column=1, padx=1)
btn_demote = tk.Button(frm_results, bg="grey", text="Demote", command=demote)
btn_demote.grid(row=0, column=0, padx=1)
frm_results.pack()

next()
window.mainloop()