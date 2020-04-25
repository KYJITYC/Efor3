from tkinter import *
from random import randrange as rnd, choice
import time
points=0
root = Tk()
root.geometry('800x600')
canv = Canvas(root,bg='black')
canv.pack(fill=BOTH,expand=1)

class Ball:
    def __init__(self,color):
        global x, y,r
        #self.canv=canv

        x = rnd (100, 700)
        y = rnd (100, 500)
        r = rnd (30, 50)

        #self.colors = choice(['red', 'orange', 'yellow', 'green', 'blue'])
        canv.create_oval(
            x - r, y - r,
            x + r, y + r,
            fill=color, width=0
        )


    def ball_gen(self):
        #self.canv.delete(ALL)

        Ball(color)

        root.after(1000, self.ball_gen)

    def click(self,event):
        global points

        if (self.x-self.r)<=event.x<=(self.x+self.r) and (self.y-self.r)<=event.y<=(self.y+self.r):
            points += 1
            print(points)
        #self.click

a=Ball('green')
b=Ball('red')
b.ball_gen()
#a.ball_gen()
canv.bind('<Button-1>', a.click)
mainloop()