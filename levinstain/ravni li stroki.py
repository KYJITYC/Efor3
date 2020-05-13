def equal(A,B):
    if len(A)!=len(B):
        return False
    for i in range (len(A)):
        if A[i]!=B[i]:
            return False
    return True
if __name__=='__main__':
    print (equal(('qwm'),('qtyhm')))