def merge(A:list,B:list):
    '''obiedinjaet 2 otsortirovannih spiska v 1 otsortirovannij'''
    C=[0]*(len(A)+len(B))
    i=n=k=0
    #print(A,B)
    while i<len(A) and k<len(B):
        if A[i]<=B[k]:
           # print(A[i], B[k])
            C[n]=A[i]; n+=1; i+=1
        else:
            C[n]=B[k]; n+=1; k+=1
        #print(C)
    while i<len(A):
        C[n]=A[i];n+=1; i+=1
    while k<len(B):
        C[n]=B[k];n+=1; k+=1

    return C


def merge_sort(A):
    '''sortiruet spisok drobja po tsifre na levij i pravij posle obiedinjaet merge-em'''
    print('A',A)
    if len(A)<=1:
        return
    middle=len(A)//2
    L=[A[i] for i in range (0,middle)]
    R=[A[i] for i in range (middle, len(A))]
    print('1',L,R)
    merge_sort(L)# posle togo kak A stanet 1 tsifroj -return-merge_sort R
    print('2L', L,R)
    merge_sort(R)# posle return suda prihodit A iz 2 tsifor. posle delenija R-1 tsifra-return
    print('3R', L, R)
    C=merge (L,R)# v merge prihodit 2 chisla. On ih sortiruet i vozvraschaet
    print('C',C)
    for i in range(len(A)):
        A[i]=C[i] #zamena znachenij A na otsortirovannie (v pervoj iteratsii - pervie 2 chisla)
        print('AC', A)

Q=[3, 2, 8, 7, 6,0, 10,9, 1, 5, 4]
merge_sort(Q)
print(Q)

def lcs(A,B):
    '''naibolshaja obschaja posledovatelnost'''
    C=[]
    F=[[0]*(len(B)+1) for i in range (len(A)+1)]
    print(F)
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if A[i-1]==B[j-1]:
                F[i][j]=F[i-1][j-1]+1
                C.append(A[i-1])# odinakovie elementi
                print(F,C, i-1,j-1 )
            else:
                F[i][j]=max(F[i][j-1],F[i-1][j])
                print(F)

    return F[-1][-1],C #poslednie elementi
#a=[1,2,3,7,8,9,0,3,4,6,]
#b=[1,2,5,3,2,9]
#print()

def gis(a: list) -> int:
    """Длина наибольшей возрастающей подпоследовательность массива."""
    f = [0]*len(a)
    for i in range(len(a)):

        m = 0
        for j in range(i):
            print(f, i,j)
            if a[i] > a[j] and f[j] > m:
                m = f[j]
                print(m)
        f[i] = m + 1
    return max(f) if f else 0
#=[2,6,7,1,2]
#print(gis(a))