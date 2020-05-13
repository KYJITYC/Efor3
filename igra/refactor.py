import tkinter as tk
import random
import time

def main():
    global canv, root, w,h, points,x_event,y_event,xs_event,ys_event, name
    name = input('введите имя: ')
    points=0
    w=800
    h=600
    x_event= y_event=ys_event=xs_event=-1
    root = tk.Tk()
    root.geometry(str(w)+'x'+ str(h))
    canv = tk.Canvas(root,bg='white')
    canv.pack(fill=tk.BOTH,expand=1)
    canv.bind('<Button-1>', click)
    button = tk.Button(root, text="сохранить")
    button.bind('<Button-1>', count)
    button.pack()
    s = Square()
    b = Ball()

    b.motion()
    s.motion()
    root.mainloop()

def click(event):
    '''передает координаты нажатия фигурам'''
    global x_event,y_event,xs_event,ys_event

    x_event=event.x
    xs_event=event.x
    y_event=event.y
    ys_event=event.y

    return x_event,y_event,xs_event,ys_event

def count(event):
    '''сохраняет очки в файл'''
    global points, name
    print('{}--{}'.format(name, points))
    with open(r'/home/efor/Efor3/fail.txt', 'a') as x:
        d=str('\n{}--{}'.format(name,points))
        x.write(d)
        print('{}--{}'.format(name,points))



class Ball:
    def __init__(self):
        self.vx = 2
        self.vy = 2
        self.x =x= random.randrange(100, 750)
        self.y =y= random.randrange(100, 550)
        self.r =r= random.randrange(30, 50)
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        self.ball = canv.create_oval(x - r, y - r, x + r, y + r, fill=random.choice(colors), width=0)
        #canv.bind('<Button-1>', self.click)

    def ball_gen(self):
        '''новый шар, старый стирает'''
        canv.delete(self.ball)
        new_ball = Ball()
        new_ball.motion()

    def click_b(self): #пишет что не дает эффекта
        global points,x_event,y_event
        '''создает шар, считает попадания'''
        #print(x_event, y_event)
        if x_event and y_event !=-1:
            dx = abs(x_event - self.x)
            dy = abs(y_event - self.y)
            if dx <= self.r and dy <= self.r:
                print('попал')
                points += 1
                print(points)

                self.ball_gen()
            x_event = y_event = -1

    def move(self):
        '''двигает ball на vx vy'''
        canv.move(self.ball, self.vx, self.vy)


    def track(self):
        '''трэкает координаты ху'''
        self.x += self.vx
        self.y += self.vy

    def vector_reverse(self):
        '''отскок от границ'''
        if self.x + self.r > w or self.x - self.r <= 0:
            self. vx = -self.vx
        if self.y + self.r > h or self.y - self.r <= 0:
            self.vy = -self.vy

    def motion(self):
        '''движение с отстлеживанием'''
        self.vector_reverse()
        self.move()
        self.track()
        self.click_b()
        root.after(5, self.motion)


class Square:
    def __init__(self):
        self.vx =vx= -3
        self.vy =vy= 3
        self.x = x=random.randrange(100, 750)
        self.y =y= random.randrange(100, 550)
        self.r = r=random.randrange(30, 50)
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        self.square = canv.create_rectangle((x - r, y - r),
                                            (x + r, y + r),
                                            fill=random.choice(colors))
        #canv.bind('<Button-1>', self.click)

    def square_gen(self):
        '''новый квадрат, старый стирает'''
        canv.delete(self.square)
        new_square=Square()
        new_square.motion()

    def move(self):
        '''двигает square на vx vy'''
        canv.move(self.square, self.vx, self.vy)

    def track(self):
        '''трэкает координаты ху'''
        self.x += self.vx
        self.y += self.vy

    def vector_reverse(self):
        '''отскок от границ'''
        if self.x + self.r > w or self.x - self.r <= 0:
            self.vx = -self.vx
        if self.y + self.r > h or self.y - self.r <= 0:
            self.vy = -self.vy

    def motion(self):
        '''движение с отстлеживанием'''
        self.vector_reverse()
        self.move()
        self.track()
        self.click()
        root.after(5, self.motion)

    def click(self):
        '''создает квадрат, считает попадания'''
        global points,xs_event,ys_event

        if xs_event and ys_event != -1:
            dx = abs(xs_event - self.x)
            dy = abs(ys_event - self.y)

            if dx <= self.r and dy <= self.r:
                print('попал')
                # canv.delete(self.square)
                points += 1
                print(points)
                self.square_gen()
            xs_event = ys_event = -1


main()
