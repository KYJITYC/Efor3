
def prostie(R=1):
    R=int(input('interval:'))+1
    A=[True]*(R)
    Pr=[]
    A[0]=A[1] =False
    for k in range(2,R):
        if A[k]==True:
            for m in range (2*k,R,k):
                A[m]=False
    for k in range(R):
        if A[k]==True:
            Pr.append(k)
        #print(k,'-','prostoe' if A[k]==True else 'sostavnoe')
    return(Pr)
