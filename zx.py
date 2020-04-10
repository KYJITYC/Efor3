from graph import *
#moveTo(100,100)
y=300
x=300
n=1
#h=(y-0.2*y)/n
penj=0.2*y
#y=0.2y+n*(y-0.2*y)
brushColor('brown')
polygon([(x,100),(x-20,y),(x+20,y),(x,100)])

def tree (x,y):
 # y=300-0.2*y
  brushColor('green')
  while y>=100:
    polygon([(300, y), (300 - x,y+ y/3), (300+x , y+ y/3), (300, y)])
    y=y- 20
    x=x-x/4
    print(y)
  #polygon([(300, y), (300 - x, y + y / 4), (300 + x, y + y / 4), (300, y)])
  



tree(80,200)


run()