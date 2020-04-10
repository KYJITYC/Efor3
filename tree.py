from graph import *



def tree (x,y):
    x1=y/2
    penj = 0.2 * y
    brushColor('brown')
    polygon([(x, 0), (x - y/10, y), (x + y/10, y), (x, 0)])
    brushColor('green')
    h = (y-penj)//6
    y1=h*5

    while y1>=0:
        polygon([(x, y1), (x - x1, y1 + y/5), (x + x1, y1 + y/5), (x, y1)])
        y1=y1 -h
        x1=x1-x1/5
        print (y1)



tree(100,200)


run()