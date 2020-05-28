'''V={'A',"B",'C','D'}
E={('A','B'),
   ('B','C'),
   ('C','D'),
   }'''

'''мартица смежности'''

V=['A',"B",'C','D'] # A--B--C--D
index={V[i]:i for i in range(len(V))}
print(index)
                #    A  B  C  D # какие есть ребра
A=[[0,1,0,0],   # A  0  1  0  0
   [1,0,1,0],   # B  1  0  1  0
   [0,1,0,1],   # C  0  1  0  1
   [0,0,1,0],]  # D  0  0  1  1

'''списки смежности'''

G={'A':{'B'},
   'B':{'C','D'},
   'C':{'B','D'},
   'D':{'C'}
}
for neighbour in G[V]: # V параметр, например 'A' или 'C'
    print(neighbour)
'''
networkx
deixtra'''

'''поиск соседей (строит мартицу А если ли ребро между 2 вершинами)'''
#N - вершины
#M - ребра
N,M=[int(x) for x in input('n m:').split()] # количество вершин и ребер
V=[]
index={}
A=[[0]*N for i in range(N)]
for i in range(M):
    v1,v2=input('v1 v2:').split() # название 2 вершин ребра, например А В
    for v in v1,v2:
        if v not in index:
            V.append(v)
            index[v]=len(V)-1
            #print(V,index)
    v1_i=index[v1]
    v2_i=index[v2]
    A[v1_i][v2_i]=1 #ребро есть
    A[v2_i][v1_i]=1
   # print (A) # пересеячения

'''поиск соседей  для спискаов смежностей (строит мартицу А если ли ребро между 2 вершинами)'''
#N - вершины
#M - ребра
N,M=[int(x) for x in input('n m:').split()] # количество вершин и ребер
Graf={}
for i in range(M):
   v1, v2 = input('v1 v2:').split() # название 2 вершин ребра, например А В
   for v,u in (v1,v2),(v2,v1): # сначала в и у как в1 в2 потом как в2 в1
       if v not in Graf:
           Graf[v]={u} # добавляется запись о вершине v у которой соседняя-u
       else:
           Graf[v].add(u)# к вершине v добавляется соответствие вершина u

