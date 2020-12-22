import tkinter as tk
from quiz_util import *
from tkinter import *
from quiz_util import cycle
from PIL import ImageTk, Image
import leitner.leitner

def answer():
    global card
    print("answer")
    text = card.answer
    txt_answer.delete("1.0", "end")
    txt_answer.insert(tk.END, text)


def promote():
    global card
    print("promote")
    leitner.move_id_to_box(card.category_id, card.box + 1, card.box)
    card.box += 1
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
    if card.box > 1:  # can't demote if card is in box 1
        print('Demoting')
        leitner.move_id_to_box(card.category_id, card.box - 1, card.box)
        card.box -= 1
        leitner.remove_id_from_test_cycle(card.category_id)
        cycle.id_list.remove(card.category_id)
        next()
    else:
        print("leave")
        leitner.remove_id_from_test_cycle(card.category_id)
        cycle.id_list.remove(card.category_id)
        next()


def next():
    global cycle
    global cards
    if len(cycle.id_list) == 0:  # if we answered all questions in the cycle
        cycle.id_list.append('empty')
        # make sure the cycle file has empty tag in it
        leitner.save_test_cycle_file(cycle.id_list)
        print('End of test cycle ' + str(cycle.cycle_num))
        cards = {}
        if test == 1:
            leitner.set_path('quizs\\')
            card_files = ('algo_cards', 'data_struct_cards', 'oop_cards', 'python_cards', 'uml_cards')
        else:
           leitner.set_path('quizs\\study\\')
           card_files = ('interview_cards')
        leitner.set_card_file_names(card_files)
        cards = leitner.load_cards()

        cycle = leitner.load_test_cycle()

        test_cycle_file_name = 'testcycle' + str(cycle.cycle_num)
    global card
    card = cards[cycle.id_list[0]]
    lbl_test_cycle_value["text"] = str(cycle.cycle_num)
    lbl_cycle_questions_value["text"] = str(len(cycle.id_list))
    lbl_ID_value["text"] = card.category_id
    lbl_box_value["text"] = str(card.box)
    text = card.question
    txt_question.delete("1.0", "end")
    txt_question.insert(tk.END, text)
    txt_answer.delete("1.0", "end")
    update_boxes()

def load_images():
    global img_test_boxes
    img_test_boxes = [None] * 11
    global img_no_test_boxes
    img_no_test_boxes = [None] * 11
    zoom=0.25
    w=int(246*zoom)
    h=int(92*zoom)
    img_test_boxes[0] = ImageTk.PhotoImage(Image.open("images/boxe.png").resize((w,h), Image.ANTIALIAS))
    img_no_test_boxes[0] = ImageTk.PhotoImage(Image.open("images/boxen.png").resize((w,h), Image.ANTIALIAS))
    img_test_boxes[1] = ImageTk.PhotoImage(Image.open("images/box1.png").resize((w,h), Image.ANTIALIAS))
    img_no_test_boxes[1] = ImageTk.PhotoImage(Image.open("images/box1n.png").resize((w,h), Image.ANTIALIAS))
    img_test_boxes[2] = ImageTk.PhotoImage(Image.open("images/box2.png").resize((w,h), Image.ANTIALIAS))
    img_no_test_boxes[2] = ImageTk.PhotoImage(Image.open("images/box2n.png").resize((w,h), Image.ANTIALIAS))
    img_test_boxes[3] = ImageTk.PhotoImage(Image.open("images/box3.png").resize((w,h), Image.ANTIALIAS))
    img_no_test_boxes[3] = ImageTk.PhotoImage(Image.open("images/box3n.png").resize((w,h), Image.ANTIALIAS))
    img_test_boxes[4] = ImageTk.PhotoImage(Image.open("images/box4.png").resize((w,h), Image.ANTIALIAS))
    img_no_test_boxes[4] = ImageTk.PhotoImage(Image.open("images/box4n.png").resize((w,h), Image.ANTIALIAS))
    img_test_boxes[5] = ImageTk.PhotoImage(Image.open("images/box5.png").resize((w,h), Image.ANTIALIAS))
    img_no_test_boxes[5] = ImageTk.PhotoImage(Image.open("images/box5n.png").resize((w,h), Image.ANTIALIAS))
    img_test_boxes[6] = ImageTk.PhotoImage(Image.open("images/box6.png").resize((w,h), Image.ANTIALIAS))
    img_no_test_boxes[6] = ImageTk.PhotoImage(Image.open("images/box6n.png").resize((w,h), Image.ANTIALIAS))
    img_test_boxes[7] = ImageTk.PhotoImage(Image.open("images/box7.png").resize((w,h), Image.ANTIALIAS))
    img_no_test_boxes[7] = ImageTk.PhotoImage(Image.open("images/box7n.png").resize((w,h), Image.ANTIALIAS))
    img_test_boxes[8] = ImageTk.PhotoImage(Image.open("images/box8.png").resize((w,h), Image.ANTIALIAS))
    img_no_test_boxes[8] = ImageTk.PhotoImage(Image.open("images/box8n.png").resize((w,h), Image.ANTIALIAS))
    img_test_boxes[9] = ImageTk.PhotoImage(Image.open("images/box9.png").resize((w,h), Image.ANTIALIAS))
    img_no_test_boxes[9] = ImageTk.PhotoImage(Image.open("images/box9n.png").resize((w,h), Image.ANTIALIAS))
    img_test_boxes[10] = ImageTk.PhotoImage(Image.open("images/box10.png").resize((w,h), Image.ANTIALIAS))
    img_no_test_boxes[10] = ImageTk.PhotoImage(Image.open("images/box10n.png").resize((w,h), Image.ANTIALIAS))

def update_boxes():
    box_cards = leitner.count_box_cards()
    total_cards = sum(box_cards)
    lbl_total_cards["text"] = str(total_cards)
    box_cards_percent=[0,0,0,0,0,0]
    c=0
    for count in box_cards:
        box_cards_percent[c]=int(count/total_cards*10)
        c+=1

    boxes_tested = [True, False, False, False, False, False]
    if cycle.cycle_num%2 == 0:
        boxes_tested[1]=True
    if cycle.cycle_num%4 == 0:
        boxes_tested[2]=True
    if cycle.cycle_num%8 == 0:
        boxes_tested[3]=True
    if cycle.cycle_num%16 == 0:
        boxes_tested[4]=True
    box1=0
    box2=1;
    box3=2;
    box4=3;
    box5=4;
    box6=5
    #for box 1 which is in every cycle, yellow background
    box1_image=img_test_boxes[box_cards_percent[box1]]
    lbl_box1.configure(image=box1_image)
    lbl_box1.image = box1_image


    if boxes_tested[box2]: # Yellow
        box2_image=img_test_boxes[box_cards_percent[box2]]
        lbl_box2.configure(image=box2_image)
        lbl_box2.image = box2_image
    else: # Orange
        box2_image=img_no_test_boxes[box_cards_percent[box2]]
        lbl_box2.configure(image=box2_image)
        lbl_box2.image = box2_image


    if boxes_tested[box3]: # Yellow
        box3_image=img_test_boxes[box_cards_percent[box3]]
        lbl_box3.configure(image=box3_image)
        lbl_box3.image = box3_image
    else: # Orange
        box3_image=img_no_test_boxes[box_cards_percent[box3]]
        lbl_box3.configure(image=box3_image)
        lbl_box3.image = box3_image

    if boxes_tested[box4]: # Yellow
        box4_image=img_test_boxes[box_cards_percent[box4]]
        lbl_box4.configure(image=box4_image)
        lbl_box4.image = box4_image
    else: # Orange
        box4_image=img_no_test_boxes[box_cards_percent[box3]]
        lbl_box4.configure(image=box4_image)
        lbl_box4.image = box4_image

    if boxes_tested[box5]: # Yellow
        box5_image=img_test_boxes[box_cards_percent[box5]]
        lbl_box5.configure(image=box5_image)
        lbl_box5.image = box5_image
    else: # Orange
        box5_image=img_no_test_boxes[box_cards_percent[box5]]
        lbl_box5.configure(image=box5_image)
        lbl_box5.image = box5_image

    lbl_box1_count["text"] = box_cards[box1]
    lbl_box2_count["text"] = box_cards[box2]
    lbl_box3_count["text"] = box_cards[box3]
    lbl_box4_count["text"] = box_cards[box4]
    lbl_box5_count["text"] = box_cards[box5]
    lbl_box6_count["text"] = box_cards[box6]




card = cards[cycle.id_list[0]]
window = tk.Tk()
window.title("Leitner Quiz")
window.columnconfigure(0, minsize=50)
window.rowconfigure(11, minsize=50)
# "Cycle number "+str(cycle.cycle_num)
load_images()

frm_info = Frame(window)
lbl_test_cycle = tk.Label(master=frm_info, justify=LEFT, text="Test Cycle ")
lbl_test_cycle.grid(row=0, column=0, padx=1, sticky="E")
lbl_test_cycle_value = tk.Label(master=frm_info, fg="red", justify=LEFT, text="1")
lbl_test_cycle_value.grid(row=0, column=1, padx=1, sticky="W")

lbl_cycle_questions = tk.Label(master=frm_info, text="Number of questions left in test cycle ")
lbl_cycle_questions.grid(row=0, column=2, padx=1, sticky="E")
lbl_cycle_questions_value = tk.Label(master=frm_info, fg="red", text="1")
lbl_cycle_questions_value.grid(row=0, column=3, padx=1, sticky="W")

lbl_ID = tk.Label(master=frm_info, text="Question ID ")
lbl_ID.grid(row=1, column=0, padx=1, sticky="E")
lbl_ID_value = tk.Label(master=frm_info, fg="red", text="bla-bla-1")
lbl_ID_value.grid(row=1, column=1, padx=1, sticky="W")

lbl_box = tk.Label(master=frm_info, text="Box Number ")
lbl_box.grid(row=1, column=2, padx=1, sticky="E")
lbl_box_value = tk.Label(master=frm_info, fg="red", text="1")
lbl_box_value.grid(row=1, column=3, padx=1, sticky="W")

frm_info.pack()

frm_boxes=Frame(window)

lbl_box1_count = tk.Label(frm_boxes, text=str(119))
lbl_box1_count.grid(row=0,column=1)
lbl_box2_count = tk.Label(frm_boxes, text=str(15))
lbl_box2_count.grid(row=0,column=2)
lbl_box3_count = tk.Label(frm_boxes, text=str(26))
lbl_box3_count.grid(row=0,column=3)
lbl_box4_count = tk.Label(frm_boxes, text=str(18))
lbl_box4_count.grid(row=0,column=4)
lbl_box5_count = tk.Label(frm_boxes, text=str(40))
lbl_box5_count.grid(row=0,column=5)
lbl_box6_count = tk.Label(frm_boxes, text=str(201))
lbl_box6_count.grid(row=0,column=6)

lbl_total_cards =  tk.Label(frm_boxes, text=str(0))
lbl_total_cards.grid(row=1,column=0)
lbl_box1 = tk.Label(frm_boxes, image=img_test_boxes[8])
lbl_box1.grid(row=1,column=1)
lbl_box2 = tk.Label(frm_boxes, image=img_no_test_boxes[0])
lbl_box2.grid(row=1,column=2)
lbl_box3 = tk.Label(frm_boxes, image=img_no_test_boxes[0])
lbl_box3.grid(row=1,column=3)
lbl_box4 = tk.Label(frm_boxes, image=img_no_test_boxes[0])
lbl_box4.grid(row=1,column=4)
lbl_box5 = tk.Label(frm_boxes, image=img_no_test_boxes[0])
lbl_box5.grid(row=1,column=5)
lbl_box6 = tk.Label(frm_boxes, image=img_no_test_boxes[0])
lbl_box6.grid(row=1,column=6)
frm_boxes.pack()

lbl_question = tk.Label(master=window, fg="green", text="Question")
lbl_question.pack()

txt_question = tk.Text(window)
txt_question.configure(height=5, width=50)
txt_question.pack()
frm_answer = Frame(window)
lbl_answer = tk.Label(master=frm_answer, fg="blue", text="Answer")
lbl_answer.grid(row=0, column=0, padx=1)
btn_answer = tk.Button(frm_answer, fg="cyan", bg="blue", text="Show Answer", command=answer)
btn_answer.grid(row=1, column=0, padx=1, sticky="W")
txt_answer = tk.Text(frm_answer)
txt_answer.grid(row=2, column=0)
txt_answer.configure(height=5, width=50)
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
