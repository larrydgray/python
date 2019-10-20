import json
from tkinter import *
root = Tk()
root.title('Segmented Line')
cw=300
ch=200
canvas_1 = Canvas(root, width=cw, height=ch, background="black")
canvas_1.grid(row=0,column=1)
with open('sprites.json') as json_file:
    data = json.load(json_file)
    for p in data['sprites']:
        print('Name: ' + p['name'])
        print('')
    
    shape=data['sprites'][0]['shape']
    for i in range(0,len(shape)):
        print(i)
        if i%2!=0:
            shape[i]=(-shape[i])+50
    canvas_1.create_line(shape,fill=data['sprites'][0]['color'])

root.mainloop()

