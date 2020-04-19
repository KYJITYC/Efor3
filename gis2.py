def gis(A):
    F=[0]*(len(A))
    C=[]
    for i in range (len(A)) :
        m=0
        for j in range(i):
            if A[i]>A[j] and F[j]>m:
                m=F[j]
                C.append([A[j],A[i]])
        F[i]=m+1
        print(F,m)
    return max(*F),C

a=[2,1,3,2,0]
print(gis(a))

                
