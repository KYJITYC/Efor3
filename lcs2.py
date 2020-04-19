def lcs(A,B):
    F=[[0]*(len(B)+1) for i in range(len(A)+1)]
    C=[]
    for i in range(1,len(A)+1):
        n=0
        for j in range (1,len(B)+1):
            if A[i-1]==B[j-1]:
                F[i][j]=F[i-1][j-1]+1
            if n< F[i][j]: 
                n=F[i][j]
                C.append(A[i-1])
            else:
                F[i][j]=max(F[i-1][j],F[i][j-1])
    return F[-1][-1], C

A=[5,1,3,4,2]
B=[3,3,5,6,1]
print(lcs(A,B))
        
