from tkinter import *
from random import randrange as rnd, choice
import time
points=0
root = Tk()
root.geometry('800x600')
canv = Canvas(root,bg='black')
canv.pack(fill=BOTH,expand=1)

class Ball:
    def __init__(self):
      self.points = 0


    def new_ball(self):
       # global ex,ey,er
        canv.delete(ALL)
        self.x = x = rnd(100, 700)
        self.y = y = rnd(100, 500)
        self.r = r = rnd(30, 50)
        self.colors = choice(['red', 'orange', 'yellow', 'green', 'blue'])
        #self.life = 1
        #self.points = 1
        canv.create_oval(
            x - r, y - r,
            x + r, y + r,
            fill=self.colors, width=0
        )
        root.after(1000, self.new_ball)

    def click(self,event):
        global points
        if (self.x-self.r)<=event.x<=(self.x+self.r) and (self.y-self.r)<=event.y<=(self.y+self.r):
            points += 1
            print(points)

a=Ball()
b=Ball()
a.new_ball()
b.new_ball()
canv.bind('<Button-1>', a.click)
mainloop()