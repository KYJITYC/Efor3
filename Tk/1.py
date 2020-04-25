
from tkinter import *
'''razbivka slov po alfavitu po najatiu knopki'''
root=Tk()

entry=Entry(root,width=20)
button=Button (root,text='preobrazovat')
label=Label(root, bg='black',fg='white',width=20)

def strToSortlist(event):
    s = entry.get()
    s = s.split()
    s.sort()
    label['text'] = ' '.join(s)

button.bind('<Button-1>',strToSortlist)

entry.pack()
button.pack()
label.pack()
root.mainloop()
