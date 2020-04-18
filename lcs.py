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