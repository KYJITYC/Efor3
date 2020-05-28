'''множество'''
a=set()#пустое множетво
n=len(a)
b=set('fsdfsdf')# по 1 разу каждую букву
print('f' in b) #True
b.add('q') # в случайное место
print(b) # {'s', 'd', 'q', 'f'}, каждый раз в случайном порядке
a.discard('q')# если q нет то ошибки нет
b.remove('x')# если x нет то ошибка key error
b.pop()# случайный

'''операции'''
c=a|b ==a.union(b)# объединить
c=a&b==a.intersection(b) # общие элементы
c=a-b==a.difference(b)
c=a^b==a.symmetric_difference(b) # все те, что не общие
a>=b # True когда а-надмножество b @можно не упорядочевать@
a<b #True когда а-надмножество b и a!=b @можно не упорядочевать@


'''словари'''
d={}==dict() # пустой словарь
n=len(d)
d= {'one' : 1,
    'two' : 2,
    'three':3} # слева ключ, справа значение ключа
c=zip(a,b) # c итерируемый объект (последовательность). объединяет 2 одинаковых по длине списка
d=dict(zip(k,v)) # k-список ключей. v - список значений
d['four']=4 # появление новой пары
print(d['one']) # 1
print('five' in d) #False
del a['four'] # если 'four' нет то ошибка key error
x=d.pop(key,-1) # если key нет, то x например =-1. Ошибка не появится
for key i d:
    print(key,d[key]) # ключ,значение

A=list(d.items()) # список ключ/значение