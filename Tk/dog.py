from tkinter import *
from random import randint, choice

h=600
w=800

class Ball:
    def __init__(self):
        global x, y,r,dx,dy
        #self.canv=canv
        self.dx=dx=2
        self.dy=dy=2
        self.r = r = randint(30, 50)
        self.x = x=randint(self.r, w-self.r)
        self.y =y= randint(self.r, h-self.r)
        #self.color=color
        self.color = choice(['red', 'orange', 'yellow', 'green', 'blue'])
        self.ball_id=canv.create_oval(
            self.x - self.r, self.y - self.r,
            self.x + self.r, self.y + self.r,
            fill=self.color, width=0
        )



    def ball_gen(self):
        #self.canv.delete(ALL)

        Ball(self.color)

        root.after(1000, self.ball_gen)

    def click(self,event):
        global points

        if (self.x-self.r)<=event.x<=(self.x+self.r) and (self.y-self.r)<=event.y<=(self.y+self.r):
            points += 1
            print(points)
        #self.click

    def move(self):
        self.x+=self.dx
        self.y += self.dy
        if self.x+self.r>w or self.x-self.r<=0:
            self.dx = -self.dx
        if self.y+self.r>h or self.y-self.r<=0:
            self.dy = -self.dy

    def show(self):

        canv.move(self.ball_id,self.dx, self.dy)

def main():
    global root,canv,balls,points
    points = 0
    root = Tk()
    root.geometry(str(w)+'x'+ str(h))
    canv = Canvas(root, bg='black')
    canv.pack(fill=BOTH, expand=1)
    balls=[Ball() for i in range(5)]
    tick()
    mainloop()

def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(5, tick)

if __name__=='__main__':

    main()

'''a=Ball('green')
b=Ball('red')
b.ball_gen()

a.ball_gen()
b.tick()
canv.bind('<Button-1>', a.click)
mainloop()'''