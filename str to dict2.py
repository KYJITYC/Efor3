
a=('abcde')
c=[]
d={}
for i in enumerate(a):
    c.append(i)
print(c)
for i,j in c:
    d[j]=i
print(d)




for i,x in enumerate(a):
    print(i,x)

#b=dict (s.split(':',1) for s in c)